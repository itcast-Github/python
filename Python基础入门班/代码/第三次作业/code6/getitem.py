class Fib(object):
	def __getitem__(self, n):
		if isinstance(n, int): # n是索引
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice): # n是切片
			start = n.start
			stop = n.stop
			step = n.step
			if start is None:
				start = 0
			if step is None:
				step = 1	
			a, b = 0, 1
			L = []
			for x in range(start+1):
				a, b = b, a + b
				if x == start:
					L.append(a)
			next = start + step			
			for i in range(next, stop, step):
				for x in range(step):
					a, b = b, a + b
				L.append(a)			
			return L

f = Fib()
print(f[0:5])
print(f[:10])
print(f[0:10:2])