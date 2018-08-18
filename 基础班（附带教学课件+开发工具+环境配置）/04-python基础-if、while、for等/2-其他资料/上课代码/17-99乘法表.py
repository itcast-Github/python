#外边一层循环控制行数
i = 1

while i<=9:

    #里面一层循环控制没一行中的列数
    j = 1
    while j<=i:
        print("%d*%d=%-2d  "%(j,i,j*i),end="")
        j+=1

    print("")
    i+=1


