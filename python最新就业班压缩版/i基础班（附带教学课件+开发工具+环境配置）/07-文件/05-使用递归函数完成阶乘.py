#什么叫递归：一个函数调用了它自己本身，那么这样的函数就叫做递归函数

'''
def A():
    print("adfasdfasdf")
    A()



A()
'''


def test(num):
    if num>1:
        return num*test(num-1)
    else:
        return 1



result = test(4)
print(result)

# 打印
# 4 x 3 x 2 x 1 = 24
