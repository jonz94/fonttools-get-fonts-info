#! /usr/bin/python

import os

from fontTools.ttLib import TTFont


def fix(filename):
    font = TTFont(filename, recalcBBoxes=False)
    fontName = font["name"]
    characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    for entry in fontName.names:
        nameID = entry.nameID
        platformID = entry.platformID
        platEncID = entry.platEncID
        langID = entry.langID

        if nameID in [1, 3, 4, 6]:
            fontName.setName(
                f"Crazy {characters} Regular",
                nameID,
                platformID,
                platEncID,
                langID,
            )

    font.save(filename)
    font.close()


def main():
    workspace = os.environ.get("GITHUB_WORKSPACE") or os.path.abspath(__file__).replace(
        "/fix.py", ""
    )

    for file in os.listdir(os.fsencode(workspace)):
        filename = os.fsdecode(file)
        if filename.endswith(".ttf") or filename.endswith(".otf"):
            fix(filename)


if __name__ == "__main__":
    main()
