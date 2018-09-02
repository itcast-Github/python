
i = 0
#控制行数
while i<5:
    #方法1
    #print("*"*i)


    #方法2
    #控制一行中的个数
    j = 0
    while j<=i:
        print("* ", end='')
        j+=1

    print("")
    i+=1
