import csv
import med


def main():
    word = ""
    while word != "q":
        word = input("Type word: ").lower()
        suggestion = autocomplete(word)
        suggestion_freq = autocomplete_using_freq(word)
        autocorrect_sugg = autocorrect(word)
        print("First three suggestions: ", suggestion)
        print("Suggestions based on frequency: ", suggestion_freq)
        print("Autocorrect suggestion: ", autocorrect_sugg)

def get_word_list():
    words = open("./alphabetical.csv", "r")
    reader = csv.reader(words)

    return reader

def extract_words(suggestions):
    return [x[0] for x in suggestions[:3]]

def get_suggestions(word):
    reader = get_word_list()
    suggestions = []

    for row in reader:
        if all([len(word) <= len(row[0]) and word[i] == row[0][i] for i in range(len(word))]):
            suggestions.append(row)

    return suggestions

def autocomplete(word):
    suggestions = get_suggestions(word)

    return ", ".join(extract_words(suggestions))

def autocomplete_using_freq(word):
    def sort(x):
        return int(x[1])

    suggestions = get_suggestions(word)
    suggestions.sort(key=sort, reverse=True)

    return ", ".join(extract_words(suggestions))

def autocorrect(word):
    best_match = None
    
    reader = get_word_list()

    for row in reader:
        dist = med.minimum_edit_distance(word, row[0])

        if best_match == None or dist < best_match[1]:
            best_match = (row[0], dist)
    
    return best_match[0]

main()

