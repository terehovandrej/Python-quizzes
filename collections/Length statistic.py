from collections import Counter

a = input()
b = a.split(" ")
word_len = []
for word in b:
    word_len.append(len(word))
b = Counter(word_len).most_common()
c = sorted(b)
for i in c:
    print(f"{i[0]}: {i[1]}")
