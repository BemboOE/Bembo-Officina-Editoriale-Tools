#!/usr/bin/env python3
# coding: utf-8

# ------------------------ #
# Parsing Markdown Sources #
# ------------------------ #

# --- Modules --- #
# std library
from html.parser import HTMLParser
from pathlib import Path
from html import escape

# --- Constants --- #
TEMPLATES_FOLDER = Path('templates')

BLOCK_STYLES = set(['ol', 'p', 'code', 'ul', 'h1', 'li', 'h2', 'h3', 'blockquote', 'figcaption', 'img', 'figure'])
INLINE_STYLES = set(['em', 'strong', 'a', 'span', 'sup'])

TAG_2_STYLE = {
    'p': 'testo',
    'code': 'autore e affiliazione',
    'blockquote': None,
    'h1': 'h1',
    'h2': 'h2',
    'h3': 'h3',
    'a': 'span',
    'em': 'corsivo',
    'ul': 'ul',
    'li': None,
}

CLASSNAME_2_STYLENAME = {
    'abstract': 'testo, primo paragrafo',
    'attribuzioni': 'testo, primo paragrafo',
    'keywords': 'keywords',
}

REPLACEMENTS = [
    # (old vs new)
    ('<blockquote>\n<p', '<blockquote><p',),
    ('</p>\n</blockquote>', '</p></blockquote>'),

    ('<p aid:pstyle="testo, primo paragrafo"><code aid:pstyle="autore e affiliazione">', '<code aid:pstyle="autore e affiliazione">'),
    ('<code aid:pstyle="autore e affiliazione">\n', '\n<code aid:pstyle="autore e affiliazione">'),
    ('\n</code>', '</code>'),
    ('</code></p>', '</code>'),

    ('<p aid:pstyle="abstract">\n', '<p aid:pstyle="abstract">'),
    ('<p aid:pstyle="keywords">\n', '<p aid:pstyle="keywords">'),

    ('\n\n\n\n', '\n'),
    ('\n\n\n', '\n'),
    ('\n\n', '\n'),
    ('\n</p>', '</p>'),
]

# --- Objects & Methods --- #
def runReplacements(txt):
    for old, new in REPLACEMENTS:
        txt = txt.replace(old, new)
    return txt

class MarkdownParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.openTags = []
        self.xml = []
        self.prevTag = None
        self.prevContent = None

    def handle_starttag(self, tag, attrs):
        self.openTags.append(tag)
        styleName = TAG_2_STYLE[tag] if tag in TAG_2_STYLE else None

        if tag in BLOCK_STYLES:
            # images
            if tag == 'img':
                attrsDict = {kk: vv for (kk, vv) in attrs}
                src = attrsDict['src'].replace('../', '', 1)
                figcaption = attrsDict['alt'] if 'alt' in attrsDict else ''
                xmlTag = f'<Image href="File:///{src}"></Image><p aid:pstyle="figcaption">{figcaption}</p>'

            # text styles
            else:
                if tag == 'p':
                    # abstract, attributions, keywords
                    if attrs:
                        attrName, attrValue = attrs[0]
                        assert attrName == 'class', f'the following attribute is not supported: {attrName}'
                        styleName = CLASSNAME_2_STYLENAME[attrValue]
                    # blockquote
                    elif len(self.openTags) > 1 and self.openTags[-2] == 'blockquote':
                        styleName = 'Citazione'
                    # handling two kinds of p
                    elif self.prevTag == tag:
                        styleName += ', a seguire'
                    else:
                        styleName += ', primo paragrafo'

                # handling lists
                elif tag == 'ol' and self.prevTag == tag:
                    styleName += '2'

                # handling li inside ol and ul
                elif tag == 'li':
                    styleName = 'ul1' if len(self.openTags) > 1 and self.openTags[-2] == 'ul' else 'ol1'

                xmlTag = f'<{tag} aid:pstyle="{styleName}">' if styleName else f'<{tag}>'
            self.xml.append(xmlTag)

        elif tag in INLINE_STYLES:
            xmlTag = f'<{tag} aid:cstyle="{styleName}">' if styleName else f'<{tag}>'
            self.xml.append(xmlTag)

        else:
            print(f'missing tag: {tag}')
            raise Exception

    def handle_endtag(self, tag):
        if self.openTags:
            self.openTags.pop()
        self.xml.append(f'</{tag}>')
        self.prevTag = tag

    def handle_data(self, data):
        self.xml.append(escape(data))
        self.prevContent = data

    def getXML(self):
        return runReplacements("".join(self.xml))


def read(aPath):
    with open(aPath) as txtFile:
        return txtFile.read()

def chainMarkdownStrings(txtFolder):
    portions = []

    # colophon
    portions.append(read(txtFolder / 'colophon.md'))

    # chapters
    markdownPaths = list((txtFolder / 'chapters').glob('*.md'))
    markdownPaths.sort()
    for markdownPath in markdownPaths:
        portions.append(read(markdownPath))

    gluedPath = txtFolder / 'gluedMarkdown.md'
    with open(gluedPath, 'w', encoding='utf-8') as gluedFile:
        gluedFile.write('\n'.join(portions))

    return gluedPath
