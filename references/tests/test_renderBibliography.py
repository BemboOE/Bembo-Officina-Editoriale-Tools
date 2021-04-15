#!/usr/bin/env python3
# coding: utf-8

# ------------------- #
# Render Biblio Tests #
# ------------------- #

# --- Modules --- #
from pytest import param, mark

import json
from pathlib import Path

import biblib.bib
from biblio.renderBibliography import generateBibliography, nth
from biblio.fromBibLatexToJSON import processTitle, processNames, parseDate

# --- Constants --- #
MARKUP_START = """<root xmlns:aid="http://ns.adobe.com/AdobeInDesign/4.0/" xmlns:aid5="http://ns.adobe.com/AdobeInDesign/5.0/"><bibliography>\n<item aid:pstyle='biblioItem'>"""
MARKUP_END = """</item>\n</bibliography></root>"""

OPEN_EM = "<em aid:cstyle='emphasis'>"
CLOSE_EM = '</em>'

with open('tests/apa7.json', mode='r', encoding='utf-8') as jsonFile:
    apa7 = json.loads(jsonFile.read())

with open('tests/edgeCases.json', mode='r', encoding='utf-8') as jsonFile:
    edgeCases = json.loads(jsonFile.read())

testsFolder = Path('tests')
bibRawSource = {}
for eachBibPath in [pp for pp in testsFolder.iterdir() if pp.suffix == '.bib']:
    with open(eachBibPath, mode='r', encoding='utf-8') as bibFile:
        bibDB = biblib.bib.Parser().parse(bibFile).get_entries()
        bibRawSource.update(bibDB)


apa7_testData = [
    # ---- Articles ---- #
    # newspaper article
    param(
        'guarino_how_2017',
        f"Guarino, B. (2017, December 4). How will humanity react to alien life? Psychologists have some predictions. {OPEN_EM}The Washington Post{CLOSE_EM}. https://www.washingtonpost.com/news/speaking-of-science/wp/2017/12/04/how-will-humanity-react-to-alien-life-psychologists-have-some-predictions"
    ),

    param(
        'hess_cats_2019',
        f"Hess, A. (2019, January 3). Cats who take direction. {OPEN_EM}The New York Times{CLOSE_EM}, C1"
    ),

    # magazine article
    param(
        'bergeson_really_2019',
        f"Bergeson, S. (2019, January 4). Really cool neutral plasmas. {OPEN_EM}Science{CLOSE_EM}{OPEN_EM}, 363{CLOSE_EM}(6422), 33–34. https://doi.org/10.1126/science.aau7988"
    ),

    param(
        'bustillos_video_2013',
        f"Bustillos, M. (2013, March 19). On video games and storytelling: An interview with Tom Bissell. {OPEN_EM}The New Yorker{CLOSE_EM}. https://www.newyorker.com/books/page-turner/on-videogames- and-storytelling-an-interview-with-tom-bissell"
    ),

    param(
        'weir_forgiveness_2017',
        f"Weir, K. (2017, January). Forgiveness can improve mental and physical health. {OPEN_EM}Monitor on Psychology{CLOSE_EM}{OPEN_EM}, 48{CLOSE_EM}(1), 30"
    ),

    # journal article with DOI
    param(
        'mccauley_language_2019',
        f"McCauley, S. M., &amp; Christiansen, M. H. (2019). Language learning as language use: A cross-linguistic model of child language development. {OPEN_EM}Psychological Review{CLOSE_EM}{OPEN_EM}, 126{CLOSE_EM}(1), 1–51. https://doi.org/10.1037/rev0000126"
    ),

    # journal, magazine, or newspaper article without a DOI, from most academic research databases or print version
    param(
        'anderson_getting_2018',
        f"Anderson, M. (2018). Getting Consistent with Consequences. {OPEN_EM}Educational Leadership{CLOSE_EM}{OPEN_EM}, 76{CLOSE_EM}(1), 26–33",
    ),

    # journal article with a DOI, 21 or more authours
    param(
        'kalnay_ncepncar_1996',
        f"Kalnay, E., Kanamitsu, M., Kistler, R., Collins, W., Deaven, D., Gandin, L., Iredell, M., Saha, S., White, G., Woollen, J., Zhu, Y., Chelliah, M., Ebisuzaki, W., Higgins, W., Janowiak, J., Mo, K. C., Ropelewski, C., Wang, J., Leetmaa, A., … Joseph, D. (1996). The NCEP/NCAR 40-Year Reanalysis Project. {OPEN_EM}Bulletin of the American Meteorological Society{CLOSE_EM}{OPEN_EM}, 77{CLOSE_EM}(3), 437–472. https://doi.org/10.1175/1520-0477(1996)077&lt;0437:TNYRP&gt;2.0.CO;2"
    ),

    # journal article, in press
    param(
        'pachur_unpacking_nodate',
        f"Pachur, T., &amp; Scheibehenne, B. (in press). Unpacking buyer–seller differences in valuation from experience: A cognitive modeling approach. {OPEN_EM}Psychonomic Bulletin &amp; Review{CLOSE_EM}"
    ),

    # special section or special issue in a journal
    param(
        'lilienfeld_heterodox_2018',
        f"Lilienfeld, S. O. (Ed.). (2018). Heterodox issues in psychology [Special section]. {OPEN_EM}Archives of Scientific Psychology{CLOSE_EM}{OPEN_EM}, 6{CLOSE_EM}(1), 51–104"
    ),

    param(
        'mcdaniel_science_2018',
        f"McDaniel, S. H., Salas, E., &amp; Kazak, A. E. (Eds.). (2018). The science of teamwork [Special issue]. {OPEN_EM}American Psychologist{CLOSE_EM}{OPEN_EM}, 73{CLOSE_EM}(4)"
    ),

    # editorial
    param(
        'cuellar_study_2016',
        f"Cuellar, N. G. (2016). Study Abroad Programs [Editorial]. {OPEN_EM}Journal of Transcultural Nursing{CLOSE_EM}{OPEN_EM}, 27{CLOSE_EM}(3), 209. https://doi.org/10.1177/1043659616638722"
    ),

    # Reviews
    # film review published in a journal
    param(
        'mirabito_bringing_2016',
        f'Mirabito, L. A., &amp; Heck, N. C. (2016). Bringing LGBTQ youth theater into the spotlight [Review of the film {OPEN_EM}The year we thought about love{CLOSE_EM}, by E. Brodsky, Dir.]. {OPEN_EM}Psychology of Sexual Orientation and Gender Diversity{CLOSE_EM}{OPEN_EM}, 3{CLOSE_EM}(4), 499–500. https://doi.org/10.1037/sgd0000205',
    ),

    # book review published in a newspaper
    param(
        'santos_reframing_2019',
        f'Santos, F. (2019, January 11). Reframing refugee children’s stories [Review of the book {OPEN_EM}We are displaced: My journey and stories from refugee girls around the world{CLOSE_EM}, by M. Yousafzai]. {OPEN_EM}The New York Times{CLOSE_EM}. https://nyti.ms/2Hlgjk3',
    ),

    # tv series episode review published on a website
    param(
        'perkins_good_2018',
        f'Perkins, D. (2018, February 1). {OPEN_EM}The Good Place ends its remarkable second season with irrational hope, unexpected gifts, and a smile {CLOSE_EM}[Review of the TV series episode {OPEN_EM}Somewhere else{CLOSE_EM}, by M. Schur, Writer &amp; Dir.]. A.V. Club. https://www.avclub.com/the-good-place-ends-its-remarkable-second-season-with-i-1822649316',
    ),

    # ---- Book / Ebook / Audio Book ---- #
    # authored book with a DOI
    param(
        'brown_feminist_2018',
        f'Brown, L. S. (2018). {OPEN_EM}Feminist therapy{CLOSE_EM} (2nd ed.). American Psychological Association. https://doi.org/10.1037/0000092-000'
    ),

    # authored book with editor credited on the book cover
    param(
        'meadows_thinking_2008',
        f'Meadows, D. H. (2008). {OPEN_EM}Thinking in Systems: A Primer{CLOSE_EM} (D. Wright, Ed.). Chelsea Green Publishing'
    ),

    # edited book without a DOI, from most academic research databases or print version
    param(
        'hacker_hughes_military_2017',
        f'Hacker Hughes, J. (Ed.). (2017). {OPEN_EM}Military Veteran Psychological Health and Social Care: Contemporary Approaches{CLOSE_EM} (1st ed.). Routledge',
    ),

    # edited book with a DOI, with multiple publishers
    param(
        'schmid_entrenchment_2017',
        f'Schmid, H.-J. (Ed.). (2017). {OPEN_EM}Entrenchment and the psychology of language learning: How we reorganize and adapt linguistic knowledge{CLOSE_EM}. American Psychological Association; De Gruyter Mouton. https://doi.org/10.1037/15969-000'
    ),

    # book in another language
    param(
        'amano_nihongo_2000',
        f'Amano, N., &amp; Kondo, H. (2000). {OPEN_EM}Nihongo no goi tokusei {CLOSE_EM}[Lexical characteristics of Japanese language] (Vol. 7). Sansei-do',
    ),

    param(
        'piaget_psychologie_1966',
        f'Piaget, J., &amp; Inhelder, B. (1966). {OPEN_EM}La psychologie de l’enfant {CLOSE_EM}[The psychology of the child]. Quadrige',
    ),

    # republished book
    param(
        'freud_interpretation_2010',
        f'Freud, S. (2010). {OPEN_EM}The Interpretation of Dreams: The Complete and Definitive Text{CLOSE_EM} (J. Strachey, Ed. &amp; Trans.). Basic Books. (Original work published 1900)'
    ),

    # book republished in translation
    param(
        'piaget_psychology_1969',
        f'Piaget, J., &amp; Inhelder, B. (1969). {OPEN_EM}The Psychology of the Child{CLOSE_EM} (H. Weaver, Trans.; 2nd ed.). Basic Books. (Original work published 1966)'
    ),

    # one volume of a multivolume work
    param(
        'fiske_handbook_2010',
        f'Fiske, S. T., Gilbert, D. T., &amp; Lindzey, G. (Eds.). (2010). {OPEN_EM}Handbook of Social Psychology{CLOSE_EM} (5th ed., Vol. 1). John Wiley &amp; Sons. https://doi.org/10.1002/9780470561119',
    ),

    # diagnostic manual (DSM, ICD)
    param(
        'american_psychiatric_association_diagnostic_2013',
        f'American Psychiatric Association. (2013). {OPEN_EM}Diagnostic and Statistical Manual of Mental Disorders{CLOSE_EM} (5th ed.). American Psychiatric Association. https://doi.org/10.1176/appi.books.9780890425596'
    ),

    param(
        'world_health_organization_international_2019',
        f'World Health Organization. (2019). {OPEN_EM}International statistical classification of diseases and related health problems{CLOSE_EM} (11th ed.). https://icd.who.int/'
    ),

    # dictionary, thesaurus, or encyclopedia
    param(
        'american_psychological_association_apa_nodate',
        f'American Psychological Association. (n.d.). {OPEN_EM}APA dictionary of psychology{CLOSE_EM}. Retrieved June 14, 2019, from https://dictionary.apa.org/',
    ),

    param(
        'merriam-webster_merriam-webstercom_nodate',
        f'Merriam-Webster. (n.d.). {OPEN_EM}Merriam-Webster.com dictionary{CLOSE_EM}. Retrieved May 5, 2019, from https://www.merriamwebster.com/',
    ),

    param(
        'zalta_stanford_2019',
        f'Zalta, E. N. (Ed.). (2019). {OPEN_EM}The Stanford encyclopedia of philosophy{CLOSE_EM} (Summer 2019 ed.). Stanford University. https://plato.stanford.edu/archives/sum2019/',
    ),

    # authored ebook (e.g., Kindle book) or audiobook without a DOI, with a nondatabase URL
    param(
        'cain_quiet_2012',
        f'Cain, S. (2012). {OPEN_EM}Quiet: The power of introverts in a world that can’t stop talking{CLOSE_EM} (K. Mazur, Narr.) [Audiobook]. Random House Audio. http://bit.ly/2G0BpbI',
    ),

    # edited ebook (e.g., Kindle book) or audiobook without a DOI, with a nondatabase URL
    param(
        'pridham_guided_2018',
        f'Pridham, K. F., Limbo, R., &amp; Schroeder, M. (Eds.). (2018). {OPEN_EM}Guided Participation in Pediatric Nursing Practice: Relationship-Based Teaching and Learning with Parents, Children, and Adolescents{CLOSE_EM} (1st ed.). Springer Publishing Company. http://a.co/0IAiVgt',
    ),

    # ---- Book Chapters and Entries in Reference Works ---- #
    # chapter in an edited book with a DOI
    param(
        'iwamasa_affirmative_2019',
        f'Balsam, K. F., Martell, C. R., Jones, K. P., &amp; Safren, S. A. (2019). Affirmative cognitive behavior therapy with sexual and gender minority people. In G. Y. Iwamasa, &amp; P. A. Hays (Eds.), {OPEN_EM}Culturally responsive cognitive behavior therapy: Practice and supervision{CLOSE_EM} (2nd ed., pp. 287–314). American Psychological Association. https://doi.org/10.1037/0000119-012',
    ),

    # chapter in an edited ebook (e.g., Kindle book) or audiobook without a DOI, with nondatabase URL
    param(
        'tafoya_back_2005',
        f'Tafoya, N., &amp; Del Vecchio, A. (2005). Back to the future: An examination of the Native American Holocaust experience. In M. McGoldrick, J. Giordano, &amp; N. Garcia-Preto (Eds.), {OPEN_EM}Ethnicity and family therapy{CLOSE_EM} (3rd ed., pp. 55–63). Guilford Press. http://a.co/36xRhBT',
    ),

    # chapter in a volume of a multivolume work
    param(
        'goldin-meadow_gesture_2015',
        f'Goldin-Meadow, S. (2015). Gesture and Cognitive Development. In L. S. Liben, &amp; U. Mueller (Eds.), {OPEN_EM}Handbook of Child Psychology and Developmental Science{CLOSE_EM}{OPEN_EM}: Vol. 2. Cognitive Processes{CLOSE_EM} (7th ed., pp. 339–380). John Wiley &amp; Sons. https://doi.org/10.1002/9781118963418.childpsy209',
    ),

    # work in anthology
    param(
        'gold_group_1999',
        f'Lewin, K. (1999). Group decision and social change. In M. Gold (Ed.), {OPEN_EM}The complete social scientist: A Kurt Lewin reader{CLOSE_EM} (pp. 265–284). American Psychological Association. https://doi.org/10.1037/10319-010. (Original work published 1948)',
    ),

    # ---- Entry in a Dictionary, Thesaurus, or Encyclopedia ---- #
    # entry in a dictionary, thesaurus, or encyclopedia, with group author
    param(
        'american_psychological_association_positive_nodate',
        f'American Psychological Association. (n.d.). Positive transference. In {OPEN_EM}APA dictionary of psychology{CLOSE_EM}. Retrieved August 31, 2019, from https://dictionary.apa.org/positive-transference',
    ),

    # entry in a dictionary, thesaurus, or encyclopedia, with individual author
    param(
        'graham_behaviorism_2019',
        f'Graham, G. (2019). Behaviorism. In E. N. Zalta (Ed.), {OPEN_EM}The Stanford encyclopedia of philosophy{CLOSE_EM} (Summer 2019 ed.). Stanford University. https://plato.stanford.edu/archives/sum2019/entries/behaviorism/',
    ),

    # wikipedia entry
    param(
        'noauthor_list_2019',
        f'List of oldest companies. (2019, January 13). In {OPEN_EM}Wikipedia{CLOSE_EM}. https://en.wikipedia.org/wiki/List_of_oldest_companies',
    ),

    # ---- Conference Sessions & Presentations ---- #
    # conference session
    param(
        'fistek_everybodys_nodate',
        f'Fistek, A., Jester, E., &amp; Sonnenberg, K. (2017, July 12-15). {OPEN_EM}Everybody’s got a little music in them: Using music therapy to connect, engage, and motivate{CLOSE_EM} [Conference session]. Autism Society National Conference, Milwaukee, Wl, United States. https://asa.confex.com/asa/2017/webprogramarchives/Session9517.html',
    ),

    # paper presentation
    param(
        'maddox_if_nodate',
        f'Maddox, S., Hurling, J., Stewart, E., &amp; Edwards, A. (2016, March 30-April 2). {OPEN_EM}If mama ain’t happy, nobody’s happy: The effect of parental depression on mood dysrégulation in children{CLOSE_EM} [Paper presentation]. Southeastern Psychological Association 62nd Annual Meeting, New Orleans, LA, United States',
    ),

    # poster presentation
    param(
        'pearson_fat_nodate',
        f'Pearson, J. (2018, September 27-30). {OPEN_EM}Fat talk and its effects on state-based body image in women{CLOSE_EM} [Poster presentation]. Australian Psychological Society Congress, Sydney, NSW, Australia. http://bit.ly/2XGSThP',
    ),

    # ---- Symposium Contribution ---- #
    # check ref table

    # ---- Atti di convegno ---- #
    # check ref table

    # ---- Thesis ---- #
    # unpublished dissertation or thesis
    param(
        'harris_instructional_2014',
        f'Harris, L. (2014). {OPEN_EM}Instructional leadership perceptions and practices of elementary school leaders{CLOSE_EM} [Unpublished doctoral dissertation]. University of Virginia',
    ),

    # dissertation or thesis from a database
    param(
        'hollander_resistance_2017',
        f'Hollander, M. M. (2017). {OPEN_EM}Resistance to authority: Methodological innovations and new lessons from the Milgram experiment{CLOSE_EM} (Publication No. 10289373) [Doctoral dissertation, University of Wisconsin-Madison]. ProQuest Dissertations and Theses Global',
    ),

    # dissertation or thesis published online (not in a database)
    param(
        'hutcheson_dealing_2012',
        f'Hutcheson, V. H. (2012). {OPEN_EM}Dealing with dual differences: Social coping strategies of gifted and lesbian, gay; bisexual, transgender, and queer adolescents{CLOSE_EM} [Master’s thesis, The College of William &amp; Mary]. William &amp; Mary Digital Archive. https://digitalarchive.wm.edu/bitstream/handle/10288/16594/HutchesonVirginia2012.pdf',
    ),

    # ---- Personal Comunication (letters, emails, instant messaging, interviews, conversations) ---- #
    # check ref table

    # ---- Manuscript + Informally Published Work ---- #
    # unpublished manuscript
    param(
        'yoo_linking_2016',
        f'Yoo, J., Miyamoto, Y., Rigotti, A., &amp; Ryff, C. (2016). {OPEN_EM}Linking positive affect to blood lipids: A cultural perspective{CLOSE_EM} [Unpublished manuscript]. Department of Psychology, University of Wisconsin-Madison',
    ),

    # manuscript in preparation
    param(
        'oshea_understanding_2018',
        f'O&#39;Shea, M. (2018). {OPEN_EM}Understanding proactive behavior in the workplace as a function of gender{CLOSE_EM} [Manuscript in preparation]. Department of Management, University of Kansas',
    ),

    # manuscript submitted for publication
    param(
        'lippincott_emotion_2019',
        f'Lippincott, T., &amp; Poindexter, E. K. (2019). {OPEN_EM}Emotion recognition as a function of facial cues: Implications for practice{CLOSE_EM} [Manuscript submitted for publication]. Department of Psychology, University of Washington',
    ),

    # ---- informally published work, from a preprint archive or an institutional repository ---- #
    # not solved yet
    # not solved yet

    # ---- Reports ---- #
    # report by a government agency or other organization
    param(
        'australian_government_productivity_commission__new_zealand_productivity_commission_strengthening_2012',
        f'Australian Government Productivity Commission &amp; New Zealand Productivity Commission. (2012). {OPEN_EM}Strengthening trans-Tasman economic relations{CLOSE_EM}. https://www.pc.gov.au/inquiries/completed/australia-new-zealand/report/trans-tasman.pdf',
    ),

    param(
        'canada_council_for_the_arts_what_2013',
        f'Canada Council for the Arts. (2013). {OPEN_EM}What we heard: Summary of key findings: 2013 Canada Council’s Inter-Arts Office consultation{CLOSE_EM}. http://publications.gc.ca/collections/collection_2017/canadacouncil/K23-65-2013-eng.pdf',
    ),

    param(
        'national_cancer_institute_facing_2018',
        f'National Cancer Institute. (2018). {OPEN_EM}Facing forward: Life after cancer treatment{CLOSE_EM} (NIH Publication No. 18-2424). U.S. Department of Health and Human Services, National Institutes of Health. https://www.cancer.gov/publications/patient-education/life- after-treatment.pdf',
    ),

    # report by individual authors at a government agency or other organization
    param(
        'fried_democratic_2018',
        f'Fried, D., &amp; Polyakova, A. (2018). {OPEN_EM}Democratic defense against disinformation{CLOSE_EM}. Atlantic Council. https://www.atlanticcouncil.org/images/publications/Democratic_Defense_Against_Disinformation_FINAL.pdf',
    ),

    # report by individual authors at a government agency, published as part of a series
    param(
        'blackwell_summary_2014',
        f'Blackwell, D. L., Lucas, J. W., &amp; Clarke, T. C. (2014). {OPEN_EM}Summary health statistics for U.S. adults: National Health Interview Survey, 2012{CLOSE_EM} (Vital and Health Statistics Series 10, Issue 260). Centers for Disease Control and Prevention. https://www.cdc.gov/nchs/data/series/sr_10/sr10_260.pdf',
    ),

    # report by a task force, working group, or other group
    param(
        'british_cardiovascular_society_working_group_british_2016',
        f'British Cardiovascular Society Working Group. (2016). {OPEN_EM}British Cardiovascular Society Working Group report: Out-of-hours cardiovascular care: Management of cardiac emergencies and hospital in-patients{CLOSE_EM}. British Cardiovascular Society. http://www.bcs.com/documents/BCSOOHWP_Final_Report_05092016.pdf',
    ),

    # annual report
    param(
        'us_securities_and_exchange_commission_agency_2017',
        f'U.S. Securities and Exchange Commission. (2017). {OPEN_EM}Agency financial report: Fiscal year 2017{CLOSE_EM}. https://www.sec.gov/files/sec- 2017-agency-financial-report.pdf',
    ),

    # ---- Press Release ---- #
    param(
        'us_food_and_drug_administration_fda_2019',
        f'U.S. Food and Drug Administration. (2019, February 14). {OPEN_EM}FDA authorizes first interoperable insulin pump intended to allow patients to customize treatment through their individual diabetes management devices{CLOSE_EM} [Press release]. https://www.fda.gov/NewsEvents/Newsroom/PressAnnouncements/ucm631412.htm',
    ),

    # Blog
    # blog post
    param(
        'klymkowsky_can_2018',
        f'Klymkowsky, M. (2018, September 15). {OPEN_EM}Can we talk scientifically about free will?{CLOSE_EM} Sci-Ed. https://blogs.plos.org/scied/2018/09/15/can-we-talk-scientifically-about-free-will/',
    ),

    # comment on an online periodical article or post
    param(
        'ks_in_nj_this_2019',
        f'KS in NJ. (2019, January 15). From this article, it sounds like men are figuring something out that women have known forever. I know of many [Comment on the article {OPEN_EM}How workout buddies can help stave off loneliness{CLOSE_EM}]. {OPEN_EM}The Washington Post{CLOSE_EM}. https://wapo.st/2HDToGJ',
    ),

    # Social (facebook, twitter, instagram)
    # tweet
    param(
        'apa_education_apaeducation_college_2018',
        f'APA Education [@APAEducation]. (2018, June 29). {OPEN_EM}College students are forming mental-health clubs — and they’re making a difference @washingtonpost{CLOSE_EM} [Thumbnail with link attached] [Tweet]. Twitter. https://twitter.com/apaeducation/status/1012810490530140161',
    ),

    param(
        'badlands_national_park_badlandsnps_biologists_2018',
        f'Badlands National Park [@BadlandsNPS]. (2018, February 26). {OPEN_EM}Biologists have identified more than 400 different plant species growing in @BadlandsNPS #DYK #biodiversity{CLOSE_EM} [Tweet]. Twitter. https://twitter.com/badlandsnps/status/968196500412133379',
    ),

    param(
        'white_b_bettymwhite_i_2018',
        f'White, B. [@BettyMWhite]. (2018, June 21). {OPEN_EM}I treasure every minute we spent together #koko{CLOSE_EM} [Image attached] [Tweet]. Twitter. https://twitter.com/BettyMWhite/status/1009951892846227456',
    ),

    # twitter profile
    param(
        'apa_style_apa_style_tweets_nodate',
        f'APA Style [@APA_Style]. (n.d.). {OPEN_EM}Tweets{CLOSE_EM} [Twitter profile]. Twitter. Retrieved November 1, 2019, from https://twitter.com/apa_style',
    ),

    # facebook post
    param(
        'gaiman_100000_2018',
        f'Gaiman, N. (2018, March 22). {OPEN_EM}100,000+ Rohingya refugees could be at serious risk during Bangladesh’s monsoon season. My fellow UNHCR Goodwill Ambassador Cate Blanchett is{CLOSE_EM} [Image attached] [Status update]. Facebook. https://www.facebook.com/neilgaiman/posts/10155317238526016',
    ),

    param(
        'national_institute_of_mental_health_suicide_2018',
        f'National Institute of Mental Health. (2018, November 28). {OPEN_EM}Suicide affects all ages, genders, races, and ethnicities. Check out these 5 Action Steps for Helping Someone in Emotional Pain{CLOSE_EM} [Infographic]. Facebook. http://bit.ly/321Qstq',
    ),

    # facebook page
    param(
        'smithsonians_national_zoo_and_conservation_biology_institute_home_nodate',
        f'Smithsonian’s National Zoo and Conservation Biology Institute. (n.d.). {OPEN_EM}Home{CLOSE_EM} [Facebook page]. Facebook. Retrieved July 22, 2019, from https://www.facebook.com/nationalzoo/',
    ),

    # instagram photo or video
    param(
        'zeitz_mocaa_zeitzmocaa_grade_2018',
        f'Zeitz MOCAA [@zeitzmocaa]. (2018, November 26). {OPEN_EM}Grade 6 learners from Parkfields Primary School in Hanover Park visited the museum for a tour and workshop hosted by our Centre for Art…{CLOSE_EM} [Photographs]. Instagram. https://www.instagram.com/p/BqpHpjFBs3b/',
    ),

    # instagram highlight
    param(
        'the_new_york_public_library_nypl_raven_nodate',
        f'The New York Public Library [@nypl]. (n.d.). {OPEN_EM}The Raven{CLOSE_EM} [Highlight]. Instagram. Retrieved April 16, 2019, from https://bitly.com/2FV8bu3',
    ),

    # --- Forum ---- #
    # Online forum post
    param(
        'national_aeronautics_and_space_administration_nasa_im_2018',
        f"National Aeronautics and Space Administration [nasa]. (2018, September 12). {OPEN_EM}I’m NASA astronaut Scott Tingle. Ask me anything about adjusting to being back on Earth after my first spaceflight!{CLOSE_EM} [Online forum post] Reddit. https://www.reddit.com/r/IAmA/comments/9fagqy/im_nasa_astronaut_scott_tingle_ask_me_anything/",
    ),

    # ---- Webpages ---- #
    # Webpage on a news website
    param(
        'avramova_secret_2019',
        f"Avramova, N. (2019, January 3). {OPEN_EM}The secret to a long, happy, healthy life? Think age-positive{CLOSE_EM}. CNN. Retrieved July 9, 2020, from https://edition.cnn.com/2019/01/03/health/respect-toward-elderly-leads-to-long-life-intl/index.html",
    ),

    param(
        'bologna_what_2018',
        f"Bologna, C. (2018, June 27). {OPEN_EM}What Happens to Your Mind and Body When You Feel Homesick?{CLOSE_EM} HuffPost. https://www.huffpost.com/entry/what-happens-mind-body-homesick_n_5b201ebde4b09d7a3d77eee1",
    ),

    # Webpage on a website with a group author
    param(
        'centers_for_disease_control_and_prevention_people_2018',
        f"Centers for Disease Control and Prevention. (2018, January 23). {OPEN_EM}People at high risk of developing flu-related complications{CLOSE_EM}. https://www.cdc.gov/flu/highrisk/index.htm",
    ),

    # Webpage on a website with an individual author
    param(
        'martin_lillie_be_2016',
        f"Martin Lillie, C. M. (2016, December 29). {OPEN_EM}Be kind to yourself: How self-compassion can improve your resiliency{CLOSE_EM}. Mayo Clinic. http://www.ethicsguidebook.ac.uk/EthicsPrinciples",
    ),

    # Webpage on a website with no date
    param(
        'boddy_ethics_nodate',
        f"Boddy, J., Neumann, T., Jennings, S., Morrow, V., Alderson, R., Rees, R., &amp; Gibson, W. (n.d.). {OPEN_EM}Ethics principles{CLOSE_EM}. The Research Ethics Guidebook: A Resource for Social Scientists. http://www.ethicsguidebook.ac.uk/EthicsPrinciples",
    ),

    param(
        'national_nurses_united_what_nodate',
        f"National Nurses United. (n.d.). {OPEN_EM}What Employers Should Do to Protect Nurses from Zika{CLOSE_EM}. https://www.nationalnursesunited.org/what-employers-should-do-to-protect-rns-from-zika",
    ),

    # Webpage on a website with a retrieval date
    param(
        'us_census_bureau_us_nodate',
        f"U.S. Census Bureau. (n.d.). {OPEN_EM}U.S. and world population clock{CLOSE_EM}. U.S. Department of Commerce. Retrieved July 3, 2019, from https://www.census.gov/popclock/",
    ),

    # ---- Ted talk, Webinar recorded, Youtube video or other streaming video ---- #
    # Ted Talk
    param(
        'giertz_why_2018',
        f"Giertz, S. (2018, April). {OPEN_EM}Why you should make useless things{CLOSE_EM} [Video], TED Conferences. https://www.ted.com/talks/simone_giertz_why_you_should_make_useless_things",
    ),

    param(
        'ted_brene_2012',
        f"TED. (2012, March 16). {OPEN_EM}Brené Brown: Listening to shame{CLOSE_EM} [Video], YouTube. https://www.youtube.com/watch?v=psN1DORYYV0",
    ),

    # Webinar, recorded
    param(
        'goldberg_evaluating_2018',
        f"Goldberg, J. F. (2018). {OPEN_EM}Evaluating Adverse Drug Effects{CLOSE_EM} [Webinar], American Psychiatric Association. http://education.psychiatry.org/Users/ProductDetails.aspx?ActivityID=6172",
    ),

    # YouTube video or other streaming video (es. Vimeo)
    param(
        'cutts_happiness_2017',
        f"Cutts, S. (2017, November 24). {OPEN_EM}Happiness{CLOSE_EM} [Video], Vimeo. https://vimeo.com/244405542",
    ),

    param(
        'fogarty_m_grammar_girl_how_2016',
        f"Fogarty, M. [Grammar Girl]. (2016, September 30). {OPEN_EM}How to diagram a sentence (absolute basics){CLOSE_EM} [Video], YouTube. https://youtu.be/deiEY5Yq1qI",
    ),

    # ---- Music ---- #
    # Music album
    param(
        'bach_brandenburg_2010',
        f"Bach, J. S. (2010). {OPEN_EM}The Brandenburg concertos: Concertos BWV 1043 &amp; 1060{CLOSE_EM} [Album recorded by Academy of St Martin in the Fields]. Decca. (Original work published 1721)",
    ),

    # Single song/track
    param(
        'beethoven_symphony_2012',
        f"Beethoven, L. van. (2012). Symphony No. 3 in E-flat major [Song recorded by Staatskapelle Dresden]. On {OPEN_EM}Beethoven: Complete symphonies. Brilliant Classics{CLOSE_EM}. (Original work published 1804)",
    ),

    param(
        'beyonce_formation_2016',
        f"Beyoncé. (2016). Formation [Song]. On {OPEN_EM}Lemonade{CLOSE_EM}. Parkwood; Columbia.",
    ),

    # ---- Podcast ---- #
    # Podcast
    param(
        'vedantam_s_host_hidden_2015',
        f"Vedantam, S. (Host). (2015). {OPEN_EM}Hidden brain{CLOSE_EM} [Audio podcast]. NPR. https://www.npr.org/series/423302056/hidden-brain",
    ),

    # Podcast episode
    param(
        'glass_i_host_amusement_2011',
        f"Glass, I. (Host). (2011, August 12). Amusement park (No. 443) [Audio podcast episode]. In {OPEN_EM}This American life{CLOSE_EM}. WBEZ Chicago. https://www.thisamericanlife.org/radio-archives/episode/443/amusement-park",
    ),
    # ---- Radio, recording ---- #
    # Radio interview recording in a digital archive
    param(
        'de_beauvoir_simone_1960',
        f"de Beauvoir, S. (1960, May 4). {OPEN_EM}Simone de Beauvoir discusses the art of writing{CLOSE_EM} [Interview]. Studs Terkel Radio Archive; The Chicago History Museum. https://studsterkel.wfmt.com/programs/simone-de-beauvoir-discusses-art-writing",
    ),

    # Speech audio recording
    param(
        'king_i_1963',
        f"King, M. L. jr. (1963, August 28). {OPEN_EM}I have a dream{CLOSE_EM} [Speech audio recording]. American Rhetoric. https://www.americanrhetoric.com/speeches/mlkihaveadream.htm",
    ),
    # ---- Film, video, tv series ---- #

    # Film or video
    param(
        'forman_m_director_one_1975',
        f"Forman, M. (Director). (1975). {OPEN_EM}One flew over the cuckoo’s nest{CLOSE_EM} [Film]. United Artists",
    ),

    param(
        'fosha_d_guest_expert_accelerated_2017',
        f"Fosha, D. (Guest Expert), &amp; Levenson, H. (Host). (2017). {OPEN_EM}Accelerated experiential dynamic psychotherapy (AEDP) supervision{CLOSE_EM} [Film; educational DVD]. American Psychological Association. https://www.apa.org/pubs/videos/4310958.aspx",
    ),

    param(
        'jackson_p_director_lord_2001',
        f"Jackson, P. (Director). (2001). {OPEN_EM}The lord of the rings: The fellowship of the ring{CLOSE_EM} [Film; four-disc special extended ed. on DVD]. WingNut Films; The Saul Zaentz Company",
    ),

    # Film or video in another language
    param(
        'malle_l_director_au_1987',
        f"Malle, L. (Director). (1987). {OPEN_EM}Au revoir les enfants {CLOSE_EM}[Goodbye children] [Film]. Nouvelles Éditions de Films",
    ),

    # TV series
    param(
        'simon_wire_nodate',
        f"Simon, D., Colesberry, R. F., &amp; Kostroff Noble, N. (Executive Producers). (2002-2008). {OPEN_EM}The wire{CLOSE_EM} [TV series]. Blown Deadline Productions; HBO",
    ),

    # TV series episode or webisode
    param(
        'barris_k_writer__director_lemons_2017',
        f"Barris, K. (Writer &amp; Director). (2017, January 11). Lemons (Season 3, Episode 12) [TV series episode]. In K. Barris, J. Groff, A. Anderson, E. B. Dobbins, L. Fishburne, &amp; H. Sugland (Executive Producers), {OPEN_EM}Black-ish{ CLOSE_EM}. Wilmore Films; Artists First; Cinema Gypsy Productions; ABC Studios",
    ),

    # --- artwork, graphics, maps, photographs ---- #
    # Artwork in museum or on a museum website
    param(
        'delacroix_faust_nodate',
        f"Delacroix, E. (1826-1827). {OPEN_EM}Faust attempts to seduce Marguerite{CLOSE_EM} [Lithograph]. The Louvre, Paris, France.",
    ),

    param(
        'wood_american_1930',
        f"Wood, G. (1930). {OPEN_EM}American gothic{CLOSE_EM} [Painting]. Art Institute of Chicago, Chicago, IL, United States. https://www.artic.edu/aic/collections/artwork/6565",
    ),

    # Map
    param(
        'cable_racial_2013',
        f"Cable, D. (2013). {OPEN_EM}The racial dot map{CLOSE_EM} [Map]. University of Virginia, Weldon Cooper Center for Public Service. https://demographics.coopercenter.org/Racial-Dot-Map",
    ),

    param(
        'google_google_nodate',
        "Google. (n.d.). [Google Maps directions for driving from La Paz, Bolivia, to Lima, Peru] [Map]. Retrieved February 16, 2020, from https://goo.gl/YYE3GR",
    ),

    # photographs
    param(
        'mccurry_afghan_1985',
        f"McCurry, S. (1985). {OPEN_EM}Afghan girl{CLOSE_EM} [Photograph]. National Geographic. https://www.nationalgeographic.com/magazine/national-geographic-magazine-50- years-of-covers/#/ngm-1985-jun-714.jpg",
    ),

    param(
        'rinaldi_notitle_2016',
        "Rinaldi, J. (2016). [Photograph series of a boy who finds his footing after abuse by those he trusted]. The Pulitzer Prizes. https://www.pulitzer.org/winners/jessica-rinaldi",
    ),

    # ---- legal ---- #
    # not solved yet

    # ---- patents ---- #
    # patents
    param(
        'hiremath_using_2016',
        f"Hiremath, S. C., Kumar, S., Lu, F., &amp; Salehi, A. (2016). {OPEN_EM}Using metaphors to present concepts across different intellectual domains{CLOSE_EM} (U.S. Patent No. 9,367,592). U.S. Patent and Trademark Office. http://patft.uspto.gov/netacgi/nph-Parser?patentnumber=9367592",
    ),

    param(
        'kasabov_data_2010',
        f"Kasabov, N. K. (2010). {OPEN_EM}Data analysis and predictive systems and related methodologies{CLOSE_EM} (N.Z. Patent 572036). New Zealand Intellectual Property Office. https://app.iponz.govt.nz/app/Extra/IP/Mutual/Browse.aspx?sid=637094081061108163",
    ),

    # ---- data sets + raw data ---- #
    # dataset
    param(
        'dsouza_cognitive_2018',
        f"D&#39;Souza, A., &amp; Wiseheart, M. (2018). {OPEN_EM}Cognitive Effects of Music and Dance Training in Children{CLOSE_EM} (ICPSR 37080; Version V1) [Data set]. ICPSR. https://doi.org/10.3886/ICPSR37080.V1",
    ),

    param(
        'national_center_for_education_statistics_fast_2016',
        f"National Center For Education Statistics. (2016). {OPEN_EM}Fast Response Survey System (FRSS): Teachers&#39; Use of Educational Technology in U.S. Public Schools, 2009{CLOSE_EM} (ICPSR 35531; Version V3) [Data set and code book]. National Archive of Data on Arts and Culture. https://doi.org/10.3886/ICPSR35531.V3",
    ),

    param(
        'pew_research_center_american_2018',
        f"Pew Research Center. (2018). {OPEN_EM}American trends panel Wave 26{CLOSE_EM} [Data Set]. https://www.pewsocialtrends.org/dataset/american-trends-panel-wave-26/",
    ),

    # ---- Unpublished raw data ---- #
    # not solved yet

    # ---- software + app ---- #
    # software
    param(
        'borenstein_comprehensive_2014',
        f"Borenstein, M., Hedges, L., Higgins, J., &amp; Rothstein, H. (2014). {OPEN_EM}Comprehensive meta-analysis{CLOSE_EM} (Version 3.3.070) [Computer software], Biostat. https://www.meta-analysis.com/",
    ),

    # Mobile app
    param(
        'epocrates_epocrates_2019',
        f"Epocrates. (2019). {OPEN_EM}Epocrates medical references{CLOSE_EM} (Version 18.12) [Mobile app]. App Store. https://itunes.apple.com/us/app/epocrates/id281935788?mt=8",
    ),
]

edgeCases_testData = [
    # custom edge cases
    param(
        'bonini_lessing_notazioni_2010',
        f'Bonini Lessing, E. (2010). Notazioni sinsemiche di processi interattivi. {OPEN_EM}Il Verri – Newbasic{CLOSE_EM} (43), 85–91'
    ),

    param(
        'bourzac_child_2012',
        f'Bourzac, K. (2012). Child development: The first steps. {OPEN_EM}Nature{CLOSE_EM}{OPEN_EM}, 491{CLOSE_EM}, S7. https://doi.org/http://dx.doi.org/10.1038/491S7a'
    ),

    param(
        'bourdieu_il_2003',
        f'Bourdieu, P. (2003a). {OPEN_EM}Il mestiere di scienziato. Corso al college de France 2000-2001{CLOSE_EM} (A. Serra, Trans.). Feltrinelli. (Original work published 2001)',
    ),

    param(
        'bourdieu_per_2003',
        f'Bourdieu, P. (2003b). {OPEN_EM}Per una teoria della pratica. Con tre studi di etnologia cabila{CLOSE_EM} (I. Maffi, Trans.). Raffaello Cortina Editore',
    ),

    param(
        'fleming_v_director_gone_1939',
        f"Fleming, V. (Director). (1939). {OPEN_EM}Gone with the wind{CLOSE_EM} [Film]. Selznick International Pictures; Metro-Goldwyn-Mayer",
    ),

    param(
        'alfredson_t_director_lat_2008',
        f"Alfredson, T. (Director). (2008). {OPEN_EM}Låt den rätte komma in {CLOSE_EM}[Let the right one in] [Film]. Magnolia",
    ),


    param(
        'serling_r_twilight_nodate',
        f"Serling, R. (Executive Producer). (1959-1964). {OPEN_EM}The twilight zone{CLOSE_EM} [TV series]. Cayuga Productions; CBS Productions",
    ),

    param(
        'favreau_j_writer_chapter_2019',
        f"Favreau, J. (Writer), &amp; Filoni, D. (Director). (2019, November 12). Chapter 1 (Season 1, Episode 1) [TV series episode]. In J. Favreau, D. Filoni, K. Kennedy, &amp; C. Wilson (Executive Producers), {OPEN_EM}The Mandalorian{CLOSE_EM}. Lucasfilm; Golem Creations",
    ),

    param(
        'sherman-palladino_a_writer__director_all_2018',
        f"Sherman-Palladino, A. (Writer &amp; Director). (2018, December 5). All alone (Season 2, Episode 10) [TV series episode]. In A. Sherman-Palladino, D. Filoni, D. Palladino, D. Gilbert, M. Shapiro, S. Carino, &amp; S. Lawrence (Executive Producers), {OPEN_EM}The marvelous Mrs. Maisel{CLOSE_EM}. Dorothy Parker Drank Here Productions; Picrow; Amazon Studios",
    ),
    param(
        'castle_shadowing_nodate',
        f'Castle, R. (in press). Shadowing a police officer: How to be unobtrusive while solving cases in spectacular fashion. {OPEN_EM}Professional Writers’ Journal{CLOSE_EM}',
    ),
    param(
        'smith_language_nodate',
        f'Smith, J. M., &amp; Davis, H. (in press). Language acquisition among autistic children. {OPEN_EM}Journal of Developmental Psychology{CLOSE_EM}'
    ),
]

@mark.parametrize("recordKey, expectedRes", edgeCases_testData)
def test_edgeCases(recordKey, expectedRes):
    biblioDB = [edgeCases[recordKey]]
    templateStr = generateBibliography(biblioDB)
    assert templateStr == f'{MARKUP_START}{expectedRes}{MARKUP_END}'

@mark.parametrize("recordKey, expectedRes", apa7_testData)
def test_APAreferences(recordKey, expectedRes):
    biblioDB = [apa7[recordKey]]
    templateStr = generateBibliography(biblioDB)
    assert templateStr == f'{MARKUP_START}{expectedRes}{MARKUP_END}'


processTitle_testData = [
    param(
        'mcdaniel_science_2018',
        'The science of teamwork [Special issue]'
    ),
    param(
        'cuellar_study_2016',
        'Study Abroad Programs [Editorial]'
    ),
    param(
        'santos_reframing_2019',
        'Reframing refugee children’s stories [Review of the book *We are displaced: My journey and stories from refugee girls around the world*, by M. Yousafzai]'
    ),
    param(
        'the_new_york_public_library_nypl_raven_nodate',
        'The Raven'
    ),
    param(
        'ks_in_nj_this_2019',
        'From this article, it sounds like men are figuring something out that women have known forever. I know of many [Comment on the article *How workout buddies can help stave off loneliness*]'
    )
]

@mark.parametrize("recordKey, expectedRes", processTitle_testData)
def test_processTitle(recordKey, expectedRes):
    record = bibRawSource[recordKey]
    assert processTitle(record) == expectedRes


nth_testData = [
    param('0th', '0'),
    param('1st', '1'),
    param('2nd', '2'),
    param('3rd', '3'),
    param('4th', '4'),
    param('5th', '5'),
    param('6th', '6'),
    param('7th', '7'),
    param('8th', '8'),
    param('9th', '9'),
    param('10th', '10'),
    param('11th', '11'),
    param('12th', '12'),
    param('13th', '13'),
    param('14th', '14'),
    param('15th', '15'),
    param('16th', '16'),
    param('17th', '17'),
    param('18th', '18'),
    param('19th', '19'),
    param('20th', '20'),
    param('30th', '30'),
    param('40th', '40'),
    param('50th', '50'),
    param('60th', '60'),
    param('70th', '70'),
    param('80th', '80'),
    param('90th', '90')
]

@mark.parametrize("expectedRes, number", nth_testData)
def test_nth(expectedRes, number):
    assert expectedRes == nth(number)


processName_testData = [
    param('Sherman-Palladino, A. (Writer \\& Director)', 'sherman-palladino_a_writer__director_all_2018', 'author'),
    param('King, M. L. jr', 'king_i_1963', 'editora'),
    param('Beethoven, L. van', 'beethoven_symphony_2012', 'editora'),
    param('McCauley, S. M., & Christiansen, M. H.', 'mccauley_language_2019', 'author'),
    param('Tafoya, N., & Del Vecchio, A.', 'tafoya_back_2005', 'author'),
    param('Goldberg, J. F.', 'goldberg_evaluating_2018', 'author'),
    param('de Beauvoir, S.', 'de_beauvoir_simone_1960', 'editora'),
    param('Schmid, H.-J.', 'schmid_entrenchment_2017', 'editor')
]

@mark.parametrize("expectedRes, recordKey, field", processName_testData)
def test_processName(recordKey, field, expectedRes):
    record = bibRawSource[recordKey]
    prettyAuthors, multipleAuthors = processNames(record, fieldName=field)
    assert prettyAuthors == expectedRes


parseDate_testData = [
    param({'start': {'year': '2017', 'month': 'July', 'day': '12'},
           'end':   {'year': '2017', 'month': 'July', 'day': '15'}},
          'fistek_everybodys_nodate',
          'note'),
    param({'year': '2010'},    # (original date 1900)
          'freud_interpretation_2010',
          'date'),
    param({'year': '2017', 'month': 'December', 'day': '4'},
          'guarino_how_2017',
          'date'),
    param({'year': '2017', 'month': 'January'},
          'weir_forgiveness_2017',
          'date'),
    param({'year': '2019', 'month': 'January', 'day': '13'},
          'noauthor_list_2019',
          'date'),
    param({'year': '2019', 'month': 'January', 'day': '3'},
          'avramova_secret_2019',
          'date')
]

@mark.parametrize("expectedRes, recordKey, field", parseDate_testData)
def test_parseDate(expectedRes, recordKey, field):
    record = bibRawSource[recordKey]
    if '/' in record[field]:
        start, end = record[field].split('/')
        assert expectedRes == {'start': parseDate(start), 'end': parseDate(end)}
    else:
        assert parseDate(record[field]) == expectedRes
