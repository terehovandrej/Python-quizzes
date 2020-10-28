
myString = input()
myList = list(myString + '*')
count = 1
newString = ''
for i in range(len(myList)-1):
    if myList[i] == myList[i+1]:
        count +=1
    else:
        if count == 1:
            newString += str(myList[i])
        else:
            newString += str(count)
            newString += str(myList[i])
            count = 1
print(newString)
