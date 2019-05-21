# num = 100
def test1():
    # num = 200
    def test2():
        num = 300
        print(num)
    return test2


ret = test1()
ret()


# num = 100
# 猜测打印正确
# 100

# num = 200
# 猜测打印正确
# 200

# num = 300
# 猜测打印正确
# 300
