# 1. Fundamentos de la Arquitectura de Decisión

Esta guía propone seis fundamentos para comprender decisiones. No constituyen una definición universal de la Arquitectura de Decisión, ni deben entenderse como etapas de un proceso o como una lista de elementos obligatorios. Son una proposición conceptual para hacer explícitas características recurrentes de las decisiones y las relaciones entre ellas.

Un fundamento, en este contexto, es una característica estructural de la decisión. Ayuda a comprender una dimensión que está presente cuando se considera, realiza una elección y esta produce efectos. No define, por sí mismo, cómo debe conducirse la decisión. Su función es ofrecer una referencia para comprender la situación antes de determinar cómo actuar sobre ella.

Esta distinción es importante porque las decisiones concretas suelen ser tratadas mediante métodos, técnicas y frameworks desarrollados para determinados contextos. Estos enfoques organizan formas de trabajo y ofrecen mecanismos para abordar problemas específicos. Los fundamentos propuestos aquí están en un nivel anterior: buscan describir características de la propia decisión, independientemente de la forma particular utilizada para conducirla.

Las características de una decisión, sin embargo, no aparecen de forma aislada. Una decisión ocurre en algún dominio y parte de determinadas condiciones. Está orientada por objetivos, pero estos objetivos deben considerarse frente a aquello que todavía no conocemos. La elección produce consecuencias, y esas consecuencias modifican las condiciones en las que se tomarán decisiones posteriores.

Esta estructura puede observarse en diferentes tipos de decisión. Una decisión arquitectónica, una decisión de negocio, una decisión de proyecto o una decisión personal tienen naturalezas distintas, pero todas ocurren en alguna situación, persiguen algún resultado, se toman con conocimiento incompleto y producen efectos que pueden alterar lo que será posible hacer posteriormente.

El objetivo de este capítulo no es presentar una nueva terminología para sustituir conceptos ya establecidos. Muchas de las ideas aquí presentadas son conocidas y aparecen, con diferentes nombres y niveles de formalización, en disciplinas como arquitectura, gestión, ingeniería, emprendimiento y desarrollo de productos.

La proposición es otra: partir de las cuestiones más básicas que necesitamos responder para comprender una decisión y, a partir de ellas, identificar las necesidades que se derivan. En lugar de comenzar por los métodos disponibles e intentar encajar la decisión en sus estructuras, comenzamos preguntando qué necesita comprenderse sobre la propia decisión.

¿Cuáles son las condiciones mínimas que necesitamos conocer para comprender una decisión? ¿Qué define el campo en el que ocurre? ¿A partir de qué situación se toma? ¿Qué orienta la elección? ¿Qué todavía no sabemos? ¿Qué cambia como consecuencia de la decisión? ¿Y cómo condicionan estos cambios las decisiones siguientes?

Es a partir de estas cuestiones que llegamos a los fundamentos presentados a continuación. Cada uno busca responder a una cuestión más básica de la estructura de la decisión y, a partir de ella, permite derivar necesidades que pueden ser tratadas por diferentes prácticas y enfoques.

## 1.1. Toda decisión ocurre dentro de uno o más dominios

Toda decisión ocurre dentro de uno o más dominios de conocimiento, actividad o problema. El dominio establece el campo en el que se comprende la decisión y proporciona conceptos, conocimientos, criterios y prácticas utilizados para interpretar situaciones y evaluar alternativas.

Una decisión sobre una plataforma de pagos, por ejemplo, puede requerir conocimientos de arquitectura, seguridad, finanzas, producto, operaciones y regulación. Cada dominio contribuye con referencias propias para comprender diferentes aspectos de la decisión.

La participación de diferentes dominios no significa simplemente reunir especialistas en una misma discusión. Cada dominio puede observar una parte diferente de la situación y utilizar criterios diferentes para evaluar las alternativas. Una alternativa técnicamente adecuada puede ser inviable desde el punto de vista financiero. Una solución financieramente atractiva puede crear riesgos operativos. Una decisión adecuada para el producto puede entrar en conflicto con una restricción regulatoria.

Por eso, el dominio no es solo el asunto sobre el que estamos hablando. Influye en lo que consideramos relevante, qué conceptos utilizamos y qué preguntas deben hacerse.

Una decisión de arquitectura de software moviliza conceptos como componentes, interfaces, tecnologías, atributos de calidad y dependencias. Una decisión de gestión de proyectos puede involucrar alcance, plazo, presupuesto, recursos, riesgos y dependencias. Una decisión emprendedora puede involucrar clientes, mercado, propuesta de valor, modelo de negocio y asignación de recursos.

El conocimiento especializado proporciona referencias para el análisis, pero no determina una única respuesta. Dos decisiones pueden ocurrir en el mismo dominio y llegar a elecciones diferentes porque tienen objetivos, condiciones, restricciones o alternativas diferentes.

Esto también explica por qué las prácticas desarrolladas en un dominio no deben transferirse automáticamente a otro. Una práctica puede tener sentido porque responde a una necesidad específica de ese campo y porque sus conceptos, criterios y artefactos fueron construidos para determinadas condiciones.

La primera necesidad producida por este fundamento es la delimitación del dominio. Necesitamos saber en qué campos se inserta la decisión, qué conocimientos son relevantes, qué participantes deben considerarse y qué límites definen aquello que está siendo analizado.

Delimitar no significa necesariamente elegir un único dominio. Una decisión puede atravesar deliberadamente fronteras entre áreas. El objetivo es hacer visibles estas fronteras para que podamos comprender qué perspectivas forman parte de la decisión y qué conocimientos necesitamos movilizar.

Esta necesidad puede atenderse mediante prácticas como definición de alcance, identificación de fronteras, modelado de dominio, identificación de stakeholders y construcción de un lenguaje común. Diferentes frameworks organizan estas prácticas de maneras diferentes, pero todos están, en alguna medida, respondiendo a la necesidad de comprender dónde está inserta la decisión.

## 1.2. Toda decisión parte de un contexto inicial

Toda decisión parte de una situación existente. El contexto inicial reúne las condiciones relevantes para comprender la decisión en el momento en que es considerada.

Dominio y contexto no son lo mismo. El dominio define el campo en el que la decisión tiene sentido y proporciona las referencias utilizadas para comprenderla. El contexto define las condiciones particulares en las que ocurre.

Estas condiciones pueden incluir recursos disponibles, restricciones, información, evidencias, premisas, compromisos, dependencias, decisiones anteriores y otras circunstancias que influyen en las posibilidades consideradas.

El mismo dominio puede presentar contextos completamente diferentes. Una decisión de arquitectura puede ocurrir en un sistema nuevo o en un entorno legado. Puede existir un equipo experimentado o un equipo que todavía necesita adquirir conocimiento. Puede haber presupuesto disponible o una restricción financiera significativa. Puede existir libertad tecnológica o una dependencia contractual que limite las alternativas.

Estas diferencias no son detalles periféricos. Pueden alterar completamente el conjunto de alternativas viables y la forma en que cada alternativa debe evaluarse.

El contexto tampoco es estático. Pueden surgir nuevas informaciones, consumirse recursos, cambiar restricciones y producir decisiones anteriores efectos inesperados. Por eso, el contexto considerado al inicio de una decisión puede no ser exactamente el mismo contexto encontrado durante su realización.

Esta característica también explica por qué la experiencia anterior no puede tratarse como una solución preparada. Una experiencia pasada puede proporcionar referencias útiles, patrones e hipótesis, pero su aplicabilidad depende de las condiciones actuales.

La experiencia proporciona referencias. El contexto determina su aplicabilidad.

La segunda necesidad producida por este fundamento es la explicitación de las condiciones de la decisión. Necesitamos identificar qué existe, qué recursos están disponibles, qué restricciones deben respetarse, qué premisas se están asumiendo, qué dependencias existen y qué información todavía no está disponible.

Esta necesidad se atiende mediante prácticas de diagnóstico, levantamiento de restricciones, identificación de premisas, análisis de dependencias, comprensión del entorno existente e identificación de las condiciones actuales. El objetivo no es describir toda la realidad, sino hacer visibles las condiciones que realmente influyen en la decisión.

Esto es particularmente importante cuando se aplicará un método o framework. Las prácticas de un framework fueron desarrolladas para atender determinadas necesidades y presuponen determinadas condiciones de aplicación. Utilizarlas sin verificar si estas condiciones existen puede producir una situación en la que seguimos correctamente el método, pero tratamos un problema diferente del que realmente tenemos.

Es en este punto donde aparece una de las diferencias entre conocer un método y saber utilizarlo. La aplicación adecuada de una práctica depende de la capacidad de reconocer las condiciones para las que fue concebida y verificar si esas condiciones están presentes en la situación actual.

## 1.3. Toda decisión está orientada por uno o más objetivos

Toda decisión está relacionada con uno o más resultados que se pretende alcanzar, preservar o evitar. Estos objetivos orientan la elección y proporcionan una referencia para determinar qué se pretende obtener.

Un objetivo puede estar claramente formulado o permanecer implícito. Una persona puede decidir reducir costes sin haber definido previamente cuánto pretende reducir o en cuánto tiempo. Una organización puede decidir modernizar un sistema sin haber aclarado si el objetivo principal es reducir costes, aumentar capacidad, disminuir riesgos o permitir una nueva estrategia de negocio.

Un objetivo no existe de forma independiente del dominio y del contexto. Todo objetivo presupone una realidad a la que se refiere y condiciones en las que el resultado pretendido es relevante, incluso cuando estas referencias no se explicitan.

Consideremos, por ejemplo, el objetivo de “reducir el tiempo de aprobación”. Para que esta afirmación tenga significado, es necesario que exista alguna realidad en la que haya un proceso de aprobación, una definición de lo que representa ese tiempo y condiciones en las que su reducción sea deseada. “Reducir costes” presupone costes de algo. “Aumentar disponibilidad” presupone un sistema, servicio u operación. Cuanto más se eliminan estas referencias, más genérico y menos informativo se vuelve el objetivo.

Esto significa que la formulación de un objetivo ya contiene supuestos sobre el dominio y el contexto de la decisión. El análisis puede hacer explícitos estos supuestos y verificar si corresponden a la realidad. Por lo tanto, una investigación puede comenzar por el objetivo, pero el objetivo no debe tratarse como algo semánticamente independiente del dominio y del contexto.

La relación entre estas dimensiones tampoco implica una secuencia rígida. Es posible comenzar por el objetivo, el dominio, el contexto o una situación percibida como problemática. Lo importante es reconocer que la comprensión adecuada de un objetivo involucra la realidad a la que se refiere y las condiciones en las que es relevante.

Cuando los objetivos no son identificados o comprendidos por quien decide, tenemos una decisión ciega. La decisión todavía posee una dirección o finalidad, pero parte de la lógica que orienta la elección permanece implícita.

La explicitación de los objetivos permite establecer qué debe considerarse en la elección. Sin saber qué se pretende alcanzar, resulta difícil determinar qué alternativas son relevantes y qué características deben considerarse en la comparación entre ellas.

Una decisión también puede involucrar objetivos diferentes que no pueden atenderse simultáneamente en la misma medida. Reducir costes puede entrar en conflicto con aumentar la calidad. Acelerar una entrega puede entrar en conflicto con reducir riesgos. Aumentar la flexibilidad puede entrar en conflicto con reducir la complejidad.

Por eso, definir objetivos no significa simplemente producir una lista. Es necesario comprender qué objetivos existen, cómo se relacionan y cuáles de ellos son prioritarios cuando no pueden atenderse simultáneamente.

Los objetivos también pueden cambiar durante el análisis. Nuevas informaciones pueden mostrar que aquello que parecía importante inicialmente ya no es relevante, que determinado objetivo no es viable en las condiciones existentes o que otro objetivo, antes no considerado, es más importante para la decisión.

Esto crea una relación importante entre objetivo y problema. Una situación se convierte en un problema en relación con algún resultado pretendido. Si el objetivo cambia, la interpretación de la situación también puede cambiar.

Por ejemplo, “sustituir el sistema actual” puede parecer inicialmente un problema técnico. Pero, si el objetivo es reducir el tiempo necesario para lanzar nuevos productos, puede no ser necesario sustituir todo el sistema. El problema puede estar relacionado con una capacidad específica, y no con la tecnología en su conjunto.

En este sentido, problema y objetivo no deben tratarse como elementos completamente independientes. La definición de lo que necesita resolverse depende, en parte, del resultado que se pretende alcanzar.

La definición de los objetivos también establece la necesidad de criterios de evaluación. Es necesario contar con referencias que permitan determinar en qué medida una alternativa atiende a lo que se pretende alcanzar.

Estos criterios pueden asumir diferentes formas, como requisitos, métricas, indicadores, atributos de calidad, condiciones de éxito o límites aceptables. No todo objetivo necesita reducirse a una métrica. Lo importante es que exista una forma suficientemente clara de evaluar si aquello que fue elegido atiende a los objetivos de la decisión.

## 1.4. Toda decisión implica algún grado de incertidumbre

Una decisión implica elegir entre posibilidades sin conocer completamente sus consecuencias o las condiciones futuras. El grado de incertidumbre varía según la cantidad y la calidad de la información disponible, la experiencia acumulada y la previsibilidad de la situación.

Algunas decisiones cuentan con una gran cantidad de datos y evidencias. Otras deben tomarse con información escasa y muchas incógnitas. También existen situaciones en las que las consecuencias de una alternativa son ampliamente conocidas. En estos casos, la incertidumbre puede ser pequeña, pero todavía existe una elección sobre cómo actuar.

La incertidumbre también puede tener diferentes orígenes. Podemos no comprender suficientemente el problema, no saber cómo funcionará una solución, no conseguir prever el comportamiento de usuarios o clientes, depender de factores externos o no saber cómo evolucionarán determinadas variables.

Esta distinción es importante porque diferentes tipos de incertidumbre requieren diferentes formas de investigación. Cuando no comprendemos el problema, necesitamos aprender sobre la situación. Cuando no sabemos si una solución funciona, podemos necesitar experimentar. Cuando conocemos las alternativas, pero no sabemos qué consecuencias ocurrirán, podemos necesitar analizar riesgos y escenarios.

La incertidumbre no necesita eliminarse antes de actuar. Podemos buscar información, consultar especialistas, probar hipótesis, realizar experimentos, construir prototipos o esperar nuevos datos.

Cada alternativa, sin embargo, tiene su propio coste. Investigar más puede reducir el desconocimiento, pero también consumir tiempo, recursos u oportunidades. Un experimento puede generar evidencias, pero requiere inversión. Esperar más información puede mejorar una decisión o simplemente retrasar una acción necesaria.

Decidir implica, por lo tanto, evaluar no solo qué alternativas están disponibles, sino también cuánto vale la pena aprender antes de actuar.

Esta evaluación también depende de la naturaleza de las consecuencias. Cuando una decisión es fácilmente reversible, puede ser aceptable avanzar con un mayor grado de incertidumbre. Cuando una elección crea compromisos difíciles de deshacer, el coste de una decisión prematura puede ser mucho mayor.

La cuarta necesidad producida por este fundamento es el tratamiento de lo desconocido. Necesitamos identificar aquello que todavía no sabemos, evaluar su importancia y decidir cómo afrontar esta incertidumbre.

Hipótesis, evidencias, experimentos, prototipos, investigaciones, escenarios, riesgos y oportunidades son diferentes formas de tratar aquello que todavía no conocemos.

Lean Startup, por ejemplo, estructura prácticas para transformar hipótesis en experimentos y aprendizaje. Design Thinking utiliza actividades de investigación, prototipado y prueba para aprender sobre necesidades y posibles soluciones. La gestión de riesgos estructura la identificación y el análisis de eventos inciertos y sus posibles consecuencias.

Estos enfoques no son equivalentes y no deben aplicarse simplemente porque una decisión contiene incertidumbre. La cuestión es comprender qué incertidumbre existe, qué conocimiento falta y qué práctica puede producir evidencia relevante para la decisión.

## 1.5. Toda decisión produce consecuencias directas e indirectas

Una decisión produce más que un resultado inmediato. Puede comprometer recursos, crear dependencias, establecer restricciones, eliminar caminos o hacer que determinados cambios sean más costosos. Algunas de estas consecuencias aparecen directamente después de la decisión, mientras que otras surgen como efectos indirectos de aquello que fue modificado.

Las consecuencias también pueden propagarse a otras partes de la situación. Una decisión sobre tecnología puede alterar el trabajo de un equipo. Una decisión de proyecto puede modificar responsabilidades, plazos o recursos. Una decisión de producto puede afectar a clientes, usuarios o socios. Un cambio organizacional puede crear nuevos compromisos para otras áreas.

Cuando una decisión produce efectos sobre otras personas o grupos, surge también una necesidad de comunicación. Es necesario hacer comprensible qué se decidió, por qué se tomó la decisión, qué consecuencias se esperan y qué cambia para aquellos que se verán afectados o deberán actuar a partir de ella. En este sentido, la comunicación no es solo una actividad posterior a la decisión, sino parte del tratamiento de sus consecuencias.

Una decisión también puede preservar opciones, generar nuevas alternativas o producir información útil para decisiones posteriores. Sus efectos, por lo tanto, no se limitan a lo que ocurre inmediatamente después de la elección. Algunas consecuencias modifican las condiciones en las que se tomarán otras decisiones.

Es en este sentido que podemos comprender el espacio de posibilidades. Representa aquello que puede hacerse a partir de determinado momento, considerando los recursos, compromisos, dependencias y restricciones existentes. Las consecuencias de una decisión pueden alterar este espacio, haciendo que algunas posibilidades sean más accesibles, otras más difíciles y algunas inviables.

Alterar el espacio de posibilidades no significa necesariamente reducir opciones. Una elección puede eliminar determinados caminos y, al mismo tiempo, crear otros. Una nueva capacidad tecnológica puede abrir alternativas que no existían. Una decisión comercial puede crear acceso a un mercado y cerrar otro.

Toda elección también implica trade-offs. Al favorecer determinado resultado, una decisión puede exigir concesiones en otros objetivos, criterios o posibilidades.

Mejorar el rendimiento puede aumentar el coste. Reducir el plazo puede aumentar el riesgo. Aumentar la flexibilidad puede elevar la complejidad. Preservar la compatibilidad puede limitar la capacidad de evolución. En muchos casos, no existe una alternativa que maximice simultáneamente todos los objetivos.

Esta dinámica puede observarse mediante la idea de opcionalidad. Algunas elecciones preservan una mayor capacidad de cambio futuro. Otras aumentan los compromisos y reducen el margen de maniobra. La consecuencia de una decisión, por lo tanto, también puede observarse a través de la capacidad que preserva o elimina para decisiones posteriores.

La reversibilidad es relevante en este punto. Una decisión fácil de deshacer produce consecuencias diferentes de una decisión que requiere un gran esfuerzo o coste para ser revertida. Esto no significa que las decisiones reversibles sean siempre mejores, sino que su estructura de consecuencias es diferente.

El tiempo hace que esta dinámica sea aún más evidente. Posponer una elección puede permitir que surjan nuevas informaciones, pero también puede hacer que desaparezca una oportunidad, consumir recursos o permitir que otras decisiones se tomen antes.

Permanecer en el estado actual no significa permanecer frente a las mismas alternativas. El propio contexto continúa evolucionando, y la ausencia de una decisión puede hacer que determinadas opciones se vuelvan más costosas, inviables o simplemente dejen de existir.

Es en este sentido que no decidir deliberadamente también puede constituir una decisión. Existe una diferencia entre elegir conscientemente no actuar y simplemente no percibir que era necesario tomar una decisión, pero ambas situaciones pueden producir efectos sobre las posibilidades futuras.

La quinta necesidad producida por este fundamento es comprender, tratar y comunicar las consecuencias de las alternativas consideradas. Esto implica analizar no solo qué alternativa produce determinado resultado, sino también qué efectos directos e indirectos puede generar, quién puede verse afectado, cómo deben comunicarse estos efectos y cómo la decisión modifica las condiciones para las decisiones siguientes.

Escenarios, análisis de alternativas, trade-offs, comunicación, coordinación, reversibilidad, dependencias, coste de oportunidad, opcionalidad y path dependency son diferentes formas de tratar esta necesidad.

El objetivo no es encontrar una alternativa universalmente mejor. Es comprender cómo cada alternativa responde a los objetivos y restricciones existentes, qué consecuencias produce, quién puede verse afectado y cómo estas consecuencias alteran el espacio de posibilidades para el futuro.

## 1.6. Toda decisión participa en un proceso de evolución

Una decisión modifica la situación siguiente porque sus consecuencias alteran el espacio de posibilidades. Los recursos pueden consumirse o crearse, pueden asumirse compromisos, pueden surgir dependencias, pueden eliminarse o abrirse alternativas y puede producirse nueva información.

Esta alteración del espacio de posibilidades modifica las condiciones que se observarán para las decisiones siguientes. El contexto puede cambiar, algunos objetivos pueden dejar de ser viables o adquirir importancia, pueden surgir o desaparecer nuevas incertidumbres y pueden pasar a existir otras alternativas.

Es en este sentido que esta guía utiliza el término evolución. Evolución significa cambio de estado a lo largo del tiempo como consecuencia de las decisiones, las acciones realizadas, la información producida y las condiciones que se modifican. No implica necesariamente mejora.

Un sistema puede acercarse a sus objetivos, pero también puede acumular restricciones, dependencias, costes o problemas que dificulten cambios posteriores. Una organización puede aprender de una decisión y, al mismo tiempo, asumir compromisos que condicionen sus próximas elecciones.

Planificación, ejecución, observación y aprendizaje forman parte de esta dinámica. Una decisión puede mantenerse, revisarse o sustituirse conforme surgen nuevos datos y conforme se modifican las condiciones para nuevas elecciones.

Modelos como PDCA y OODA representan diferentes formas de organizar ciclos de este tipo. No son modelos de Arquitectura de Decisión, pero ayudan a ilustrar una dinámica en la que acción, observación, aprendizaje y cambio están relacionados.

Cuando este proceso se repite, las elecciones anteriores pasan a influir en las siguientes. Generan dependencias, compromisos, restricciones y aprendizajes que pasan a formar parte de las condiciones de las próximas elecciones.

Esta acumulación también aparece en la arquitectura de sistemas. La arquitectura actual puede verse como resultado de muchas decisiones tomadas a lo largo del tiempo, algunas deliberadas y otras condicionadas por las circunstancias existentes.

Una decisión arquitectónica, por ejemplo, puede introducir una tecnología. Después, esta tecnología pasa a influir en la contratación de profesionales, la elección de herramientas, los costes operativos y las decisiones de integración. Una decisión inicial, por lo tanto, participa en la formación de las condiciones para decisiones posteriores.

Esto significa que una decisión no debe analizarse únicamente por el estado existente en el momento en que se toma. También necesitamos considerar los efectos que produce sobre el espacio de posibilidades, las condiciones de las decisiones futuras y el conocimiento que genera.

La sexta necesidad producida por este fundamento es la observación, el aprendizaje y la preservación del conocimiento producido por la evolución.

Necesitamos poder observar qué ocurrió, comparar el resultado con aquello que esperábamos y comprender las razones de eventuales diferencias.

También necesitamos poder recuperar información relevante sobre decisiones anteriores cuando nuevas decisiones dependan de ellas. Esto no significa documentarlo todo. Significa preservar aquello que será necesario para comprender decisiones relevantes en el futuro.

Dependiendo del dominio, esto puede hacerse mediante indicadores, feedback, retrospectivas, registros de decisiones, documentación, experimentos u otros mecanismos de aprendizaje.

La trazabilidad surge como una forma de preservar este conocimiento, pero no es el objetivo en sí mismo. El objetivo es mantener la capacidad de comprender la evolución y utilizar el conocimiento producido para orientar decisiones futuras.

## 1.7. Cómo se relacionan los fundamentos

Los seis fundamentos propuestos en esta guía no deben interpretarse como seis asuntos independientes. Describen diferentes dimensiones de una misma estructura de decisión.

Una decisión ocurre en un dominio, pero ese dominio siempre se manifiesta dentro de un contexto específico. El contexto define condiciones que influyen en aquello que puede hacerse. Dentro de estas condiciones, existen objetivos que orientan la elección. Como el futuro no se conoce por completo, existe incertidumbre. La decisión produce consecuencias directas e indirectas, que pueden afectar a personas, recursos, sistemas y las condiciones para decisiones futuras. Estas consecuencias alteran el espacio de posibilidades y, al hacerlo, modifican las condiciones en las que se tomarán nuevas decisiones. Es en este proceso donde ocurre la evolución.

Así, podemos visualizar esta relación de forma encadenada:

Dominio → contexto → objetivos → incertidumbre → consecuencias → evolución

El encadenamiento no representa una secuencia de etapas. Representa una relación entre dimensiones que se influyen continuamente.

Una nueva información sobre el dominio puede alterar nuestra comprensión del contexto. Un cambio en el contexto puede hacer que un objetivo sea inviable o revelar otro más importante. Un objetivo diferente puede cambiar qué alternativas se consideran. Una nueva evidencia puede reducir una incertidumbre. Una decisión puede producir consecuencias que eliminen una alternativa futura o creen una nueva posibilidad. Estas alteraciones modifican el espacio de posibilidades y, en consecuencia, las condiciones disponibles para las decisiones siguientes. Un resultado inesperado también puede volver a alterar el contexto y exigir una nueva comprensión de la situación.

La decisión, por lo tanto, no ocurre dentro de una estructura estática. Ocurre dentro de una estructura que se modifica mientras aprendemos, elegimos y actuamos.

Esta relación ayuda a explicar por qué diferentes prácticas y frameworks pueden parecer tan diferentes y, aun así, tratar necesidades relacionadas.

Podemos establecer una segunda relación:

Característica → necesidad → práctica → framework

El dominio produce la necesidad de delimitación. Esta necesidad puede tratarse mediante prácticas de definición de fronteras, modelado, alcance y lenguaje común. DDD, por ejemplo, ofrece prácticas para comprender y delimitar dominios, establecer modelos y definir bounded contexts. Otros enfoques de arquitectura, gestión y análisis de negocios también poseen prácticas destinadas a hacer explícitos los límites de aquello que está siendo analizado.

El contexto produce la necesidad de explicitar las condiciones existentes. Esto puede involucrar el levantamiento de restricciones, premisas, dependencias, situación actual, stakeholders y recursos disponibles. arc42 trabaja explícitamente con contexto y alcance, restricciones y estrategia de solución. TOGAF también estructura actividades relacionadas con la comprensión del entorno, arquitectura y transición. En proyectos, las prácticas de planificación y diagnóstico cumplen funciones similares.

Los objetivos producen la necesidad de criterios de evaluación. Requisitos, métricas, indicadores, atributos de calidad y criterios de éxito son algunas de las formas posibles de atender esta necesidad. Scrum utiliza Product Goal y Sprint Goal para orientar el trabajo. PMBOK trabaja con objetivos, planificación, entrega y medición. En arquitectura, los requisitos funcionales, atributos de calidad y restricciones ayudan a establecer referencias para evaluar alternativas.

La incertidumbre produce la necesidad de tratar aquello que todavía no conocemos. En este caso, podemos utilizar análisis de riesgos, formulación de hipótesis, experimentación, prototipado, investigación, escenarios u otras prácticas de investigación. Lean Startup utiliza experimentación y aprendizaje para probar hipótesis. Design Thinking utiliza investigación, ideación, prototipado y prueba para aprender sobre necesidades y posibles soluciones. Las prácticas de gestión de riesgos tratan eventos inciertos y sus posibles consecuencias.

Las consecuencias producen la necesidad de analizar sus efectos y tratar aquellos que deben ser considerados por la decisión. Esto incluye comprender impactos directos e indirectos, identificar quién puede verse afectado, comunicar cambios relevantes, coordinar acciones derivadas y evaluar cómo la decisión modifica las condiciones para elecciones futuras. En este punto aparecen prácticas como análisis de escenarios, comparación de alternativas, identificación de trade-offs, análisis de reversibilidad, evaluación de dependencias, comunicación y coordinación. En planificación, diferentes opciones de ejecución pueden compararse según sus impactos, costes, riesgos y compromisos.

La evolución produce la necesidad de observar resultados, aprender y preservar conocimiento. Scrum incorpora inspección y adaptación. Lean Startup estructura ciclos de construcción, medición y aprendizaje. Las retrospectivas permiten examinar la experiencia de un ciclo y ajustar el siguiente. Los ADRs preservan conocimiento sobre decisiones que continúan influyendo en la evolución de la arquitectura. Otros métodos y prácticas utilizan mecanismos diferentes para atender la misma necesidad fundamental.

Estos ejemplos no significan que cada framework pertenezca a un solo fundamento. Esa sería una interpretación excesivamente rígida. Un framework puede atender varias necesidades al mismo tiempo porque una práctica frecuentemente actúa sobre más de una dimensión de la decisión.

Scrum, por ejemplo, no trata únicamente la evolución. Sus objetivos orientan el trabajo, sus mecanismos de inspección producen información y su adaptación permite revisar decisiones conforme surgen nuevas evidencias. Lean Startup no trata únicamente la incertidumbre. Sus ciclos también conectan objetivos, evidencias, resultados y evolución. arc42 no trata únicamente la documentación. Su estructura relaciona contexto, objetivos, restricciones, calidad, decisiones, riesgos y conocimiento arquitectónico.

Lo mismo se aplica a las prácticas de arquitectura. Una decisión arquitectónica necesita considerar el dominio en el que existe el sistema, las condiciones actuales, los objetivos de calidad y negocio, las incertidumbres técnicas, las alternativas disponibles y las consecuencias que serán asumidas por la arquitectura a lo largo del tiempo.

Por eso, el framework no necesita ser el punto de partida. Puede ser una respuesta a una necesidad que ya ha sido identificada.

Esta inversión es importante. En lugar de preguntar primero “¿qué framework debemos utilizar?”, podemos comenzar preguntando: “¿qué decisión estamos intentando conducir?”, “¿qué características de esta decisión necesitan ser tratadas?”, “¿qué necesidades surgen de estas características?” y, solo entonces, “¿qué prácticas o frameworks pueden ayudarnos?”.

Los seis fundamentos propuestos en esta guía, por lo tanto, no buscan sustituir DDD, TOGAF, arc42, Scrum, PMBOK, Lean Startup, Design Thinking, ADR u otros métodos. Ofrecen una forma de observar qué están intentando tratar estos enfoques y de reconocer que diferentes disciplinas pueden desarrollar respuestas distintas para necesidades estructuralmente relacionadas.

Esta perspectiva será importante en los capítulos siguientes. Después de comprender las características generales de una decisión, necesitamos entrar en la situación concreta en la que ocurre. Antes de definir qué problema resolver o qué solución aplicar, necesitamos comprender el dominio, el contexto, los límites y las condiciones existentes.

Es a partir de ahí que la Arquitectura de Decisión deja de ser únicamente una estructura conceptual y pasa a orientar la conducción de una decisión real.
