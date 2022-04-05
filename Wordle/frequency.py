import csv

words = {}

with open("wordle/unigram_freq.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for word, count in reader:
        words[word] = int(count)


def of_word(word):
    return words.get(word, 0)