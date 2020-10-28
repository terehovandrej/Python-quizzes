import re

a = input()
b = re.findall(r"\d*\w", a)
for i in b:
    c = i[-1]
    d = i[:-1]
    if d.isdigit():
        print(int(d) * c, end='', sep='')
    else:
        print(c, end='', sep='')

# 3ab4c2CaB

