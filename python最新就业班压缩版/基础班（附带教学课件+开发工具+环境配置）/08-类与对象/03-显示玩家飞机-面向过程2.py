#调用pygame包
import pygame
#调用PYGAME模块
from pygame.locals import *

#创建一个飞机的类
class Hero(object):
    #定义一个实例方法，添加属性
    def __init__(self):
        # self.hero = pygame.image.load("./feiji/hero.gif")
        self.x = 230
        self.y = 600
        self.image = pygame.image.load("./feiji/hero.gif")        

    #定义一个实例方法，导入图片
    def heroImage(self):        
        return self.image

    #定义一个实例方法，接收图像，并且输入飞机位置
    def heroBlit(self):
        screen.blit(hero,(Herox,Heroy))

#检测设置
if __name__ == "__main__":

    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,600),0,32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png").convert()
    x=230
    y=450
 
    hero = Hero()
    #把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))
        screen.blit(hero.heroImage(),(x,y))
        #判断用户输入的键
        for event in pygame.event.get():
            if event.type == QUIT:
                print('exit')
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    x -= 20
                    print('left')
                elif event.key == K_d or event.key == K_RIGHT:
                    x += 20
                    print('right')
                elif event.key == K_SPACE:
                    print('space')
        pygame.display.update()







