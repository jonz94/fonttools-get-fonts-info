#! /usr/bin/python

import os
import sys
from pathlib import Path
from fontTools.ttLib import TTFont


def getName(nameID):
    return {
        0: "Copyright",
        1: "Family",
        2: "Styles (SubFamily)",
        3: "UniqueID",
        4: "Fullname",
        5: "Version",
        6: "Fontname",
        16: "Preferred Family",
        17: "Preferred Styles",
        18: "Compatible Full",
    }.get(nameID, "unknown")


def printFontDictionary(filename):
    font = TTFont(filename, recalcBBoxes=False)
    fontName = font["name"]

    for entry in fontName.names:
        nameID = entry.nameID
        platformID = entry.platformID
        platEncID = entry.platEncID
        langID = entry.langID

        if nameID == 0:
            continue

        key = f"{filename},{nameID},{platformID},{platEncID},{langID}"
        value = f"{entry.toUnicode()}"

        print(f'"{key}": "{value}"')

    font.close()


def printsFontInfo(filename):
    font = TTFont(filename, recalcBBoxes=False)
    fontName = font["name"]

    print("========================================")
    print(f"filename: {filename}")

    for entry in fontName.names:
        if entry.nameID == 0:
            continue

        print("----------------------------------------")
        print(f"nameID: {entry.nameID}, {getName(entry.nameID)}")
        print("----------------------------------------")
        print(f"string: {entry.toUnicode()}")
        print(f"platformID: {entry.platformID}")
        print(f"platEncID: {entry.platEncID}")
        print(f"langID: {entry.langID}")

    font.close()


def main():
    workspace = os.environ.get("GITHUB_WORKSPACE") or Path(__file__).parent

    for file in os.listdir(os.fsencode(workspace)):
        filename = os.fsdecode(file)
        if filename.endswith(".ttf") or filename.endswith(".otf"):
            if len(sys.argv) == 1:
                printsFontInfo(filename)
            else:
                printFontDictionary(filename)


if __name__ == "__main__":
    main()
