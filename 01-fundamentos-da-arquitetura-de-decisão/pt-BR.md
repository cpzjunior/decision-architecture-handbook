# 1. Fundamentos da Arquitetura de Decisão

Os fundamentos da Arquitetura de Decisão são referências que orientam como decisões podem ser compreendidas, estruturadas e desenvolvidas ao longo do tempo. Não são etapas de um processo nem uma lista de elementos obrigatórios. São proposições a partir das quais os demais conceitos deste guia podem ser organizados.

Métodos e frameworks apresentam maneiras particulares de lidar com problemas. Eles definem processos, práticas, artefatos, papéis e técnicas adequados a determinados domínios e situações. Conhecer apenas essas formas de aplicação, porém, pode levar à utilização correta de uma prática sem uma compreensão suficiente da necessidade que ela procura atender.

Os fundamentos permitem observar o que existe por trás dessas práticas. Eles ajudam a identificar as condições que influenciam uma decisão, os objetivos que orientam a escolha, aquilo que ainda não conhecemos, as alternativas disponíveis e as consequências que podem alterar decisões futuras.

Essa perspectiva também permite reconhecer relações entre disciplinas sem concluir que seus métodos sejam intercambiáveis. Práticas desenvolvidas em arquitetura, gestão, empreendedorismo, desenvolvimento de produtos ou outras áreas podem responder a necessidades semelhantes, ainda que utilizem linguagens, processos e artefatos diferentes.

Essa é a função dos fundamentos neste guia. Eles estabelecem uma camada de entendimento anterior à escolha de métodos e ferramentas. Primeiro procuramos compreender a estrutura da decisão e as necessidades que ela produz; depois identificamos quais práticas podem atender a essas necessidades e quais frameworks podem organizá-las.

Para quem já trabalha com arquitetura, gestão, estratégia, empreendedorismo ou tomada de decisão, muitas dessas ideias são familiares. Elas aparecem na prática com diferentes nomes e níveis de formalização. O objetivo não é reivindicar conceitos inéditos, mas tornar explícita uma lógica que costuma estar distribuída entre diferentes disciplinas.

Os seis fundamentos a seguir estabelecem essa base.

## 1.1. Toda decisão ocorre dentro de um ou mais domínios

Toda decisão ocorre dentro de um ou mais domínios de conhecimento, atividade ou problema. O domínio estabelece o campo no qual a decisão é compreendida e fornece conceitos, conhecimentos, critérios e práticas utilizados para interpretar situações e avaliar alternativas.

Uma decisão sobre uma plataforma de pagamentos, por exemplo, pode exigir conhecimentos de arquitetura, segurança, finanças, produto, operações e regulamentação. Cada domínio contribui com referências próprias para compreender diferentes aspectos da decisão.

A participação de diferentes domínios não significa apenas reunir especialistas em uma mesma discussão. Cada domínio pode enxergar uma parte diferente da situação e utilizar critérios diferentes para avaliar as alternativas. Uma alternativa tecnicamente adequada pode ser inviável do ponto de vista financeiro. Uma solução financeiramente atraente pode criar riscos operacionais. Uma decisão adequada para o produto pode entrar em conflito com uma restrição regulatória.

Por isso, o domínio não é apenas o assunto sobre o qual estamos falando. Ele influencia o que consideramos relevante, quais conceitos utilizamos e quais perguntas precisam ser feitas.

Uma decisão de arquitetura de software mobiliza conceitos como componentes, interfaces, tecnologias, atributos de qualidade e dependências. Uma decisão de gestão de projetos pode envolver escopo, prazo, orçamento, recursos, riscos e dependências. Uma decisão empreendedora pode envolver clientes, mercado, proposta de valor, modelo de negócio e alocação de recursos.

O conhecimento especializado fornece referências para a análise, mas não determina uma única resposta. Duas decisões podem ocorrer no mesmo domínio e chegar a escolhas diferentes porque possuem objetivos, condições, restrições ou alternativas diferentes.

Isso também explica por que práticas desenvolvidas em um domínio não devem ser transferidas automaticamente para outro. Uma prática pode fazer sentido porque responde a uma necessidade específica daquele campo e porque seus conceitos, critérios e artefatos foram construídos para determinadas condições.

A primeira necessidade produzida por essa característica é a delimitação do domínio. Precisamos saber em quais campos a decisão se insere, quais conhecimentos são relevantes, quais participantes precisam ser considerados e quais limites definem aquilo que está sendo analisado.

Delimitar não significa necessariamente escolher um único domínio. Uma decisão pode deliberadamente atravessar fronteiras entre áreas. O objetivo é tornar essas fronteiras visíveis para que possamos compreender quais perspectivas fazem parte da decisão e quais conhecimentos precisamos mobilizar.

Essa necessidade pode ser atendida por práticas como definição de escopo, identificação de fronteiras, modelagem de domínio, identificação de stakeholders e construção de uma linguagem comum. Frameworks diferentes organizam essas práticas de maneiras diferentes, mas todos estão, em alguma medida, respondendo à necessidade de compreender onde a decisão está inserida.

## 1.2. Toda decisão parte de um contexto inicial

Toda decisão parte de uma situação existente. O contexto inicial reúne as condições relevantes para compreender a decisão no momento em que ela é considerada.

Domínio e contexto não são a mesma coisa. O domínio define o campo em que a decisão faz sentido e fornece as referências utilizadas para compreendê-la. O contexto define as condições particulares nas quais ela ocorre.

Essas condições podem incluir recursos disponíveis, restrições, informações, evidências, premissas, compromissos, dependências, decisões anteriores e outras circunstâncias que influenciam as possibilidades consideradas.

O mesmo domínio pode apresentar contextos completamente diferentes. Uma decisão de arquitetura pode ocorrer em um sistema novo ou em um ambiente legado. Pode existir uma equipe experiente ou uma equipe que ainda precisa adquirir conhecimento. Pode haver orçamento disponível ou uma restrição financeira significativa. Pode existir liberdade tecnológica ou uma dependência contratual que limite as alternativas.

Essas diferenças não são detalhes periféricos. Elas podem alterar completamente o conjunto de alternativas viáveis e a forma como cada alternativa deve ser avaliada.

O contexto também não é estático. Novas informações podem surgir, recursos podem ser consumidos, restrições podem mudar e decisões anteriores podem produzir efeitos inesperados. Por isso, o contexto considerado no início de uma decisão pode não ser exatamente o mesmo contexto encontrado durante sua realização.

Essa característica também explica por que experiência anterior não pode ser tratada como uma solução pronta. Uma experiência passada pode fornecer referências úteis, padrões e hipóteses, mas sua aplicabilidade depende das condições atuais.

A experiência fornece referências. O contexto determina sua aplicabilidade.

A segunda necessidade produzida por essa característica é a explicitação das condições da decisão. Precisamos identificar o que existe, quais recursos estão disponíveis, quais restrições precisam ser respeitadas, quais premissas estão sendo assumidas, quais dependências existem e quais informações ainda não estão disponíveis.

Essa necessidade é atendida por práticas de diagnóstico, levantamento de restrições, identificação de premissas, análise de dependências, compreensão do ambiente existente e identificação das condições atuais. O objetivo não é descrever toda a realidade, mas tornar visíveis as condições que realmente influenciam a decisão.

Isso é particularmente importante quando um método ou framework será aplicado. As práticas de um framework foram desenvolvidas para atender determinadas necessidades e pressupõem determinadas condições de aplicação. Utilizá-las sem verificar se essas condições existem pode produzir uma situação em que seguimos corretamente o método, mas tratamos um problema diferente daquele que realmente temos.

É nesse ponto que aparece uma das diferenças entre conhecer um método e saber utilizá-lo. A aplicação adequada de uma prática depende da capacidade de reconhecer as condições para as quais ela foi concebida e verificar se essas condições estão presentes na situação atual.

## 1.3. Toda decisão é orientada por um ou mais objetivos

Toda decisão está relacionada a um ou mais resultados que se pretende alcançar, preservar ou evitar. Esses objetivos orientam, de forma explícita ou implícita, a avaliação das alternativas e fornecem uma referência para determinar o que se espera obter.

Um objetivo pode estar claramente formulado ou permanecer implícito. Uma pessoa pode decidir reduzir custos sem ter definido previamente quanto pretende reduzir ou em quanto tempo. Uma organização pode decidir modernizar um sistema sem ter esclarecido se o objetivo principal é reduzir custos, aumentar capacidade, diminuir riscos ou permitir uma nova estratégia de negócio.

A existência de um objetivo implícito não significa que a decisão seja necessariamente inválida. Significa que parte da lógica que orienta a escolha ainda não foi explicitada.

Quando os objetivos não são identificados ou compreendidos por quem decide, temos uma decisão cega. A decisão ainda possui uma direção ou finalidade, mas ela não está suficientemente clara para orientar a análise de forma consciente e verificável.

A explicitação dos objetivos também permite comparar alternativas. Sem saber o que estamos tentando alcançar, podemos comparar soluções com base em preferências, familiaridade ou critérios circunstanciais que não representam aquilo que realmente importa.

Os objetivos também podem entrar em conflito. Reduzir custos pode entrar em conflito com aumentar qualidade. Acelerar uma entrega pode aumentar riscos. Preservar uma arquitetura existente pode limitar mudanças futuras. Aumentar flexibilidade pode elevar complexidade.

Por isso, definir objetivos não significa simplesmente produzir uma lista. É necessário compreender as relações entre eles e reconhecer quando uma alternativa atende bem a um objetivo, mas produz consequências desfavoráveis em outro.

Os objetivos também podem mudar durante a análise. Novas informações podem mostrar que aquilo que parecia importante inicialmente não é mais relevante, que um objetivo é inviável nas condições existentes ou que existe um resultado mais importante que não havia sido considerado.

Isso cria uma relação importante entre objetivo e problema. Uma situação se torna um problema em relação a algum resultado pretendido. Se o objetivo muda, a interpretação da situação também pode mudar.

Por exemplo, “substituir o sistema atual” pode parecer inicialmente um problema técnico. Mas, se o objetivo real for reduzir o tempo necessário para lançar novos produtos, talvez substituir o sistema inteiro não seja a única alternativa. O problema pode estar relacionado a uma capacidade específica, e não necessariamente à tecnologia como um todo.

Nesse sentido, problema e objetivo não devem ser tratados como elementos completamente independentes. A definição do que precisa ser resolvido depende, em parte, do resultado que consideramos necessário alcançar.

A terceira necessidade produzida por essa característica é a definição de critérios de avaliação. Se existem objetivos, precisamos de referências que permitam avaliar alternativas e verificar posteriormente se o resultado alcançado atende ao que se pretendia.

Esses critérios podem assumir diferentes formas. Podem ser requisitos, métricas, indicadores, atributos de qualidade, condições de sucesso, limites aceitáveis ou outras referências adequadas ao domínio e ao objetivo. Nem todo objetivo precisa ser reduzido a uma métrica. O importante é existir uma forma suficientemente clara de avaliar a relação entre a escolha e aquilo que se pretende alcançar.

## 1.4. Toda decisão envolve algum grau de incerteza

Uma decisão envolve escolher entre possibilidades sem conhecer completamente suas consequências ou as condições futuras. O grau de incerteza varia conforme a quantidade e a qualidade das informações disponíveis, a experiência acumulada e a previsibilidade da situação.

Algumas decisões contam com grande quantidade de dados e evidências. Outras precisam ser tomadas com informações escassas e muitas incógnitas. Também existem situações em que as consequências de uma alternativa são amplamente conhecidas. Nesses casos, a incerteza pode ser pequena, mas ainda existe uma escolha sobre como agir.

A incerteza também pode ter origens diferentes. Podemos não conhecer suficientemente o problema, não saber como uma solução irá funcionar, não conseguir prever o comportamento de usuários ou clientes, depender de fatores externos ou não saber como determinadas variáveis irão evoluir.

Essa distinção é importante porque diferentes tipos de incerteza exigem diferentes formas de investigação. Quando não compreendemos o problema, precisamos aprender sobre a situação. Quando não sabemos se uma solução funciona, podemos precisar experimentar. Quando conhecemos as alternativas, mas não sabemos quais consequências ocorrerão, podemos precisar analisar riscos e cenários.

A incerteza não precisa ser eliminada antes de agir. Podemos buscar informações, consultar especialistas, testar hipóteses, executar experimentos, construir protótipos ou aguardar novos dados.

Cada alternativa, porém, possui seu próprio custo. Investigar mais pode reduzir o desconhecimento, mas também consumir tempo, recursos ou oportunidades. Um experimento pode gerar evidências, mas exige investimento. Esperar por mais informações pode melhorar uma decisão ou simplesmente atrasar uma ação necessária.

Decidir envolve, portanto, avaliar não apenas quais alternativas estão disponíveis, mas também quanto vale a pena aprender antes de agir.

Essa avaliação também depende da natureza das consequências. Quando uma decisão é facilmente reversível, pode ser aceitável avançar com maior grau de incerteza. Quando uma escolha cria compromissos difíceis de desfazer, o custo de uma decisão prematura pode ser muito maior.

A quarta necessidade produzida por essa característica é o tratamento do desconhecido. Precisamos identificar aquilo que ainda não sabemos, avaliar sua importância e decidir como lidar com essa incerteza.

Hipóteses, evidências, experimentos, protótipos, pesquisas, cenários, riscos e oportunidades são diferentes formas de tratar aquilo que ainda não conhecemos.

Lean Startup, por exemplo, estrutura práticas para transformar hipóteses em experimentos e aprendizado. Design Thinking utiliza atividades de investigação, prototipação e teste para aprender sobre necessidades e possíveis soluções. Gestão de riscos estrutura a identificação e análise de eventos incertos e suas possíveis consequências.

Essas abordagens não são equivalentes e não devem ser aplicadas apenas porque uma decisão contém incerteza. A questão é compreender qual incerteza existe, qual conhecimento está faltando e qual prática pode produzir evidência relevante para a decisão.

## 1.5. Toda decisão produz consequências diretas e indiretas

Uma decisão produz mais do que um resultado imediato. Ela pode comprometer recursos, criar dependências, estabelecer restrições, eliminar caminhos ou tornar determinadas mudanças mais custosas. Algumas dessas consequências aparecem diretamente após a decisão, enquanto outras surgem como efeitos indiretos daquilo que foi alterado.

As consequências também podem se propagar para outras partes da situação. Uma decisão sobre tecnologia pode alterar o trabalho de uma equipe. Uma decisão de projeto pode modificar responsabilidades, prazos ou recursos. Uma decisão de produto pode afetar clientes, usuários ou parceiros. Uma mudança organizacional pode criar novos compromissos para outras áreas.

Quando uma decisão produz efeitos sobre outras pessoas ou grupos, surge também uma necessidade de comunicação. É preciso tornar compreensível o que foi decidido, por que a decisão foi tomada, quais consequências são esperadas e o que muda para aqueles que serão afetados ou precisarão agir a partir dela. Nesse sentido, a comunicação não é apenas uma atividade posterior à decisão, mas parte do tratamento de suas consequências.

Uma decisão também pode preservar opções, gerar novas alternativas ou produzir informação útil para decisões posteriores. Seus efeitos, portanto, não se limitam ao que acontece imediatamente após a escolha. Algumas consequências modificam as condições nas quais outras decisões serão tomadas.

É nesse sentido que podemos compreender o espaço de possibilidades. Ele representa aquilo que pode ser feito a partir de determinado momento, considerando os recursos, compromissos, dependências e restrições existentes. As consequências de uma decisão podem alterar esse espaço, tornando algumas possibilidades mais acessíveis, outras mais difíceis e algumas inviáveis.

Alterar o espaço de possibilidades não significa necessariamente reduzir opções. Uma escolha pode eliminar determinados caminhos e, ao mesmo tempo, criar outros. Uma nova capacidade tecnológica pode abrir alternativas que não existiam. Uma decisão comercial pode criar acesso a um mercado e fechar outro.

Toda escolha também envolve trade-offs. Ao favorecer determinado resultado, uma decisão pode exigir concessões em outros objetivos, critérios ou possibilidades.

Melhorar desempenho pode aumentar custo. Reduzir prazo pode aumentar risco. Aumentar flexibilidade pode elevar complexidade. Preservar compatibilidade pode limitar a capacidade de evolução. Em muitos casos, não existe uma alternativa que maximize simultaneamente todos os objetivos.

Essa dinâmica pode ser observada pela ideia de opcionalidade. Algumas escolhas preservam maior capacidade de mudança futura. Outras aumentam compromissos e reduzem a margem de manobra. A consequência de uma decisão, portanto, também pode ser observada pela capacidade que ela preserva ou elimina para decisões posteriores.

A reversibilidade é relevante nesse ponto. Uma decisão fácil de desfazer produz consequências diferentes de uma decisão que exige grande esforço ou custo para ser revertida. Isso não significa que decisões reversíveis sejam sempre melhores, mas que sua estrutura de consequências é diferente.

O tempo torna essa dinâmica ainda mais evidente. Adiar uma escolha pode permitir que novas informações surjam, mas também pode fazer uma oportunidade desaparecer, consumir recursos ou permitir que outras decisões sejam tomadas antes.

Permanecer no estado atual não significa permanecer diante das mesmas alternativas. O próprio contexto continua evoluindo, e a ausência de uma decisão pode fazer com que determinadas opções se tornem mais caras, inviáveis ou simplesmente deixem de existir.

É nesse sentido que não decidir deliberadamente também pode constituir uma decisão. Existe diferença entre escolher conscientemente não agir e simplesmente não perceber que uma decisão precisava ser tomada, mas ambas as situações podem produzir efeitos sobre as possibilidades futuras.

A quinta necessidade produzida por essa característica é compreender, tratar e comunicar as consequências das alternativas consideradas. Isso envolve analisar não apenas qual alternativa produz determinado resultado, mas também quais efeitos diretos e indiretos ela pode gerar, quem pode ser afetado, como esses efeitos precisam ser comunicados e como a decisão modifica as condições para as próximas decisões.

Cenários, análise de alternativas, trade-offs, comunicação, coordenação, reversibilidade, dependências, custo de oportunidade, opcionalidade e path dependency são formas diferentes de tratar essa necessidade.

O objetivo não é encontrar uma alternativa universalmente melhor. É compreender como cada alternativa responde aos objetivos e às restrições existentes, quais consequências produz, quem pode ser afetado e como essas consequências alteram o espaço de possibilidades para o futuro.

## 1.6. Toda decisão participa de um processo de evolução

Uma decisão modifica a situação seguinte. As consequências produzidas pela decisão passam a fazer parte dessa nova situação, enquanto a execução produz informação, revela efeitos esperados e inesperados e pode criar novas condições que exigem ajustes de direção.

Neste guia, evolução significa mudança de estado ao longo do tempo. Não implica necessariamente melhoria.

Um sistema pode se aproximar de seus objetivos, mas também pode acumular restrições, dependências, custos ou problemas que dificultem mudanças posteriores. Uma organização pode aprender com uma decisão e, ao mesmo tempo, assumir compromissos que condicionam suas próximas escolhas.

Planejamento, execução, observação e aprendizado fazem parte dessa dinâmica. Uma decisão pode ser mantida, revista ou substituída conforme surgem novos dados.

Modelos como PDCA e OODA representam diferentes formas de organizar ciclos desse tipo. Não são modelos de Arquitetura de Decisão, mas ajudam a ilustrar uma dinâmica em que ação, observação, aprendizado e mudança estão relacionados.

Quando esse processo se repete, escolhas anteriores passam a influenciar as seguintes. Elas geram dependências, compromissos, restrições e aprendizados que passam a fazer parte das condições das próximas escolhas.

Essa acumulação também aparece na arquitetura de sistemas. A arquitetura atual pode ser vista como resultado de muitas decisões tomadas ao longo do tempo, algumas deliberadas, outras condicionadas pelas circunstâncias existentes.

Uma decisão arquitetural, por exemplo, pode introduzir uma tecnologia. Depois, essa tecnologia passa a influenciar a contratação de profissionais, a escolha de ferramentas, os custos operacionais e as decisões de integração. Uma decisão inicial, portanto, participa da formação das condições para decisões posteriores.

Isso significa que uma decisão não deve ser analisada apenas pelo estado existente no momento em que é tomada. Também precisamos considerar os efeitos que produz sobre a evolução e o conhecimento que gera para decisões futuras.

A sexta necessidade produzida por essa característica é a observação, o aprendizado e a preservação do conhecimento produzido pela evolução.

Precisamos conseguir observar o que aconteceu, comparar o resultado com aquilo que esperávamos e compreender as razões de eventuais diferenças.

Também precisamos conseguir recuperar informações relevantes sobre decisões anteriores quando novas decisões dependerem delas. Isso não significa documentar tudo. Significa preservar aquilo que será necessário para compreender decisões relevantes no futuro.

Dependendo do domínio, isso pode ser feito por meio de indicadores, feedback, retrospectivas, registros de decisão, documentação, experimentos ou outros mecanismos de aprendizado.

A rastreabilidade surge como uma forma de preservar esse conhecimento, mas ela não é o objetivo em si. O objetivo é manter a capacidade de compreender a evolução e utilizar o conhecimento produzido para orientar decisões futuras.

## 1.7. Como os fundamentos se relacionam

Os seis fundamentos não devem ser interpretados como seis assuntos independentes. Eles descrevem dimensões diferentes de uma mesma estrutura de decisão.

Uma decisão ocorre em um domínio, mas esse domínio sempre se manifesta dentro de um contexto específico. O contexto define condições que influenciam aquilo que pode ser feito. Dentro dessas condições, existem objetivos que orientam a escolha. Como o futuro não é completamente conhecido, existe incerteza. A decisão produz consequências diretas e indiretas, que podem afetar pessoas, recursos, sistemas e as condições para decisões futuras. Essas consequências passam a fazer parte da evolução e influenciam decisões posteriores.

Assim, podemos visualizar a estrutura de forma encadeada:

Domínio → contexto → objetivos → incerteza → consequências → evolução

Esse encadeamento não representa uma sequência de etapas. Uma mudança em qualquer dimensão pode afetar as demais.

Uma nova informação sobre o domínio pode alterar nossa compreensão do contexto. Uma mudança no contexto pode tornar um objetivo inviável ou revelar outro mais importante. Um objetivo diferente pode mudar quais alternativas são consideradas. Uma nova evidência pode reduzir uma incerteza. Uma decisão pode produzir consequências que eliminam uma alternativa futura ou criam uma nova possibilidade. Um resultado inesperado pode alterar novamente o contexto.

A decisão, portanto, não acontece dentro de uma estrutura estática. Ela acontece dentro de uma estrutura que se modifica enquanto aprendemos, escolhemos e agimos.

Essa relação ajuda a explicar por que diferentes práticas e frameworks podem parecer tão diferentes e, ainda assim, tratar necessidades relacionadas.

Podemos estabelecer uma segunda relação:

Característica → necessidade → prática → framework

O domínio produz a necessidade de delimitação. Essa necessidade pode ser tratada por práticas de definição de fronteiras, modelagem, escopo e linguagem comum. DDD, por exemplo, oferece práticas para compreender e delimitar domínios, estabelecer modelos e definir bounded contexts. Outras abordagens de arquitetura, gestão e análise de negócios também possuem práticas destinadas a tornar explícitos os limites daquilo que está sendo analisado.

O contexto produz a necessidade de explicitar as condições existentes. Isso pode envolver levantamento de restrições, premissas, dependências, situação atual, stakeholders e recursos disponíveis. arc42 trabalha explicitamente com contexto e escopo, restrições e estratégia de solução. TOGAF também estrutura atividades relacionadas à compreensão do ambiente, arquitetura e transição. Em projetos, práticas de planejamento e diagnóstico cumprem funções semelhantes.

Os objetivos produzem a necessidade de critérios de avaliação. Requisitos, métricas, indicadores, atributos de qualidade e critérios de sucesso são algumas das formas possíveis de atender essa necessidade. Scrum utiliza Product Goal e Sprint Goal para orientar o trabalho. PMBOK trabalha com objetivos, planejamento, entrega e medição. Em arquitetura, requisitos funcionais, atributos de qualidade e restrições ajudam a estabelecer referências para avaliar alternativas.

A incerteza produz a necessidade de tratar aquilo que ainda não conhecemos. Nesse caso, podemos utilizar análise de riscos, formulação de hipóteses, experimentação, prototipação, pesquisa, cenários ou outras práticas de investigação. Lean Startup utiliza experimentação e aprendizado para testar hipóteses. Design Thinking utiliza investigação, ideação, prototipação e teste para aprender sobre necessidades e possíveis soluções. Práticas de gestão de riscos tratam eventos incertos e suas possíveis consequências.

As consequências produzem a necessidade de analisar seus efeitos e tratar aqueles que precisam ser considerados pela decisão. Isso inclui compreender impactos diretos e indiretos, identificar quem pode ser afetado, comunicar mudanças relevantes, coordenar ações decorrentes e avaliar como a decisão modifica as condições para escolhas futuras. Nesse ponto aparecem práticas como análise de cenários, comparação de alternativas, identificação de trade-offs, análise de reversibilidade, avaliação de dependências, comunicação e coordenação. Em planejamento, diferentes opções de execução podem ser comparadas de acordo com seus impactos, custos, riscos e compromissos.

A evolução produz a necessidade de observar resultados, aprender e preservar conhecimento. Scrum incorpora inspeção e adaptação. Lean Startup estrutura ciclos de construção, medição e aprendizado. Retrospectivas permitem examinar a experiência de um ciclo e ajustar o seguinte. ADRs preservam conhecimento sobre decisões que continuam influenciando a evolução da arquitetura. Outros métodos e práticas utilizam mecanismos diferentes para atender à mesma necessidade fundamental.

Esses exemplos não significam que cada framework pertença a apenas um fundamento. Essa seria uma interpretação excessivamente rígida. Um framework pode atender várias necessidades ao mesmo tempo porque uma prática frequentemente atua sobre mais de uma dimensão da decisão.

Scrum, por exemplo, não trata apenas de evolução. Seus objetivos orientam o trabalho, seus mecanismos de inspeção produzem informação e sua adaptação permite revisar decisões conforme novas evidências surgem. Lean Startup não trata apenas de incerteza. Seus ciclos também conectam objetivos, evidências, resultados e evolução. arc42 não trata apenas de documentação. Sua estrutura relaciona contexto, objetivos, restrições, qualidade, decisões, riscos e conhecimento arquitetural.

O mesmo vale para as práticas de arquitetura. Uma decisão arquitetural precisa considerar o domínio em que o sistema existe, as condições atuais, os objetivos de qualidade e negócio, as incertezas técnicas, as alternativas disponíveis e as consequências que serão carregadas pela arquitetura ao longo do tempo.

Por isso, o framework não precisa ser o ponto de partida. Ele pode ser uma resposta a uma necessidade que já foi identificada.

Essa inversão é importante. Em vez de perguntar primeiro “qual framework devemos usar?”, podemos começar perguntando: “qual decisão estamos tentando conduzir?”, “quais características dessa decisão precisam ser tratadas?”, “quais necessidades surgem dessas características?” e, somente então, “quais práticas ou frameworks podem nos ajudar?”.

Os fundamentos, portanto, não procuram substituir DDD, TOGAF, arc42, Scrum, PMBOK, Lean Startup, Design Thinking, ADR ou outros métodos. Eles oferecem uma forma de enxergar o que essas abordagens estão tentando tratar e de reconhecer que diferentes disciplinas podem desenvolver respostas distintas para necessidades estruturalmente relacionadas.

Essa perspectiva será importante nos capítulos seguintes. Depois de compreender as características gerais de uma decisão, precisamos entrar na situação concreta em que ela acontece. Antes de definir qual problema resolver ou qual solução aplicar, precisamos compreender o domínio, o contexto, os limites e as condições existentes.

É a partir daí que a Arquitetura de Decisão deixa de ser apenas uma estrutura conceitual e passa a orientar a condução de uma decisão real.
