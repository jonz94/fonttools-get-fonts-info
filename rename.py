#! /usr/bin/python

import os

from fontTools.ttLib import TTFont


def getCharName(char):
    return {
        "!": "Exclamation-Mark",
        '"': "Double-Quotes",
        "#": "Number",
        "$": "Dollar",
        "%": "Percent-Sign",
        "&": "Ampersand",
        "'": "Single-Quote",
        "(": "Open-Parenthesis",
        ")": "Close-Parenthesis",
        "*": "Asterisk",
        "+": "Plus",
        ",": "Comma",
        "-": "Hyphen",
        ".": "Period",
        "/": "Slash",
        ":": "Colon",
        ";": "Semicolon",
        "<": "Less-Than",
        "=": "Equals",
        ">": "Greater-Than",
        "?": "Question-Mark",
        "@": "At-Symbol",
        "[": "Opening-Bracket",
        "\\": "Backslash",
        "]": "Closing-Bracket",
        "^": "Caret",
        "_": "Underscore",
        "`": "Grave-Accent",
        "{": "Opening-Brace",
        "|": "Vertical-Bar",
        "}": "Closing-Brace",
        "~": "Tilde",
    }.get(char, "Unknown")


def rename(filename):
    font = TTFont(filename, recalcBBoxes=False)
    fontName = font["name"]
    characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for char in characters:
        for entry in fontName.names:
            nameID = entry.nameID
            platformID = entry.platformID
            platEncID = entry.platEncID
            langID = entry.langID

            if nameID in [1, 3, 4, 6]:
                fontName.setName(
                    f"Lato{char}Regular",
                    nameID,
                    platformID,
                    platEncID,
                    langID,
                )

        font.save(f"Lato-{getCharName(char)}-Regular.ttf")


def main():
    workspace = os.environ.get("GITHUB_WORKSPACE") or os.path.abspath(__file__).replace(
        "/rename.py", ""
    )

    for file in os.listdir(os.fsencode(workspace)):
        filename = os.fsdecode(file)
        if filename.endswith(".ttf") or filename.endswith(".otf"):
            rename(filename)


if __name__ == "__main__":
    main()
