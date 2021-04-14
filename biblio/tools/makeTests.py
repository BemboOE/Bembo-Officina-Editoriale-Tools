#!/usr/bin/env python3
# coding: utf-8

# ------------ #
# Script title #
# ------------ #

# -- Modules -- #
import json

# -- Constants -- #

# -- Objects, Functions, Procedures -- #

# -- Variables -- #

# -- Instructions -- #
if __name__ == '__main__':
    with open('../tests/articles.json', mode='r', encoding='utf-8') as jsonFile:
        articlesDB = json.loads(jsonFile.read())

    for articleID, eachArticle in articlesDB.items():
        funcStr = f"""def test_{articleID}():
    biblioDB = {{'{articleID}': {eachArticle}}}
    templateStr = generateBibliography(biblioDB)
    expectedRes = ""
    assert templateStr == expectedRes\n\n"""
        print(funcStr)