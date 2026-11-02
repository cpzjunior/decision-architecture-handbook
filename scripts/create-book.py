
from pathlib import Path
from urllib.parse import unquote
import os
import re
import shutil
import subprocess
import tempfile

import yaml


# Languages to be generated.
LANGUAGES = ["pt-BR"]

# Project configuration.
ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT_DIR / "output"
OUTPUT_BASENAME = "decision-architecture-handbook"


def get_language_paths(language):
    """Build all file paths for a language edition."""
    return {
        "readme": ROOT_DIR / f"README.{language}.md",
        "metadata": ROOT_DIR / "metadata" / f"{language}.yaml",
        "cover": ROOT_DIR / "cover" / f"{language}.jpg",
        "pdf": OUTPUT_DIR / f"{OUTPUT_BASENAME}-{language}.pdf",
        "epub": OUTPUT_DIR / f"{OUTPUT_BASENAME}-{language}.epub",
    }


def check_dependencies():
    """Check whether required external tools are installed."""
    required_tools = ["pandoc", "xelatex"]

    for tool in required_tools:
        if shutil.which(tool) is None:
            raise RuntimeError(
                f"Required tool '{tool}' was not found in PATH."
            )


def load_metadata(metadata_file):
    """Load and validate book metadata."""
    if not metadata_file.is_file():
        raise FileNotFoundError(
            f"Metadata file not found: {metadata_file}"
        )

    with metadata_file.open("r", encoding="utf-8") as file:
        metadata = yaml.safe_load(file)

    if not isinstance(metadata, dict):
        raise ValueError(
            f"Invalid metadata file: {metadata_file}"
        )

    return metadata


def get_cover_path(metadata, language):
    """Resolve and validate the cover image path."""
    cover_value = metadata.get(
        "cover-image",
        f"cover/{language}.jpg"
    )

    cover_path = (ROOT_DIR / cover_value).resolve()

    if not cover_path.is_file():
        raise FileNotFoundError(
            f"Cover image not found: {cover_path}"
        )

    return cover_path


def extract_chapter_paths(readme_file):
    """Extract chapter paths in the order defined by the README index."""
    if not readme_file.is_file():
        raise FileNotFoundError(
            f"README file not found: {readme_file}"
        )

    content = readme_file.read_text(encoding="utf-8")

    # Locate the index section.
    index_match = re.search(
        r"^##\s+Índice\s*$([\s\S]*?)(?=^##\s+|\Z)",
        content,
        flags=re.MULTILINE | re.IGNORECASE,
    )

    if not index_match:
        raise ValueError(
            f"The '## Índice' section was not found in {readme_file.name}."
        )

    index_content = index_match.group(1)

    # Extract Markdown links from the index.
    links = re.findall(
        r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+[^)]*)?\)",
        index_content,
    )

    chapter_paths = []
    seen_paths = set()

    for link in links:
        link = unquote(link.strip().strip("<>"))

        # Remove URL fragments and query parameters.
        link = link.split("#", 1)[0].split("?", 1)[0]

        # Only include Markdown files.
        if not link.lower().endswith(".md"):
            continue

        # Ignore external links.
        if re.match(
            r"^[a-z][a-z0-9+.-]*://",
            link,
            flags=re.IGNORECASE,
        ):
            continue

        # Resolve paths relative to the repository root.
        chapter_path = (ROOT_DIR / link).resolve()

        # Prevent files outside the repository from being included.
        if ROOT_DIR not in chapter_path.parents:
            raise ValueError(
                f"Chapter path is outside the repository: {link}"
            )

        if not chapter_path.is_file():
            raise FileNotFoundError(
                f"Chapter file not found: {chapter_path}"
            )

        # Avoid duplicate chapters while preserving their original order.
        if chapter_path not in seen_paths:
            chapter_paths.append(chapter_path)
            seen_paths.add(chapter_path)

    if not chapter_paths:
        raise ValueError(
            f"No Markdown chapters found in {readme_file.name}."
        )

    return chapter_paths


def build_resource_path(chapter_paths):
    """Build the resource search path for local images and assets."""
    resource_dirs = {ROOT_DIR}

    for chapter_path in chapter_paths:
        resource_dirs.add(chapter_path.parent)

    return os.pathsep.join(
        str(path) for path in sorted(resource_dirs)
    )


def create_combined_markdown(chapter_paths, destination, add_page_breaks):
    """Combine chapters while preserving the README order."""
    with destination.open("w", encoding="utf-8") as output_file:
        for index, chapter_path in enumerate(chapter_paths):
            if index > 0 and add_page_breaks:
                # Insert a page break before each new chapter in the PDF.
                output_file.write("\n\\newpage\n\n")
            else:
                output_file.write("\n\n")

            chapter_content = chapter_path.read_text(
                encoding="utf-8"
            )

            output_file.write(chapter_content)
            output_file.write("\n\n")


def escape_latex_path(path):
    """Escape special characters in a LaTeX file path."""
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }

    return "".join(
        replacements.get(character, character)
        for character in path
    )


def create_pdf_header(cover_path, destination):
    """Create a LaTeX header that uses the image as the PDF cover."""
    cover_relative_path = cover_path.relative_to(
        ROOT_DIR
    ).as_posix()

    cover_relative_path = escape_latex_path(
        cover_relative_path
    )

    latex_header = rf"""
\usepackage{{graphicx}}
\usepackage{{geometry}}

\makeatletter
\renewcommand{{\maketitle}}{{%
    \begin{{titlepage}}
        \newgeometry{{margin=0pt}}
        \thispagestyle{{empty}}
        \noindent
        \includegraphics[
            width=\paperwidth,
            height=\paperheight
        ]{{{cover_relative_path}}}
    \end{{titlepage}}
    \restoregeometry
}}
\makeatother
"""

    destination.write_text(
        latex_header,
        encoding="utf-8"
    )


def build_pdf(metadata_file, chapter_paths, cover_path, output_file):
    """Generate the PDF edition."""
    with tempfile.TemporaryDirectory(
        dir=OUTPUT_DIR,
        prefix="pdf-"
    ) as temp_dir:

        temp_path = Path(temp_dir)
        combined_file = temp_path / "book.md"
        header_file = temp_path / "cover-header.tex"

        create_combined_markdown(
            chapter_paths,
            combined_file,
            add_page_breaks=True,
        )

        create_pdf_header(
            cover_path,
            header_file,
        )

        resource_path = build_resource_path(chapter_paths)

        command = [
            "pandoc",
            str(combined_file),
            "--from=markdown",
            "--standalone",
            f"--metadata-file={metadata_file}",
            "--toc",
            "--toc-depth=2",
            "--pdf-engine=xelatex",
            f"--include-in-header={header_file}",
            f"--resource-path={resource_path}",
            f"--output={output_file}",
        ]

        subprocess.run(
            command,
            cwd=ROOT_DIR,
            check=True,
        )

    print(f"PDF generated: {output_file}")


def build_epub(metadata_file, chapter_paths, cover_path, output_file):
    """Generate the EPUB edition."""
    with tempfile.TemporaryDirectory(
        dir=OUTPUT_DIR,
        prefix="epub-"
    ) as temp_dir:

        combined_file = Path(temp_dir) / "book.md"

        # EPUB is reflowable, so fixed page breaks are not inserted.
        create_combined_markdown(
            chapter_paths,
            combined_file,
            add_page_breaks=False,
        )

        resource_path = build_resource_path(chapter_paths)

        command = [
            "pandoc",
            str(combined_file),
            "--from=markdown",
            "--standalone",
            f"--metadata-file={metadata_file}",
            "--toc",
            "--toc-depth=2",
            "--split-level=1",
            f"--epub-cover-image={cover_path}",
            f"--resource-path={resource_path}",
            f"--output={output_file}",
        ]

        subprocess.run(
            command,
            cwd=ROOT_DIR,
            check=True,
        )

    print(f"EPUB generated: {output_file}")


def build_language_edition(language):
    """Generate PDF and EPUB files for one language."""
    print(f"\nBuilding book edition: {language}")

    paths = get_language_paths(language)

    metadata = load_metadata(paths["metadata"])
    cover_path = get_cover_path(metadata, language)
    chapter_paths = extract_chapter_paths(paths["readme"])

    print(f"Found {len(chapter_paths)} chapters:")

    for chapter_path in chapter_paths:
        print(f"  - {chapter_path.relative_to(ROOT_DIR)}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    build_pdf(
        paths["metadata"],
        chapter_paths,
        cover_path,
        paths["pdf"],
    )

    build_epub(
        paths["metadata"],
        chapter_paths,
        cover_path,
        paths["epub"],
    )


def main():
    """Generate all configured language editions."""
    check_dependencies()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for language in LANGUAGES:
        build_language_edition(language)

    print("\nBook generation completed.")


if __name__ == "__main__":
    main()
