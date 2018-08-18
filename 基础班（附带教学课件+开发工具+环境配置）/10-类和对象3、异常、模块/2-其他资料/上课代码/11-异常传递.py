def test1():
    print("------1-1------")
    print(num)
    print("------1-2------")


def test2():
    print("------2-1------")
    test1()
    print("------2-2------")

def test3():
    try:
        print("------2-1------")
        test1()
        print("------2-2------")
    except Exception as result:
        print("捕获到了异常:%s"%result)


test3()
