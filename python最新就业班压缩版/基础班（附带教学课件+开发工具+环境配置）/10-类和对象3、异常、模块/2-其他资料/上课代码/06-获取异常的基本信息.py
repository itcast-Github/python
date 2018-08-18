try:
#    print(abc)
    open("abc.txt")
except (NameError,FileNotFoundError) as result:
    print("产生了一个异常....%s"%result)
