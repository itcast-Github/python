#coding=utf-8

'''
	2. 检测键盘
'''

import pygame

#导入按键的检测
from pygame.locals import *

if __name__ == '__main__':

	screen = pygame.display.set_mode((480,890),0,32)

	bgImageFile = './feiji/background.png'

	background = pygame.image.load(bgImageFile).convert()

	# 1.显示背景
	# screen.blit(background,(0,0))
	# pygame.display.update()
	# 2.步骤１显示的背景　一闪而过
	while True:
		screen.blit(background,(0,0))


		#判断是否是点击了退出按钮
		for event in pygame.event.get():
			# print(event.type)
			if event.type == QUIT:
				print("exit")
				exit()
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					print('left')
				
				elif event.key == K_d or event.key == K_RIGHT:
					print('right')

				elif event.key == K_SPACE:
					print('space')



		pygame.display.update()
