aStr = "hello world ,hhhh world heihei"

def replaceStr(temp, oldStr, newStr):
    while True:
        print(temp)
        position = temp.find(oldStr)
        if position == -1:
            break
        temp = temp[:position] + newStr + temp[position+len(oldStr):]
    return temp

def replaceStr2(temp, oldStr, newStr):
	result = temp.split(oldStr)
	return newStr.join(result)


result = replaceStr(aStr, "h", "H")
print(result)

# 打印
# hello world ,hhhh world heihei
# Hello world ,hhhh world heihei
# Hello world ,Hhhh world heihei
# Hello world ,HHhh world heihei
# Hello world ,HHHh world heihei
# Hello world ,HHHH world heihei
# Hello world ,HHHH world Heihei
# Hello world ,HHHH world HeiHei
# Hello world ,HHHH world HeiHei