import re
inp = 'Он --- серо-буро-малиновая редиска!! >>>:-> А не кот. www.kot.ru'

result = []
for m in re.finditer(r'\b\w+(?:-\w+(?:-\w+)?)?\b', inp):
    result.append(m)
print(result)
print(len(result))

