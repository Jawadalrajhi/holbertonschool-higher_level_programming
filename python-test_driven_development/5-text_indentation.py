#!/usr/bin/python3
'''prints a text with 2 new lines after each
of these characters: ., ? and :'''


def text_indentation(text):
    '''prints a text with 2 new lines after each
    of these characters: ., ? and :'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    i = 0
    while i < len(text):
        char = text[i]
        print(char, end="")
        if char in ['.', '?', ':']:
            print()
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            i -= 1
        i += 1
