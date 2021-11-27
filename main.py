#! /usr/bin/python

import os
import sys
from traceback import print_list, print_stack, print_tb

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


def printFontDictory(filename):
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
        if entry.langID == 0:
            continue

        encoding = (
            "utf_16_be"
            if entry.platformID == 3 and entry.platEncID in [1, 10]
            else "ascii"
        )

        print("----------------------------------------")
        print(f"nameID: {entry.nameID}, {getName(entry.nameID)}")
        print("----------------------------------------")
        if encoding == "utf_16_be":
            print(f"string: {entry.string.decode(encoding)}")
        else:
            print(f"string: {entry.string}")
        print(f"platformID: {entry.platformID}")
        print(f"platEncID: {entry.platEncID}")
        print(f"langID: {entry.langID}")

    font.close()


def main():
    workspace = os.environ.get("GITHUB_WORKSPACE") or os.path.abspath(__file__).replace(
        "/main.py", ""
    )

    for file in os.listdir(os.fsencode(workspace)):
        filename = os.fsdecode(file)
        if filename.endswith(".ttf") or filename.endswith(".otf"):
            if len(sys.argv) == 1:
                printsFontInfo(filename)
            else:
                printFontDictory(filename)


if __name__ == "__main__":
    main()
