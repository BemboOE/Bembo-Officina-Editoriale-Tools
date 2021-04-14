#!/usr/bin/env python3
# coding: utf-8

# ------------------------- #
# Render Bembo Bibliography #
# ------------------------- #

# --- Modules --- #
# std library
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import windowed
from collections import namedtuple

# --- Constants --- #
TEMPLATES_FOLDER = Path(__file__).parent.absolute() / 'templates'
RichChar = namedtuple('RichChar', ['chr', 'tags'])

# --- Jinja Filters --- #
def parseTitle(txt):
    # expand txt in rich txt
    richTxt = []
    delimiters = set()
    for eachChar in txt:
        if eachChar == '*':
            delimiters.remove('*') if '*' in delimiters else delimiters.add('*')
            # asterisk should not figure in the final string
            continue
        elif eachChar == '[':
            delimiters.add('[')
        richTxt.append(RichChar(chr=eachChar, tags=set(delimiters)))

        # in this way ] is kept with the right delimiter
        if eachChar == ']':
            delimiters.remove('[')

    # regroup runs
    runs = []
    thisRun = {'chrs': [], 'tags': set()}
    for thisChr, nextChr in windowed(richTxt, 2):

        thisRun['chrs'].append(thisChr.chr)
        thisRun['tags'].update(thisChr.tags)
        if thisChr.tags != nextChr.tags:
            thisRun['chrs'] = ''.join(thisRun['chrs'])
            runs.append(thisRun)
            thisRun = {'chrs': [], 'tags': set()}

    thisRun['chrs'].append(nextChr.chr)
    thisRun['tags'].update(nextChr.tags)
    thisRun['chrs'] = ''.join(thisRun['chrs'])
    runs.append(thisRun)

    return runs

def nth(numberTxt):
    if numberTxt.isdigit():
        nn = int(numberTxt)
        """from http://www.rosettacode.org/wiki/N%27th#Python"""
        suffixes = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
        return "%i%s" % (nn, suffixes[nn % 10] if nn % 100 <= 10 or nn % 100 > 20 else 'th')
    return numberTxt

# --- Methods --- #
def generateBibliography(biblioDB):
    biblioEnv = Environment(loader=FileSystemLoader(TEMPLATES_FOLDER),
                            autoescape=select_autoescape(['xml', 'html']),
                            extensions=['jinja2.ext.do'])
    biblioEnv.filters['nth'] = nth
    biblioEnv.filters['parseTitle'] = parseTitle
    biblioTemplate = biblioEnv.get_template('bibliography.xml.j2')
    biblioStr = biblioTemplate.render(bibliography=biblioDB,
                                      trim_blocks=True,
                                      lstrip_blocks=True)
    return biblioStr


if __name__ == '__main__':
    testsFolder = Path('tests')

    for eachJsonPath in [pp for pp in testsFolder.iterdir() if pp.suffix == '.json']:
        with open(eachJsonPath, mode='r', encoding='utf-8') as jsonFile:
            biblioDB = json.loads(jsonFile.read())
        records = [rec for (_id, rec) in biblioDB.items()]
        biblioXML = generateBibliography(records)
        with open(eachJsonPath.with_suffix('.xml'), mode='w', encoding='utf-8') as xmlFile:
            xmlFile.write(biblioXML)
