import random

def test(n):
    newList = []
    while True:

        if len(newList)==10:
            break

        num = random.randint(1,n)
        if num not in newList:
            newList.append(num)


    return newList


result = test(10)
print(result)


