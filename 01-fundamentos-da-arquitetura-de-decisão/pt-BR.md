# 1. Fundamentos da Arquitetura de Decisão

Os fundamentos da Arquitetura de Decisão são referências que orientam como decisões podem ser compreendidas, estruturadas e desenvolvidas ao longo do tempo. Não são etapas de um processo nem uma lista de elementos obrigatórios. São proposições a partir das quais os demais conceitos deste guia podem ser organizados.

Métodos e frameworks apresentam maneiras particulares de lidar com problemas. Eles definem processos, práticas, artefatos, papéis e técnicas adequados a determinados domínios e situações. Conhecer apenas essas formas de aplicação, porém, pode levar à utilização correta de uma prática sem uma compreensão suficiente do problema que ela procura resolver.

Os fundamentos permitem observar o que existe por trás dessas práticas. Ajudam a identificar condições, premissas, fatores que influenciam escolhas e consequências possíveis. Também permitem reconhecer relações entre disciplinas sem concluir que seus métodos sejam intercambiáveis.

Essa é a função dos fundamentos neste guia. Eles estabelecem uma camada de entendimento anterior à escolha de métodos e ferramentas. Primeiro procuramos compreender a estrutura da decisão; depois identificamos quais práticas são adequadas ao domínio e à situação.

Para quem já trabalha com arquitetura, gestão, estratégia, empreendedorismo ou tomada de decisão, muitas dessas ideias são familiares. Elas aparecem na prática com diferentes nomes e níveis de formalização. O objetivo não é reivindicar conceitos inéditos, mas tornar explícita uma lógica que costuma estar distribuída entre diferentes disciplinas.

Os seis fundamentos a seguir estabelecem essa base.

## 1.1 Toda decisão ocorre dentro de um domínio

Toda decisão ocorre dentro de um domínio de conhecimento, atividade ou problema. O domínio estabelece o campo no qual ela é compreendida e fornece conceitos, conhecimentos, critérios e práticas utilizados para interpretar situações e avaliar alternativas.

Ele não determina uma única resposta. Diferentes decisões podem ocorrer dentro do mesmo domínio, com objetivos, alternativas e critérios distintos. O conhecimento especializado fornece referências para a análise, mas não elimina a necessidade de escolher entre possibilidades.

Uma decisão de arquitetura de software, por exemplo, pertence ao domínio da arquitetura de soluções. Nesse campo, conceitos como componentes, interfaces, tecnologias, atributos de qualidade e dependências fazem parte da linguagem utilizada para compreender situações e avaliar alternativas.

Uma decisão de gestão de projetos mobiliza conceitos como escopo, prazo, orçamento, recursos, riscos e dependências. Uma decisão empreendedora pode envolver clientes, mercado, proposta de valor, modelo de negócio e alocação de recursos.

Cada domínio possui conhecimentos e práticas próprios porque os problemas, critérios e formas de avaliação não são iguais em todas as áreas.

Ainda assim, decisões de diferentes domínios podem compartilhar propriedades que permitem analisá-las por uma perspectiva comum. Essa possibilidade de identificar padrões entre áreas distintas é uma das bases da Arquitetura de Decisão.

## 1.2 Toda decisão parte de um contexto inicial

Uma decisão parte de uma situação existente. O contexto inicial reúne as condições relevantes para compreendê-la no momento em que a escolha é realizada.

Essas condições podem incluir objetivos existentes, recursos disponíveis, restrições, informações, evidências, premissas, compromissos, dependências e outros fatores que influenciam as alternativas consideradas.

O contexto não é estático. Ele representa uma situação em determinado momento e pode mudar à medida que novas informações surgem, recursos são consumidos, restrições são alteradas ou decisões anteriores produzem efeitos.

O mesmo domínio pode apresentar contextos completamente diferentes. Uma decisão de arquitetura de software, por exemplo, pode ocorrer em um sistema novo ou legado, com diferentes requisitos, orçamentos, tecnologias, competências disponíveis e restrições regulatórias.

Compreender o contexto inicial significa identificar as condições que tornam determinadas alternativas possíveis, desejáveis ou inviáveis naquele momento.

A referência temporal é importante porque a escolha parte de uma situação existente e contribui para produzir uma situação diferente.

## 1.3 Toda decisão é orientada por um objetivo ou meta

Uma decisão está relacionada a um resultado que se pretende alcançar, preservar ou evitar. Esse resultado orienta a avaliação das alternativas e fornece uma referência para determinar se a escolha atende ao que se pretende obter.

Objetivos descrevem resultados pretendidos. Metas tornam esses resultados mais específicos ao estabelecer condições de realização, como valores, limites ou prazos.

Por exemplo, reduzir o tempo de entrega é um objetivo. Reduzir o tempo médio de entrega de dez para cinco dias até o final do trimestre é uma meta associada a esse objetivo.

Nem sempre o objetivo está completamente definido no início. A análise pode revelar que a formulação inicial era inadequada, incompleta ou incompatível com as condições existentes. Nesse caso, ele pode ser revisado antes da escolha.

Isso cria uma relação importante entre objetivo e problema. Uma situação se torna um problema em relação a algum resultado pretendido. Se esse resultado muda, a interpretação da situação também pode mudar.

Por isso, definir o que queremos alcançar faz parte da estrutura da decisão, mas essa definição pode ser refinada durante a análise.

## 1.4 Toda decisão ocorre sob incerteza

Uma decisão envolve escolher entre possibilidades sem conhecer completamente suas consequências. Quanto maior o desconhecimento sobre os efeitos das alternativas ou sobre as condições futuras, maior a incerteza envolvida.

Isso não significa que todas as decisões tenham o mesmo grau de incerteza. Algumas contam com grande quantidade de dados, experiência e evidências. Outras precisam ser tomadas com informações escassas e muitas incógnitas. Também existem situações em que as consequências de uma alternativa são praticamente conhecidas. Nesses casos, a decisão pode se aproximar de uma execução determinada.

A incerteza não precisa ser eliminada antes de agir. Podemos buscar informações, consultar especialistas, testar hipóteses, executar experimentos ou aguardar novos dados. Cada alternativa, porém, possui seu próprio custo. Investigar mais pode reduzir o desconhecimento, mas também consumir tempo, recursos ou oportunidades.

Decidir envolve avaliar não apenas quais alternativas estão disponíveis, mas também quanto vale a pena aprender antes de agir e quando o conhecimento disponível já é suficiente para avançar.

Hipóteses, evidências, experimentos, aprendizado e gestão de risco são diferentes formas de lidar com aquilo que ainda não sabemos.

## 1.5 Toda decisão altera o espaço de possibilidades

Uma decisão produz mais do que um resultado imediato. Ela pode comprometer recursos, criar dependências, estabelecer restrições, eliminar caminhos ou tornar determinadas mudanças mais custosas. Também pode preservar opções, gerar novas alternativas ou produzir informação útil para decisões posteriores.

Alterar o espaço de possibilidades não significa necessariamente reduzir opções. Uma escolha pode eliminar determinados caminhos e, ao mesmo tempo, criar outros. Pode tornar uma alternativa mais acessível, outra mais cara e uma terceira inviável.

Essa dinâmica pode ser observada pela ideia de opcionalidade. Algumas escolhas preservam maior capacidade de mudança futura; outras aumentam compromissos e reduzem a margem de manobra.

O tempo torna essa dinâmica ainda mais evidente. Adiar uma escolha pode permitir que novas informações surjam, mas também pode fazer uma oportunidade desaparecer, consumir recursos ou permitir que outras pessoas decidam primeiro. Permanecer no estado atual não significa permanecer diante das mesmas alternativas.

É nesse sentido que não decidir também pode constituir uma decisão. Não porque ação e inação sejam equivalentes, mas porque a ausência de uma escolha deliberada também pode produzir efeitos sobre o que será possível fazer posteriormente.

Consequências, dependências, compromissos, reversibilidade, irreversibilidade, custo de oportunidade, opcionalidade e path dependency são diferentes maneiras de analisar essa transformação.

Uma decisão deve, portanto, ser observada não apenas pelo resultado que produz, mas também pelas condições que deixa para as escolhas seguintes.

## 1.6 Toda decisão participa de um processo de evolução

Uma decisão modifica a situação seguinte. A execução produz informação, as consequências revelam efeitos esperados e inesperados e novas condições podem exigir ajustes de direção.

Neste guia, evolução significa mudança de estado ao longo do tempo. Não implica necessariamente melhoria. Um sistema pode evoluir para uma situação mais adequada aos seus objetivos, mas também pode acumular restrições, dependências, custos ou problemas que dificultem mudanças posteriores.

Planejamento, execução, observação e aprendizado fazem parte dessa dinâmica. Uma decisão pode ser mantida, revista ou substituída conforme surgem novos dados. Modelos como PDCA e OODA representam diferentes formas de organizar ciclos desse tipo. Não são modelos de Arquitetura de Decisão, mas ajudam a ilustrar a relação entre ação, observação, aprendizado e mudança.

Quando esse processo se repete, escolhas anteriores passam a influenciar as seguintes. Elas geram dependências, compromissos, restrições e aprendizados que se incorporam ao estado atual do sistema.

É nesse sentido que uma arquitetura pode ser compreendida como uma estrutura que também resulta das decisões acumuladas ao longo da evolução de um sistema.

Os seis fundamentos formam uma estrutura conceitual. A decisão ocorre dentro de um domínio, parte de um contexto inicial, é orientada por um objetivo ou meta, acontece sob incerteza, modifica o espaço de possibilidades e passa a fazer parte da evolução do sistema.

Essa estrutura pode ser observada em diferentes domínios sem pressupor que sejam equivalentes. Na arquitetura de soluções, na gestão de projetos, no empreendedorismo e em decisões profissionais ou pessoais, os fundamentos assumem formas próprias conforme os problemas, conhecimentos e condições envolvidos.

É nesse sentido que a Arquitetura de Decisão é transversal: não porque exista um método comum que possa ser aplicado indistintamente a todos os domínios, mas porque os mesmos fundamentos permitem observar a dinâmica das decisões em diferentes campos.

A partir dessa base, podemos examinar os elementos que compõem uma decisão e compreender como eles se relacionam, variam conforme o domínio e assumem formas diferentes em cada situação.
