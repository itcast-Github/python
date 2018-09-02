#coding=utf-8
'''

老王开枪打敌人

抽象：类

人：
属性：血，
方法：安子弹、安弹夹、开枪，掉血

枪：
属性：
方法：连接弹夹，

子弹：
属性：杀伤力
方法：伤害

弹夹：
属性：容量、容纳
方法：保存子弹

'''


# class animal:
# 	num = 0
# 	def __init__(self):
# 		self.color = 'bai'
# 	def method(self):
# 		print ('----method------')

class Cake(object):
	def __init__(self,weidao='默认'):
		self.taste = weidao


class CakeStore(object):
	def taste(self,weidao):
		
		cake = Cake()
		print('----品尝蛋糕----%s'%cake.taste)






# def logged(when):
# 	def log(f,*args,**kwargs):
# 		print('fun:%s args:%r kwargs:%r '%(f,args,kwargs))