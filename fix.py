#! /usr/bin/python

import os
from pathlib import Path
from fontTools.ttLib import TTFont


def fix(filename):
    font = TTFont(filename, recalcBBoxes=False)
    fontName = font["name"]

    originFontUniqueID = fontName.getName(3, 3, 1, 1033).toUnicode()

    for entry in fontName.names:
        nameID = entry.nameID
        platformID = entry.platformID
        platEncID = entry.platEncID
        langID = entry.langID

        if langID in [1028, 1041, 2052, 3076]:
            string = (
                entry.toUnicode()
                .replace(" CL", " CL Nerd Font")
                .replace(" TC", " TC Nerd Font")
                .replace(" J", " J Nerd Font")
                .replace(" SC", " SC Nerd Font")
                .replace(" HC", " HC Nerd Font")
            )
            fontName.setName(string, nameID, platformID, platEncID, langID)

        elif nameID in [1, 16]:
            style = fontName.getName(2, 3, 1, 1033).toUnicode()
            string = originFontUniqueID.replace(f" {style}", " Nerd Font")
            fontName.setName(string, nameID, platformID, platEncID, langID)

        elif nameID == 3:
            style = fontName.getName(2, 3, 1, 1033).toUnicode()
            string = originFontUniqueID.replace(f" {style}", f" Nerd Font {style}")
            fontName.setName(string, nameID, platformID, platEncID, langID)

        elif nameID == 6:
            string = f"{fontName.getName(4,3,1,1033)} {fontName.getName(2,3,1,1033)}"
            string = string.replace(" ", "-")
            fontName.setName(string, nameID, platformID, platEncID, langID)
            pass

    font.save(filename)
    font.close()


def main():
    workspace = os.environ.get("GITHUB_WORKSPACE") or Path(__file__).parent

    for file in os.listdir(os.fsencode(workspace)):
        filename = os.fsdecode(file)
        if filename.endswith(".ttf") or filename.endswith(".otf"):
            fix(filename)


if __name__ == "__main__":
    main()
