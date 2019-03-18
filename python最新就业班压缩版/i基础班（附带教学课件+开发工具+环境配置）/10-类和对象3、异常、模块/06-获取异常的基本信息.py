try:
#    print(abc)
    open("abc.txt")
except (NameError,FileNotFoundError) as result:
    print("产生了一个异常....%s"%result)

# 打印
# 产生了一个异常....[Errno 2] No such file or directory: 'abc.txt'