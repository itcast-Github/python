# 抛出异常

你可以用raise语句来引发一个异常。异常/错误对象必须有一个名字，且它们应是Error或Exception类的子类

下面是一个引发异常的例子:

```python

class ShortInputException(Exception):
	'''你定义的异常类。'''
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	s = input('请输入 --> ')
	
	if len(s) < 3:
		# raise引发一个你定义的异常
		raise ShortInputException(len(s), 3)
	
except EOFError:
	print("你输入了一个结束标记EOF")
except ShortInputException, x:#x这个变量被绑定到了错误的实例
	print('ShortInputException: 输入的长度是 %d,长度至少应是 %d'% (x.length, x.atleast))
else:
	print('没有异常发生.')
```

运行结果如下:
```
	$ python raising.py
	请输入 -->
	你输入了一个结束标记EOF

	$ python raising.py
	请输入 --> --> ab
	ShortInputException: 输入的长度是 2, 长度至少应是 3

	$ python raising.py
	请输入 --> abc
	没有异常发生.
```