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
        <tr style="border-color:lightgray">
        	  <td colspan=3 style="background-color:lightgray">Date</td>
            <td colspan=9>2016-12-29</td>
        </tr>
   </tbody>
</table>

oppure

<table>
    <tbody>
        <tr style="border-color:lightgray">
        	  <td colspan=3 style="background-color:lightgray">Date</td>
            <td colspan=9>2018</td>
        </tr>
   </tbody>
</table>


- Gli **intervalli di data**, che vanno sempre scritti nel campo **Extra** tramite il parametro “Issued”, vanno composte nel formato `Issued: "YYYY-MM-DD/YYYY-MM-DD"`. Quando presente il parametro “issued” sovrascrive il campo **Date** se presente.

<table>
    <tbody>
        <tr style="border-color:lightgray">
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
        <tr style="border-color:lightgray">
        	  <td colspan=3 style="background-color:lightgray">Date</td>
            <td colspan=9>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
        </tr>
   </tbody>
</table>

- Qualora la pubblicazione non sia stata ancora rilasciata ma è in corso il processo di revisione scientifica (“in press”) va lasciato vuoto il campo **Date**, e la specificazione va inserita nel campo **Extra** tramite il parametro `Issued: "in press”`.

<table>
    <tbody>
        <tr style="border-color:lightgray">
        	  <td colspan=3 style="background-color:lightgray">Date</td>
            <td colspan=9>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
        </tr>
        <tr style="border-color:lightgray">
        	  <td colspan=3 style="background-color:lightgray">Extra</td>
            <td colspan=9>Issued: "in press"</td>
        </tr>
   </tbody>
</table>


- Qualora si dovesse indicare l’anno di pubblicazione dell’opera originale di un autore, indicare l’anno dell’opera originale nel campo **Extra** tramite il parametro `Original date: “YYYY”`.

<table>
    <tbody>
        <tr style="border-color:lightgray">
        	  <td colspan=3 style="background-color:lightgray">Extra</td>
            <td colspan=9>Original Date: "1900"</td>
        </tr>
   </tbody>
</table>

<!--GP arrivato qui 210526-->

## **Nomi di autori ed editori**
- I nomi degli autori (o degli altri tipi di creatori) possono essere scritti per esteso oppure con il nome abbreviato. Per lo stile APA 7th edition, verranno sempre comunque abbreviati.

||||
|--|--|--|
|Author|`Freud`|`Sigmund`|
||||
oppure
||||
|--|--|--|
|Author|`Freud`|`S.`|
||||

- Zotero consente di scrivere i nomi di autori (e altri creatori) in due diverse modalità: una modalità a campo unico, e una a campo spezzato per nome e per cognome. Il cambio di modalità è possibile cliccando l’icona apposita di fianco al campo del nome.
La modalità spezzata è quella che generalmente risponde a quasi tutti gli usi, e quando si tratta di persone. La modalità a campo unico viene utilizzata quando il creatore è una associazione, oppure è necessario specificare il ruolo del creatore (che chiaramente non fa parte né del nome e né del cognome).
Nel caso sia necessario utilizzare

e.g. 1
||||
|--|--|--|
|Author|`Freud`|`Sigmund`|
||||
oppure
|||
|--|--|
|Author|`American Psychological Association`|
|||

e.g. 2
|||
|--|--|
|Director|`Sherman-Palladino, A. (Writer & Director)`|
|||
oppure
||||
|--|--|--|
|Producer|`Sherman-Palladino`|`A.`|
||||

- I nomi di autori (o altri creatori di opere) che includono delle abbreviazioni (es. “Martin Luther King jr”) vanno composti indicando Cognome: cognome,  Nome: abbreviazione, nome.

||||
|--|--|--|
|Author|`King`|`jr, Martin Luther`|
||||

- Qualora vi siano preposizioni al cognome (es. “Ludwig van Beethoven”) queste devono essere scritte a seguito del nome

||||
|--|--|--|
|Author|`Beethoven`|`Ludwig van`|
||||

-	Quando si compila una reference che possiede uno o più autori, ma che fa parte di una pubblicazione curata da uno o più editori, segnare tutti i nomi dei soggetti assegnando loro il ruolo corretto. Sia Zotero che il sistema Bembo li formatterà correttamente nelle posizioni adeguate.

e. g. Balsam, K. F., Martell, C. R., Jones, K. P., & Safren, S. A. (2019). Affirmative cognitive behavior therapy with sexual and gender minority people. In G. Y. Iwamasa, & P. A. Hays (Eds.), *Culturally responsive cognitive behavior therapy: Practice and supervision* (2nd ed., pp. 287–314). American Psychological Association. https://doi.org/10.1037/0000119-012

||||
|--|--|--|
|Editor|`Iwamasa`|`Gayle Y.`|
|Editor|`Hays`|`Pamela A.`|
|Author|`Balsam`|`Kimberly F.`|
|Author|`Martell`|`Christopher R.`|
|Author|`Jones`|`Kyle P.`|
|Author|`Safren`|`Steven A.`|
||||

- Quando si compila una reference, tipicamente di un contenuto audiovisuale, che identifica come autori dell’opera lo sceneggiatore e/o il regista (da scrivere nel campo Director solo), ma che è parte di una serie, occorre indicare anche i produttori esecutivi della serie come campo Producer. Se si indicano solamente i produttori esecutivi, la reference li posiziona al posto dei Director. In questo tipo di reference, indicare quindi SOLO eventuali Director (sceneggiatore e/o regista) e Producer (produttori)
    
e.g. Favreau, J. (Writer), & Filoni, D. (Director). (2019, November 12). Chapter 1 (Season 1, Episode 1) [TV series episode]. In J. Favreau, D. Filoni, K. Kennedy, & C. Wilson (Executive Producers), The Mandalorian. Lucasfilm; Golem Creations.

||||
|--|--|--|
|Director|`Favreau, J. (Writer)`
|Director|`Filoni, D. (Director)`|
|Producer|`Favreau`|`J.`|
|Producer|`Filoni`|`D.`|
|Producer|`Kennedy`|`K.`|
|Producer|`Wilson`|`C.`|
||||

**Titolazioni e annotazioni specifiche**

- Alcuni tipi di reference richiedono all’autore di specificare alcune informazioni tra parentesi quadre ([ ]). Quando ciò avviene, il sistema Bembo scrive automaticamente queste parti di informazione con lo stile appropriato.

||||
|--|--|--|
|Title|`Heterodox issues in psychology [Special section]`|
||||
oppure
||||
|--|--|--|
|Title|`Study Abroad Programs [Editorial]`|
||||

- Alcuni tipi di reference impongono l’uso di uno stile non corsivo per parti di titolazioni o altri campi, le quali sono racchiuse tra parentesi quadre ([ ]). Tuttavia, può essere necessario dover scrivere parti di informazioni in corsivo, anche se esse sono racchiuse tra quadre. Per fare ciò, è necessario racchiudere tra asterischi tali parti di testo (* *). Gli esempi specifici vengono illustrati nella parte successiva del documento, ma in linea generale la formattazione per queste informazioni è la seguente:
    
||||
|--|--|--|
|Title|`Bringing LGBTQ youth theater into the spotlight [Review of the film *The year we thought about love*, by E. Brodsky, Dir.].`|
||||

**Edizioni e note su edizioni**

- I numeri di edizione vanno indicati con un semplice numero arabico, senza ordinali. Le edizioni con diciture particolari (e.g. “North American edition”, o “Global edition”) vanno indicate senza aggiungere la dicitura “edition”

||||
|--|--|--|
|Edition|`2`|
||||
oppure
||||
|--|--|--|
|Edition|`Summer 2019`|
||||
oppure
||||
|--|--|--|
|Edition|`North American`|
||||

**Archivi e collocazioni in archivi**

- Qualora la reference necessiti di indicare il nome dell’archivio (campo Archive) e la collocazione del documento nell’archivio (campo Loc. in Archive), occorre indicare anche nel campo Extra le medesime informazioni tramite i parametri “collection-title” e “collection-number”.

||||
|--|--|--|
|Archive|`ProQuest Dissertations and Theses Global`|
|Loc. in Archive|`Publication No. 10289373`|
|Extra|`collection-title: “ProQuest Dissertations and Theses Global” collection-number: “Publication No. 10289373”`|
||||

