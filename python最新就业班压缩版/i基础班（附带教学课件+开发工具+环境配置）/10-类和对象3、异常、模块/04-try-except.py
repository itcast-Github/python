try:

   print(abc)
    # 打印：没有定义变量。。。。。

    # open("abc.txt")
    # 打印：没有文件.....

except NameError:
    print("没有定义变量。。。。。")
except FileNotFoundError:
    print("没有文件.....")


