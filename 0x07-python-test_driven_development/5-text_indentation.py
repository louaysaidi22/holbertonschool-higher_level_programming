#!/usr/bin/python3
"""task4"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".:?":
            while text[i+1] == " ":
                i += 1
            print("\n")
        i += 1
