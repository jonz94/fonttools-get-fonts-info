#! /usr/bin/python

import os
from traceback import print_list, print_stack, print_tb

from fontTools.ttLib import TTFont


def fix(filename):
    font = TTFont(filename, recalcBBoxes=False)
    fontName = font["name"]

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
        if nameID == 1:
            pass

        # if entry.nameID in [1, 3, 4, 6, 16, 18]:
        #     key = f"{filename},{nameID},{platformID},{platEncID},{langID}"
        #     value = f"{entry.toUnicode()}"

        #     print(f'"{key}": "{value}"')

        # if nameID == 1 and langID == 1033:
        #     print(fontName.getName(18, 3, 1, 1033).toUnicode().rsplit(" ", 3)[0])

        #     key = f"{filename},{nameID},{platformID},{platEncID},{langID}"
        #     value = f"{entry.toUnicode()}"

        #     print(f'"{key}": "{value}"')

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
