#!/usr/bin/env python3
# coding: utf-8

# ---------------- #
# Build Bembo Docs #
# ---------------- #

# --- Modules --- #
import gspread
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from renderBibliography import nth, parseTitle

# --- Constants --- #
TEMPLATES_FOLDER = Path('templates')
DOCS_FOLDER = Path('docs')
TESTS_FOLDER = Path('tests')

CLIENT = gspread.service_account(filename='.config/gspread/service_account.json')

# --- Objects & Methods --- #
def loadSingleRefTemplate():
    env = Environment(loader=FileSystemLoader(TEMPLATES_FOLDER),
                               autoescape=select_autoescape(['html']),
                               extensions=['jinja2.ext.do'])
    env.filters['nth'] = nth
    env.filters['parseTitle'] = parseTitle
    template = env.get_template('singleReference.j2')
    return template

def loadDocsTemplate():
    env = Environment(loader=FileSystemLoader(TEMPLATES_FOLDER),
                               autoescape=select_autoescape(['html']),
                               extensions=['jinja2.ext.do'])
    env.filters['nth'] = nth
    env.filters['parseTitle'] = parseTitle
    template = env.get_template('docs.html.j2')
    return template

def buildDocs():
    singleReferenceTemplate = loadSingleRefTemplate()
    docsTemplate = loadDocsTemplate()

    # extract data from spreadsheet
    # {'Test': '', 'APA category': 'APA CASUSTOM EDGE CASES', 'APA prototype': '', 'entry ID': '', 'Zotero item type': '', 'Required fields': '', 'Optional fields': '', 'Notes': ''}
    table = CLIENT.open("Documentazione References Prototypes").sheet1.get_all_records()

    # build ref strings
    with open(TESTS_FOLDER / 'apa7.json', mode='r', encoding='utf-8') as jsonFile:
        apa7 = json.loads(jsonFile.read())

    with open(TESTS_FOLDER / 'edgeCases.json', mode='r', encoding='utf-8') as jsonFile:
        edgeCases = json.loads(jsonFile.read())

    for eachKey, record in {**apa7, **edgeCases}.items():
        reference = singleReferenceTemplate.render(record=record,
                                                   isHtml=True,
                                                   trim_blocks=True,
                                                   lstrip_blocks=True)
        for eachRow in table:
            if eachRow['entry ID'] == eachKey:
                eachRow['Reference'] = reference
                break

    docsStr = docsTemplate.render(table=table)
    with open(DOCS_FOLDER / 'README.md', mode='w', encoding='utf-8') as htmlFile:
        htmlFile.write(docsStr)


# --- Instructions --- #
if __name__ == '__main__':
    buildDocs()
