sentence = ["readability counts", "you only live once"]

for word in sentence:
    (lambda word: word.capitalize() + '.')(word)
