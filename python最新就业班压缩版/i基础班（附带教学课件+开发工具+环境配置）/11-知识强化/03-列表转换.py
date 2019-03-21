a = [x for x in range(1,10)]
b = [a[i:i+3] for i in range(0,len(a),3)]
print(a)
print(b)
print(range(0,len(a),3))
print(a[0:3])

# 打印
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# range(0, 9, 3) # 即[0,3,6]
# [1, 2, 3]