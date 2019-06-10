def w1(func):
    def inner():
        print("---正在验证权限----")
        func()
    return inner

def f1():
    print("---f1---")

def f2():
    print("---f2---")

#innerFunc = w1(f1)
#innerFunc()

f1 = w1(f1)
f1()


# 猜测打印正确
# ---正在验证权限----
# ---f1---

