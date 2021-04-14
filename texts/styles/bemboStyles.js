var regularPointSize = 11.8
var smallerPointSize = 10.5
var lineHeight = 13.2

paragraphStylesData = {
    // START SOMMARIO
    'titolo numero capitolo (sommario)': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'tracking': 25,
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'leftIndent': (lineHeight*5) + 'pt',
        'spaceAfter': '0 pt',
        'hyphenation': false,
        'keepLinesTogether': true,
        'keepAllLinesTogether': true,
        'keepWithPrevious': true,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'numero di pagina (sommario)': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'leftIndent': (lineHeight * 3) + 'pt',
        'firstLineIndent': (-lineHeight * 3) + ' pt',
        'hyphenation': false,
        'keepLinesTogether': true,
        'keepAllLinesTogether': true,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'autore affiliazione (sommario)': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Italic',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepWithPrevious': true,
        'spaceAfter': lineHeight
    },
    'sommario': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'tracking': 25,
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'hyphenation': false,
        'keepLinesTogether': true,
        'leftIndent': (lineHeight * 3) + 'pt',
        'spaceAfter': lineHeight + 'pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'keepWithNext': 1,
        'capitalization': Capitalization.ALL_CAPS,
    },
    // END SOMMARIO

    'ol1': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'firstLineIndent': '-28 pt',
        'tabList': [
            {'alignment' : TabStopAlignment.LEFT_ALIGN, 'position' : "28 pt"},
        ],
        'spaceAfter': lineHeight + 'pt',
        'leftIndent': '28 pt',
        'spaceBefore': lineHeight + 'pt',
        'rightIndent': lineHeight + 'pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'hyphenation': false,
        'bulletsAndNumberingListType': ListType.NUMBERED_LIST,
        'bulletsAlignment': ListAlignment.LEFT_ALIGN,
        'bulletsTextAfter': '\t',
        'numberingLevel': 3,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'ol2': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'firstLineIndent': '-28 pt',
        'tabList': [
            {'alignment' : TabStopAlignment.LEFT_ALIGN, 'position' : "28 pt"},
        ],
        'spaceAfter': lineHeight + 'pt',
        'leftIndent': (lineHeight * 3) + 'pt',
        'spaceBefore': lineHeight + 'pt',
        'rightIndent': lineHeight + 'pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'hyphenation': false,
        'bulletsAndNumberingListType': ListType.NUMBERED_LIST,
        'bulletsAlignment': ListAlignment.LEFT_ALIGN,
        'bulletsTextAfter': '\t',
        'numberingLevel': 2,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'ul2': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'firstLineIndent': '-28 pt',
        'tabList': [
            {'alignment' : TabStopAlignment.LEFT_ALIGN, 'position' : "28 pt"},
        ],
        'spaceAfter': lineHeight + 'pt',
        'leftIndent': (lineHeight * 3) + 'pt',
        'spaceBefore': lineHeight + 'pt',
        'rightIndent': lineHeight + 'pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'hyphenation': false,
        'bulletsAndNumberingListType': ListType.BULLET_LIST,
        'bulletsAlignment': ListAlignment.LEFT_ALIGN,
        'bulletsTextAfter': '\t',
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'ul1': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'firstLineIndent': '-28 pt',
        'tabList': [
            {'alignment' : TabStopAlignment.LEFT_ALIGN, 'position' : "28 pt"},
        ],
        'spaceAfter': lineHeight + 'pt',
        'leftIndent': '28 pt',
        'spaceBefore': lineHeight + 'pt',
        'rightIndent': lineHeight + 'pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'hyphenation': false,
        'bulletsAndNumberingListType': ListType.BULLET_LIST,
        'bulletsAlignment': ListAlignment.LEFT_ALIGN,
        'bulletsTextAfter': '\t',
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'h1': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': '32 pt',
        'leading': '52.8 pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'spaceAfter': (lineHeight * 3) + 'pt',
        'hyphenation': false,
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'h2': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': '16 pt',
        'leading': '26.4 pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'hyphenation': false,
        'spaceAfter': (lineHeight * 3) + 'pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'h3': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'tracking': 25,
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'leftIndent': '28 pt',
        'spaceBefore': '26.4 pt',
        'spaceAfter': lineHeight + 'pt',
        'hyphenation': false,
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'testo, primo paragrafo': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'spaceAfter': '0 pt',
        'spaceBefore': '0 pt',
        'hyphenation': true,
        'hyphenateWordsLongerThan': 6,
        'hyphenateAfterFirst': 4,
        'hyphenateBeforeLast': 2,
        'hyphenateLadderLimit': 2,
        'hyphenationZone': (lineHeight * 3) + 'pt',
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'testo, a seguire': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'firstLineIndent': lineHeight + 'pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'hyphenation': true,
        'hyphenateWordsLongerThan': 6,
        'hyphenateAfterFirst': 4,
        'hyphenateBeforeLast': 2,
        'hyphenateLadderLimit': 2,
        'hyphenationZone': (lineHeight * 3) + 'pt',
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'testo, primo paragrafo - riga per riga': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'composer': "$ID/HL Single",
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'spaceAfter': '0 pt',
        'spaceBefore': '0 pt',
        'hyphenation': true,
        'hyphenateWordsLongerThan': 6,
        'hyphenateAfterFirst': 4,
        'hyphenateBeforeLast': 2,
        'hyphenateLadderLimit': 2,
        'hyphenationZone': (lineHeight * 3) + 'pt',
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'testo, a seguire - riga per riga': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'composer': "$ID/HL Single",
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'firstLineIndent': lineHeight + 'pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'hyphenation': true,
        'hyphenateWordsLongerThan': 6,
        'hyphenateAfterFirst': 4,
        'hyphenateBeforeLast': 2,
        'hyphenateLadderLimit': 2,
        'hyphenationZone': (lineHeight * 3) + 'pt',
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'keywords': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Italic',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepWithPrevious': true,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'hyphenation': true,
        'hyphenateWordsLongerThan': 6,
        'hyphenateAfterFirst': 4,
        'hyphenateBeforeLast': 2,
        'hyphenateLadderLimit': 2,
        'hyphenationZone': (lineHeight * 3) + 'pt',
        'spaceBefore': '26.4 pt',
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'colophon': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': '9.4 pt',
        'leading': '10.56 pt',
        'appliedLanguage': "Italiano",
        'justification': Justification.LEFT_ALIGN,
        'spaceBefore': '0 pt',
        'spaceAfter': '0 pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'hyphenation': true,
        'hyphenateWordsLongerThan': 6,
        'hyphenateAfterFirst': 4,
        'hyphenateBeforeLast': 2,
        'hyphenateLadderLimit': 2,
        'hyphenationZone': (lineHeight * 3) + 'pt',
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'note': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'hyphenation': true,
        'hyphenateWordsLongerThan': 6,
        'hyphenateAfterFirst': 4,
        'hyphenateBeforeLast': 2,
        'hyphenateLadderLimit': 2,
        'hyphenationZone': (lineHeight * 3) + 'pt',
        'bulletsAndNumberingListType': ListType.NUMBERED_LIST,
        'bulletsAlignment': ListAlignment.LEFT_ALIGN,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'autore e affiliazione': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Italic',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'sameParaStyleSpacing': '0 pt',
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'spaceAfter': '26.4 pt',
        'leftIndent': '56.5 pt',
        'hyphenation': false,
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'citazione': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': smallerPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'spaceBefore': lineHeight + 'pt',
        'spaceAfter': lineHeight + 'pt',
        'leftIndent': '56.5 pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'hyphenation': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'voce (bibliografia)': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': smallerPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'firstLineIndent': (-lineHeight * 3) + ' pt',
        'leftIndent': (lineHeight * 3) + 'pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': true,
        'hyphenation': true,
        'hyphenateWordsLongerThan': 6,
        'hyphenateAfterFirst': 4,
        'hyphenateBeforeLast': 2,
        'hyphenateLadderLimit': 2,
        'hyphenationZone': (lineHeight * 3) + 'pt',
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'titolo (bibliografia)': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Medium',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'startParagraph': StartParagraph.NEXT_FRAME,
        'appliedLanguage': "Italiano",
        'gridAlignment': GridAlignment.ALIGN_BASELINE,
        'justification': Justification.LEFT_ALIGN,
        'firstLineIndent': (-lineHeight * 3) + ' pt',
        'spaceAfter': lineHeight + 'pt',
        'leftIndent': (lineHeight * 3) + 'pt',
        'spaceBefore': '26.4 pt',
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'hyphenation': false,
        'otfFigureStyle': OTFFigureStyle.DEFAULT_VALUE,
    },
    'didascalia': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': '8.8 pt',
        'leading': '9.9 pt',
        'appliedLanguage': "Italiano",
        'gridAlignFirstLineOnly': true,
        'justification': Justification.LEFT_ALIGN,
        'keepLinesTogether': true,
        'keepAllLinesTogether': false,
        'hyphenation': false,
        'keepFirstLines': 2,
        'keepLastLines': 2,
        'otfFigureStyle': OTFFigureStyle.TABULAR_LINING,
    },
    'numeri di pagina': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Light',
        'pointSize': '35.4 pt',
        'leading': '39.6 pt',
        'hyphenation': false,
        'justification': Justification.LEFT_ALIGN,
        'otfFigureStyle': OTFFigureStyle.PROPORTIONAL_OLDSTYLE,
    },
}

characterStyles = {
    'numero rimando nota': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Regular',
        'pointSize': regularPointSize + 'pt',
        'leading': lineHeight + 'pt',
        'otfFigureStyle': OTFFigureStyle.PROPORTIONAL_LINING,
    },
    'corsivo': {
        'appliedFont': 'Cormorant',
        'fontStyle': 'Italic',
    },
}

// functions
function grabStyleOrGroup(attrName, obj) {
    try {
      return obj.add({"name": attrName});
    }
    catch(err) {
      return obj.itemByName(attrName);
    }
}

function populate(style, data) {
    for (var attrName in data) {
        style[attrName] = data[attrName];
    }
}

// instructions
var doc = app.activeDocument;

for (var sourceKey in paragraphStylesData) {
    var sourceValue = paragraphStylesData[sourceKey]
    var indd_pStyle = grabStyleOrGroup(sourceKey, doc.paragraphStyles)
    populate(indd_pStyle, sourceValue)
}

for (var sourceStyleName in characterStyles) {
    var sourceCStyle = characterStyles[sourceStyleName];
    var indd_cStyle = grabStyleOrGroup(sourceStyleName, doc.characterStyles)
    populate(indd_cStyle, sourceCStyle)
}