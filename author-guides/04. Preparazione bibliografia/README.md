# 4. Linee guida per la preparazione della bibliografia

**Bembo Officina Editoriale**

**Scuola di dottorato dell’Università Iuav di Venezia**


## 4.1 Introduzione all’interfaccia del software di reference management Zotero

Il software Zotero ha una interfaccia divisa in sezioni (Fig.1). 

![Figura 1. Interfaccia di zotero con indicate le diverse sezioni](_img/fig.1_zotero_UI_sections.png "Fig.1. Sezioni dell'interfaccia di Zotero")


- La **barra a sinistra** riporta le **collezioni** disponibili nel proprio software, sia locali sia condivise.
- La **sezione centrale** riporta la **lista di tutti i reference** [riferimenti] inclusi in una collezione.
- La **sezione destra** riporta le informazioni (**metadati**) catalogati per lo specifico riferimento evidenziato. Per compilare correttamente i reference secondo le seguenti linee guida è fondamentale saper compilare in particolar modo la sezione di destra.  

Nella questa **sezione di destra dei metadati** ci sono **tre aree fondamentali** in cui inserire informazioni:

- **Item type**: è un menu a tendina che permette di definire il **tipo di documento** che si sta descrivendo. **Ogni tipologia prevede specifici campi con metadati**;
- **Fields**: sono i **campi da compilare** con le informazioni (metadati) per fare in modo che Zotero e il sistema Bembo creino correttamente i reference secondo uno stile citazionale definito. In questo caso APA 7ma edizione;
- **Field Extra**: è un **campo speciale**, rispetto agli altri campi che ammettono solo una riga di testo come contenuto, il field Extra può accogliere **diversi tipi di informazioni** e permette di specificare parametri e metadati.

Nel paragrafo seguente viene precisato come compilare correttamente i metadati per i campi Item, Fields e Extra.

## 4.2. Linee guida generali per la catalogazione delle reference nel software Zotero

Le indicazioni generali presentate in questa sezione riguardano tutti i reference, indipendentemente dal tipo di documento che si sta descrivendo.

### Date e intervalli di date

- Le **date** vanno composte nel formato `YYYY-MM-DD`, ogni altro formato non è accettato. Chiaramente, se non si conoscono mese e giorno, o quei dati non sono appropriati per la reference da compilare, inserire solamente i dati a disposizione.


<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray">Date</td>
            <td colspan=9>2016-12-29</td>
        </tr>
   </tbody>
</table>

oppure

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray">Date</td>
            <td colspan=9>2018</td>
        </tr>
   </tbody>
</table>


- Gli **intervalli di data**, che vanno sempre scritti nel campo **Extra** tramite il parametro “Issued”, vanno composte nel formato `Issued: "YYYY-MM-DD/YYYY-MM-DD"`. Quando presente il parametro “issued” sovrascrive il campo **Date** se presente.

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Extra </td>
            <td colspan=9>Issued: "2018-09-27/2018-09-30"</td>
        </tr>
   </tbody>
</table>

<table>
    <tbody>
        <tr style="font-size:small">
        	  <td colspan=3>esempi</td>
            <td colspan=9>Pearson, J. (2018, September 27-30). <em>Fat talk and its effects on state-based body image in women</em> [Poster presentation]. Australian Psychological Society Congress, Sydney, NSW, Australia. http://bit.ly/2XGSThP<br>
            <hr>
            Maddox, S., Hurling, J., Stewart, E., & Edwards, A. (2016, March 30-April 2). <em>If mama ain’t happy, nobody’s happy: The effect of parental depression on mood dysrégulation in children</em> [Paper presentation]. Southeastern Psychological Association 62nd Annual Meeting, New Orleans, LA, United States
</td>
        </tr>
   </tbody>
</table>

 - Qualora la **pubblicazione non sia stata ancora rilasciata** ma è in processo di revisione scientifica, lasciare il campo Date vuoto, il sistema Bembo aggiungerà la dicitura `“in press”` nel caso si tratti di un articolo o di un libro.
Stesso vale per le altre reference che non hanno una data di pubblicazione: lasciando il campo **Date** vuoto, il sistema Bembo aggiungerà la dicitura `“n.d.”`.

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray">Date</td>
            <td colspan=9>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
        </tr>
   </tbody>
</table>

- Qualora la pubblicazione non sia stata ancora rilasciata ma è in corso il processo di revisione scientifica (“in press”) va lasciato vuoto il campo **Date**, e la specificazione va inserita nel campo **Extra** tramite il parametro `Issued: "in press”`.

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray">Date</td>
            <td colspan=9>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray">Extra</td>
            <td colspan=9>Issued: "in press"</td>
        </tr>
   </tbody>
</table>


- Qualora si dovesse indicare l’anno di pubblicazione dell’opera originale di un autore, indicare l’anno dell’opera originale nel campo **Extra** tramite il parametro `Original date: “YYYY”`.

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray">Extra</td>
            <td colspan=9>Original Date: "1900"</td>
        </tr>
   </tbody>
</table>



### Nomi di autori ed editori

- I nomi degli autori (o degli altri tipi di creatori) possono essere scritti per esteso oppure con il nome abbreviato. Per lo stile APA 7th edition, verranno sempre comunque abbreviati.

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Author </td>
            <td colspan=3> Freud </td>
            <td colspan=6> Sigmund </td>
        		 </tr>
		 <tr style="background-color: white">
		 <td colspan=9>oppure<oppure>
		 </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Author </td>
            <td colspan=3> Freud </td>
            <td colspan=6> S. </td>
        </tr>
   </tbody>
</table>

- Zotero consente di scrivere i nomi di autori (e altri creatori) in due diverse modalità: una modalità a campo unico, e una a campo spezzato per nome e per cognome. Il cambio di modalità è possibile cliccando l’icona apposita di fianco al campo del nome.<br>
La modalità spezzata è quella che generalmente risponde a quasi tutti gli usi, e quando si tratta di persone. La modalità a campo unico viene utilizzata quando il creatore è una associazione, oppure è necessario specificare il ruolo del creatore (che chiaramente non fa parte né del nome e né del cognome).
Nel caso sia necessario utilizzare

**es. 1**

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Author </td>
            <td colspan=3> Freud </td>
            <td colspan=6> Sigmund </td>
		 </tr>
		 <tr style="background-color: white">
		 <td colspan=9>oppure<oppure>
		 </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Author </td>
            <td colspan=6> American Psychological Association </td>
        </tr>
   </tbody>
</table>

**es. 2**

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Director </td>
            <td colspan=6> Sherman-Palladino, A. (Writer & Director) </td>
        </tr>
		 <tr style="background-color: white">
		 <td colspan=9>oppure<oppure>
		 </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Director </td>
            <td colspan=3> Freud </td>
            <td colspan=6> Sigmund </td>
		 </tr>
   </tbody>
</table>

- I nomi di autori (o altri creatori di opere) che includono delle abbreviazioni (es. “Martin Luther King jr”) vanno composti indicando Cognome: cognome,  Nome: abbreviazione, nome.

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Author </td>
            <td colspan=6> King </td>
            <td colspan=6> jr, Martin Luther</td>
        </tr>
   </tbody>
</table>


- Qualora vi siano preposizioni al cognome (es. “Ludwig van Beethoven”) queste devono essere scritte a seguito del nome

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Author </td>
            <td colspan=6> Beethoven </td>
            <td colspan=6> Ludwig van </td>
        </tr>
   </tbody>
</table>


-	Quando si compila un reference che possiede uno o più autori, ma che fa parte di una pubblicazione curata da uno o più editori, segnare tutti i nomi dei soggetti assegnando loro il ruolo corretto. Sia Zotero che il sistema Bembo li formatterà correttamente nelle posizioni adeguate.

**es.** Balsam, K. F., Martell, C. R., Jones, K. P., & Safren, S. A. (2019). Affirmative cognitive behavior therapy with sexual and gender minority people. In G. Y. Iwamasa, & P. A. Hays (Eds.), *Culturally responsive cognitive behavior therapy: Practice and supervision* (2nd ed., pp. 287–314). American Psychological Association. https://doi.org/10.1037/0000119-012

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Editor </td>
            <td colspan=6> Iwamasa </td>
            <td colspan=6> Gayle Y.</td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Editor </td>
            <td colspan=6"> Hays </td>
            <td colspan=6> Pamela A. </td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Author </td>
            <td colspan=6> Balsam </td>
            <td colspan=6> Kimberly F.</td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Author </td>
            <td colspan=6> Martell </td>
            <td colspan=6> Christopher R.</td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Author </td>
            <td colspan=6> Jones </td>
            <td colspan=6> Kyle P.</td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Author </td>
            <td colspan=6> Safren </td>
            <td colspan=6> Steven A. </td>
        </tr>
   </tbody>
</table>


- Quando si compila un reference, tipicamente di un contenuto audiovisivo, che ha un proprio sceneggiatore e/o regista, ma che è parte di una serie, occorre sempre: indicare sceneggiatore e/o regista nel campo Director; indicare sempre anche i produttori esecutivi della serie nel campo Producer. Attenzione: se si indicano solamente i produttori esecutivi, Zotero li posiziona al posto dei Director.
In questo tipo di reference, indicare quindi **SOLO** eventuali Director (sceneggiatore e/o regista) e Producer (produttori).
    
e.g. Favreau, J. (Writer), & Filoni, D. (Director). (2019, November 12). Chapter 1 (Season 1, Episode 1) [TV series episode]. In J. Favreau, D. Filoni, K. Kennedy, & C. Wilson (Executive Producers), The Mandalorian. Lucasfilm; Golem Creations.

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Director </td>
            <td colspan=12> Favreau, J. (Writer) </td>

        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Director </td>
            <td colspan=12"> Filoni, D. (Director) </td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Producer </td>
            <td colspan=6> Favreau </td>
            <td colspan=6> J.</td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Producer </td>
            <td colspan=6> Filoni </td>
            <td colspan=6> D.</td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Producer </td>
            <td colspan=6> Kennedy </td>
            <td colspan=6> K.</td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Producer </td>
            <td colspan=6> Wilson </td>
            <td colspan=6> C. </td>
        </tr>
   </tbody>
</table>





### Titolazioni e annotazioni specifiche

- Per alcuni reference lo stile APA 7ma edizione richiede di precisare alcune informazioni fra parentesi quadre dopo il titolo (es. il tipo di documento). Queste informazioni risultano generalmente in tondo. Alcuni tipi di reference richiedono di specificare alcune informazioni tra parentesi quadre ([ ]). Il sistema Bembo scrive  automaticamente queste parti di informazione con lo stile appropriato.

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Title </td>
            <td colspan=9> Heterodox issues in psychology [Special section] </td>
        </tr>
   </tbody>
</table>

oppure

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Title </td>
            <td colspan=9> Study Abroad Programs [Editorial] </td>
        </tr>
   </tbody>
</table>

- Quando è necessario applicare lo stile corsivo a una specifica informazione data tra parentesi quadre dopo il titolo, è possibile farlo racchiudendo fra asterischi la parte di testo interessata (* *).<br>
Gli esempi specifici vengono illustrati nella Sezione 3, ma in linea generale la formattazione per queste informazioni è la seguente:
    
<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Title </td>
            <td colspan=9> Bringing LGBTQ youth theater into the spotlight [Review of the film *The year we thought about love*, by E. Brodsky, Dir.]. </td>
        </tr>
   </tbody>
</table>


### Edizioni e note su edizioni

- I numeri di edizione vanno indicati con un semplice numero arabo, senza ordinali. Le edizioni con diciture particolari (es. “North American edition”, o “Global edition”) vanno indicate senza aggiungere la dicitura “edition”.

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Edition </td>
            <td colspan=9> 2 </td>
        </tr>
   </tbody>
</table>

oppure

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Edition </td>
            <td colspan=9> Summer 2019 </td>
        </tr>
   </tbody>
</table>

oppure

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Edition </td>
            <td colspan=9> North American </td>
        </tr>
   </tbody>
</table>


### Archivi e collocazioni in archivi

- Qualora il reference necessiti di indicare il nome dell’archivio (campo Archive) e la collocazione del documento nell’archivio (campo Loc. in Archive), occorre indicare anche nel campo Extra le medesime informazioni tramite i parametri “collection-title” e “collection-number”.

<table>
    <tbody>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Archive </td>
            <td colspan=12> ProQuest Dissertations and Theses Global
 </td>

        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Loc. in Archive </td>
            <td colspan=12"> Publication No. 10289373 </td>
        </tr>
        <tr style="background-color: white">
        	  <td colspan=3 style="background-color:lightgray"> Extra </td>
            <td colspan=12"> collection-title: “ProQuest Dissertations and Theses Global”<br>
			  collection-number: “Publication No. 10289373”</td>
        </tr>
   </tbody>
</table>


## 4.3 Linee guida particolari per la descrizione di specifici tipi di reference nel software Zotero

Le indicazioni presentate in questa sezione riguardano i differenti tipi di documenti, e di reference.

La tabella seguente guida gli autori nella scelta del  tipo di reference e indica come impostare correttamente i relativi metadati in Zotero.

Le colonne della tabella esplicitano le informazioni rilevanti per la scelta e la logica di composizione dei reference:

- **APA category**: Il manuale APA 7ma edizione categorizza i vari tipi di reference per “macro gruppi”, individuando ad esempio “Articles”, “Books”, “Book Chapters”, “Webpages” ecc. Questo primo livello di categorizzazione aiuta l’autore a cercare intuitivamente nella Tabella 1. Linee guida per la preparazione dei reference in Zotero utile per il tipo di documento da catalogare e citare;
- **APA prototype**: A seguito della prima categorizzazione, segue una categorizzazione più fine del tipo di documento da citare. Spesso questa seconda categorizzazione distingue sotto-gruppi di documenti, o sfumature di forma tra documenti simili, e porta l’autore a scegliere definitivamente la modalità di citazione del documento.
- **Zotero Item type**: Questa colonna della tabella aiuta a scegliere l’Item Type corretto per la compilazione di reference in relazione alle casistiche previste da APA 7ma edizione.  
- **Required fields**: Questa colonna riporta quali campi di Zotero è obbligatorio compilare per ottenere una reference formattata correttamente, sia da Zotero stesso sia dal Sistema Bembo. Gli autori sono tenuti a compilare questi campi.
- **Optional fields**: Questa colonna riporta quali campi di Zotero sono facoltativi, perché non strettamente essenziali alla identificazione del reference, ma importanti per una sua corretta compilazione.
- **Notes**: Questa colonna riporta alcuni suggerimenti per guidare gli autori nella corretta compilazione del database dei reference in Zotero, e quindi il successivo corretto invio e generazione della lista di reference.

Gli autori sono invitati quindi a usare la seguente tabella (Tab. 1) come “mappa” per individuare le informazioni da inserire in Zotero per ogni tipo di reference da citare nel proprio scritto.

Nel raro caso in cui possa capitare un tipo di reference da citare che non è indicata nella tabella qui a seguito, si suggerisce di raccogliere / fare una lista dei casi e confrontarsi con la redazione di Bembo OE.


**Tabella 1. Lista completa delle tipologie di reference e indicazioni per la catalogazione in Zotero**

`Qui va inserita la tabella generata dal Sistema Bembo. Ora finisce in /references/docs/README.md`

## 4.4 Esportazione file .bib per la consegna

Una volta che gli autori hanno completato la compilazione della  collezione di reference per il proprio scritto, è sufficiente cliccare con il tasto destro sulla cartella della collezione nel pannello delle collezioni (barra di sinistra), e scegliere l’opzione “Esporta collezione” / “Export collection”.

![Figura 2. Interfaccia di zotero con istruzione di click destro su collezione e pop-up menù](_img/fig.2 zotero export collection.png "Fig.2. Esportazione collezione Zotero")

Quando compare la finestra per la selezione del formato di esportazione, scegliere il formato “BibLaTeX”.


![Figura 3. Popup di zotero con scelta del formato di esportazione](_img/fig.3 zotero export biblatex.png "Fig.3. Scelta formato di esportazione in BibLaTeX")

Verrà chiesto dove salvare il file formato .bib generato e questo poi verrà esportato. Tale file .bib deve essere consegnato alla redazione di Bembo OE congiuntamente alla cartella compressa .zip contente i file markdown con gli scritti dell’autore.

I reference inviati verranno sempre inclusi negli elaborati con le informazioni bibliografiche formattate in lingua inglese, indipendentemente dalla lingua dello scritto.
