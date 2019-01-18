def test():
    if 1>0:
        return 100
    else:
        return 200

    #上面的if等价于下面的方式

    if 1>0:
        num = 100
    else:
        num = 200
    return num

print(test())

#100
