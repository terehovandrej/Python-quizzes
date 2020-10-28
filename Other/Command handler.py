b = True
while b:
    a = input()
    if a == "End":
        print("Good bye!")
        b = False
    else:
        print(f'Processing "{a}" command...')
