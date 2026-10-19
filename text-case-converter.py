"""
Day 13 - 2026-10-19
Tool: Text Case Converter
What it does: Converts any text between UPPER CASE, lower case, Title
Case, Sentence case and aLtErNaTiNg case, and can also count words -
handy for fixing a message typed with Caps Lock on or formatting a
title for a post, CV or assignment.
Who it helps: Anyone writing posts, emails, assignments or shop signs
who needs clean, correctly-cased text without retyping it.
"""


def to_upper(text):
    return text.upper()


def to_lower(text):
    return text.lower()


def to_title(text):
    return text.title()


def to_sentence(text):
    """First letter of each sentence in upper case, the rest lower."""
    text = text.strip().lower()
    result = []
    capitalise_next = True
    for ch in text:
        if capitalise_next and ch.isalpha():
            result.append(ch.upper())
            capitalise_next = False
        else:
            result.append(ch)
        if ch in ".!?":
            capitalise_next = True
    return "".join(result)


def to_alternating(text):
    """aLtErNaTiNg case, often used playfully in chats."""
    result = []
    upper = False
    for ch in text:
        if ch.isalpha():
            result.append(ch.upper() if upper else ch.lower())
            upper = not upper
        else:
            result.append(ch)
    return "".join(result)


def word_count(text):
    return len(text.split())


if __name__ == "__main__":
    messy = "hELLO. this is ARIFUL. caps lock was ON!"
    print("Original:  ", messy)
    print("Upper:     ", to_upper(messy))
    print("Lower:     ", to_lower(messy))
    print("Sentence:  ", to_sentence(messy))
    print("Title:     ", to_title("my new shop in dhaka"))
    print("Alternating:", to_alternating("good morning"))
    print("Word count of original:", word_count(messy))
