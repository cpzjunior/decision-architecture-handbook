# 1. Fundamentos da Arquitetura de Decisão

Os fundamentos da Arquitetura de Decisão são os princípios que orientam como decisões podem ser compreendidas, estruturadas e desenvolvidas ao longo do tempo. Não são etapas de um processo nem uma lista de elementos obrigatórios. São referências conceituais a partir das quais os demais conceitos deste guia podem ser organizados.

Conhecer esses princípios é importante porque métodos e frameworks apresentam maneiras particulares de lidar com problemas. Eles definem processos, práticas, artefatos, papéis e técnicas adequados a determinadas situações. Quando conhecemos apenas essas formas de aplicação, podemos utilizar uma prática corretamente sem compreender completamente o problema que ela procura resolver.

Os princípios permitem enxergar além da prática. Ajudam a identificar quais condições justificam determinado método, quais premissas estão envolvidas e quais aspectos pertencem ao problema ou à maneira escolhida para tratá-lo. Também permitem reconhecer relações entre disciplinas sem concluir que suas abordagens sejam intercambiáveis.

Essa é a função dos fundamentos neste guia. Eles estabelecem uma camada de entendimento anterior à escolha de métodos e ferramentas. Primeiro procuramos compreender a natureza da situação e das decisões envolvidas; depois identificamos quais práticas são adequadas ao domínio e ao momento.

Para quem já trabalha com arquitetura, gestão, estratégia, empreendedorismo ou tomada de decisão, muitas dessas ideias são familiares. Elas aparecem na prática com diferentes nomes e níveis de formalização. O objetivo não é reivindicar conceitos inéditos, mas tornar explícita uma lógica que costuma estar distribuída entre diferentes disciplinas.

Os cinco fundamentos a seguir estabelecem essa base.

## 1.1 Toda decisão ocorre sob incerteza

Uma decisão surge quando precisamos escolher entre possibilidades sem conhecer completamente suas consequências. Quanto maior o desconhecimento sobre os efeitos das alternativas ou sobre as condições futuras, maior a incerteza envolvida.

Isso não significa que todas as decisões tenham o mesmo grau de incerteza. Algumas contam com grande quantidade de dados, experiência e evidências. Outras precisam ser tomadas com informações escassas e muitas incógnitas. Também existem situações em que as consequências de uma alternativa são praticamente conhecidas. Nesses casos, a decisão pode se aproximar de uma execução determinada.

A incerteza não precisa ser eliminada antes de agir. Podemos buscar informação, consultar especialistas, testar hipóteses, executar experimentos ou aguardar novos dados. Cada alternativa, porém, possui seu próprio custo. Investigar mais pode reduzir o desconhecimento, mas também consumir tempo, recursos ou oportunidades.

Decidir envolve avaliar não apenas quais alternativas estão disponíveis, mas também quanto vale a pena aprender antes de agir e quando o conhecimento disponível já é suficiente para avançar.

Hipóteses, evidências, experimentos, aprendizado e gestão de risco são diferentes formas de lidar com aquilo que ainda não sabemos. A maneira como essas práticas são utilizadas depende do campo em que a decisão ocorre.

## 1.2 Toda decisão ocorre dentro de um domínio

Toda decisão ocorre dentro de um domínio de conhecimento, atividade ou problema. O domínio estabelece o campo no qual a decisão é compreendida e fornece conceitos, conhecimentos, critérios e práticas utilizados para interpretar problemas e avaliar alternativas.

O domínio não determina uma única resposta. Diferentes decisões podem ser tomadas dentro do mesmo domínio, com objetivos, alternativas e critérios distintos. O conhecimento do domínio fornece referências para a decisão, mas não elimina a incerteza nem substitui o raciocínio necessário para escolher entre possibilidades.

Uma decisão de arquitetura de software, por exemplo, pertence ao domínio da arquitetura de soluções. Nesse domínio, conceitos como componentes, interfaces, tecnologias, atributos de qualidade e dependências fazem parte da linguagem utilizada para compreender o problema e avaliar alternativas.

Uma decisão de gestão de projetos pertence a outro domínio e mobiliza conceitos como escopo, prazo, orçamento, recursos, riscos e dependências. Uma decisão empreendedora pode envolver clientes, mercado, proposta de valor, modelo de negócio e alocação de recursos.

Cada domínio possui conhecimentos e práticas próprios. Essa especialização é necessária porque os problemas, critérios e formas de avaliação não são iguais em todas as áreas.

Ainda assim, decisões de diferentes domínios podem compartilhar propriedades que permitem analisá-las por uma perspectiva comum. É essa possibilidade de identificar padrões entre áreas distintas que permite à Arquitetura de Decisão estabelecer uma linguagem transversal.

## 1.3 Toda decisão é contextual

Nenhuma decisão existe isoladamente das condições em que é realizada. A mesma alternativa pode produzir resultados diferentes conforme os objetivos, recursos, restrições, informações disponíveis e condições esperadas.

O contexto descreve as condições particulares em que uma decisão ocorre. Objetivos indicam o que se pretende alcançar. Restrições estabelecem limites. Informações e evidências ajudam a caracterizar a situação. Premissas registram aquilo que estamos considerando verdadeiro ou provável para poder avançar.

Domínio e contexto, portanto, cumprem papéis diferentes. O domínio define o campo de conhecimento ou atividade no qual a decisão é compreendida; o contexto define as condições particulares nas quais ela ocorre.

Uma decisão de arquitetura de software pode pertencer ao mesmo domínio em diferentes organizações, mas apresentar contextos completamente distintos. Requisitos, orçamento, sistemas existentes, regulamentações, competências disponíveis e prioridades podem alterar significativamente as alternativas e os critérios utilizados.

Essas condições também mudam. Um novo concorrente, uma nova tecnologia, uma alteração orçamentária, uma mudança de prioridade ou uma informação anteriormente desconhecida pode modificar significativamente a situação. Uma alternativa que fazia sentido em determinado momento pode deixar de ser adequada posteriormente sem que a decisão original tenha sido equivocada.

Compreender o contexto significa identificar as condições que tornam determinadas alternativas possíveis, desejáveis ou inviáveis. Essas condições não permanecem necessariamente as mesmas depois que uma decisão é tomada. A própria decisão pode modificar recursos, compromissos, informações e restrições presentes posteriormente.

Por isso, compreender uma decisão exige observar não apenas as condições em que ela foi tomada, mas também o estado que ela ajuda a produzir.

## 1.4 Toda decisão altera o espaço de possibilidades

Uma decisão produz mais do que um resultado imediato. Ela pode comprometer recursos, criar dependências, estabelecer restrições, eliminar caminhos ou tornar determinadas mudanças mais custosas. Também pode preservar opções, gerar novas alternativas ou produzir informação útil para decisões posteriores.

Alterar o espaço de possibilidades não significa necessariamente reduzir opções. Uma decisão pode eliminar determinados caminhos e, ao mesmo tempo, criar outros. Pode tornar uma alternativa mais acessível, outra mais cara e uma terceira inviável. Pode ainda preservar possibilidades que seriam perdidas caso outro caminho fosse escolhido.

Essa dinâmica pode ser observada pela ideia de opcionalidade. Algumas decisões preservam maior capacidade de mudança futura; outras aumentam compromissos e reduzem a margem de manobra. O valor de uma decisão, portanto, pode estar não apenas no resultado que entrega agora, mas também nas possibilidades que preserva ou cria para depois.

O tempo torna essa dinâmica ainda mais evidente. Adiar uma decisão pode permitir que novas informações surjam, mas também pode fazer uma oportunidade desaparecer, consumir recursos ou permitir que outras pessoas decidam primeiro. Permanecer no estado atual não significa permanecer diante das mesmas alternativas.

É nesse sentido que não decidir também pode constituir uma decisão. Não porque ação e inação sejam equivalentes, mas porque a ausência de uma escolha deliberada também pode produzir efeitos sobre o que será possível fazer posteriormente.

Consequências, dependências, compromissos, reversibilidade, irreversibilidade, custo de oportunidade, opcionalidade e path dependency são diferentes maneiras de analisar essa transformação.

Uma decisão deve, portanto, ser observada não apenas pelo que produz, mas também pelas condições que deixa para as decisões seguintes.

## 1.5 Toda decisão participa de um processo de evolução

Uma decisão modifica a situação seguinte. A execução produz informação, as consequências revelam efeitos esperados e inesperados e novas condições podem exigir ajustes de direção.

Neste guia, evolução significa mudança de estado ao longo do tempo. Não implica necessariamente melhoria. Um sistema pode evoluir para uma situação mais adequada aos seus objetivos, mas também pode acumular restrições, dependências, custos ou problemas que dificultem mudanças posteriores.

Planejamento, execução, observação e aprendizado fazem parte dessa dinâmica. Uma decisão pode ser mantida, revista ou substituída conforme surgem novos dados. Modelos como PDCA e OODA representam diferentes formas de organizar ciclos desse tipo. Não são modelos de Arquitetura de Decisão, mas ajudam a ilustrar a relação entre ação, observação, aprendizado e mudança.

Quando esse processo se repete, decisões anteriores passam a influenciar as seguintes. Elas geram dependências, compromissos, restrições e aprendizados que se incorporam ao estado atual do sistema.

É nesse sentido que uma arquitetura pode ser compreendida como uma estrutura que também resulta das decisões acumuladas ao longo da evolução de um sistema.

Os cinco fundamentos formam uma sequência conceitual. A decisão parte de conhecimento incompleto, ocorre dentro de um domínio, é realizada sob condições particulares, modifica o espaço de possibilidades e passa a fazer parte da evolução do sistema.

Essa sequência permite observar diferentes formas de arquitetura sem pressupor que seus domínios sejam equivalentes. Na arquitetura de soluções, na gestão de projetos, no empreendedorismo e em decisões profissionais ou pessoais, os fundamentos assumem formas próprias conforme os problemas, conhecimentos e condições envolvidos.

É nesse sentido que a Arquitetura de Decisão é transversal: não porque exista um método comum que possa ser aplicado indistintamente a todos os domínios, mas porque os mesmos fundamentos permitem observar a dinâmica das decisões em diferentes campos.

A partir dessa base, podemos examinar os elementos que compõem uma decisão e compreender como eles se relacionam, variam conforme o domínio e assumem formas diferentes em cada contexto.
