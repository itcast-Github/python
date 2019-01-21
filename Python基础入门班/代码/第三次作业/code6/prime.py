import math
class Prime1000:
	def __init__(self):
		self.MAXN = 1000
		self.sieveflag = []
		for i in range(self.MAXN+1):
			self.sieveflag.append(True)	
		self.sieveflag[0] = False
		self.sieveflag[1] = False
		self.sieveflag[2] = True
		self.sindex = 0
		self.resarr = []
		self.esieve(self.sieveflag, self.MAXN)
		
		
	def __iter__(self):
		return self
	
	def esieve(self, sflag, n):
		for i in  range(3, n+1, 2):  #处理偶数
			sflag[i] = True
			i = i + 1
			sflag[i] = False
		max = math.sqrt(n)
		max = int(max)
		for i in  range(3, max+1):   #处理倍数
			if sflag[i]:
				for j in range(2*i, n+1, i):
					sflag[j] = False
		for i in range(2, n+1):
			if sflag[i]:
				self.resarr.append(i)
				
					
	def __next__(self):
		res = self.resarr[self.sindex]
		self.sindex = self.sindex + 1
		if self.sindex == len(self.resarr):		
			raise StopIteration()
		return res
		
for i in Prime1000(): 
	print(i)