class filesets:
	@staticmethod
	def load_datas():
		x = []
		y = []
		with open('pima-indians-diabetes.txt', 'r') as f: 
			for line in f:  
				line = line.strip()
				line = line.split(',')
				x.append(line[:len(line)-1])
				y.append(line[len(line)-1])
		print('\nOriginal data looks like this: \n', x)
		print('\nLabels looks like this: \n', y)
		d = {'data' : x, 'target' : y}
		return d