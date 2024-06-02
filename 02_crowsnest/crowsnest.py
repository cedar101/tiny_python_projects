from collections import OrderedDict


silent_letter_words = set("heir honor hour".split())


def choose_article(word: str) -> str:
    return (
        ("an" if word[0].islower() else "An")
        if word[0].lower() in "aeiou"  # or word.lower() in silent_letter_words
        else ("a" if word[0].islower() else "A")
    )


def choose_article_dict(word: str, dictionary: OrderedDict) -> str:
    try:
        pronunciations = dictionary[word.lower()]
    except KeyError:
        first_character = word[0]
    else:
        iter_pronunciations = iter(pronunciations)
        first_character = next(iter_pronunciations)[0][0]
    return (
        ("an" if word[0].islower() else "An")
        if first_character.lower() in "aeiou"
        else ("a" if word[0].islower() else "A")
    )
