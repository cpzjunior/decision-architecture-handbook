# 1. Fondamenti dell'Architettura delle Decisioni

Questa guida propone sei fondamenti per comprendere le decisioni. Non costituiscono una definizione universale dell'Architettura delle Decisioni, né devono essere intesi come fasi di un processo o come un elenco di elementi obbligatori. Sono una proposta concettuale per rendere esplicite caratteristiche ricorrenti delle decisioni e le relazioni tra esse.

Un fondamento, in questo contesto, è una caratteristica strutturale della decisione. Aiuta a comprendere una dimensione presente quando una scelta viene considerata, effettuata e produce effetti. Non definisce, di per sé, come la decisione debba essere condotta. La sua funzione è offrire un riferimento per comprendere la situazione prima di determinare come agire su di essa.

Questa distinzione è importante perché le decisioni concrete sono frequentemente trattate mediante metodi, tecniche e framework sviluppati per determinati contesti. Questi approcci organizzano modalità di lavoro e offrono meccanismi per affrontare problemi specifici. I fondamenti proposti qui si collocano a un livello precedente: cercano di descrivere caratteristiche della decisione stessa, indipendentemente dalla particolare modalità utilizzata per condurla.

Le caratteristiche di una decisione, tuttavia, non compaiono isolate. Una decisione avviene in un determinato dominio e parte da determinate condizioni. È orientata da obiettivi, ma questi obiettivi devono essere considerati alla luce di ciò che ancora non conosciamo. La scelta produce conseguenze e tali conseguenze modificano le condizioni nelle quali verranno prese decisioni successive.

Questa struttura può essere osservata in diversi tipi di decisione. Una decisione architetturale, una decisione aziendale, una decisione di progetto o una decisione personale hanno nature diverse, ma tutte avvengono in una determinata situazione, perseguono un determinato risultato, vengono prese con conoscenze incomplete e producono effetti che possono modificare ciò che sarà possibile fare in seguito.

L'obiettivo di questo capitolo non è presentare una nuova terminologia per sostituire concetti già consolidati. Molte delle idee qui presentate sono note e compaiono, con nomi e livelli di formalizzazione differenti, in discipline come architettura, gestione, ingegneria, imprenditorialità e sviluppo di prodotti.

La proposta è un'altra: partire dalle questioni più basilari a cui dobbiamo rispondere per comprendere una decisione e, a partire da esse, identificare le necessità che ne derivano. Invece di partire dai metodi disponibili e cercare di adattare la decisione alle loro strutture, iniziamo chiedendoci cosa deve essere compreso sulla decisione stessa.

Quali sono le condizioni minime che dobbiamo conoscere per comprendere una decisione? Cosa definisce il campo in cui essa avviene? Da quale situazione viene presa? Cosa orienta la scelta? Cosa ancora non sappiamo? Cosa cambia come conseguenza della decisione? E come questi cambiamenti condizionano le decisioni successive?

È a partire da queste domande che arriviamo ai fondamenti presentati di seguito. Ognuno cerca di rispondere a una questione più basilare della struttura della decisione e, a partire da essa, permette di derivare necessità che possono essere trattate da diverse pratiche e approcci.

## 1.1. Ogni decisione avviene all'interno di uno o più domini

Ogni decisione avviene all'interno di uno o più domini di conoscenza, attività o problema. Il dominio stabilisce il campo nel quale la decisione viene compresa e fornisce concetti, conoscenze, criteri e pratiche utilizzati per interpretare situazioni e valutare alternative.

Una decisione relativa a una piattaforma di pagamenti, ad esempio, può richiedere conoscenze di architettura, sicurezza, finanza, prodotto, operazioni e regolamentazione. Ogni dominio contribuisce con propri riferimenti per comprendere diversi aspetti della decisione.

La partecipazione di domini diversi non significa soltanto riunire specialisti nella stessa discussione. Ogni dominio può vedere una parte diversa della situazione e utilizzare criteri diversi per valutare le alternative. Un'alternativa tecnicamente adeguata può essere finanziariamente impraticabile. Una soluzione finanziariamente attraente può creare rischi operativi. Una decisione adeguata per il prodotto può entrare in conflitto con un vincolo normativo.

Per questo, il dominio non è soltanto l'argomento di cui stiamo parlando. Influenza ciò che consideriamo rilevante, quali concetti utilizziamo e quali domande devono essere poste.

Una decisione di architettura software mobilita concetti come componenti, interfacce, tecnologie, attributi di qualità e dipendenze. Una decisione di project management può coinvolgere ambito, tempi, budget, risorse, rischi e dipendenze. Una decisione imprenditoriale può coinvolgere clienti, mercato, proposta di valore, modello di business e allocazione delle risorse.

La conoscenza specialistica fornisce riferimenti per l'analisi, ma non determina un'unica risposta. Due decisioni possono avvenire nello stesso dominio e arrivare a scelte diverse perché possiedono obiettivi, condizioni, vincoli o alternative differenti.

Questo spiega anche perché le pratiche sviluppate in un dominio non debbano essere trasferite automaticamente a un altro. Una pratica può avere senso perché risponde a una necessità specifica di quel campo e perché i suoi concetti, criteri e artefatti sono stati costruiti per determinate condizioni.

La prima necessità prodotta da questo fondamento è la delimitazione del dominio. Dobbiamo sapere in quali ambiti si inserisce la decisione, quali conoscenze sono rilevanti, quali partecipanti devono essere considerati e quali limiti definiscono ciò che viene analizzato.

Delimitare non significa necessariamente scegliere un unico dominio. Una decisione può deliberatamente attraversare i confini tra aree. L'obiettivo è rendere visibili questi confini affinché possiamo comprendere quali prospettive fanno parte della decisione e quali conoscenze dobbiamo mobilitare.

Questa necessità può essere soddisfatta mediante pratiche come la definizione dell'ambito, l'identificazione dei confini, la modellazione del dominio, l'identificazione degli stakeholder e la costruzione di un linguaggio comune. Framework diversi organizzano queste pratiche in modi diversi, ma tutti rispondono, in qualche misura, alla necessità di comprendere dove è inserita la decisione.

## 1.2. Ogni decisione parte da un contesto iniziale

Ogni decisione parte da una situazione esistente. Il contesto iniziale riunisce le condizioni rilevanti per comprendere la decisione nel momento in cui viene presa in considerazione.

Dominio e contesto non sono la stessa cosa. Il dominio definisce il campo nel quale la decisione ha senso e fornisce i riferimenti utilizzati per comprenderla. Il contesto definisce le condizioni specifiche nelle quali essa avviene.

Queste condizioni possono includere risorse disponibili, vincoli, informazioni, evidenze, assunzioni, impegni, dipendenze, decisioni precedenti e altre circostanze che influenzano le possibilità considerate.

Lo stesso dominio può presentare contesti completamente diversi. Una decisione architetturale può avvenire in un sistema nuovo o in un ambiente legacy. Può esserci un team esperto oppure un team che deve ancora acquisire conoscenze. Può esserci un budget disponibile oppure un vincolo finanziario significativo. Può esserci libertà tecnologica oppure una dipendenza contrattuale che limita le alternative.

Queste differenze non sono dettagli periferici. Possono modificare completamente l'insieme delle alternative praticabili e il modo in cui ciascuna alternativa deve essere valutata.

Anche il contesto non è statico. Possono emergere nuove informazioni, le risorse possono essere consumate, i vincoli possono cambiare e le decisioni precedenti possono produrre effetti inattesi. Per questo, il contesto considerato all'inizio di una decisione potrebbe non essere esattamente lo stesso contesto incontrato durante la sua realizzazione.

Questa caratteristica spiega anche perché l'esperienza precedente non possa essere trattata come una soluzione pronta. Un'esperienza passata può fornire riferimenti utili, pattern e ipotesi, ma la sua applicabilità dipende dalle condizioni attuali.

L'esperienza fornisce riferimenti. Il contesto determina la loro applicabilità.

La seconda necessità prodotta da questo fondamento è l'esplicitazione delle condizioni della decisione. Dobbiamo identificare ciò che esiste, quali risorse sono disponibili, quali vincoli devono essere rispettati, quali assunzioni vengono fatte, quali dipendenze esistono e quali informazioni non sono ancora disponibili.

Questa necessità viene soddisfatta da pratiche di diagnosi, rilevazione dei vincoli, identificazione delle assunzioni, analisi delle dipendenze, comprensione dell'ambiente esistente e identificazione delle condizioni attuali. L'obiettivo non è descrivere tutta la realtà, ma rendere visibili le condizioni che influenzano realmente la decisione.

Questo è particolarmente importante quando verrà applicato un metodo o un framework. Le pratiche di un framework sono state sviluppate per soddisfare determinate necessità e presuppongono determinate condizioni di applicazione. Utilizzarle senza verificare se tali condizioni esistono può produrre una situazione in cui seguiamo correttamente il metodo, ma trattiamo un problema diverso da quello che abbiamo realmente.

È a questo punto che emerge una delle differenze tra conoscere un metodo e saperlo utilizzare. L'applicazione adeguata di una pratica dipende dalla capacità di riconoscere le condizioni per le quali è stata concepita e verificare se tali condizioni sono presenti nella situazione attuale.

## 1.3. Ogni decisione è orientata da uno o più obiettivi

Ogni decisione è collegata a uno o più risultati che si intende raggiungere, preservare o evitare. Questi obiettivi orientano la scelta e forniscono un riferimento per determinare ciò che si intende ottenere.

Un obiettivo può essere formulato chiaramente oppure rimanere implicito. Una persona può decidere di ridurre i costi senza aver definito in precedenza quanto intende ridurli o in quanto tempo. Un'organizzazione può decidere di modernizzare un sistema senza aver chiarito se l'obiettivo principale sia ridurre i costi, aumentare la capacità, diminuire i rischi o consentire una nuova strategia aziendale.

Un obiettivo non esiste indipendentemente dal dominio e dal contesto. Ogni obiettivo presuppone una realtà alla quale si riferisce e condizioni nelle quali il risultato desiderato è rilevante, anche quando questi riferimenti non vengono esplicitati.

Consideriamo, ad esempio, l'obiettivo di “ridurre il tempo di approvazione”. Affinché questa affermazione abbia significato, è necessario che esista una realtà nella quale vi sia un processo di approvazione, una definizione di ciò che rappresenta questo tempo e condizioni nelle quali la sua riduzione sia desiderata. “Ridurre i costi” presuppone costi di qualcosa. “Aumentare la disponibilità” presuppone un sistema, un servizio o un'operazione. Quanto più questi riferimenti vengono rimossi, tanto più generico e meno informativo diventa l'obiettivo.

Ciò significa che la formulazione di un obiettivo contiene già assunzioni sul dominio e sul contesto della decisione. L'analisi può rendere esplicite queste assunzioni e verificare se corrispondono alla realtà. Pertanto, un'indagine può iniziare dall'obiettivo, ma l'obiettivo non deve essere trattato come qualcosa di semanticamente indipendente dal dominio e dal contesto.

La relazione tra queste dimensioni non implica nemmeno una sequenza rigida. È possibile iniziare dall'obiettivo, dal dominio, dal contesto o da una situazione percepita come problematica. L'importante è riconoscere che la corretta comprensione di un obiettivo coinvolge la realtà alla quale si riferisce e le condizioni nelle quali è rilevante.

Quando gli obiettivi non vengono identificati o compresi da chi decide, abbiamo una decisione cieca. La decisione possiede comunque una direzione o una finalità, ma parte della logica che orienta la scelta rimane implicita.

L'esplicitazione degli obiettivi permette di stabilire cosa debba essere considerato nella scelta. Senza sapere cosa si intende raggiungere, diventa difficile determinare quali alternative siano rilevanti e quali caratteristiche debbano essere considerate nel confronto tra esse.

Una decisione può inoltre coinvolgere obiettivi diversi che non possono essere soddisfatti simultaneamente nella stessa misura. Ridurre i costi può entrare in conflitto con l'aumento della qualità. Accelerare una consegna può entrare in conflitto con la riduzione dei rischi. Aumentare la flessibilità può entrare in conflitto con la riduzione della complessità.

Per questo, definire gli obiettivi non significa semplicemente produrre un elenco. È necessario comprendere quali obiettivi esistono, come si relazionano e quali di essi siano prioritari quando non possono essere soddisfatti simultaneamente.

Gli obiettivi possono anche cambiare durante l'analisi. Nuove informazioni possono mostrare che ciò che inizialmente sembrava importante non è più rilevante, che un determinato obiettivo non è praticabile nelle condizioni esistenti o che un altro obiettivo, precedentemente non considerato, è più importante per la decisione.

Questo crea una relazione importante tra obiettivo e problema. Una situazione diventa un problema in relazione a un determinato risultato desiderato. Se l'obiettivo cambia, può cambiare anche l'interpretazione della situazione.

Ad esempio, “sostituire il sistema attuale” può sembrare inizialmente un problema tecnico. Ma, se l'obiettivo è ridurre il tempo necessario per lanciare nuovi prodotti, potrebbe non essere necessario sostituire l'intero sistema. Il problema potrebbe essere legato a una capacità specifica e non alla tecnologia nel suo complesso.

In questo senso, problema e obiettivo non devono essere trattati come elementi completamente indipendenti. La definizione di ciò che deve essere risolto dipende, in parte, dal risultato che si intende raggiungere.

La definizione degli obiettivi stabilisce anche la necessità di criteri di valutazione. È necessario disporre di riferimenti che permettano di determinare in quale misura un'alternativa soddisfi ciò che si intende raggiungere.

Questi criteri possono assumere forme diverse, come requisiti, metriche, indicatori, attributi di qualità, condizioni di successo o limiti accettabili. Non ogni obiettivo deve essere ridotto a una metrica. L'importante è che esista un modo sufficientemente chiaro per valutare se ciò che è stato scelto soddisfa gli obiettivi della decisione.

## 1.4. Ogni decisione implica un certo grado di incertezza

Una decisione implica scegliere tra possibilità senza conoscere completamente le loro conseguenze o le condizioni future. Il grado di incertezza varia in base alla quantità e alla qualità delle informazioni disponibili, all'esperienza accumulata e alla prevedibilità della situazione.

Alcune decisioni dispongono di una grande quantità di dati ed evidenze. Altre devono essere prese con informazioni scarse e molte incognite. Esistono anche situazioni in cui le conseguenze di un'alternativa sono ampiamente conosciute. In questi casi, l'incertezza può essere ridotta, ma esiste comunque una scelta su come agire.

L'incertezza può inoltre avere origini diverse. Potremmo non comprendere sufficientemente il problema, non sapere come funzionerà una soluzione, non riuscire a prevedere il comportamento degli utenti o dei clienti, dipendere da fattori esterni o non sapere come determinate variabili evolveranno.

Questa distinzione è importante perché diversi tipi di incertezza richiedono diverse forme di indagine. Quando non comprendiamo il problema, dobbiamo apprendere sulla situazione. Quando non sappiamo se una soluzione funziona, potremmo aver bisogno di sperimentare. Quando conosciamo le alternative ma non sappiamo quali conseguenze si verificheranno, potremmo aver bisogno di analizzare rischi e scenari.

L'incertezza non deve necessariamente essere eliminata prima di agire. Possiamo cercare informazioni, consultare esperti, testare ipotesi, eseguire esperimenti, costruire prototipi o attendere nuovi dati.

Ogni alternativa, tuttavia, ha il proprio costo. Indagare ulteriormente può ridurre ciò che non conosciamo, ma può anche consumare tempo, risorse o opportunità. Un esperimento può generare evidenze, ma richiede un investimento. Attendere ulteriori informazioni può migliorare una decisione oppure semplicemente ritardare un'azione necessaria.

Decidere implica quindi valutare non solo quali alternative siano disponibili, ma anche quanto valga la pena apprendere prima di agire.

Questa valutazione dipende anche dalla natura delle conseguenze. Quando una decisione è facilmente reversibile, può essere accettabile procedere con un maggiore grado di incertezza. Quando una scelta crea impegni difficili da annullare, il costo di una decisione prematura può essere molto maggiore.

La quarta necessità prodotta da questo fondamento è il trattamento dell'ignoto. Dobbiamo identificare ciò che ancora non sappiamo, valutarne l'importanza e decidere come gestire tale incertezza.

Ipotesi, evidenze, esperimenti, prototipi, ricerche, scenari, rischi e opportunità sono diverse modalità di trattare ciò che ancora non conosciamo.

Lean Startup, ad esempio, struttura pratiche per trasformare le ipotesi in esperimenti e apprendimento. Design Thinking utilizza attività di indagine, prototipazione e test per apprendere sulle necessità e sulle possibili soluzioni. La gestione dei rischi struttura l'identificazione e l'analisi degli eventi incerti e delle loro possibili conseguenze.

Questi approcci non sono equivalenti e non devono essere applicati semplicemente perché una decisione contiene incertezza. La questione è comprendere quale incertezza esiste, quale conoscenza manca e quale pratica può produrre evidenze rilevanti per la decisione.

## 1.5. Ogni decisione produce conseguenze dirette e indirette

Una decisione produce più di un risultato immediato. Può impegnare risorse, creare dipendenze, stabilire vincoli, eliminare percorsi o rendere determinate modifiche più costose. Alcune di queste conseguenze compaiono direttamente dopo la decisione, mentre altre emergono come effetti indiretti di ciò che è stato modificato.

Le conseguenze possono inoltre propagarsi ad altre parti della situazione. Una decisione sulla tecnologia può modificare il lavoro di un team. Una decisione di progetto può modificare responsabilità, tempi o risorse. Una decisione di prodotto può influenzare clienti, utenti o partner. Un cambiamento organizzativo può creare nuovi impegni per altre aree.

Quando una decisione produce effetti su altre persone o gruppi, emerge anche una necessità di comunicazione. È necessario rendere comprensibile ciò che è stato deciso, perché la decisione è stata presa, quali conseguenze sono previste e cosa cambia per coloro che saranno interessati o dovranno agire a partire da essa. In questo senso, la comunicazione non è soltanto un'attività successiva alla decisione, ma parte della gestione delle sue conseguenze.

Una decisione può inoltre preservare opzioni, generare nuove alternative o produrre informazioni utili per decisioni successive. I suoi effetti, quindi, non si limitano a ciò che accade immediatamente dopo la scelta. Alcune conseguenze modificano le condizioni nelle quali verranno prese altre decisioni.

È in questo senso che possiamo comprendere lo spazio delle possibilità. Esso rappresenta ciò che può essere fatto a partire da un determinato momento, considerando le risorse, gli impegni, le dipendenze e i vincoli esistenti. Le conseguenze di una decisione possono modificare questo spazio, rendendo alcune possibilità più accessibili, altre più difficili e altre ancora impraticabili.

Modificare lo spazio delle possibilità non significa necessariamente ridurre le opzioni. Una scelta può eliminare determinati percorsi e, allo stesso tempo, crearne altri. Una nuova capacità tecnologica può aprire alternative che prima non esistevano. Una decisione commerciale può creare accesso a un mercato e chiuderne un altro.

Ogni scelta implica anche trade-off. Favorendo un determinato risultato, una decisione può richiedere concessioni rispetto ad altri obiettivi, criteri o possibilità.

Migliorare le prestazioni può aumentare i costi. Ridurre i tempi può aumentare i rischi. Aumentare la flessibilità può elevare la complessità. Preservare la compatibilità può limitare la capacità di evoluzione. In molti casi, non esiste un'alternativa che massimizzi simultaneamente tutti gli obiettivi.

Questa dinamica può essere osservata attraverso l'idea di opzionalità. Alcune scelte preservano una maggiore capacità di cambiamento futuro. Altre aumentano gli impegni e riducono il margine di manovra. La conseguenza di una decisione può quindi essere osservata anche attraverso la capacità che essa preserva o elimina per le decisioni successive.

La reversibilità è rilevante a questo punto. Una decisione facile da annullare produce conseguenze diverse da una decisione che richiede grande sforzo o costo per essere invertita. Ciò non significa che le decisioni reversibili siano sempre migliori, ma che la loro struttura delle conseguenze è diversa.

Il tempo rende questa dinamica ancora più evidente. Rimandare una scelta può consentire l'emergere di nuove informazioni, ma può anche far scomparire un'opportunità, consumare risorse o permettere che altre decisioni vengano prese prima.

Rimanere nello stato attuale non significa rimanere di fronte alle stesse alternative. Anche il contesto continua a evolvere e l'assenza di una decisione può fare sì che determinate opzioni diventino più costose, impraticabili o semplicemente cessino di esistere.

È in questo senso che anche non decidere deliberatamente può costituire una decisione. Esiste una differenza tra scegliere consapevolmente di non agire e semplicemente non rendersi conto che era necessario prendere una decisione, ma entrambe le situazioni possono produrre effetti sulle possibilità future.

La quinta necessità prodotta da questo fondamento è comprendere, trattare e comunicare le conseguenze delle alternative considerate. Ciò implica analizzare non solo quale alternativa produca un determinato risultato, ma anche quali effetti diretti e indiretti possa generare, chi possa essere interessato, come tali effetti debbano essere comunicati e come la decisione modifichi le condizioni per le decisioni successive.

Scenari, analisi delle alternative, trade-off, comunicazione, coordinamento, reversibilità, dipendenze, costo opportunità, opzionalità e path dependency sono diverse modalità di trattare questa necessità.

L'obiettivo non è trovare un'alternativa universalmente migliore. È comprendere come ciascuna alternativa risponde agli obiettivi e ai vincoli esistenti, quali conseguenze produce, chi può esserne interessato e come tali conseguenze modificano lo spazio delle possibilità per il futuro.

## 1.6. Ogni decisione partecipa a un processo di evoluzione

Una decisione modifica la situazione successiva perché le sue conseguenze alterano lo spazio delle possibilità. Le risorse possono essere consumate o create, gli impegni possono essere assunti, possono emergere dipendenze, le alternative possono essere eliminate o aperte e possono essere prodotte nuove informazioni.

Questa alterazione dello spazio delle possibilità modifica le condizioni che saranno osservate per le decisioni successive. Il contesto può cambiare, alcuni obiettivi possono diventare impraticabili o acquisire importanza, nuove incertezze possono emergere o scomparire e altre alternative possono diventare disponibili.

È in questo senso che questa guida utilizza il termine evoluzione. Evoluzione significa cambiamento di stato nel tempo come conseguenza delle decisioni, delle azioni realizzate, delle informazioni prodotte e delle condizioni che cambiano. Non implica necessariamente un miglioramento.

Un sistema può avvicinarsi ai propri obiettivi, ma può anche accumulare vincoli, dipendenze, costi o problemi che rendono più difficili i cambiamenti successivi. Un'organizzazione può imparare da una decisione e, allo stesso tempo, assumere impegni che condizionano le proprie scelte successive.

Pianificazione, esecuzione, osservazione e apprendimento fanno parte di questa dinamica. Una decisione può essere mantenuta, rivista o sostituita man mano che emergono nuovi dati e che cambiano le condizioni per nuove scelte.

Modelli come PDCA e OODA rappresentano diversi modi di organizzare cicli di questo tipo. Non sono modelli di Architettura delle Decisioni, ma aiutano a illustrare una dinamica nella quale azione, osservazione, apprendimento e cambiamento sono correlati.

Quando questo processo si ripete, le scelte precedenti iniziano a influenzare quelle successive. Generano dipendenze, impegni, vincoli e apprendimenti che entrano a far parte delle condizioni delle scelte future.

Questa accumulazione appare anche nell'architettura dei sistemi. L'architettura attuale può essere vista come il risultato di molte decisioni prese nel corso del tempo, alcune deliberate, altre condizionate dalle circostanze esistenti.

Una decisione architetturale, ad esempio, può introdurre una tecnologia. Successivamente, questa tecnologia influenza l'assunzione di professionisti, la scelta degli strumenti, i costi operativi e le decisioni di integrazione. Una decisione iniziale, quindi, partecipa alla formazione delle condizioni per le decisioni successive.

Ciò significa che una decisione non deve essere analizzata soltanto rispetto allo stato esistente nel momento in cui viene presa. Dobbiamo considerare anche gli effetti che produce sullo spazio delle possibilità, sulle condizioni delle decisioni future e sulla conoscenza che genera.

La sesta necessità prodotta da questo fondamento è l'osservazione, l'apprendimento e la conservazione della conoscenza prodotta dall'evoluzione.

Dobbiamo essere in grado di osservare ciò che è accaduto, confrontare il risultato con ciò che ci aspettavamo e comprendere le ragioni di eventuali differenze.

Dobbiamo inoltre essere in grado di recuperare informazioni rilevanti sulle decisioni precedenti quando nuove decisioni dipendono da esse. Ciò non significa documentare tutto. Significa preservare ciò che sarà necessario per comprendere decisioni rilevanti in futuro.

A seconda del dominio, ciò può essere realizzato mediante indicatori, feedback, retrospettive, registri delle decisioni, documentazione, esperimenti o altri meccanismi di apprendimento.

La tracciabilità emerge come un modo per preservare questa conoscenza, ma non è l'obiettivo in sé. L'obiettivo è mantenere la capacità di comprendere l'evoluzione e utilizzare la conoscenza prodotta per orientare le decisioni future.

## 1.7. Come si relazionano i fondamenti

I sei fondamenti proposti in questa guida non devono essere interpretati come sei argomenti indipendenti. Descrivono dimensioni diverse della stessa struttura decisionale.

Una decisione avviene in un dominio, ma tale dominio si manifesta sempre all'interno di un contesto specifico. Il contesto definisce condizioni che influenzano ciò che può essere fatto. All'interno di queste condizioni esistono obiettivi che orientano la scelta. Poiché il futuro non è completamente conosciuto, esiste incertezza. La decisione produce conseguenze dirette e indirette, che possono influenzare persone, risorse, sistemi e le condizioni per le decisioni future. Queste conseguenze modificano lo spazio delle possibilità e, facendolo, modificano le condizioni nelle quali verranno prese nuove decisioni. È in questo processo che avviene l'evoluzione.

Possiamo quindi visualizzare questa relazione in forma concatenata:

Dominio → contesto → obiettivi → incertezza → conseguenze → evoluzione

Il concatenamento non rappresenta una sequenza di fasi. Rappresenta una relazione tra dimensioni che si influenzano continuamente.

Una nuova informazione sul dominio può modificare la nostra comprensione del contesto. Un cambiamento nel contesto può rendere un obiettivo impraticabile o rivelarne un altro più importante. Un obiettivo diverso può cambiare quali alternative vengono considerate. Una nuova evidenza può ridurre un'incertezza. Una decisione può produrre conseguenze che eliminano un'alternativa futura o creano una nuova possibilità. Questi cambiamenti modificano lo spazio delle possibilità e, di conseguenza, le condizioni disponibili per le decisioni successive. Anche un risultato inatteso può modificare nuovamente il contesto e richiedere una nuova comprensione della situazione.

La decisione, quindi, non avviene all'interno di una struttura statica. Avviene all'interno di una struttura che si modifica mentre apprendiamo, scegliamo e agiamo.

Questa relazione aiuta a spiegare perché pratiche e framework diversi possano sembrare così differenti e, allo stesso tempo, trattare necessità correlate.

Possiamo stabilire una seconda relazione:

Caratteristica → necessità → pratica → framework

Il dominio produce la necessità di delimitazione. Questa necessità può essere trattata mediante pratiche di definizione dei confini, modellazione, ambito e linguaggio comune. DDD, ad esempio, offre pratiche per comprendere e delimitare i domini, stabilire modelli e definire bounded contexts. Anche altri approcci di architettura, gestione e analisi aziendale possiedono pratiche destinate a rendere espliciti i limiti di ciò che viene analizzato.

Il contesto produce la necessità di esplicitare le condizioni esistenti. Ciò può coinvolgere la rilevazione di vincoli, assunzioni, dipendenze, situazione attuale, stakeholder e risorse disponibili. arc42 lavora esplicitamente con contesto e ambito, vincoli e strategia della soluzione. Anche TOGAF struttura attività relative alla comprensione dell'ambiente, dell'architettura e della transizione. Nei progetti, le pratiche di pianificazione e diagnosi svolgono funzioni simili.

Gli obiettivi producono la necessità di criteri di valutazione. Requisiti, metriche, indicatori, attributi di qualità e criteri di successo sono alcune delle possibili modalità per soddisfare questa necessità. Scrum utilizza Product Goal e Sprint Goal per orientare il lavoro. PMBOK lavora con obiettivi, pianificazione, delivery e misurazione. In architettura, requisiti funzionali, attributi di qualità e vincoli aiutano a stabilire riferimenti per valutare le alternative.

L'incertezza produce la necessità di trattare ciò che ancora non conosciamo. In questo caso, possiamo utilizzare analisi dei rischi, formulazione di ipotesi, sperimentazione, prototipazione, ricerca, scenari o altre pratiche di indagine. Lean Startup utilizza sperimentazione e apprendimento per testare ipotesi. Design Thinking utilizza indagine, ideazione, prototipazione e test per apprendere sulle necessità e sulle possibili soluzioni. Le pratiche di gestione dei rischi trattano eventi incerti e le loro possibili conseguenze.

Le conseguenze producono la necessità di analizzare i loro effetti e trattare quelli che devono essere considerati dalla decisione. Ciò include comprendere gli impatti diretti e indiretti, identificare chi può essere interessato, comunicare i cambiamenti rilevanti, coordinare le azioni conseguenti e valutare come la decisione modifichi le condizioni per le scelte future. A questo punto emergono pratiche come analisi degli scenari, confronto delle alternative, identificazione dei trade-off, analisi della reversibilità, valutazione delle dipendenze, comunicazione e coordinamento. Nella pianificazione, diverse opzioni di esecuzione possono essere confrontate in base ai loro impatti, costi, rischi e impegni.

L'evoluzione produce la necessità di osservare i risultati, apprendere e preservare la conoscenza. Scrum incorpora ispezione e adattamento. Lean Startup struttura cicli di costruzione, misurazione e apprendimento. Le retrospettive permettono di esaminare l'esperienza di un ciclo e adattare quello successivo. Gli ADR preservano la conoscenza sulle decisioni che continuano a influenzare l'evoluzione dell'architettura. Altri metodi e pratiche utilizzano meccanismi diversi per soddisfare la stessa necessità fondamentale.

Questi esempi non significano che ogni framework appartenga a un solo fondamento. Questa sarebbe un'interpretazione eccessivamente rigida. Un framework può soddisfare diverse necessità contemporaneamente perché una pratica agisce frequentemente su più di una dimensione della decisione.

Scrum, ad esempio, non tratta soltanto l'evoluzione. I suoi obiettivi orientano il lavoro, i suoi meccanismi di ispezione producono informazioni e il suo adattamento permette di rivedere le decisioni man mano che emergono nuove evidenze. Lean Startup non tratta soltanto l'incertezza. I suoi cicli collegano anche obiettivi, evidenze, risultati ed evoluzione. arc42 non tratta soltanto la documentazione. La sua struttura mette in relazione contesto, obiettivi, vincoli, qualità, decisioni, rischi e conoscenza architetturale.

Lo stesso vale per le pratiche di architettura. Una decisione architetturale deve considerare il dominio nel quale esiste il sistema, le condizioni attuali, gli obiettivi di qualità e di business, le incertezze tecniche, le alternative disponibili e le conseguenze che saranno portate dall'architettura nel tempo.

Per questo, il framework non deve necessariamente essere il punto di partenza. Può essere una risposta a una necessità che è già stata identificata.

Questa inversione è importante. Invece di chiedere prima “quale framework dobbiamo usare?”, possiamo iniziare chiedendo: “quale decisione stiamo cercando di condurre?”, “quali caratteristiche di questa decisione devono essere trattate?”, “quali necessità emergono da queste caratteristiche?” e, solo allora, “quali pratiche o framework possono aiutarci?”.

I sei fondamenti proposti in questa guida, quindi, non cercano di sostituire DDD, TOGAF, arc42, Scrum, PMBOK, Lean Startup, Design Thinking, ADR o altri metodi. Offrono un modo per vedere ciò che questi approcci cercano di trattare e per riconoscere che discipline diverse possono sviluppare risposte differenti a necessità strutturalmente correlate.

Questa prospettiva sarà importante nei capitoli successivi. Dopo aver compreso le caratteristiche generali di una decisione, dobbiamo entrare nella situazione concreta in cui essa avviene. Prima di definire quale problema risolvere o quale soluzione applicare, dobbiamo comprendere il dominio, il contesto, i limiti e le condizioni esistenti.

È da qui che l'Architettura delle Decisioni smette di essere soltanto una struttura concettuale e inizia a orientare la conduzione di una decisione reale.
