import os

path = os.path.dirname(os.path.abspath(__file__))


def order_word():
    file = open(path + "/words.txt", "r")
    lines = file.readlines()
    file.close()

    words = []
    for line in lines:
        words.append(line.strip())

    words.pop(0)
    words.sort()

    words_distinct = []

    for word in words:
        if word not in words_distinct:
            words_distinct.append(word)

    words_distinct.sort()

    file = open(path + "/words_distinct.txt", "w")
    file.write(str(len(words_distinct)) + "\n")

    for word in words_distinct:
        file.write(str(words.count(word)) + " ")

    file.close()


order_word()
