from pathlib import Path
import os
import re
import shutil
import subprocess
import tempfile

import yaml

# ============================================================
# Project configuration
# ============================================================

# Languages to be generated.
LANGUAGES = ["pt-BR", "es", "en", "it"]

# Project directories.
PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "output"

# Output filename prefix.
PROJECT_NAME = "decision-architecture-handbook"

# Book chapters, in publication order.
# Each entry represents a directory containing a language-specific Markdown file.
CHAPTERS = [
    "introduction",
    "01-foundations-of-decision-architecture",
    "02-understanding-the-domain-of-a-decision",
    "03-discovering-the-initial-context",
    "04-establishing-objectives",
    "05-managing-risks-and-uncertainties",
    "06-predicting-direct-and-indirect-consequences",
    "07-dealing-with-the-evolution-of-a-decision",
    "08-more-practical-examples-of-application",
    "conclusion",
]


# ============================================================
# Configuration helpers
# ============================================================

def get_language_paths(language):
    """Build all file paths for a language edition."""
    return {
        "metadata": PROJECT_DIR / "metadata" / f"{language}.yaml",
        "cover": PROJECT_DIR / "cover" / f"{language}.jpg",
        "pdf": OUTPUT_DIR / f"{PROJECT_NAME}-{language}.pdf",
        "epub": OUTPUT_DIR / f"{PROJECT_NAME}-{language}.epub",
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

    cover_path = (PROJECT_DIR / cover_value).resolve()

    if not cover_path.is_file():
        raise FileNotFoundError(
            f"Cover image not found: {cover_path}"
        )

    return cover_path


def get_chapter_paths(language):
    """Resolve chapter Markdown files in publication order."""

    filename_by_language = {
        "pt-BR": "README.pt-BR.md",
        "en": "README.md",
        "es": "README.es.md",
        "it": "README.it.md",
        "ai": "README.ai.md",
    }

    if language not in filename_by_language:
        raise ValueError(f"Unsupported language: {language}")

    chapter_paths = []

    for chapter in CHAPTERS:
        chapter_path = (
            PROJECT_DIR / chapter / filename_by_language[language]
        ).resolve()

        # Prevent chapter paths from escaping the project directory.
        if PROJECT_DIR not in chapter_path.parents:
            raise ValueError(f"Invalid chapter path: {chapter_path}")

        if not chapter_path.is_file():
            raise FileNotFoundError(
                f"Chapter file not found: {chapter_path}"
            )

        chapter_paths.append(chapter_path)

    if not chapter_paths:
        raise ValueError("No chapters configured.")

    return chapter_paths


# ============================================================
# Markdown and resource helpers
# ============================================================

def build_resource_path(chapter_paths):
    """Build the resource search path for local images and assets."""
    resource_dirs = {PROJECT_DIR}

    for chapter_path in chapter_paths:
        resource_dirs.add(chapter_path.parent)

    return os.pathsep.join(
        str(path) for path in sorted(resource_dirs)
    )


def create_combined_markdown(chapter_paths, destination, add_page_breaks):
    """Combine chapters while preserving the configured order."""
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
    """Create a LaTeX header for the PDF cover and page layout."""
    cover_relative_path = cover_path.relative_to(
        PROJECT_DIR
    ).as_posix()

    cover_relative_path = escape_latex_path(
        cover_relative_path
    )

    latex_header = rf"""
\usepackage{{graphicx}}
\usepackage{{eso-pic}}
\usepackage{{etoolbox}}
\usepackage{{geometry}}
\geometry{{
    top=2cm,
    bottom=2cm,
    inner=2.5cm,
    outer=2cm
}}

% Insert the cover as the background of the first page.
\AtBeginDocument{{
    \thispagestyle{{empty}}
    \AddToShipoutPictureBG*{{
        \AtPageLowerLeft{{
            \includegraphics[
                width=\paperwidth,
                height=\paperheight
            ]{{{cover_relative_path}}}
        }}
    }}
    \null
    \clearpage
    \ClearShipoutPictureBG
    \let\maketitle\relax
}}

% Start the introduction on a new page after the table of contents.
\apptocmd{{\tableofcontents}}{{\clearpage}}{{}}{{}}
"""

    destination.write_text(
        latex_header,
        encoding="utf-8"
    )


# ============================================================
# PDF generation
# ============================================================

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
            cwd=PROJECT_DIR,
            check=True,
        )

    print(f"PDF generated: {output_file}")


# ============================================================
# EPUB generation
# ============================================================

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
            cwd=PROJECT_DIR,
            check=True,
        )

    print(f"EPUB generated: {output_file}")


# ============================================================
# Book generation
# ============================================================

def build_language_edition(language):
    """Generate PDF and EPUB files for one language."""
    print(f"\nBuilding book edition: {language}")

    paths = get_language_paths(language)

    metadata = load_metadata(paths["metadata"])
    cover_path = get_cover_path(metadata, language)
    chapter_paths = get_chapter_paths(language)

    print(f"Found {len(chapter_paths)} chapters:")

    for chapter_path in chapter_paths:
        print(f"  - {chapter_path.relative_to(PROJECT_DIR)}")

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
