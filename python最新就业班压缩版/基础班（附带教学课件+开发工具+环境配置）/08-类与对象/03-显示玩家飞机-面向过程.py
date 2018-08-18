#调用pygame包
import pygame
#调用PYGAME模块
from pygame.locals import *

#检测设置
# if __name__ == '__main__':

#     #创建一个窗口，用来显示内容,
#     screen = pygame.display.set_mode((480,890),0,32)
#     #创建一个和窗口大小相同的图片，用来充当背景
#     background = pygame.image.load('./feiji/background.png').convert()
#     #创建一个飞机的图片
#     hero = pygame.image.load('./feiji/hero.gif').convert()

if __name__ == "__main__":

    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,890),0,32)

    1     #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png").convert()
    
    #测试，用来创建一个玩家飞机的图片
    hero = pygame.image.load("./feiji/hero.gif").convert()
    x = 0
    y = 0

    #把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))
        screen.blit(hero,(x,y))

        #判断用户输入的键
        for event in pygame.event.get():
            if event.type == QUIT:
                print('exit')
                exit()
            elif event.type == KEYDOWN:
                if event.kay == K_a or event.kay == K_LEFT:
                    x -= 5
                elif event.kay == K_d or event.kay == K_RIGHT:
                    x += 5
                elif event.kay == K_SPACE:
                    print('space')
        pygame.display.update




