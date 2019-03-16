'''
g_a = 100

g_list = [11,22]

def A():
    global g_a
    print(g_a)

    #global g_list
    g_list.append(33)
    print(g_list)


def B():
    print(g_list)

A()

# 打印：
# 100
# [11, 22, 33]

B()

# 打印：
# [11, 22, 33]

'''


# 注意点 可变类型与不可变类型作为参数都是传的引用
# 不可变类型的加global，可变的随意，爱加不加
# 重名的函数  下面的会把上面的覆盖

def A(a,b):
    print("------A-------")

def A():
    print("------B-----")

A(11,22)
