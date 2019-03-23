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

# 打印类似列表
# [8, 1, 10, 7, 9, 6, 5, 3, 2, 4]