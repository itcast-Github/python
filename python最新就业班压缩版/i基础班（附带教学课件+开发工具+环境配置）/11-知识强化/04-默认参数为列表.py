def test(a,b=[],c={}):
    b.append(a)
    c[a] = a
    return b,c

list1 = test(10)
list2 = test(123, ['a','b','c'])
list3 = test('a')

print(list1)
print(list2)
print(list3)
