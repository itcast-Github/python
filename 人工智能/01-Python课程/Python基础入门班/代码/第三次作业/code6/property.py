import traceback

class Screen:
	@property
	def width(self):
		return self._width	
	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise ValueError('not int')
		elif (value < 0) or (value > 100):
			raise ValueError('not between 0 ~ 100')
		self._width = value	
	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self, value):
		if not isinstance(value, int):
			raise ValueError('not int')
		elif (value < 0) or (value > 100):
			raise ValueError('not between 0 ~ 100')
		self._height = value
	
	@property
	def resolution(self):
		return self._width * self._height
		
scr = Screen();
scr.width = 90
print(scr.width)
scr.height = 90
print(scr.height)
print(scr.resolution)
try:
    scr.width = 'abc'
except ValueError:
    traceback.print_exc()
try:
    scr.width = 101
except:
    traceback.print_exc()
try:
    scr.resolution = 150
except AttributeError:
    traceback.print_exc()






