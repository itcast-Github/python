import pygame
from pygame.locals import*

class Plan:

    #飞机的属性
    def __init__(self):
        self.x=240
        self.y=420
        self.game=pygame.image.load('./feiji/hero.gif').convert()

    #飞机有一个移动方法
    def move(self):
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_a or event.key==K_LEFT:
                    self.x-=7
                elif event.key==K_d or event.key==K_RIGHT:
                    self.x+=7
if __name__=='__main__':
    #创建一个窗口，用来显示内容
    screen =pygame.display.set_mode((480,530),0,32)
    #创建一个和窗口大小一样的图片，用来显示背景
    background=pygame.image.load('./feiji/background.png').convert()
    plan=Plan()
    while True:

        screen.blit(background,(0,0))
        screen.blit(plan.game,(plan.x,plan.y))
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE:
                    iprint('space')
        pygame.display.update()
        plan.move()
