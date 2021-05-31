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


-   Quando si compila un reference che possiede uno o più autori, ma che fa parte di una pubblicazione curata da uno o più editori, segnare tutti i nomi dei soggetti assegnando loro il ruolo corretto. Sia Zotero che il sistema Bembo li formatterà correttamente nelle posizioni adeguate.

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
            <td colspan=6> Hays </td>
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
            <td colspan=12> Filoni, D. (Director) </td>
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

- Quando è necessario applicare lo stile corsivo a una specifica informazione data tra parentesi quadre dopo il titolo, è possibile farlo racchiudendo fra asterischi la parte di testo interessata (\* \*).<br>
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
            <td colspan=12> ProQuest Dissertations and Theses Global</td>
        </tr>
        <tr style="background-color: white">
              <td colspan=3 style="background-color:lightgray"> Loc. in Archive </td>
            <td colspan=12> Publication No. 10289373 </td>
        </tr>
        <tr style="background-color: white">
              <td colspan=3 style="background-color:lightgray"> Extra </td>
            <td colspan=12> collection-title: “ProQuest Dissertations and Theses Global”<br>
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

<!-- START AUTOMATIC REFERENCES TABLE -->
<table>
<tr><th>APA category</th><th>APA prototype</th><th>Reference</th><th>Zotero item type</th><th>Required fields</th><th>Optional fields</th><th>Notes</th></tr>

    <tr><td colspan="7"><strong>APA Custom Edge Cases</strong></td></tr>

    <tr>
            <td>Articles</td>
            <td>journal article without issue number</td>
            <td>Bourzac, K. (2012). Child development: The first steps. <em>Nature</em><em>, 491</em>, S7. https://doi.org/http://dx.doi.org/10.1038/491S7a</td>
            <td>journal article</td>
            <td>title, author, pubblication, volume, pages, date, DOI</td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>Articles</td>
            <td>journal article without volume number</td>
            <td>Bonini Lessing, E. (2010). Notazioni sinsemiche di processi interattivi. <em>Il Verri – Newbasic</em> (43), 85–91</td>
            <td>journal article</td>
            <td>title, author, publication, issue, pages, date</td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>authored books from the same author, published in the same year</td>
            <td>Bourdieu, P. (2003a). <em>Il mestiere di scienziato. Corso al college de France 2000-2001</em> (A. Serra, Trans.). Feltrinelli. (Original work published 2001)</td>
            <td>book</td>
            <td>title, author, translator, series, publisher, date, ISBN, extra</td>
            <td></td>
            <td> add on Extra field: Original Date: "2001"</td></tr>

    <tr>
            <td>
Book / Ebook / Audio Book</td>
            <td>authored books from the same author, published in the same year</td>
            <td>Bourdieu, P. (2003b). <em>Per una teoria della pratica. Con tre studi di etnologia cabila</em> (I. Maffi, Trans.). Raffaello Cortina Editore</td>
            <td>book</td>
            <td>title, author, translator, series, volume, publisher, date, ISBN</td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>
Film, video, tv series</td>
            <td>Film or video</td>
            <td>Fleming, V. (Director). (1939). <em>Gone with the wind</em> [Film]. Selznick International Pictures; Metro-Goldwyn-Mayer</td>
            <td>film</td>
            <td>title, director, distributor, date, extra</td>
            <td></td>
            <td> add on Extra field: Medium "Film"</td></tr>

    <tr>
            <td>Film, video, tv series</td>
            <td>Film or video in another language</td>
            <td>Alfredson, T. (Director). (2008). <em>Låt den rätte komma in </em>[Let the right one in] [Film]. Magnolia</td>
            <td>film</td>
            <td>title, director, distributor, date, extra</td>
            <td></td>
            <td> add on Extra field: Medium "Film"</td></tr>

    <tr>
            <td>Film, video, tv series</td>
            <td>TV series</td>
            <td>Serling, R. (Executive Producer). (1959-1964). <em>The twilight zone</em> [TV series]. Cayuga Productions; CBS Productions</td>
            <td>film</td>
            <td>title, producer, network, extra</td>
            <td></td>
            <td>add on Producer field: Serling, R. (Executive Producer)
add on Exttra field:
Medium: "TV series"
Issued: "1959/1964"</td></tr>

    <tr>
            <td>Film, video, tv series</td>
            <td>TV series episode or webisode</td>
            <td>Favreau, J. (Writer), &amp; Filoni, D. (Director). (2019, November 12). Chapter 1 (Season 1, Episode 1) [TV series episode]. In J. Favreau, D. Filoni, K. Kennedy, &amp; C. Wilson (Executive Producers), <em>The Mandalorian</em>. Lucasfilm; Golem Creations</td>
            <td>tv broadcast</td>
            <td>title, director, producer, program title, episode number, network, date, extra</td>
            <td></td>
            <td>add on Director field: Favreau, J. (Writer)
add on Director field: Filoni, D. (Director)
add on Extra field: Medium "TV series episode"</td></tr>

    <tr>
            <td>Film, video, tv series</td>
            <td>TV series episode or webisode</td>
            <td>Sherman-Palladino, A. (Writer &amp; Director). (2018, December 5). All alone (Season 2, Episode 10) [TV series episode]. In A. Sherman-Palladino, D. Filoni, D. Palladino, D. Gilbert, M. Shapiro, S. Carino, &amp; S. Lawrence (Executive Producers), <em>The marvelous Mrs. Maisel</em>. Dorothy Parker Drank Here Productions; Picrow; Amazon Studios</td>
            <td>tv broadcast</td>
            <td>title, director, producer, program title, episode number, network, date, extra</td>
            <td></td>
            <td>add on Director field: Sherman-Palladino, A. (Writer & Director)
add on Extra field: Medium "TV series episode"</td></tr>

    <tr><td colspan="7"><strong>APA 7th CASES 2020-2021</strong></td></tr>

    <tr>
            <td>Articles</td>
            <td>newspaper article</td>
            <td>Hess, A. (2019, January 3). Cats who take direction. <em>The New York Times</em>, C1</td>
            <td>newspaper article</td>
            <td>title, author, publication, date</td>
            <td>pages</td>
            <td>dates should include day and month</td></tr>

    <tr>
            <td>Articles</td>
            <td>magazine article</td>
            <td>Bergeson, S. (2019, January 4). Really cool neutral plasmas. <em>Science</em><em>, 363</em>(6422), 33–34. https://doi.org/10.1126/science.aau7988</td>
            <td>journal article</td>
            <td>title, author, publication, date</td>
            <td>volume, issue, pages, DOI</td>
            <td>add only month and date after year; between DOI and URL the sysyem prefers DOI</td></tr>

    <tr>
            <td>Articles</td>
            <td>magazine article</td>
            <td>Bustillos, M. (2013, March 19). On video games and storytelling: An interview with Tom Bissell. <em>The New Yorker</em>. https://www.newyorker.com/books/page-turner/on-videogames- and-storytelling-an-interview-with-tom-bissell</td>
            <td>magazine article</td>
            <td>title, author, publication, date</td>
            <td>URL</td>
            <td>add only month and date after year; between DOI and URL the sysyem prefers DOI</td></tr>

    <tr>
            <td>Articles</td>
            <td>magazine article</td>
            <td>Weir, K. (2017, January). Forgiveness can improve mental and physical health. <em>Monitor on Psychology</em><em>, 48</em>(1), 30</td>
            <td>journal article</td>
            <td>title, author, publication, date</td>
            <td>volume, issue, pages</td>
            <td>add only month and date after year; between DOI and URL the sysyem prefers DOI</td></tr>

    <tr>
            <td>Articles</td>
            <td>journal article with DOI</td>
            <td>McCauley, S. M., &amp; Christiansen, M. H. (2019). Language learning as language use: A cross-linguistic model of child language development. <em>Psychological Review</em><em>, 126</em>(1), 1–51. https://doi.org/10.1037/rev0000126</td>
            <td>journal article</td>
            <td>title, author, publication, date</td>
            <td>volume, issue, pages, DOI </td>
            <td></td></tr>

    <tr>
            <td>Articles</td>
            <td>journal, magazine, or newspaper article without a DOI, from most academic research databases or print version</td>
            <td>Anderson, M. (2018). Getting Consistent with Consequences. <em>Educational Leadership</em><em>, 76</em>(1), 26–33</td>
            <td>journal article</td>
            <td>title, author, publication, date</td>
            <td>volume, issue, pages</td>
            <td></td></tr>

    <tr>
            <td>Articles</td>
            <td>journal article with a DOI, 21 or more authours</td>
            <td>Kalnay, E., Kanamitsu, M., Kistler, R., Collins, W., Deaven, D., Gandin, L., Iredell, M., Saha, S., White, G., Woollen, J., Zhu, Y., Chelliah, M., Ebisuzaki, W., Higgins, W., Janowiak, J., Mo, K. C., Ropelewski, C., Wang, J., Leetmaa, A., … Joseph, D. (1996). The NCEP/NCAR 40-Year Reanalysis Project. <em>Bulletin of the American Meteorological Society</em><em>, 77</em>(3), 437–472. https://doi.org/10.1175/1520-0477(1996)077&lt;0437:TNYRP&gt;2.0.CO;2</td>
            <td>journal article</td>
            <td>title, author, publication, date</td>
            <td>volume, issue, pages, DOI</td>
            <td></td></tr>

    <tr>
            <td>Articles</td>
            <td>journal article, in press</td>
            <td>Pachur, T., &amp; Scheibehenne, B. (in press). Unpacking buyer–seller differences in valuation from experience: A cognitive modeling approach. <em>Psychonomic Bulletin &amp; Review</em></td>
            <td>journal article</td>
            <td>title, author, publication, date</td>
            <td></td>
            <td>for date use in press</td></tr>

    <tr>
            <td>Articles</td>
            <td>special section or special issue in a journal</td>
            <td>Lilienfeld, S. O. (Ed.). (2018). Heterodox issues in psychology [Special section]. <em>Archives of Scientific Psychology</em><em>, 6</em>(1), 51–104</td>
            <td>journal article</td>
            <td>title, author, publication, date</td>
            <td>volume, issue, pages</td>
            <td>title should include [Special section], after title</td></tr>

    <tr>
            <td>Articles</td>
            <td>special section or special issue in a journal</td>
            <td>McDaniel, S. H., Salas, E., &amp; Kazak, A. E. (Eds.). (2018). The science of teamwork [Special issue]. <em>American Psychologist</em><em>, 73</em>(4)</td>
            <td>journal article</td>
            <td>title, author, publication, date</td>
            <td>volume, issue</td>
            <td>title should include [Special issue], after title</td></tr>

    <tr>
            <td>Articles</td>
            <td>editorial</td>
            <td>Cuellar, N. G. (2016). Study Abroad Programs [Editorial]. <em>Journal of Transcultural Nursing</em><em>, 27</em>(3), 209. https://doi.org/10.1177/1043659616638722</td>
            <td>journal article</td>
            <td>title, author, publication, date</td>
            <td>volume, issue, pages, DOI</td>
            <td>title should include [Editorial], after title</td></tr>

    <tr>
            <td>Reviews</td>
            <td>film review published in a journal</td>
            <td>Mirabito, L. A., &amp; Heck, N. C. (2016). Bringing LGBTQ youth theater into the spotlight [Review of the film <em aid:cstyle='corsivo'>The year we thought about love</em>, by E. Brodsky, Dir.]. <em>Psychology of Sexual Orientation and Gender Diversity</em><em>, 3</em>(4), 499–500. https://doi.org/10.1037/sgd0000205</td>
            <td>journal article</td>
            <td>title, author, date</td>
            <td>publication, volume, issue, pages, DOI</td>
            <td>title should include [Review of Title of work reviewed, by Author], after title</td></tr>

    <tr>
            <td>Reviews</td>
            <td>book review published in a newspaper</td>
            <td>Santos, F. (2019, January 11). Reframing refugee children’s stories [Review of the book <em aid:cstyle='corsivo'>We are displaced: My journey and stories from refugee girls around the world</em>, by M. Yousafzai]. <em>The New York Times</em>. https://nyti.ms/2Hlgjk3</td>
            <td>newspaper article</td>
            <td>title, author, date</td>
            <td>publication, URL</td>
            <td>title should include [Review of Title of work reviewed, by Author], after title</td></tr>

    <tr>
            <td>Reviews</td>
            <td>tv series episode review published on a website</td>
            <td>Perkins, D. (2018, February 1). <em>The Good Place ends its remarkable second season with irrational hope, unexpected gifts, and a smile </em>[Review of the TV series episode <em>Somewhere else</em>, by M. Schur, Writer &amp; Dir.]. A.V. Club. https://www.avclub.com/the-good-place-ends-its-remarkable-second-season-with-i-1822649316</td>
            <td>web page</td>
            <td>title, author, date</td>
            <td>web title, URL</td>
            <td></td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>authored book with a DOI</td>
            <td>Brown, L. S. (2018). <em>Feminist therapy</em> (2nd ed.). American Psychological Association. https://doi.org/10.1037/0000092-000</td>
            <td>book</td>
            <td>title, date</td>
            <td>publisher, author, DOI</td>
            <td></td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>authored book with editor credited on the book cover</td>
            <td>Meadows, D. H. (2008). <em>Thinking in Systems: A Primer</em> (D. Wright, Ed.). Chelsea Green Publishing</td>
            <td>book</td>
            <td>title, date</td>
            <td>publisher, author, editor</td>
            <td></td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>edited book without a DOI, from most academic research databases or print version</td>
            <td>Hacker Hughes, J. (Ed.). (2017). <em>Military Veteran Psychological Health and Social Care: Contemporary Approaches</em> (1st ed.). Routledge</td>
            <td>book</td>
            <td>title, date</td>
            <td>editor, publisher</td>
            <td></td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>edited book with a DOI, with multiple publishers</td>
            <td>Schmid, H.-J. (Ed.). (2017). <em>Entrenchment and the psychology of language learning: How we reorganize and adapt linguistic knowledge</em>. American Psychological Association; De Gruyter Mouton. https://doi.org/10.1037/15969-000</td>
            <td>book</td>
            <td>title, date</td>
            <td>DOI, publisher</td>
            <td>more than one editor required semicolon</td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>book in another language</td>
            <td>Amano, N., &amp; Kondo, H. (2000). <em>Nihongo no goi tokusei </em>[Lexical characteristics of Japanese language] (Vol. 7). Sansei-do</td>
            <td>book</td>
            <td>title, date</td>
            <td>author, volume, publisher</td>
            <td>title should include [The translated title], after title</td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>book in another language</td>
            <td>Piaget, J., &amp; Inhelder, B. (1966). <em>La psychologie de l’enfant </em>[The psychology of the child]. Quadrige</td>
            <td>book</td>
            <td>title, date</td>
            <td>author, publisher</td>
            <td>title should include [The translated title], after title</td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>republished book</td>
            <td>Freud, S. (2010). <em>The Interpretation of Dreams: The Complete and Definitive Text</em> (J. Strachey, Ed. &amp; Trans.). Basic Books. (Original work published 1900)</td>
            <td>book</td>
            <td>title, date</td>
            <td>author, editor, translator, publisher, extra</td>
            <td>add the original edition on Extra field with the form: Original Date: yyyy</td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>book republished in translation</td>
            <td>Piaget, J., &amp; Inhelder, B. (1969). <em>The Psychology of the Child</em> (H. Weaver, Trans.; 2nd ed.). Basic Books. (Original work published 1966)</td>
            <td>book</td>
            <td>title, date</td>
            <td>author, translator, edition, publisher, extra</td>
            <td>add the original edition on Extra field with the form: Original Date: yyyy</td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>one volume of a multivolume work</td>
            <td>Fiske, S. T., Gilbert, D. T., &amp; Lindzey, G. (Eds.). (2010). <em>Handbook of Social Psychology</em> (5th ed., Vol. 1). John Wiley &amp; Sons. https://doi.org/10.1002/9780470561119</td>
            <td>book</td>
            <td>title, date</td>
            <td>editor, volume, edition, publisher, DOI</td>
            <td></td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>diagnostic manual (DSM, ICD)</td>
            <td>American Psychiatric Association. (2013). <em>Diagnostic and Statistical Manual of Mental Disorders</em> (5th ed.). American Psychiatric Association. https://doi.org/10.1176/appi.books.9780890425596</td>
            <td>book</td>
            <td>title, date</td>
            <td>author, edition, publisher, DOI</td>
            <td></td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>diagnostic manual (DSM, ICD)</td>
            <td>World Health Organization. (2019). <em>International statistical classification of diseases and related health problems</em> (11th ed.). https://icd.who.int/</td>
            <td>book</td>
            <td>title, date</td>
            <td>author, edition, publisher, URL</td>
            <td></td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>dictionary, thesaurus, or encyclopedia</td>
            <td>American Psychological Association. (n.d.). <em>APA dictionary of psychology</em>. Retrieved June 14, 2019, from https://dictionary.apa.org/</td>
            <td>web page</td>
            <td>title, date, URL</td>
            <td>author, accessed</td>
            <td>add on Date field the form: n.d.</td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>dictionary, thesaurus, or encyclopedia</td>
            <td>Merriam-Webster. (n.d.). <em>Merriam-Webster.com dictionary</em>. Retrieved May 5, 2019, from https://www.merriamwebster.com/</td>
            <td>web page</td>
            <td>title, date, URL</td>
            <td>accessed</td>
            <td>add on Date field the form: n.d.</td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>dictionary, thesaurus, or encyclopedia</td>
            <td>Zalta, E. N. (Ed.). (2019). <em>The Stanford encyclopedia of philosophy</em> (Summer 2019 ed.). Stanford University. https://plato.stanford.edu/archives/sum2019/</td>
            <td>book</td>
            <td>title, date, URL</td>
            <td>editor, edition, publisher</td>
            <td></td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>authored ebook (e.g., Kindle book) or audiobook without a DOI, with a nondatabase URL</td>
            <td>Cain, S. (2012). <em>Quiet: The power of introverts in a world that can’t stop talking</em> (K. Mazur, Narr.) [Audiobook]. Random House Audio. http://bit.ly/2G0BpbI</td>
            <td>book</td>
            <td>title, date, URL</td>
            <td>author, publisher, extra</td>
            <td> add on Extra field: Medium "Audiobook" wordsBy: "K.Mazur"</td></tr>

    <tr>
            <td>Book / Ebook / Audio Book</td>
            <td>edited ebook (e.g., Kindle book) or audiobook without a DOI, with a nondatabase URL</td>
            <td>Pridham, K. F., Limbo, R., &amp; Schroeder, M. (Eds.). (2018). <em>Guided Participation in Pediatric Nursing Practice: Relationship-Based Teaching and Learning with Parents, Children, and Adolescents</em> (1st ed.). Springer Publishing Company. http://a.co/0IAiVgt</td>
            <td>book</td>
            <td>title, date, URL</td>
            <td>editor, edition, publisher</td>
            <td></td></tr>

    <tr>
            <td>Book Chapters and Entries in Reference Works</td>
            <td>chapter in an edited book with a DOI</td>
            <td>Balsam, K. F., Martell, C. R., Jones, K. P., &amp; Safren, S. A. (2019). Affirmative cognitive behavior therapy with sexual and gender minority people. In G. Y. Iwamasa, &amp; P. A. Hays (Eds.), <em>Culturally responsive cognitive behavior therapy: Practice and supervision</em> (2nd ed., pp. 287–314). American Psychological Association. https://doi.org/10.1037/0000119-012</td>
            <td>book section</td>
            <td>title, author, editor, book title, publisher, date</td>
            <td>edition, DOI</td>
            <td></td></tr>

    <tr>
            <td>Book Chapters and Entries in Reference Works</td>
            <td>chapter in an edited ebook (e.g., Kindle book) or audiobook without a DOI, with nondatabase URL</td>
            <td>Tafoya, N., &amp; Del Vecchio, A. (2005). Back to the future: An examination of the Native American Holocaust experience. In M. McGoldrick, J. Giordano, &amp; N. Garcia-Preto (Eds.), <em>Ethnicity and family therapy</em> (3rd ed., pp. 55–63). Guilford Press. http://a.co/36xRhBT</td>
            <td>book section</td>
            <td>title, author, editor, book title, publisher, date</td>
            <td>edition, pages, URL</td>
            <td></td></tr>

    <tr>
            <td>Book Chapters and Entries in Reference Works</td>
            <td>chapter in a volume of a multivolume work</td>
            <td>Goldin-Meadow, S. (2015). Gesture and Cognitive Development. In L. S. Liben, &amp; U. Mueller (Eds.), <em>Handbook of Child Psychology and Developmental Science</em><em>: Vol. 2. Cognitive Processes</em> (7th ed., pp. 339–380). John Wiley &amp; Sons. https://doi.org/10.1002/9781118963418.childpsy209</td>
            <td>book section</td>
            <td>title, author, editor, book title, publisher, date</td>
            <td>volume, edition, pages, DOI</td>
            <td>add the information about number and title of volume on Volume field: Number of Volume. Title of Volume</td></tr>

    <tr>
            <td>Book Chapters and Entries in Reference Works</td>
            <td>work in anthology</td>
            <td>Lewin, K. (1999). Group decision and social change. In M. Gold (Ed.), <em>The complete social scientist: A Kurt Lewin reader</em> (pp. 265–284). American Psychological Association. https://doi.org/10.1037/10319-010. (Original work published 1948)</td>
            <td>book section</td>
            <td>title, author, editor, book title, publisher, date</td>
            <td>pages, DOI,  extra</td>
            <td>add the original edition on Extra field with the form: Original Date: yyyy</td></tr>

    <tr>
            <td>Entry in a Dictionary, Thesaurus, or Encyclopedia</td>
            <td>entry in a dictionary, thesaurus, or encyclopedia, with group author</td>
            <td>American Psychological Association. (n.d.). Positive transference. In <em>APA dictionary of psychology</em>. Retrieved August 31, 2019, from https://dictionary.apa.org/positive-transference</td>
            <td>dictionary entry</td>
            <td>title, author, date, URL</td>
            <td>dictionary title, accessed</td>
            <td></td></tr>

    <tr>
            <td>Entry in a Dictionary, Thesaurus, or Encyclopedia</td>
            <td>entry in a dictionary, thesaurus, or encyclopedia, with individual author</td>
            <td>Graham, G. (2019). Behaviorism. In E. N. Zalta (Ed.), <em>The Stanford encyclopedia of philosophy</em> (Summer 2019 ed.). Stanford University. https://plato.stanford.edu/archives/sum2019/entries/behaviorism/</td>
            <td>encyclopedia article</td>
            <td>title, author, date, URL</td>
            <td>editor, encyclopedia title, edition, publisher, date</td>
            <td></td></tr>

    <tr>
            <td>Entry in a Dictionary, Thesaurus, or Encyclopedia</td>
            <td>wikipedia entry</td>
            <td>List of oldest companies. (2019, January 13). In <em>Wikipedia</em>. https://en.wikipedia.org/wiki/List_of_oldest_companies</td>
            <td>encyclopedia article</td>
            <td>title, author, date, URL</td>
            <td>encyclopedia title</td>
            <td></td></tr>

    <tr>
            <td>Conference Sessions & Presentations</td>
            <td>conference session</td>
            <td>Fistek, A., Jester, E., &amp; Sonnenberg, K. (2017, July 12-15). <em>Everybody’s got a little music in them: Using music therapy to connect, engage, and motivate</em> [Conference session]. Autism Society National Conference, Milwaukee, Wl, United States. https://asa.confex.com/asa/2017/webprogramarchives/Session9517.html</td>
            <td>presentation</td>
            <td>title, presenter, type, place, extra</td>
            <td>URL</td>
            <td>add on Type field: Conference Session or Panel Conference
add on Extra field the period with the form: issued: "2017-07-12/2017-07-15"
add on Extra field Conference's name with the form: event:"Autism Society National Conference"</td></tr>

    <tr>
            <td>Conference Sessions & Presentations</td>
            <td>paper presentation</td>
            <td>Maddox, S., Hurling, J., Stewart, E., &amp; Edwards, A. (2016, March 30-April 2). <em>If mama ain’t happy, nobody’s happy: The effect of parental depression on mood dysrégulation in children</em> [Paper presentation]. Southeastern Psychological Association 62nd Annual Meeting, New Orleans, LA, United States</td>
            <td>presentation</td>
            <td>tittle, presenter, type, place, extra</td>
            <td></td>
            <td>add on Type field: Paper presentation
add on Extra field the period with the form: issued: "2016-03-30/2016-04-02"
add on Extra field Conference's name with the form: event: "Southeastern Psychological Association 62nd Annual Meeting"</td></tr>

    <tr>
            <td>Conference Sessions & Presentations</td>
            <td>poster presentation</td>
            <td>Pearson, J. (2018, September 27-30). <em>Fat talk and its effects on state-based body image in women</em> [Poster presentation]. Australian Psychological Society Congress, Sydney, NSW, Australia. http://bit.ly/2XGSThP</td>
            <td>presentation</td>
            <td>title, presenter, type, place, extra</td>
            <td>URL</td>
            <td>add on Type field: Poster presentation
add on Extra field the period with the form: issued: "2018-09-27/2018-09-30"
add on Extra field Conference's name with the form: event: "Australian Psychological Society Congress"</td></tr>

    <tr>
            <td>Symposium Contribution</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>Atti di convegno</td>
            <td>/</td>
            <td></td>
            <td>book/booksection/article</td>
            <td>/</td>
            <td>/</td>
            <td>title should include [Conference proceedings], after title</td></tr>

    <tr>
            <td>Cataloghi di mostre</td>
            <td>/</td>
            <td></td>
            <td>book/booksection/article</td>
            <td>/</td>
            <td>/</td>
            <td>title should include [Exhibition catalogue], after title</td></tr>

    <tr>
            <td>Thesis</td>
            <td>unpublished dissertation or thesis</td>
            <td>Harris, L. (2014). <em>Instructional leadership perceptions and practices of elementary school leaders</em> [Unpublished doctoral dissertation]. University of Virginia</td>
            <td>thesis</td>
            <td>title, author, type, university, date</td>
            <td></td>
            <td>add on Type field: Unpublished doctoral dissertation</td></tr>

    <tr>
            <td>Thesis</td>
            <td>dissertation or thesis from a database</td>
            <td>Hollander, M. M. (2017). <em>Resistance to authority: Methodological innovations and new lessons from the Milgram experiment</em> (Publication No. 10289373) [Doctoral dissertation, University of Wisconsin-Madison]. ProQuest Dissertations and Theses Global</td>
            <td>thesis</td>
            <td>title, author, type, university, date</td>
            <td>archive, loc. in archive, extra</td>
            <td>duplicate on Extra field the same information on Archive field and on Location in Archive field, with the form:
collection-title: "ProQuest Dissertations and Theses Global"
collection-number: "Publication No. 10289373"</td></tr>

    <tr>
            <td>Thesis</td>
            <td>dissertation or thesis published online (not in a database)</td>
            <td>Hutcheson, V. H. (2012). <em>Dealing with dual differences: Social coping strategies of gifted and lesbian, gay; bisexual, transgender, and queer adolescents</em> [Master’s thesis, The College of William &amp; Mary]. William &amp; Mary Digital Archive. https://digitalarchive.wm.edu/bitstream/handle/10288/16594/HutchesonVirginia2012.pdf</td>
            <td>thesis</td>
            <td>title, author, type, university, date</td>
            <td>URL, archive, extra</td>
            <td>duplicate on Extra field the same information on Archive field, with the form:
collection-title: "William & Mary Digital Archive"</td></tr>

    <tr>
            <td>Personal Comunication</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>Manuscript + Informally Published Work</td>
            <td>unpublished manuscript</td>
            <td>Yoo, J., Miyamoto, Y., Rigotti, A., &amp; Ryff, C. (2016). <em>Linking positive affect to blood lipids: A cultural perspective</em> [Unpublished manuscript]. Department of Psychology, University of Wisconsin-Madison</td>
            <td>manuscript</td>
            <td>title, author, type, place, date</td>
            <td></td>
            <td>add on Type field: Unpublished manuscript</td></tr>

    <tr>
            <td>Manuscript + Informally Published Work</td>
            <td>manuscript in preparation</td>
            <td>O&#39;Shea, M. (2018). <em>Understanding proactive behavior in the workplace as a function of gender</em> [Manuscript in preparation]. Department of Management, University of Kansas</td>
            <td>manuscript</td>
            <td>title, author, type, place, date</td>
            <td></td>
            <td>add on Type field: Manuscript in preparation</td></tr>

    <tr>
            <td>Manuscript + Informally Published Work</td>
            <td>manuscript submitted for publication</td>
            <td>Lippincott, T., &amp; Poindexter, E. K. (2019). <em>Emotion recognition as a function of facial cues: Implications for practice</em> [Manuscript submitted for publication]. Department of Psychology, University of Washington</td>
            <td>manuscript</td>
            <td>title, author, type, place, date</td>
            <td></td>
            <td>add on Type field: Manuscript submitted for publication</td></tr>

    <tr>
            <td>Manuscript + Informally Published Work</td>
            <td>informally published work, from a preprint archive or an institutional repository</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>Manuscript + Informally Published Work</td>
            <td>informally published work, from a preprint archive or an institutional repository</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>Reports</td>
            <td>report by a government agency or other organization</td>
            <td>Australian Government Productivity Commission &amp; New Zealand Productivity Commission. (2012). <em>Strengthening trans-Tasman economic relations</em>. https://www.pc.gov.au/inquiries/completed/australia-new-zealand/report/trans-tasman.pdf</td>
            <td>report</td>
            <td>title, author, date</td>
            <td>URL</td>
            <td>For reports of organizations and institutions, use the Report tab.
To indicate the document number, use the Report Number field. If the document number is preceded by the series / collection name, also enter this in the Report number field, before the document number.</td></tr>

    <tr>
            <td>Reports</td>
            <td>report by a government agency or other organization</td>
            <td>Canada Council for the Arts. (2013). <em>What we heard: Summary of key findings: 2013 Canada Council’s Inter-Arts Office consultation</em>. http://publications.gc.ca/collections/collection_2017/canadacouncil/K23-65-2013-eng.pdf</td>
            <td>report</td>
            <td>title, author, date</td>
            <td>URL</td>
            <td>For reports of organizations and institutions, use the Report tab.
To indicate the document number, use the Report Number field. If the document number is preceded by the series / collection name, also enter this in the Report number field, before the document number.</td></tr>

    <tr>
            <td>Reports</td>
            <td>report by a government agency or other organization</td>
            <td>National Cancer Institute. (2018). <em>Facing forward: Life after cancer treatment</em> (NIH Publication No. 18-2424). U.S. Department of Health and Human Services, National Institutes of Health. https://www.cancer.gov/publications/patient-education/life- after-treatment.pdf</td>
            <td>report</td>
            <td>title, author, date, report number, institution</td>
            <td>URL</td>
            <td>For reports of organizations and institutions, use the Report tab.
To indicate the document number, use the Report Number field. If the document number is preceded by the series / collection name, also enter this in the Report number field, before the document number.</td></tr>

    <tr>
            <td>Reports</td>
            <td>report by individual authors at a government agency or other organization</td>
            <td>Fried, D., &amp; Polyakova, A. (2018). <em>Democratic defense against disinformation</em>. Atlantic Council. https://www.atlanticcouncil.org/images/publications/Democratic_Defense_Against_Disinformation_FINAL.pdf</td>
            <td>report</td>
            <td>title, author, date, institution</td>
            <td>URL</td>
            <td>For reports of organizations and institutions, use the Report tab.
To indicate the document number, use the Report Number field. If the document number is preceded by the series / collection name, also enter this in the Report number field, before the document number.</td></tr>

    <tr>
            <td>Reports</td>
            <td>report by individual authors at a government agency, published as part of a series</td>
            <td>Blackwell, D. L., Lucas, J. W., &amp; Clarke, T. C. (2014). <em>Summary health statistics for U.S. adults: National Health Interview Survey, 2012</em> (Vital and Health Statistics Series 10, Issue 260). Centers for Disease Control and Prevention. https://www.cdc.gov/nchs/data/series/sr_10/sr10_260.pdf</td>
            <td>report</td>
            <td>title, author, date, report number, institution</td>
            <td>URL</td>
            <td>For reports of organizations and institutions, use the Report tab.
To indicate the document number, use the Report Number field. If the document number is preceded by the series / collection name, also enter this in the Report number field, before the document number.</td></tr>

    <tr>
            <td>Reports</td>
            <td>report by a task force, working group, or other group</td>
            <td>British Cardiovascular Society Working Group. (2016). <em>British Cardiovascular Society Working Group report: Out-of-hours cardiovascular care: Management of cardiac emergencies and hospital in-patients</em>. British Cardiovascular Society. http://www.bcs.com/documents/BCSOOHWP_Final_Report_05092016.pdf</td>
            <td>report</td>
            <td>title, author, date, institution</td>
            <td>URL</td>
            <td>To indicate the document number, use the Report Number field. If the document number is preceded by the series / collection name, also enter this in the Report number field, before the document number.</td></tr>

    <tr>
            <td>Reports</td>
            <td>annual report</td>
            <td>U.S. Securities and Exchange Commission. (2017). <em>Agency financial report: Fiscal year 2017</em>. https://www.sec.gov/files/sec- 2017-agency-financial-report.pdf</td>
            <td>report</td>
            <td>title, author, date</td>
            <td>URL</td>
            <td>To indicate the document number, use the Report Number field. If the document number is preceded by the series / collection name, also enter this in the Report number field, before the document number.</td></tr>

    <tr>
            <td>Reports</td>
            <td>Press Release</td>
            <td>U.S. Food and Drug Administration. (2019, February 14). <em>FDA authorizes first interoperable insulin pump intended to allow patients to customize treatment through their individual diabetes management devices</em> [Press release]. https://www.fda.gov/NewsEvents/Newsroom/PressAnnouncements/ucm631412.htm</td>
            <td>document</td>
            <td>title, author, date</td>
            <td>URL</td>
            <td></td></tr>

    <tr>
            <td>Blog</td>
            <td>blog post</td>
            <td></td>
            <td>blog post</td>
            <td>title, author, date</td>
            <td>URL</td>
            <td></td></tr>

    <tr>
            <td>Blog</td>
            <td>comment on an online periodical article or post</td>
            <td>KS in NJ. (2019, January 15). From this article, it sounds like men are figuring something out that women have known forever. I know of many [Comment on the article <em aid:cstyle='corsivo'>How workout buddies can help stave off loneliness</em>]. <em>The Washington Post</em>. https://wapo.st/2HDToGJ</td>
            <td>newspaper article</td>
            <td>title, author, date</td>
            <td>URL</td>
            <td></td></tr>

    <tr>
            <td>Social (facebook, twitter, instagram)</td>
            <td>tweet</td>
            <td>APA Education [@APAEducation]. (2018, June 29). <em>College students are forming mental-health clubs — and they’re making a difference @washingtonpost</em> [Thumbnail with link attached] [Tweet]. Twitter. https://twitter.com/apaeducation/status/1012810490530140161</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Twitt"</td></tr>

    <tr>
            <td>Social (facebook, twitter, instagram)</td>
            <td>tweet</td>
            <td>Badlands National Park [@BadlandsNPS]. (2018, February 26). <em>Biologists have identified more than 400 different plant species growing in @BadlandsNPS #DYK #biodiversity</em> [Tweet]. Twitter. https://twitter.com/badlandsnps/status/968196500412133379</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Twitt"</td></tr>

    <tr>
            <td>Social (facebook, twitter, instagram)</td>
            <td>tweet</td>
            <td>White, B. [@BettyMWhite]. (2018, June 21). <em>I treasure every minute we spent together #koko</em> [Image attached] [Tweet]. Twitter. https://twitter.com/BettyMWhite/status/1009951892846227456</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Twitt"</td></tr>

    <tr>
            <td>Social (facebook, twitter, instagram)</td>
            <td>twitter profile</td>
            <td>APA Style [@APA_Style]. (n.d.). <em>Tweets</em> [Twitter profile]. Twitter. Retrieved November 1, 2019, from https://twitter.com/apa_style</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Twitter profile"</td></tr>

    <tr>
            <td>Social (facebook, twitter, instagram)</td>
            <td>facebook post</td>
            <td>Gaiman, N. (2018, March 22). <em>100,000+ Rohingya refugees could be at serious risk during Bangladesh’s monsoon season. My fellow UNHCR Goodwill Ambassador Cate Blanchett is</em> [Image attached] [Status update]. Facebook. https://www.facebook.com/neilgaiman/posts/10155317238526016</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td></td></tr>

    <tr>
            <td>Social (facebook, twitter, instagram)</td>
            <td>facebook post</td>
            <td>National Institute of Mental Health. (2018, November 28). <em>Suicide affects all ages, genders, races, and ethnicities. Check out these 5 Action Steps for Helping Someone in Emotional Pain</em> [Infographic]. Facebook. http://bit.ly/321Qstq</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Infographic"</td></tr>

    <tr>
            <td>Social (facebook, twitter, instagram)</td>
            <td>facebook page</td>
            <td>Smithsonian’s National Zoo and Conservation Biology Institute. (n.d.). <em>Home</em> [Facebook page]. Facebook. Retrieved July 22, 2019, from https://www.facebook.com/nationalzoo/</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Facebook page"</td></tr>

    <tr>
            <td>Social (facebook, twitter, instagram)</td>
            <td>instagram photo or video</td>
            <td>Zeitz MOCAA [@zeitzmocaa]. (2018, November 26). <em>Grade 6 learners from Parkfields Primary School in Hanover Park visited the museum for a tour and workshop hosted by our Centre for Art…</em> [Photographs]. Instagram. https://www.instagram.com/p/BqpHpjFBs3b/</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Photographs"</td></tr>

    <tr>
            <td>Social (facebook, twitter, instagram)</td>
            <td>instagram highlight</td>
            <td>The New York Public Library [@nypl]. (n.d.). <em>The Raven</em> [Highlight]. Instagram. Retrieved April 16, 2019, from https://bitly.com/2FV8bu3</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Highlight"</td></tr>

    <tr>
            <td>Forum</td>
            <td>Online forum post</td>
            <td>National Aeronautics and Space Administration [nasa]. (2018, September 12). <em>I’m NASA astronaut Scott Tingle. Ask me anything about adjusting to being back on Earth after my first spaceflight!</em> [Online forum post] Reddit. https://www.reddit.com/r/IAmA/comments/9fagqy/im_nasa_astronaut_scott_tingle_ask_me_anything/</td>
            <td>forum post</td>
            <td>title, author, forum/listserv title, date</td>
            <td>URL</td>
            <td></td></tr>

    <tr>
            <td>Webpages</td>
            <td>Webpage on a news website</td>
            <td>Avramova, N. (2019, January 3). <em>The secret to a long, happy, healthy life? Think age-positive</em>. CNN. Retrieved July 9, 2020, from https://edition.cnn.com/2019/01/03/health/respect-toward-elderly-leads-to-long-life-intl/index.html</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>institution should be given as the Site Name</td></tr>

    <tr>
            <td>Webpages</td>
            <td>Webpage on a news website</td>
            <td>Bologna, C. (2018, June 27). <em>What Happens to Your Mind and Body When You Feel Homesick?</em> HuffPost. https://www.huffpost.com/entry/what-happens-mind-body-homesick_n_5b201ebde4b09d7a3d77eee1</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>institution should be given as the Site Name</td></tr>

    <tr>
            <td>Webpages</td>
            <td>Webpage on a website with a group author</td>
            <td>Centers for Disease Control and Prevention. (2018, January 23). <em>People at high risk of developing flu-related complications</em>. https://www.cdc.gov/flu/highrisk/index.htm</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>institution should be given as the Site Name</td></tr>

    <tr>
            <td>Webpages</td>
            <td>Webpage on a website with an individual author</td>
            <td>Martin Lillie, C. M. (2016, December 29). <em>Be kind to yourself: How self-compassion can improve your resiliency</em>. Mayo Clinic. http://www.ethicsguidebook.ac.uk/EthicsPrinciples</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>institution should be given as the Site Name</td></tr>

    <tr>
            <td>Webpages</td>
            <td>Webpage on a website with no date</td>
            <td>Boddy, J., Neumann, T., Jennings, S., Morrow, V., Alderson, R., Rees, R., &amp; Gibson, W. (n.d.). <em>Ethics principles</em>. The Research Ethics Guidebook: A Resource for Social Scientists. http://www.ethicsguidebook.ac.uk/EthicsPrinciples</td>
            <td>web page</td>
            <td>title, author, website title</td>
            <td>URL</td>
            <td>institution should be given as the Site Name</td></tr>

    <tr>
            <td>Webpages</td>
            <td>Webpage on a website with no date</td>
            <td>National Nurses United. (n.d.). <em>What Employers Should Do to Protect Nurses from Zika</em>. https://www.nationalnursesunited.org/what-employers-should-do-to-protect-rns-from-zika</td>
            <td>web page</td>
            <td>title, author, website title</td>
            <td>URL</td>
            <td>institution should be given as the Site Name</td></tr>

    <tr>
            <td>Webpages</td>
            <td>Webpage on a website with a retrieval date</td>
            <td>U.S. Census Bureau. (n.d.). <em>U.S. and world population clock</em>. U.S. Department of Commerce. Retrieved July 3, 2019, from https://www.census.gov/popclock/</td>
            <td>web page</td>
            <td>title, author, website title, date</td>
            <td>URL</td>
            <td>institution should be given as the Site Name</td></tr>

    <tr>
            <td>Ted talk, Webinar recorded, Youtube video or other streaming video</td>
            <td>Ted Talk</td>
            <td>Giertz, S. (2018, April). <em>Why you should make useless things</em> [Video], TED Conferences. https://www.ted.com/talks/simone_giertz_why_you_should_make_useless_things</td>
            <td>Video recording</td>
            <td>title, director, date</td>
            <td>URL, archive</td>
            <td>use the field type Extra: Medium "Video" and the field type: Archive "host site name"</td></tr>

    <tr>
            <td>Ted talk, Webinar recorded, Youtube video or other streaming video</td>
            <td>Ted Talk</td>
            <td>TED. (2012, March 16). <em>Brené Brown: Listening to shame</em> [Video], YouTube. https://www.youtube.com/watch?v=psN1DORYYV0</td>
            <td>Video recording</td>
            <td>title, director, date</td>
            <td>URL, archive</td>
            <td>use the field type Extra: Medium "Video" and the field type: Archive "host site name"</td></tr>

    <tr>
            <td>Ted talk, Webinar recorded, Youtube video or other streaming video</td>
            <td>Webinar, recorded</td>
            <td>Goldberg, J. F. (2018). <em>Evaluating Adverse Drug Effects</em> [Webinar], American Psychiatric Association. http://education.psychiatry.org/Users/ProductDetails.aspx?ActivityID=6172</td>
            <td>Video recording</td>
            <td>title, director, date</td>
            <td>URL, archive</td>
            <td>use the field type Extra: Medium "Webinar" and the field type: Archive "host site name"</td></tr>

    <tr>
            <td>Ted talk, Webinar recorded, Youtube video or other streaming video</td>
            <td>YouTube video or other streaming video (es. Vimeo)</td>
            <td>Cutts, S. (2017, November 24). <em>Happiness</em> [Video], Vimeo. https://vimeo.com/244405542</td>
            <td>Video recording</td>
            <td>title, director, date</td>
            <td>URL, archive</td>
            <td>use the field type Extra: Medium "Video" and the field type: Archive "host site name"</td></tr>

    <tr>
            <td>Ted talk, Webinar recorded, Youtube video or other streaming video</td>
            <td>YouTube video or other streaming video (es. Vimeo)</td>
            <td>Fogarty, M. [Grammar Girl]. (2016, September 30). <em>How to diagram a sentence (absolute basics)</em> [Video], YouTube. https://youtu.be/deiEY5Yq1qI</td>
            <td>Video recording</td>
            <td>title, director, date</td>
            <td>URL, archive</td>
            <td>manually add Grammar Girl in the "Director" field</td></tr>

    <tr>
            <td>Music</td>
            <td>Music album</td>
            <td>Bach, J. S. (2010). <em aid:cstyle='corsivo'>The Brandenburg concertos: Concertos BWV 1043 &amp; 1060</em> [Album recorded by Academy of St Martin in the Fields]. Decca. (Original work published 1721)</td>
            <td>Audio recording</td>
            <td>composer, title, date, volume</td>
            <td>place, label, URL</td>
            <td>to provide details about the album after the title use the field type Extra: Medium "details"; also for the original data field type Extra: Original Date "data"</td></tr>

    <tr>
            <td>Music</td>
            <td>Single song/track</td>
            <td>Beethoven, L. van. (2012). Symphony No. 3 in E-flat major [Song recorded by Staatskapelle Dresden]. On <em>Beethoven: Complete symphonies. Brilliant Classics</em>. (Original work published 1804)</td>
            <td>Audio recording</td>
            <td>composer, title, date, volume</td>
            <td>place, label, URL</td>
            <td></td></tr>

    <tr>
            <td>Music</td>
            <td>Single song/track</td>
            <td>Beyoncé. (2016). Formation [Song]. On <em>Lemonade</em>. Parkwood; Columbia.</td>
            <td>Audio recording</td>
            <td>performer, title, date, volume</td>
            <td>place, label, URL</td>
            <td></td></tr>

    <tr>
            <td>Podcast</td>
            <td>Podcast</td>
            <td>Vedantam, S. (Host). (2015). <em aid:cstyle='corsivo'>Hidden brain</em> [Audio podcast]. NPR. https://www.npr.org/series/423302056/hidden-brain</td>
            <td>Audio recording</td>
            <td>title, format, series title, date, archive</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Audio podcast episode"</td></tr>

    <tr>
            <td>Podcast</td>
            <td>Podcast episode</td>
            <td>Glass, I. (Host). (2011, August 12). Amusement park (No. 443) [Audio podcast episode]. In <em>This American life</em>. WBEZ Chicago. https://www.thisamericanlife.org/radio-archives/episode/443/amusement-park</td>
            <td>Audio recording</td>
            <td>title, format, series title, date, archive</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Audio podcast episode"</td></tr>

    <tr>
            <td>Radio, recording</td>
            <td>Radio interview recording in a digital archive</td>
            <td>de Beauvoir, S. (1960, May 4). <em aid:cstyle='corsivo'>Simone de Beauvoir discusses the art of writing</em> [Interview]. Studs Terkel Radio Archive; The Chicago History Museum. https://studsterkel.wfmt.com/programs/simone-de-beauvoir-discusses-art-writing</td>
            <td>Audio recording</td>
            <td>title, performer, date, archive</td>
            <td>URL</td>
            <td>use the Audio recording tab and then field type Extra: Medium "Interview"; Extra: Collection-title "Studs Terkel Radio Archive"</td></tr>

    <tr>
            <td>Radio, recording</td>
            <td>Speech audio recording</td>
            <td>King, M. L. jr. (1963, August 28). <em aid:cstyle='corsivo'>I have a dream</em> [Speech audio recording]. American Rhetoric. https://www.americanrhetoric.com/speeches/mlkihaveadream.htm</td>
            <td>Audio recording</td>
            <td>title, performer, date, archive</td>
            <td>URL</td>
            <td>use the Audio recording tab and then field type Extra: Medium "Interview"; Extra: Collection-title "American Rhetoric"</td></tr>

    <tr>
            <td>Film, video, tv series</td>
            <td>Film or video</td>
            <td>Forman, M. (Director). (1975). <em>One flew over the cuckoo’s nest</em> [Film]. United Artists</td>
            <td>Film</td>
            <td>title, director, date</td>
            <td>URL</td>
            <td>for film and video use the Film tab and then field type Extra: Medium "Film"</td></tr>

    <tr>
            <td>Film, video, tv series</td>
            <td>Film or video</td>
            <td>Fosha, D. (Guest Expert), &amp; Levenson, H. (Host). (2017). <em>Accelerated experiential dynamic psychotherapy (AEDP) supervision</em> [Film; educational DVD]. American Psychological Association. https://www.apa.org/pubs/videos/4310958.aspx</td>
            <td>Film</td>
            <td>title, director, date</td>
            <td>URL</td>
            <td>for film and video use the Film tab and then field type Extra: Medium "Film, educational DVD"</td></tr>

    <tr>
            <td>Film, video, tv series</td>
            <td>Film or video</td>
            <td>Jackson, P. (Director). (2001). <em>The lord of the rings: The fellowship of the ring</em> [Film; four-disc special extended ed. on DVD]. WingNut Films; The Saul Zaentz Company</td>
            <td>Film</td>
            <td>title, director, date</td>
            <td>URL</td>
            <td>for film and video use the Film tab and then field type Extra: Medium "Film"</td></tr>

    <tr>
            <td>Film, video, tv series</td>
            <td>Film or video in another language</td>
            <td>Malle, L. (Director). (1987). <em>Au revoir les enfants </em>[Goodbye children] [Film]. Nouvelles Éditions de Films</td>
            <td>Film</td>
            <td>title, director, date</td>
            <td>URL</td>
            <td>for film and video use the Film tab and then field type Extra: Medium "Film"</td></tr>

    <tr>
            <td>Film, video, tv series</td>
            <td>TV series</td>
            <td>Simon, D., Colesberry, R. F., &amp; Kostroff Noble, N. (Executive Producers). (2002-2008). <em>The wire</em> [TV series]. Blown Deadline Productions; HBO</td>
            <td>TV series</td>
            <td>title, producer, network, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "TV series"</td></tr>

    <tr>
            <td>Film, video, tv series</td>
            <td>TV series episode or webisode</td>
            <td>Barris, K. (Writer &amp; Director). (2017, January 11). Lemons (Season 3, Episode 12) [TV series episode]. In K. Barris, J. Groff, A. Anderson, E. B. Dobbins, L. Fishburne, &amp; H. Sugland (Executive Producers), <em>Black-ish</em>. Wilmore Films; Artists First; Cinema Gypsy Productions; ABC Studios</td>
            <td>TV series</td>
            <td>title, producer, network, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "TV series"</td></tr>

    <tr>
            <td>artwork, graphics, maps, photographs</td>
            <td>Artwork in museum or on a museum website</td>
            <td>Delacroix, E. (1826-1827). <em>Faust attempts to seduce Marguerite</em> [Lithograph]. The Louvre, Paris, France.</td>
            <td>graphic</td>
            <td>artist, archive, date, title</td>
            <td>URL</td>
            <td>For artistic and graphic works use the Graphics tab, to specify the medium or detail after the title use the field type Extra: Medium "Lithograph"</td></tr>

    <tr>
            <td>artwork, graphics, maps, photographs</td>
            <td>Artwork in museum or on a museum website</td>
            <td>Wood, G. (1930). <em>American gothic</em> [Painting]. Art Institute of Chicago, Chicago, IL, United States. https://www.artic.edu/aic/collections/artwork/6565</td>
            <td>graphic</td>
            <td>artist, archive, date, title</td>
            <td>URL</td>
            <td>For artistic and graphic works use the Graphics tab, to specify the medium or detail after the title use the field type Extra: Medium "Painting"</td></tr>

    <tr>
            <td>artwork, graphics, maps, photographs</td>
            <td>Clip art or stock image</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>artwork, graphics, maps, photographs</td>
            <td>Infographic</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>artwork, graphics, maps, photographs</td>
            <td>Map</td>
            <td>Cable, D. (2013). <em>The racial dot map</em> [Map]. University of Virginia, Weldon Cooper Center for Public Service. https://demographics.coopercenter.org/Racial-Dot-Map</td>
            <td>map</td>
            <td>title, cartographer, publisher, date</td>
            <td>URL</td>
            <td>For maps use the Map tab, to specify the medium or detail after the title use the field type Extra: Medium "Map"</td></tr>

    <tr>
            <td>artwork, graphics, maps, photographs</td>
            <td>Map</td>
            <td>Google. (n.d.). [Google Maps directions for driving from La Paz, Bolivia, to Lima, Peru] [Map]. Retrieved February 16, 2020, from https://goo.gl/YYE3GR</td>
            <td>map</td>
            <td>title, cartographer, publisher, date</td>
            <td>URL</td>
            <td>For maps use the Map tab, to specify the medium or detail after the title use the field  type Extra: Medium "Map"</td></tr>

    <tr>
            <td>artwork, graphics, maps, photographs</td>
            <td>photographs</td>
            <td>McCurry, S. (1985). <em>Afghan girl</em> [Photograph]. National Geographic. https://www.nationalgeographic.com/magazine/national-geographic-magazine-50- years-of-covers/#/ngm-1985-jun-714.jpg</td>
            <td>graphic</td>
            <td>artist, archive, date, title</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Photograph"</td></tr>

    <tr>
            <td>artwork, graphics, maps, photographs</td>
            <td>photographs</td>
            <td>Rinaldi, J. (2016). [Photograph series of a boy who finds his footing after abuse by those he trusted]. The Pulitzer Prizes. https://www.pulitzer.org/winners/jessica-rinaldi</td>
            <td>graphic</td>
            <td>artist, archive, date, title</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Photograph"</td></tr>

    <tr>
            <td>legal</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>patents</td>
            <td>patents</td>
            <td>Hiremath, S. C., Kumar, S., Lu, F., &amp; Salehi, A. (2016). <em>Using metaphors to present concepts across different intellectual domains</em> (U.S. Patent No. 9,367,592). U.S. Patent and Trademark Office. http://patft.uspto.gov/netacgi/nph-Parser?patentnumber=9367592</td>
            <td>patent</td>
            <td>inventor, patent number, title, date, assignee</td>
            <td>URL, archive</td>
            <td>Report the name of the issuing authority only in the "Assignee" field</td></tr>

    <tr>
            <td>patents</td>
            <td>patents</td>
            <td>Kasabov, N. K. (2010). <em>Data analysis and predictive systems and related methodologies</em> (N.Z. Patent 572036). New Zealand Intellectual Property Office. https://app.iponz.govt.nz/app/Extra/IP/Mutual/Browse.aspx?sid=637094081061108163</td>
            <td>patent</td>
            <td>inventor, patent number, title, date, assignee</td>
            <td>URL, archive</td>
            <td>Report the name of the issuing authority only in the "Assignee" field</td></tr>

    <tr>
            <td>data sets + row data</td>
            <td>dataset</td>
            <td>D&#39;Souza, A., &amp; Wiseheart, M. (2018). <em>Cognitive Effects of Music and Dance Training in Children</em> (ICPSR 37080; Version V1) [Data set]. ICPSR. https://doi.org/10.3886/ICPSR37080.V1</td>
            <td>document</td>
            <td>title, author, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Data set"</td></tr>

    <tr>
            <td>data sets + row data</td>
            <td>dataset</td>
            <td>National Center For Education Statistics. (2016). <em>Fast Response Survey System (FRSS): Teachers&#39; Use of Educational Technology in U.S. Public Schools, 2009</em> (ICPSR 35531; Version V3) [Data set and code book]. National Archive of Data on Arts and Culture. https://doi.org/10.3886/ICPSR35531.V3</td>
            <td>document</td>
            <td>title, author, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Data set"</td></tr>

    <tr>
            <td>data sets + row data</td>
            <td>dataset</td>
            <td>Pew Research Center. (2018). <em>American trends panel Wave 26</em> [Data Set]. https://www.pewsocialtrends.org/dataset/american-trends-panel-wave-26/</td>
            <td>document</td>
            <td>title, author, date</td>
            <td>URL</td>
            <td>use the field type Extra: Medium "Data set"</td></tr>

    <tr>
            <td>Unpublished raw data</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td></tr>

    <tr>
            <td>software + app</td>
            <td>software</td>
            <td>Borenstein, M., Hedges, L., Higgins, J., &amp; Rothstein, H. (2014). <em>Comprehensive meta-analysis</em> (Version 3.3.070) [Computer software], Biostat. https://www.meta-analysis.com/</td>
            <td>pc program</td>
            <td>title, programmer, version, company, date</td>
            <td>URL</td>
            <td></td></tr>

    <tr>
            <td>software + app</td>
            <td>mobile app</td>
            <td>Epocrates. (2019). <em>Epocrates medical references</em> (Version 18.12) [Mobile app]. App Store. https://itunes.apple.com/us/app/epocrates/id281935788?mt=8</td>
            <td>pc program</td>
            <td>title, programmer, version, company, date</td>
            <td>URL</td>
            <td>To report the repository / archive where the software is distributed in the following formula in the Extra field:
collection-title: "App Store"</td></tr>

</table>
<!-- END AUTOMATIC REFERENCES TABLE -->

## 4.4 Esportazione file .bib per la consegna

Una volta che gli autori hanno completato la compilazione della  collezione di reference per il proprio scritto, è sufficiente cliccare con il tasto destro sulla cartella della collezione nel pannello delle collezioni (barra di sinistra), e scegliere l’opzione “Esporta collezione” / “Export collection”.

![Figura 2. Interfaccia di zotero con istruzione di click destro su collezione e pop-up menù](_img/fig.2_zotero_export_collection.png "Fig.2. Esportazione collezione Zotero")

Quando compare la finestra per la selezione del formato di esportazione, scegliere il formato “BibLaTeX”.


![Figura 3. Popup di zotero con scelta del formato di esportazione](_img/fig.3_zotero_export_biblatex.png "Fig.3. Scelta formato di esportazione in BibLaTeX")

Verrà chiesto dove salvare il file formato .bib generato e questo poi verrà esportato. Tale file .bib deve essere consegnato alla redazione di Bembo OE congiuntamente alla cartella compressa .zip contente i file markdown con gli scritti dell’autore.

I reference inviati verranno sempre inclusi negli elaborati con le informazioni bibliografiche formattate in lingua inglese, indipendentemente dalla lingua dello scritto.