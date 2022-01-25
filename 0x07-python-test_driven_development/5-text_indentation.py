#!/usr/bin/python3
"""text indent"""


def text_indentation(text):
    """"text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".:?":
        text = (delimiter + "\n\n").join(
            [index.strip(" ") for index in text.split(delimiter)]
        )
    print("{}".format(text), end="")