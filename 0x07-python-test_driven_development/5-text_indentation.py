#!/usr/bin/python3
"""task4"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    line = ""
    for i in text:
        line += i
        if line == " ":
            line = ""
        if i in ".:?":
            print(line, end="")
            print("\n")
            line = ""
    print(line, end="")
