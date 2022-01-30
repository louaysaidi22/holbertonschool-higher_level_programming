#!/usr/bin/python3
"""task4"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print("{}".format(i), end="")
        if i == "." or i == "?" or i == ":":
            print("\n")
