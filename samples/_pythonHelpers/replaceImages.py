#!/usr/bin/env python3
# coding: utf-8

# ------------------------------ #
# REPLACE JPGS WITH PLACEHOLDERS #
# ------------------------------ #

# --- Modules --- #
from pathlib import Path
import drawBot as dB

# --- Constants --- #

# --- Objects & Methods --- #
def createPlaceholder(wdt, hgt, locationOnDisk):
    dB.newDrawing()
    dB.newPage(wdt, hgt)

    dB.fill(.5)
    dB.rect(0, 0, dB.width(), dB.height())

    dB.stroke(1)
    dB.strokeWidth(10)

    dB.line((0, 0), (dB.width(), dB.height()))
    dB.line((0, dB.height()), (dB.width(), 0))
    dB.saveImage(f'{locationOnDisk}')
    dB.endDrawing()


# --- Variables --- #

# --- Instructions --- #
if __name__ == '__main__':
    root_directory = Path(".")
    for eachJPG in root_directory.glob('**/*.jpg'):
        print(f"hi, I'm a file: {eachJPG}")
        wdt, hgt = dB.imageSize(f'{eachJPG}')

        createPlaceholder(wdt, hgt, eachJPG)
