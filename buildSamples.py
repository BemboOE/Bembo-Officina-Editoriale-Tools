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
from body.parsing import MarkdownParser, chainMarkdownStrings


# -- Constants -- #
HEADER_XML = """<root xmlns:aid="http://ns.adobe.com/AdobeInDesign/4.0/" xmlns:aid5="http://ns.adobe.com/AdobeInDesign/5.0/">"""
FOOTER_XML = "</root>"


# -- Objects, Functions, Procedures -- #
def buildSamples(samplesFolder):
    markdownFolders = [ff for ff in (samplesFolder / 'articles').iterdir() if ff.is_dir()]
    markdownFolders.append(samplesFolder / 'book')
    for eachMarkdownFolder in markdownFolders:
        chainedPath = chainMarkdownStrings(eachMarkdownFolder)

        # body
        result = subprocess.run(f'hoedown --html --disable-intra-emphasis --superscript "{chainedPath}"',
                                shell=True, capture_output=True, text=True).stdout
        parser = MarkdownParser()
        parser.feed(result)

        # bibliography
        fromBIBtoJSON(eachMarkdownFolder / 'bibliography.bib')
        with open(eachMarkdownFolder / 'bibliography.json', mode='r', encoding='utf-8') as biblioJSON:
            biblioDB = json.loads(biblioJSON.read())
        records = [rec for (_id, rec) in biblioDB.items()]
        biblioXML = generateBibliography(records)

        with open(chainedPath.with_suffix('.xml'), mode='w', encoding='utf-8') as xmlFile:
            xmlFile.write(f'{HEADER_XML}{parser.getXML()}\n{biblioXML}{FOOTER_XML}')


# --- Instructions --- #
if __name__ == '__main__':
    samplesFolder = Path('samples')
    buildSamples(samplesFolder)
