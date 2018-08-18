import random
def createList(n):
    newList = []
    while True:
        if len(newList)>=n:
            break

        num = random.randint(1,n)
        if num not in newList:
            newList.append(num)


    return newList



newList = createList(10)
print(newList)
