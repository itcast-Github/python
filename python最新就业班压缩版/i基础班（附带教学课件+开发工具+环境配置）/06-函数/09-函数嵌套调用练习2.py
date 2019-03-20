def add3nums(a, b, c):
    #print(a+b+c)
    #或者
    return a+b+c


def average3nums(A, B, C):

    #先求出A+B+C的结果
    result = add3nums(A, B, C)

    #再上一步的结果上 对其进行 /3
    result = result/3

    return result

averageResult = average3nums(11,22,33)
print("====>%d<====="%averageResult)

# 打印
# ====>22<=====