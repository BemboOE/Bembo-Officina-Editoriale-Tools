#!/usr/bin/env python3
# coding: utf-8

# --------------------- #
# From BibLatex to JSON #
# --------------------- #

# --- Modules --- #
# std library
import re
from string import ascii_lowercase
from operator import itemgetter
from pathlib import Path
import json
from collections import OrderedDict

# external dependencies
from more_itertools import windowed
import biblib.bib
from biblib.algo import tex_to_unicode, Name
from biblib.messages import InputError

# --- Constants --- #
TO_SKIP = ['langid', 'file', 'abstract', 'issn', 'isbn']

# when doi is in extra is automatically extracted by biblib
NOTE_ATTRS = {
    'medium':           r'[{]{0,1}[Mm]{1}edium[}]{0,1}',
    'type':             r'[{]{0,1}[Tt]{1}ype[}]{0,1}',
    'event':            r'[{]{0,1}[Ee]{1}vent[}]{0,1}',
    'originalDate':     r'[{]{0,1}[Oo]{1}riginal [Dd]{1}ate[}]{0,1}',
    'wordsBy':          r'[{]{0,1}[wW]{1}ords[bB]{1}y[}]{0,1}[}]{0,1}',
    'collectionTitle':  r'[{]{0,1}[cC]{1}ollection[- ]{1}[tT]{1}itle[}]{0,1}',
    'collectionNumber': r'[{]{0,1}[cC]{1}ollection[- ]{1}[nN]{1}umber[}]{0,1}',
    'issued':           r'[{]{0,1}[iI]{1}ssued[}]{0,1}',
    'version':          r'[{]{0,1}[vV]{1}ersion[}]{0,1}',
}

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# --- Objects & Methods --- #
def processTitle(entry):
    """from biblib/examples/bibparse"""
    title = tex_to_unicode(entry['title'],
                           pos=entry.field_pos['title'])
    return title.rstrip('.')

def collectFirstNameAbbreviations(author, separator):
    return ', ' + separator.join([f'{nn[0]}.' for nn in author.first.split(separator)]) if author.first else ''

def tex_to_apa(author, isStraight=False):
    # Ludwig van Beethoven's case
    van = ' van' if author.first.endswith(' van') else ''
    if author.first.endswith(' van'):
        author = Name(first=author.first.replace(' van', ''), von=author.von, last=author.last, jr=author.jr)

    # double names divided by hyphen, like "Hans-Jörg"
    if '-' in author.first:
        firstAbbrs = collectFirstNameAbbreviations(author, separator='-')
    else:
        firstAbbrs = collectFirstNameAbbreviations(author, separator=' ')
    von = f'{author.von} ' if author.von else ''
    jr = f' {author.jr}' if author.jr else ''
    # it doesn't look like, but this takes organizations into account
    if isStraight is False:
        return f'{von}{author.last}{firstAbbrs}{van}{jr}'.replace('{', '').replace('}', '')
    else:
        return f'{firstAbbrs.lstrip(", ")}{van} {von}{author.last}{jr}'.replace('{', '').replace('}', '')

def processNames(entry, fieldName='author', isStraight=False):
    """from biblib/examples/bibparse"""
    names = [tex_to_apa(author, isStraight) for author in entry.authors(field=fieldName) if not author.is_others()]

    if len(names) == 0:
        return None, None
    elif len(names) == 1:
        return names[0], False
    elif len(names) > 21:
        name = ', '.join(names[:19])
        name += ', … '
        name += names[-1]
    else:
        name = ', '.join(names[:-1])
        if fieldName == 'author' and entry.authors()[-1].is_others():
            name += ' et al.'
        else:
            name += ', & ' + names[-1]

    return name, True

def makeSortingString(record):
    if 'author' in record:
        author = record['author'].split(',')[0]
    elif 'editor' in record:
        author = record['editor'].split(',')[0]
    else:
        author = ''
    title = '' if 'title' not in record else record['title']
    year = '' if 'date' not in record else record['date']['year']
    return f'{author}{year}{title}'


def addLettersToDates(bibliography):
    """
    example:
    0    einstein, 1912a
    1    einstein, 1912

    1    einstein, 1912b
    2    einstein, 1912

    2    einstein, 1912c
    3    einstein, 1912

    3    einstein, 1912d
    4    schrodinger, 1920
    """
    count = 0
    tail = False
    for thisRecord, nextRecord in windowed(bibliography, 2):
        if 'author' in thisRecord and 'author' in nextRecord and 'date' in thisRecord and 'date' in nextRecord:
            if thisRecord['date'] != 'n.d.' and nextRecord['date'] != 'n.d.':
                if thisRecord['author'] == nextRecord['author']:
                    if thisRecord['date'] == nextRecord['date']:
                        thisRecord['date']['year'] += ascii_lowercase[count]
                        thisRecord['sortingStr'] = makeSortingString(thisRecord)
                        count += 1
                        tail = True
                        continue

        if tail is True:
            thisRecord['date']['year'] += ascii_lowercase[count]
            thisRecord['sortingStr'] = makeSortingString(thisRecord)
            tail = False

def parseDate(txt):
    pattern = r'(\d{4})-{0,1}(\d{0,2})-{0,1}(\d{0,2})'
    match = re.search(pattern, txt)
    if match:
        yearTxt, monthTxt, dayTxt = match.group(1), match.group(2), match.group(3)
        dateObj = {'year': '' if not yearTxt else f'{int(yearTxt)}'}
        if monthTxt:
            dateObj['month'] = MONTHS[int(monthTxt)-1]
        if dayTxt:
            dateObj['day'] = f'{int(dayTxt)}'
        return dateObj
    raise ValueError('this date cannot be parsed')

def sortBibliography(jsonDB):
    bibliography = []
    for key, value in jsonDB.items():
        record = dict(value)
        record['id'] = key
        record['sortingStr'] = makeSortingString(record)
        bibliography.append(record)
    bibliography.sort(key=itemgetter('sortingStr'))
    addLettersToDates(bibliography)
    return {bb['id']: bb for bb in bibliography}

def fromBIBtoJSON(bibPath):
    with open(bibPath, mode='r', encoding='utf-8') as bibFile:
        bibDB = biblib.bib.Parser().parse(bibFile).get_entries()

    prettyDB = OrderedDict()
    for entryID, eachEntry in bibDB.items():
        prettyDB[entryID] = {}
        prettyDB[entryID]['bibType'] = eachEntry.typ

        for attr, value in eachEntry.items():
            if attr == 'title':
                prettyTitle = processTitle(eachEntry)
                prettyDB[entryID]['title'] = prettyTitle
            elif attr == 'author':
                prettyAuthors, multipleAuthors = processNames(eachEntry)
                prettyDB[entryID]['author'] = prettyAuthors
                prettyDB[entryID]['multipleAuthors'] = multipleAuthors
            elif attr in ['editor', 'translator', 'editora']:
                prettyEditors, multipleEditors = processNames(eachEntry, fieldName=attr)
                straightEditors, _ = processNames(eachEntry, fieldName=attr, isStraight=True)
                prettyDB[entryID][attr] = prettyEditors
                prettyDB[entryID][f'multiple{attr.title()}'] = multipleEditors
                prettyDB[entryID][f'{attr}Straight'] = straightEditors
            elif attr in ['date', 'urldate']:
                dateObj = parseDate(value)
                prettyDB[entryID][attr] = dateObj
            elif attr == 'note':
                for eachKey, eachNoteAttr in NOTE_ATTRS.items():
                    pattern = re.compile(eachNoteAttr + r': "(.*?)"')
                    match = re.search(pattern, value)
                    if match:
                        captured = match.group(1).strip().replace('{', '').replace('}', '')
                        if eachKey == 'issued' and '/' in captured:
                            start, end = captured.split('/')
                            result = {'start': parseDate(start), 'end': parseDate(end)}
                        else:
                            result = captured.strip('"')

                        prettyDB[entryID][eachKey] = result
                        value = value.replace(match.group(0), '')
            else:
                if 'journaltitle' in eachEntry and attr == 'journaltitle':
                    prettyDB[entryID][attr] = tex_to_unicode(value).rstrip('.')
                elif attr not in TO_SKIP:
                    # this is definitely an hack
                    # but I can't parse with biblib underscores _
                    # and hash # chars 🤷‍♂️
                    try:
                        prettyDB[entryID][attr] = tex_to_unicode(value)
                    except InputError:
                        prettyDB[entryID][attr] = value

    sortedDB = sortBibliography(prettyDB)
    with open(bibPath.with_suffix('.json'), mode='w', encoding='utf-8') as jsonFile:
        jsonFile.write(json.dumps(sortedDB, sort_keys=False, indent=4))


# --- Instructions --- #
if __name__ == '__main__':
    testsFolder = Path('tests')
    for eachBibPath in [pp for pp in testsFolder.iterdir() if pp.suffix == '.bib']:
        fromBIBtoJSON(eachBibPath)
