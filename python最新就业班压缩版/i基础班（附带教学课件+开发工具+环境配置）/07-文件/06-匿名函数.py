'''
def test(a,b):
    return a+b


aaaa = lambda a,b:a+b


print(test(11,22))

print(aaaa(8,9))
'''



def test(a,b,xxx):
    return xxx(a,b)




result = test(11,22,lambda x,y:x-y)
print(result)

# 打印
# -11