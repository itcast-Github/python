# 打飞机代码1：搭建界面

![](../Images/项目截图-1py.png)

```python
#coding=utf-8

'''
	1. 显示一个背景
'''

import pygame


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
		pygame.display.update()

```