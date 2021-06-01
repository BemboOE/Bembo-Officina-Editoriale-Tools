# Bembo Officina Editoriale – Tools

Questo è il repository Github di **[Bembo Officina Editoriale (Bembo OE)](https://bemboedizioni.it/)**, la Officina Editoriale della Scuola di dottorato dell’Università Iuav di Venezia.  
 
**Bembo Officina Editoriale (Bembo OE) è la casa editrice della Scuola di Dottorato IUAV**. Le sue pubblicazioni sono mirate principalmente alla diffusione della conoscenza, della ricerca e dei lavori dei dottorandi.

Bembo OE adotta un **modello gratuito ad accesso aperto** (Open Access) e un processo editoriale collaborativo e condiviso, che coinvolge direttamente autori e curatori nella produzione delle pubblicazioni, nel rispetto dei criteri della più rigorosa scientificità.
 
Il modello di pubblicazione “Open Access” favorisce il più possibile la circolazione delle pubblicazioni. Non viene richiesto agli autori un contributo economico per la pubblicazione (come spesso avviene nell’ambito dell’editoria tradizionale), ma **viene richiesta collaborazione nella produzione dei volumi**, avvalendosi di  **strumenti di scrittura specifici** necessari alla casa editrice per impaginare gli elaborati.
Autori e curatori sono dunque responsabili della preparazione, della consegna e del controllo dei materiali nel rispetto delle istruzioni e delle linee guida fornite. 
 
**Le pubblicazioni seguono l’iter di pubblicazione tipico dell’ambito accademico**: le proposte di volumi o contributi vengono valutate da un comitato scientifico e, se ritenute adeguate, viene avviato un processo redazionale sui contenuti e sulla forma dei testi.
Al momento della pubblicazione, tutti i titoli saranno forniti di ISBN e DOI come avviene per tutte le pubblicazioni editoriali e accademiche. **Le pubblicazioni sono rese disponibili per il print-on-demand**, per chi volesse il proprio volume cartaceo, oppure online in versione integrale sul sito della casa editrice.
 
Le tipologie di pubblicazioni che la casa editrice accoglie sono tre:

1. **saggi** elaborati a partire dalle tesi di dottorato;
2. **atti di convegni** e di conferenze organizzati da dottorandi nell’ambito delle attività della Scuola di dottorato;
3. **materiali**, pubblicazione di **documenti originali** non ancora pubblicati o resi pubblici.
 
 
Bembo OE adotta un **sistema innovativo di impaginazione quasi totalmente automatizzato**. Per sfruttare al meglio questo sistema di produzione, autori e curatori devono preparare i testi e i riferimenti bibliografici utilizzando **specifici software open source e gratuiti** (si veda la [sezione 2. Istruzioni per software di scrittura](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/02%20IstruzionI%20per%20software#2-istruzioni-per-software-di-scrittura-per-bembo-officina-editoriale) della presente guida) per la marcatura dei testi, per la gestione delle citazioni e la creazione della lista dei riferimenti bibliografici.
Tale sistema collaborativo rende sostenibile il costo di produzione dei volumi e permette di evitare la richiesta di contributo economico agli autori.

Questo sistema di redazione dei testi è corredato da complete **linee guida per gli autori** disponibili online a partire dal sito di Bembo Officina Editoriale. Proporre un'alternativa sostenibile sia per l’università sia per i dottorandi nella pubblicazione Open Access di ricerca scientifica, in un’ottica di collaborazione reciproca, è tra principali finalità di Bembo OE.
 
Autori e curatori devono inoltre fornire materiali iconografici definitivi liberi da diritti, di loro proprietà o per le quali abbiano comunque ottenuto i diritti di pubblicazione nelle forme previste da Bembo OE. 
 
Di seguito si riporta il sommario delle linee guida e le indicazioni pratiche per ottemperare a tutte le fasi del processo di pubblicazione.

1. 📄 [Sezione 1. Liberatoria per la pubblicazione](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/01%20Liberatoria) 
2. 🖥 [Sezione 2. Istruzioni per software di scrittura](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/02%20IstruzionI%20per%20software#2-istruzioni-per-software-di-scrittura-per-bembo-officina-editoriale)
3. 📝 [Sezione 3. Norme redazionali e citazione](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/03%20Norme%20redazionali%20e%20citazione)
4. 📖 [Sezione 4. Linee guida per la preparazione della bibliografia](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/04%20Preparazione%20bibliografia)
5. ✅ [Sezione 5. Istruzioni per la consegna degli elaborati](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/05%20Istruzioni%20consegna%20elaborati%20)
6. 🔄 Sezione 6. Processo di feedback
 
Technical Dependencies
---------
- [hoedown](https://github.com/hoedown/hoedown) (C library, through homebrew)
- https://github.com/aclements/biblib
- [jinja](https://jinja.palletsprojects.com/en/3.0.x/)
- [more_itertools](https://pypi.org/project/more-itertools/)
- [gspread](https://docs.gspread.org/en/latest/)
- [pytest](https://docs.pytest.org/en/6.2.x/) for running the references test suite
