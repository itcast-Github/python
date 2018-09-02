try:

#    print(abc)
    open("abc.txt")

except NameError:
    print("没有定义变量。。。。。")
except FileNotFoundError:
    print("没有文件.....")
