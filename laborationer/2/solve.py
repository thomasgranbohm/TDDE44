"""Labb 2.

Programmet hämtar ur olika förslag på vilket ord användaren
försökte skriva in. De tre första förslagen baserat på en
alfabetiskt sorterad lista, de tre första förslagen baserat
på deras användningsfrekvens, och sist en autocomplete
funktion som hämtar ur förslag baserad på MED-storlek.
"""

import csv
import med


def get_word_list():
    """Öppnar och parsar labbens csv-fil."""
    words = open("./alphabetical.csv", "r")
    reader = csv.reader(words)

    return reader


def extract_words(suggestions):
    """Hämtar ur de första tre orden från förslagslistan."""
    return [x[0] for x in suggestions[:3]]


def get_suggestions(word):
    """Hämtar ur alla ord som kan anses som förslag.

    Ett ord anses vara ett möjligt förslag om ordets längd
    är minst lika långt som det eftersökta ordet, och om ordet
    startar med det eftersökta ordet.
    """
    reader = get_word_list()
    suggestions = []

    for row in reader:
        if len(word) <= len(row[0]) and word == row[0][: len(word)]:
            suggestions.append(row)

    return suggestions


def autocomplete(word):
    """Returnerar en sträng med de tre första förslagen."""
    suggestions = get_suggestions(word)

    return ", ".join(extract_words(suggestions))


def autocomplete_using_freq(word):
    """Returnerar en sträng med de tre första förslagen.

    Denna funktion sorterar först förslagslistan på ordets användningsfrekvens.
    """

    def sort(x):
        return int(x[1])

    suggestions = get_suggestions(word)
    suggestions.sort(key=sort, reverse=True)

    return ", ".join(extract_words(suggestions))


def autocorrect(word):
    """Hämtar det närmast matchande ordet baserat på MED-storleken."""
    best_match = None
    reader = get_word_list()

    for row in reader:
        dist = med.minimum_edit_distance(word, row[0])

        if best_match is None or dist < best_match[1]:
            best_match = (row[0], dist)

    return best_match[0]


if __name__ == "__main__":
    word = ""
    while True:
        word = input("Type word: ").lower()
        if word == "q":
            break

        suggestion = autocomplete(word)
        suggestion_freq = autocomplete_using_freq(word)
        autocorrect_sugg = autocorrect(word)
        print("First three suggestions: ", suggestion)
        print("Suggestions based on frequency: ", suggestion_freq)
        print("Autocorrect suggestion: ", autocorrect_sugg)

    print("Goodbye!")
