import random

with open('Exercises_05.02.2023/alice.txt', 'r') as f:
    text = f.read()
    text = text.lower().split()
result = {}
for i in range(0, len(text) - 1, 2):
    result.setdefault(text[i], []).append(text[i + 1])
print(result)

words = []
print('Введите слово:')
print('Чтобы закончить введите:', 'stop')
word = ()
while word != 'stop':
    word = input()
    if word in result:
        a = random.choice(result[word])
        words.append(a)
    else:
        continue
else:
    print(words)




