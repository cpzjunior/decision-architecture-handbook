# 2. Delimitando o Domínio de uma Decisão

Imagine um pesquisador interessado em estudar uma determinada espécie. Ele pode começar observando o animal, mas dificilmente compreenderá seu comportamento olhando apenas para o indivíduo. Antes, precisa entender onde aquela espécie está inserida, quais condições existem naquele ambiente, quais outros organismos participam dele e quais relações podem afetar seu comportamento. Só então as características observadas passam a ter significado.

Uma decisão possui dificuldade semelhante. Ela não acontece no vazio. Toda decisão está inserida em uma realidade que possui conceitos, elementos, regras, atores, relações, restrições e comportamentos próprios. Chamamos essa realidade de domínio.

Essa distinção é frequentemente ignorada na prática. É comum iniciar uma iniciativa definindo o objetivo, o problema, o requisito ou a solução desejada e somente depois investigar o contexto no qual essas definições foram formuladas. O problema é que o objetivo já contém uma hipótese sobre o que importa.

Começar pelo objetivo é, em certo sentido, começar na metade.

Um objetivo é uma proposição sobre uma realidade. Pretende alterar alguma coisa, preservar determinada condição, resolver uma situação ou alcançar um estado desejado. Para avaliar se essa proposição faz sentido, precisamos conhecer aquilo sobre o qual ela incide.

Considere uma instituição financeira que estabelece como objetivo reduzir o tempo necessário para abrir uma conta digital. A formulação parece clara. Podemos medir o tempo atual, definir uma meta, identificar gargalos e desenhar uma solução. Antes disso, porém, existe uma pergunta mais fundamental: o que exatamente está envolvido na abertura de uma conta?

A resposta não se limita à tela apresentada ao cliente. Existem requisitos regulatórios, mecanismos de identificação, validações de documentos, prevenção a fraude, sistemas legados, processos operacionais, responsabilidades de diferentes equipes, tratamento de exceções, dados e segurança. O tempo de abertura é apenas uma característica observável desse conjunto.

Talvez os dez minutos observados sejam consequência de uma etapa necessária para cumprir determinada regra. Talvez o maior problema esteja em uma validação posterior. Talvez reduzir o tempo aumente um risco que, naquele domínio, tenha consequências mais relevantes. Talvez o objetivo continue válido, mas precise ser reformulado diante dessas condições.

O domínio pode confirmar um objetivo, mas também pode reformulá-lo, restringi-lo ou mostrar que ele não faz sentido.

É por isso que sua precedência é conceitual, e não necessariamente operacional. Um método pode começar perguntando pelo objetivo, pelo problema ou pelo resultado esperado. Isso significa apenas que alguma compreensão do domínio foi assumida ou será construída ao longo do processo. Não altera a relação de dependência entre os conceitos.

Antes de decidir o que queremos mudar, precisamos saber sobre o que estamos decidindo.

## 2.1 Identificando o ecossistema do domínio

Antes de estabelecer os limites de um domínio, precisamos enxergar a realidade mais ampla na qual ele está inserido. Uma decisão raramente pertence a uma única dimensão. Mesmo quando parece concentrada em um processo, sistema ou área organizacional, seus efeitos podem atravessar diferentes partes da organização e ultrapassar suas fronteiras.

Podemos usar o conceito de ecossistema como uma analogia para essa visão macro. O domínio não é o ecossistema e não deve ser confundido com ele. O ecossistema representa o conjunto mais amplo no qual o domínio está inserido e ajuda a evitar que a investigação comece excessivamente próxima do objeto que já foi escolhido como foco.

Na abertura de uma conta digital, por exemplo, seria possível descrevê-la inicialmente como um problema de tecnologia: existe uma aplicação, alguns serviços e uma necessidade de melhorar o fluxo. Essa descrição é verdadeira, mas insuficiente. A mesma situação envolve clientes, operações, regulação, prevenção a fraude, segurança, dados, sistemas existentes e objetivos de negócio.

Se olharmos apenas para a aplicação, encontraremos principalmente problemas dentro da aplicação. Ao observar o conjunto, podemos descobrir que alguns deles são consequências de outras partes da organização.

O pesquisador que estuda uma espécie não precisa conhecer todo o ecossistema em profundidade, mas precisa saber o suficiente para entender onde o organismo está inserido. Sem essa visão, pode atribuir ao animal um comportamento que, na verdade, é consequência do ambiente.

Na arquitetura de decisões, a função é semelhante. Antes de perguntar qual é o domínio, precisamos saber em qual realidade ele está inserido. Isso reduz o risco de confundir o primeiro objeto encontrado com aquilo que efetivamente precisa ser estudado.

## 2.2 Delimitando um ou mais domínios

Com essa visão mais ampla, podemos estabelecer quais partes serão tratadas como domínio ou domínios da decisão.

Essa fronteira não é necessariamente única. Uma decisão pode envolver um domínio ou atravessar vários. Da mesma forma, aquilo que inicialmente parece uma única decisão pode precisar ser dividido em decisões relacionadas, enquanto preocupações aparentemente distintas podem exigir tratamento conjunto.

Na abertura de uma conta digital, podemos tratar o onboarding como uma única decisão. Também podemos separar decisões relacionadas à identificação do cliente, prevenção a fraude, aprovação da conta, experiência e operação. A escolha depende das relações entre essas preocupações, das responsabilidades envolvidas, das regras aplicáveis e do grau de autonomia de cada uma.

Não existe uma fronteira universalmente correta.

Uma organização pode tratar onboarding e prevenção a fraude conjuntamente porque suas regras e consequências são inseparáveis naquele contexto. Outra pode separá-los devido a responsabilidades, métricas, ciclos de evolução ou necessidades de governança diferentes. A fronteira, portanto, não é determinada apenas pela arquitetura técnica.

Isso também diferencia domínio de escopo. O domínio responde à pergunta “qual realidade estamos tratando?”. O escopo responde “qual parte dessa realidade estamos considerando?”. Podemos ter um domínio amplo e restringir o escopo de uma decisão a uma pequena parte dele.

No exemplo da conta digital, o domínio pode abranger toda a realidade relacionada à abertura de contas, enquanto uma decisão específica pode tratar apenas da validação de identidade. Outra pode concentrar-se no tratamento de exceções ou na prevenção a fraude.

Delimitar significa estabelecer uma fronteira que permita raciocinar com clareza sem pressupor que aquilo que ficou fora deixou de existir.

## 2.3 Identificando seus elementos

Estabelecidos os limites, precisamos observar o que existe dentro deles.

Um domínio é composto por elementos que participam da realidade que estamos estudando. Podem ser pessoas, organizações, recursos, processos, sistemas, documentos, eventos, capacidades, regras ou qualquer outro componente relevante para as decisões daquele domínio.

Na abertura de uma conta digital, encontramos clientes, documentos, dados cadastrais, mecanismos de validação, sistemas de identidade, mecanismos antifraude, operadores, sistemas legados, contas, regras regulatórias e processos internos.

Essa identificação muda a qualidade da conversa. “Precisamos melhorar a abertura de contas” é uma afirmação genérica. Quando os elementos são explicitados, surgem perguntas concretas: quem participa? Que informações são necessárias? Quais sistemas produzem ou consomem essas informações? Quem pode alterá-las? Quem é responsável por determinada decisão? Quais recursos e regras condicionam as interações?

O objetivo não é catalogar tudo que existe, mas tornar visíveis os elementos relevantes para o raciocínio. Uma arquitetura não se torna melhor por conter mais objetos documentados. O valor está em representar aqueles que ajudam a explicar o funcionamento do domínio.

Também surgem diferentes níveis de abstração. Um cliente pode ser visto como pessoa, relação contratual, identidade digital ou conjunto de dados, dependendo da perspectiva adotada. O mesmo elemento pode assumir significados diferentes quando observado a partir de outros domínios ou necessidades.

Por isso, identificar elementos não significa apenas nomeá-los. É preciso reconhecer o papel que desempenham dentro da fronteira estabelecida.

## 2.4 Compreendendo suas características

Os elementos, porém, não podem ser compreendidos apenas por sua existência. É necessário observar suas propriedades, condições, restrições e capacidades.

Na abertura de uma conta digital, um documento possui requisitos de validade. Um cliente pode estar sujeito a determinadas condições de identificação. Um operador possui responsabilidades e permissões específicas. Um mecanismo antifraude possui capacidades e limitações. Um sistema legado pode aceitar determinados formatos e rejeitar outros. Uma regra regulatória pode impor uma condição que precisa ser respeitada independentemente da tecnologia utilizada.

Essas propriedades ajudam a explicar por que elementos aparentemente semelhantes podem produzir resultados diferentes. Dois clientes podem iniciar o mesmo processo e exigir tratamentos distintos. Dois documentos podem representar identidade, mas apenas um atender às condições necessárias para determinada validação. Dois sistemas podem fornecer informações cadastrais, mas apenas um possuir autoridade sobre determinada informação.

Saber que um mecanismo antifraude existe, portanto, é diferente de conhecer os sinais que utiliza, as condições que considera relevantes, suas limitações e os efeitos de suas decisões sobre o processo. O mesmo vale para regras: reconhecer sua existência não significa compreender como se aplicam.

À medida que essas propriedades se tornam conhecidas, o domínio deixa de parecer um conjunto de elementos independentes. Suas características começam a explicar as condições sob as quais eles podem interagir e, consequentemente, os comportamentos que podem produzir.

## 2.5 Compreendendo comportamentos

A estrutura explica o que existe. O comportamento explica o que acontece.

Comportamentos representam mudanças, respostas, interações e consequências que surgem quando os elementos se relacionam sob determinadas condições.

Na abertura de uma conta digital, um documento inválido pode interromper o processo. Um sinal de risco pode direcionar uma solicitação para análise adicional. A indisponibilidade de um serviço externo pode impedir uma validação. Uma mudança regulatória pode alterar os critérios necessários para concluir a abertura. Um aumento inesperado no volume de solicitações pode modificar a operação.

Esses casos revelam uma dimensão que uma descrição estática não captura: o domínio possui dinâmica.

Por isso, listar entidades, componentes ou áreas não basta. Uma representação pode conter os elementos corretos e ainda assim distorcer o domínio se não explicar as relações e comportamentos que lhes dão significado.

Os comportamentos também ajudam a revelar fronteiras. Se uma mudança na regra de prevenção a fraude produz consequências imediatas na abertura da conta, existe uma relação relevante entre essas partes. Se uma alteração em determinado componente não produz efeitos em outra parte, essa independência também é uma informação sobre a estrutura do domínio.

No exemplo utilizado neste capítulo, reduzir o tempo de abertura não significa simplesmente remover etapas. Cada etapa possui condições e comportamentos associados. Remover uma validação pode alterar o comportamento de fraude. Automatizar uma análise pode alterar a operação. Modificar uma regra pode alterar a quantidade de casos enviados para análise manual.

A partir desse ponto, o objetivo inicial pode ser reconsiderado. Em vez de simplesmente reduzir dez minutos para dois, passamos a investigar quais comportamentos produzem o tempo atual, quais deles podem ser alterados e quais consequências essa alteração pode gerar.

## 2.6 Como todos esses elementos se relacionam

As perspectivas apresentadas não são etapas independentes. Elas formam diferentes níveis de observação da mesma realidade.

A visão do ecossistema mostra onde o domínio está inserido. A delimitação estabelece quais partes serão tratadas conjuntamente. Os elementos mostram o que existe dentro dessa fronteira. As características explicam suas propriedades e restrições. Os comportamentos mostram como esses elementos interagem e como o domínio se transforma.

No exemplo da abertura de contas, essa visão integrada altera a própria natureza da pergunta. O objetivo inicial era reduzir o tempo. Depois da investigação, sabemos que esse tempo resulta da interação entre regras, sistemas, pessoas, processos e condições. A questão passa a ser quais comportamentos queremos alterar, dentro de quais limites e com quais consequências.

É nesse momento que métodos e frameworks encontram seu lugar.

Se a necessidade for explicitar conceitos de negócio, estabelecer uma linguagem comum e definir fronteiras entre diferentes modelos de significado, práticas associadas ao Domain-Driven Design podem ser úteis. Se for necessário separar regras centrais de negócio dos detalhes de infraestrutura, princípios associados à Clean Architecture oferecem outra perspectiva. Para comunicar contexto, escopo, decisões arquiteturais e relações entre partes interessadas, arc42 fornece uma estrutura própria. Em uma perspectiva mais ampla de arquitetura empresarial, TOGAF trabalha com diferentes domínios e perspectivas arquiteturais. Quando a necessidade estiver relacionada à definição do trabalho necessário para produzir determinado resultado, conceitos de gerenciamento de escopo do PMBOK podem ser aplicados.

Essas abordagens não são diferentes formas de descrever exatamente a mesma coisa. Elas respondem a necessidades distintas que aparecem quando passamos a conhecer o domínio e suas particularidades. O conhecimento adquirido não determina automaticamente qual framework utilizar. Ele permite reconhecer quais problemas existem e, a partir deles, selecionar instrumentos adequados.

É aqui que aparece uma armadilha comum na aplicação de métodos: o “by the book”. Conhecer um framework pode criar a sensação de que seguir suas etapas, preencher seus artefatos e aplicar suas técnicas é suficiente para produzir uma boa decisão. Não é.

O problema não está em seguir o método. O problema está em confundir domínio do método com domínio da realidade.

Um profissional pode saber exatamente quais perguntas um framework recomenda fazer e ainda assim formular perguntas inadequadas porque não conhece suficientemente o objeto sobre o qual está perguntando. Pode preencher corretamente um artefato e representar incorretamente a realidade. Pode seguir todas as etapas prescritas e chegar a uma conclusão baseada em premissas que nunca foram examinadas.

Isso acontece porque frameworks são instrumentos construídos para lidar com determinados tipos de necessidade. Eles não conhecem, por si mesmos, a organização, o mercado, o processo, o produto, a regulamentação ou o sistema no qual serão aplicados. Quem conhece o método sabe como utilizá-lo. Quem conhece o domínio sabe o que está sendo analisado.

Essa distinção é fundamental para a arquitetura de decisões. O framework deve ajudar a estruturar o raciocínio, não substituir o raciocínio necessário para compreender o domínio.

O que fizemos neste capítulo foi justamente estabelecer essa visão antes de aprofundar a análise. Observamos o ecossistema no qual o domínio está inserido, definimos suas fronteiras, identificamos seus elementos, observamos suas características e procuramos compreender seus comportamentos e relações. Essa visão ainda é deliberadamente macro. Ela nos permite saber o que existe e onde estão as partes relevantes, mas não significa que todas as condições que governam essas partes já tenham sido investigadas.

E é justamente aí que começa o próximo nível de análise.

Ao identificar elementos, características e comportamentos, inevitavelmente encontramos condições que sustentam seu funcionamento. Algumas serão premissas que estamos assumindo como verdadeiras. Outras serão dependências das quais determinada parte do domínio depende para funcionar. Outras ainda serão restrições que limitam as alternativas disponíveis.

Essas condições não são um novo domínio. São um aprofundamento daquilo que acabamos de levantar.

Se neste capítulo construímos o mapa, o próximo capítulo começa a investigar o que condiciona cada parte desse mapa. A pergunta deixa de ser apenas “o que existe e como se relaciona?” e passa a ser “quais premissas estamos assumindo, de que dependemos e quais limites não podemos ignorar?”.

Essa transição é necessária porque conhecer o domínio em nível macro nos permite identificar onde investigar. Identificar premissas, dependências e restrições nos permite compreender o que condiciona aquilo que encontramos.

O domínio, portanto, não está completamente compreendido quando conseguimos nomeá-lo. A delimitação é o início de uma investigação mais profunda.
