# (lambda 매개변수 인자들: 리턴할 표현식)(전달인자들)

sentence = ["readability counts", "you only live once"]

for word in sentence:
    (lambda word: word.capitalize() + '.')(word)
