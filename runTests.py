#!/usr/bin/env python3

# ------------------------------------- #
# Create XML for test articles and book #
# ------------------------------------- #

# -- Modules -- #
from pathlib import Path
import subprocess
import json
from references.fromBibLatexToJSON import fromBIBtoJSON
from references.renderBibliography import generateBibliography
from body.parsing import MarkdownParser, glueArticle

# -- Constants -- #

# -- Objects, Functions, Procedures -- #
HEADER_XML = """<root xmlns:aid="http://ns.adobe.com/AdobeInDesign/4.0/" xmlns:aid5="http://ns.adobe.com/AdobeInDesign/5.0/">"""
FOOTER_XML = "</root>"

# -- Variables -- #
testsFolder = Path('tests')

# --- Instructions --- #
if __name__ == '__main__':
    # articles
    for eachArticleFolder in [ff for ff in (testsFolder / 'articles').iterdir() if ff.is_dir()]:
        gluedPath = glueArticle(eachArticleFolder)

        # body
        result = subprocess.run(f'hoedown --html --disable-intra-emphasis --superscript "{gluedPath}"',
                                shell=True, capture_output=True, text=True).stdout
        parser = MarkdownParser()
        parser.feed(result)

        # bibliography
        fromBIBtoJSON(eachArticleFolder / 'bibliography.bib')
        with open(eachArticleFolder / 'bibliography.json', mode='r', encoding='utf-8') as biblioJSON:
            biblioDB = json.loads(biblioJSON.read())
        records = [rec for (_id, rec) in biblioDB.items()]
        biblioXML = generateBibliography(records)

        with open(gluedPath.with_name('noParsing.html'), mode='w', encoding='utf-8') as noParsingHtmlFile:
            noParsingHtmlFile.write(result)

        with open(gluedPath.with_suffix('.xml'), mode='w', encoding='utf-8') as xmlFile:
            xmlFile.write(f'{HEADER_XML}{parser.getXML()}\n{biblioXML}{FOOTER_XML}')
