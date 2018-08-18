#coding=utf-8

i=0
num = int(input('输入多少行：'))
while i<num:
	if i<((num%2<1) and num//2 or num//2+1):
		print (' '*(num-i-1), '*'*(2*i+1))
	else:
		print (' '*(i), '*'*(2*num-i*2-1))
	i+=1
#num>=59 图形错误

# i=0
# j=5
# k=-1
# while i<9:
# 	i+=1
# 	if i<6:
# 		k+=2
# 		j-=1
# 		print (' '*j, end='')
# 		print ('*'*k)
# 	else:
# 		j+=1
# 		k-=2
# 		print (' '*j, end='')
# 		print ('*'*k)



# i=0
# n=9
# while i<9:
# 	j=0
# 	i+=1
# 	n-=1
# 	while j<i and i<5:
# 		print ('*', end='')
# 		j+=1
# 	while j<=n and i>4:
# 		print ('*',end='')
# 		j+=1
# 	print ('')
