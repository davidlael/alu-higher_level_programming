#!/usr/bin/python3
"""Module that formats text by adding two new lines."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text: String input.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in [".", "?", ":"]:
            print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
