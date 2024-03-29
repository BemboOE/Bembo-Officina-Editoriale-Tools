# 2. Istruzioni per software di scrittura per Bembo Officina Editoriale

La consegna dei testi e della bibliografia dovrà rispettare i formati richiesti da Bembo Officine Editoriale, come di seguito indicato:

1. consegnare i testi in un file Markdown (.md), componibile attraverso software gratuiti e open source come [MacDown](https://macdown.uranusjr.com/) (per Mac OS) o [Ghostwriter](https://wereturtle.github.io/ghostwriter/) (Windows e multipiattaforma). e utilizzando  il [template Markdown](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/raw/master/author-guides/02%20IstruzionI%20per%20software/TEMPLATE_BEMBO_OE.zip)fornito dalla casa editrice.
2. consegnare le bibliografie in un file BibLaTeX (.bib), componibile attraverso software open source di reference management come [Zotero](https://www.zotero.org/) (multipiattaforma).

## 2.1 Software di scrittura Markdown
Bembo OE richiede che gli autori consegnino i testi da impaginare in formato **Markdown** (con estensione .md). Il sistema Bembo per l’impaginazione automatica dei testi si serve infatti dei codici Markdown per poter funzionare.
Per brevità **le seguenti linee guida riguardano il software MacDown**, ma Ghostwriter e qualsiasi altro software di scrittura Markdown utilizzano una procedura analoga. 
 
Markdown è un markup language, ossia un sistema di taggatura dei testi che permette, attraverso l’uso di codici, di formattare testi in maniera rapida e semplice. Il numero di tag disponibili per eseguire il Markdown è minimo e facile da apprendere. A questo indirizzo si trovano i codici di taggatura: <https://www.markdownguide.org/basic-syntax/>

Per comporre i testi, gli autori devono procurarsi:

1. Il software di composizione [MacDown](https://macdown.uranusjr.com/) (per Mac OS) o [Ghostwriter](https://wereturtle.github.io/ghostwriter/) (Windows e multipiattaforma). In alternativa, per problemi di compatibilità con MacDown o Ghostwriter, è disponibile l'editor online [stackedit](https://stackedit.io/)
2. Il [template Markdown](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/raw/master/author-guides/02%20IstruzionI%20per%20software/TEMPLATE_BEMBO_OE.zip) fornito da Bembo OE

---
### 2.1.1. Download e setup del software di scrittura MacDown

Scaricare il software MacDown (per Mac OS) all’indirizzo <https://macdown.uranusjr.com>, e installarlo sul proprio computer (Fig.1)

![Figura 1. Pagina di download di MacDown](_img/fig1_macdown_download.png "Fig.1. Pagina di download di MacDown")

---
### 2.1.2. Interfaccia dell’editor

Una volta installato MacDown, il software è pronto all’uso.
L’interfaccia del software è divisa in due sezioni (Fig.2):

* **Sezione sinistra**: **word editor**, spazio nel quale gli autori scrivono i testi inserendo i codici markdown per taggare le varie parti del testo
* **Sezione destra**: **anteprima**, spazio nel quale viene mostrato il risultato della taggatura fatta dall’utente nella sezione editor, a sinistra.

![Figura 2. Interfaccia di Macdown divisa](_img/fig2_macdown_interface.png "Fig.2. Interfaccia di Macdown divisa tra editor e anteprima")

---
### 2.1.3. Utilizzo del template fornito dalla casa editrice

Il template di Bembo OE per la scrittura dei testi in Markdown, disponibile per gli autori al [seguente indirizzo](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/raw/master/author-guides/02%20IstruzionI%20per%20software/TEMPLATE_BEMBO_OE.zip).

Una volta scaricato il file .zip e aperto sul proprio computer, è possibile aprire con il software MacDown i file .md contenuti, già impostati con i codici Markdown corretti.

**Facendo attenzione a NON modificare MAI la posizione dei file**, l’autore procede inserendo i propri testi  all’interno dei file .md già predisposti. È tuttavia sempre possibile aggiungere nuovi file .md per accomodare i propri capitoli, ma vanno posizionati sempre insieme agli altri già predisposti. Le immagini vanno inserite nella cartella “images”.

Nel template sono presenti i seguenti file:

* 🗂 TEMPLATE BEMBO OE/
    * 📁 bibliography/
        * 📖 bibliography.bib
    * 📁chapters/
        * 📄 01.md
        * 📄 02.md
        * 📄 03.md
        * 📄 04.md
        * 📄 05.md
        * 📄 06.md
        * 📄 07.md
   * 📄 colophon.md
   * 📁 images/
       * 	🖼 img_1.jpg
       *  🖼 img_2.jpg
       *  🖼 tab_1.jpg
   * 📁 license/
       *  📝 bembo_licenza.docx
   *  📄 readme.md
  

---

Nella **cartella "bibliography"** va inserito il proprio file **bibliography.bib**, esportato come indicato alla sezione [4.4 Esportazione file .bib per la consegna](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/04%20Preparazione%20bibliografia#44-esportazione-file-bib-per-la-consegna) [create an anchor](#anchors-in-markdown).

Il file bibliography.bib presente nel template è un segnaposto.

---

Nella **cartella chapters** vanno inseriti tutti i capitoli di cui è composto l'elaborato dell'autore, sia che esso sia un articolo, contributo ad una raccolta di saggi (collettanea) o un libro. I capitoli sono file markdown separati.

Se l'elaborato è un libro, il primo capitolo "01.md" è necessariamente l'introduzione al libro.

Se l'elaborato è contributo ad una raccolta di saggi (collettanea) la cartella chapters conterrà un solo file denominato "01.md".

È possibile aggiungere ulteriori capitoli semplicemente creando un nuovo file .md rinominato come “*n*.md”, seguendo la numerazione progressiva, e utilizzando la stessa struttura già fornita dal template.

La successione dei file (e quindi dei capitoli che rappresentano) è regolata dalle linee guida alla sezione [5. Istruzioni per la consegna degli elaborati](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/05%20Istruzioni%20consegna%20elaborati%20#5-istruzioni-per-la-consegna-degli-elaborati).

All’interno dei file di testo in markdown vanno linkate le immagini che saranno poi inserite nella cartella “images”. Le regole per la produzione delle immagini e la loro nominazione sono visionabili dalle linee guida alla sezione [5.3 Immagini, tabelle e diagrammi, e didascalie](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/05%20Istruzioni%20consegna%20elaborati%20#53-immagini-tabelle-e-diagrammi-e-didascalie).

Nei sette file markdown contenuti nel template si possono vedere esempi di scritti.

**Nota**: È possibile scrivere i propri testi con diversi software di scrittura (e.g. Word, Libre Office, Open Office, Google Docs ecc.), e poi copiare-incollare i testi all’interno dei file Markdown, avendo cura di riattribuire la formattazione originaria usando i codici Markdown nel software MacDown (nel copiare-incollare in MacDown i testi composti in un altro software, infatti, viene persa la formattazione).

---

Nel file **colophon.md** nel quale vanno inserite le informazioni generali dell’elaborato (titolo, autori, abstract, parole chiave e attribuzioni.

---

Nella cartella **license** è contenuto il modulo di licenza da compilare e firmare per poter pubblicare con Bembo Officina Editoriale.

---

Nel file **readme.txt** gli autori possono indicare eventuali istruzioni particolari da lasciare alla redazione. File NON obbligatorio, da produrre solo se necessario.

---
### 2.1.4. Composizione in Markdown per Bembo Officina Editoriale

La composizione dei testi in Markdown da parte degli autori si basa in massima parte sulle funzioni di taggatura già presenti in Markdown che permettono di attribuire specifiche formattazioni.

L'interfaccia di MacDown presenta comandi che formattano i testi secondo la specifica Markdown.

![Figura 3. Comandi interfaccia di MacDown](_img/fig3_macdown_commands.png "Fig.3. Comandi interfaccia di MacDown")

L’uso di questi comandi inserisce già le tag adatte per formattare i testi correttamente.<br>
Tuttavia, è sempre possibile scrivere direttamente tramite tastiera i codici corretti.<br>
Qui di seguito si riportano alcuni esempi:

| Sintassi Markdown      | Anteprima formattazione |
| ----------- | ----------- |
| `# Heading level 1`    |  <h1>Heading level 1</h1>       |
| `## Heading level 2`   |  <h2>Heading level 2</h2>       |
| `### Heading level 3`   |  <h3>Heading level 3</h3>       |
| `I just love **bold text**.` | I just love **bold text**. |
| `Italicized text is the *cat's meow*.`| Italicized text is the *cat's meow*.|
| `This text is ***really important***.`| This text is ***really important***.|
|> Dorothy followed her through many of the beautiful rooms in her castle.| <blockquote>Dorothy followed her through many of the beautiful rooms in her castle.</blockquote>|
| <ol style="list-style-type: none !important"><li>1. First item</li><li>2. Second item</li><li>3. Third item<ol style="list-style-type: none"><li>1. Indented item</li><li>2. Indented item</li></li></ol style="list-style-type: none"><li>4. Fourth item</li></ol>|<ol><li>First item</li><li>Second item</li><li>Third item<ol><li>Indented item</li><li>Indented item</li></li></ol><li>Fourth item</li></ol>|
| <ul style="list-style-type: none"><li>- First item</li><li>- Second item</li><li>- Third item<ul style="list-style-type: none"><li>- Indented item</li><li>- Indented item</li></li></ul style="list-style-type: none"><li>- Fourth item</li></ul>|<ul><li>First item</li><li>Second item</li><li>Third item<ul><li>Indented item</li><li>Indented item</li></li></ul><li>Fourth item</li></ul>|

La guida completa a tutte le tag Markdown è disponibile all’indirizzo: [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/) 

---
### 2.1.5. Markdown personalizzato per Bembo OE

La gran parte dei contributi degli autori dovrà uniformarsi allo standard Markdown di base, descritto nella sezione precedente, salvo alcune eccezioni proprie al template di Bembo OE che richiedono una marcatura speciale già fornita nel template e per le quali è necessario osservare le seguenti indicazioni:

#### 2.1.5.1. Colophon e frontespizio



Le informazioni sugli autori vanno scritte nel file `colophon.md` fornito nel template, nella sezione `<!-- MODIFICARE CON INFORMAZIONI AUTORE --> `. Le informazioni sono catalogate in un tag `<p>` contenente campi da compilare.
Ogni autore troverà le proprie informazioni organizzate su 4 linee. Per aggiungere un autore, sarà necessario copiare-incollare il pezzo di codice racchiuso tra accenti gravi. es.

---
```
<p class="autore">
Nome e Cognome Primo autore
posizione nell'organizzazione
email istituzionale
istituzione
</p>

<p class="autore">
Nome e Cognome Secondo autore
posizione nell'organizzazione
email istituzionale
istituzione
</p>
```
---

Per eliminare un autore, basterà cancellare tutto il medesimo pezzo di codice racchiuso tra accenti gravi.

La stessa operazione va eseguita in fondo al colophon per compilre le informazioni necessarie al frontespizio

```
<p class="titolo-frontespizio">
TITOLO LIBRO IN CAPS LOCK
</p>

<p class="sottotitolo-frontespizio">
Eventuale Sottotitolo.
</p>

<p class='sottotitolo-frontespizio'>
Nome e cognome primo autore
</p>

```



#### 2.1.5.2. Immagini

L’inserimento delle immagini nel testo **NON** segue la sintassi Markdown, ma la sintassi HTML. Per inserire un’immagine nel testo corrente l’autore dovrà **copiare e incollare il seguente blocco di codice nel file markdown aggiornando il testo “nomefile” e “didascalia immagine”**: 

```
<figure>
	<img src="../images/nomefile.png">
	<figcaption>didascalia immagine. (© nome detentore copyright)</figcaption>
</figure>
```

N.B.: A seguito della stringa “<img src="../images/” l’autore deve **sostituire la dicitura “nomefile.png" con il nome del file** dell’immagine da inserire.
Si ricorda di **NON cambiare la posizione dei file Markdown e della cartella delle immagini**, per non compromettere il funzionamento corretto dei link e per poter visualizzare correttamente le immagini nell’anteprima di MacDown.


#### 2.1.5.3. Citazioni infratesto
Le citazioni infratestuali vanno scritte come testo corrente **secondo il manuale di stile APA 7ma edizione** (vedi linee guida [sezione 3. Norme redazionali e citazione](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/03%20Norme%20redazionali%20e%20citazione#3-norme-redazionali-e-citazione)).


#### 2.1.5.4. Note
L’impaginato di Bembo OE prevede che le note siano composte alla fine di ogni capitolo.

L’indicazione dell’apice della nota nel testo viene data con il codice:

`[^1] `
e a seguire  `[^2]`, `[^3]` … `[^n]`

Il testo delle note va inserito al termine del capitolo, **sotto la sezione "## Note"**, come segue: 

`[^1]: testo della nota`


#### 2.1.5.5. Elenco letterato
A seconda delle esigenze del testo è possibile inserire, oltre a elenchi puntati e numerati, elenchi letterati. Anche questo caso, come per le immagini, **NON** segue la sintassi Markdown, ma la sintassi HTML. Per inserire un’immagine nel testo corrente l’autore dovrà **copiare e incollare il seguente blocco di codice nel file markdown aggiornando il testo “Qui il tuo testo” all'interno del tag `<li> ... </li>`**:

```
<!--ELENCO LETTERATO-->
<ol class="elenco-lettere">
<li class="elenco-lettere"> Qui il tuo testo </li>
<li class="elenco-lettere"> Qui il tuo testo </li>
<li class="elenco-lettere"> Qui il tuo testo </li>
<li class="elenco-lettere"> Qui il tuo testo </li>
</ol>
```
#### 2.1.5.5. Autore capitolo
Nel caso un capitolo abbia una prefazione scritta da terzi, o nel caso di un contributo ad una raccolta di saggi, è possibile specificare l'autore dopo il titolo del capitolo don la seguete formattazione

```
# 01 Titolo Capitolo

#### Nome autore capitolo
##### Affiliazione autore capitolo

Testo del capitolo...

```



---
### 2.1.6. Consegna dei file

**Una volta terminata la fase di scrittura/inserimento dei testi** in Markdown, gli autori  devono **rinominare la cartella** con i file .md e le immagini secondo la **notazione “nome cognome_aammgg”**, e comprimere l’intera cartella in un file .zip. 
Alle linee guida [sezione 5. Istruzioni per la consegna degli elaborati](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/05%20Istruzioni%20consegna%20elaborati%20#5-istruzioni-per-la-consegna-degli-elaborati) viene indicata la lista completa dei documenti da includere nel file .zip da inviare alla redazione di Bembo OE.

----
## 2.2. Software di reference management Zotero

La **lista dei riferimenti bibliografici** completi, citati nel testo, deve essere fornita in **formato .bib (BibLaTeX)**.

Per ottenere tale file, gli autori devono utilizzare un software di reference management.
Le seguenti linee guida sono basate sulle procedure utilizzate dal **software Zotero**, gratuito, open source e multipiattaforma.


### 2.2.1. Download e setup del software Zotero
 
All’indirizzo [https://www.zotero.org](https://www.zotero.org), è possibile scaricare il software e installarlo sul proprio computer.

![Figura 4. Schermata di download dal sito di Zotero](_img/fig4_zotero_download.png "Fig.4. Zotero download")

Il funzionamento di Zotero e della sua interfaccia sono spiegati nel dettaglio nella [sezione 4. Preparazione bibliografia](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/04%20Preparazione%20bibliografia).

### 2.2.2. Download degli esempi di reference

Per agevolare l’autore durante la preparazione della propria collezione di reference da esportare in un file .bib, Bembo OE mette a disposizione una collezione di esempio, completamente funzionante e utilizzabile al fine di minimizzare gli errori di compilazione.

1. Il file `bibliography.bib` che è contenuto nel template per gli autori, nella cartella bibliography, contiene tutti gli esempi di reference.

2. Aprire Zotero. Recarsi nel menù `File > Importa…`
![Figura 5. Importazione del file .bib con gli esempi APA in Zotero, step 1](_img/fig5_zotero_import_step1.png "Fig. 5. Importazione del file .bib con gli esempi APA in Zotero, step 1")

3. Indicare che si vuole importare un file BibTeX e premere su “Continua”
![Figura 6. Importazione del file .bib con gli esempi APA in Zotero, step 2](_img/fig6_zotero_import_step2.png "Fig. 6. Importazione del file .bib con gli esempi APA in Zotero, step 2")

4. Indicare che si vuole importare gli elementi in una nuova collezione. Lasciare invariate tutte le impostazioni di default. Premere sul tasto “Continua”
![Figura 7. Importazione del file .bib con gli esempi APA in Zotero, step 3](_img/fig7_zotero_import_step3.png "Fig. 7. Importazione del file .bib con gli esempi APA in Zotero, step 3")

5. Visionare nell’interfaccia di Zotero tutte le reference di esempio che sono state importate. Quelle reference fungono da esempio di compilazione per tutte quelle degli autori.



### 2.2.3. Creazione della propria collezione di reference per l'invio alla redazione

Una volta installato Zotero e preso visione degli esempi di reference forniti da Bembo OE, gli autori possono procedere a creare la propria collezione da inviare poi alla redazione una volta completato lo scritto.

Per creare una nuova collezione vuota in Zotero:

1.Cliccare sul menù File e sull'opzione Nuova collezione/New collection
![Figura 8. Creazione della propria collezione di reference in Zotero, step 1, Menù File e opzione Nuova collezione](_img/fig8_zotero_collection_step1.png "Fig. 8. Creazione della propria collezione di reference in Zotero, step 1")

2.Verrà mostrata una finestra dove sarà possibile dare un nome a piacere alla propria collezione

![Figura 9. Creazione della propria collezione di reference in Zotero, step 2, pop-up menù dove inserire il nome della collezione](_img/fig9_zotero_collection_step2.png "Fig. 9. Creazione della propria collezione di reference in Zotero, step 1")

3.Scelto il nome, verrà visualizzata la propria collezione, vuota, pronta per essere riempita con le proprie reference seguendo le indicazioni fornite alla [sezione 4. Preparazione bibliografia](https://github.com/roberto-arista/Bembo-Officina-Editoriale-Tools/tree/master/author-guides/04%20Preparazione%20bibliografia).

![Figura 10. Creazione della propria collezione di reference in Zotero, step 3, visualizzazione della collezione creata, ma ancora vuota](_img/fig10_zotero_collection_step3.png "Fig. 9. Creazione della propria collezione di reference in Zotero, step 3")
