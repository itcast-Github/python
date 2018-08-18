import pygame
from pygame.locals import*
import random
#创建一个基类
class Base:
    def __init__(self,screen,name):
        #设置要显示内容的窗口
        self.screen=screen
        self.name=name

#创建一个飞机类,继承自基类
class Plan(Base):
    #重写了基类的__init__方法
    def __init__(self,screen,name):
        super().__init__(screen,name)
        self.image=pygame.image.load(self.imageName).convert()
        #用来存储飞机发射的所有导弹
        self.misslis=[]
    #显示的方法
    def display(self):
        #更新飞机的位置
        self.screen.blit(self.image,(self.x,self.y))
        #存放需要删除的对象信息
        needDelItemList=[]
        for i in self.misslis:
            if i.judge():
                needDelItemList.append(i)
        for i in needDelItemList:
            self.misslis.remove(i)
        #遍历飞机所有的导弹
        for daodan in self.misslis:
            daodan.display()
            #修改所有导弹的位置
            daodan.move()
    def shedaodan(self):
        misslis=Misslis(self.x,self.y,self.screen,self.name)
        self.misslis.append(misslis)
#创建一个玩家飞机类,继承自飞机类
class GamePlan(Plan):
    #重写父类的__init__方法
    def __init__(self,screen,name):
        #设置玩家飞机默认的位置
        self.x=230
        self.y=600
        self.imageName='./feiji/hero.gif'
        super().__init__(screen,name)
    def moveLeft(self):
        self.x-=10
    def moveRight(self):
        self.x+=10

        
#创建一个敌人飞机类，继承自飞机类
class EnemyPlan(Plan):
    #重写父类的__init__()方法
    def __init__(self,screen,name):
        #设置敌机默认的位置
        self.x=0
        self.y=0
        self.imageName='./feiji/enemy-1.gif'
        #调用父类的__init__方法
        super().__init__(screen,name)
        self.direction='right'
    def move(self):
        #如果碰到了右边的边界，就往左走，碰到了左边的边界，就往右走
        if self.direction=='right':
            self.x+=2
        elif self.direction=='left':
            self.x-=2
        if self.x>480-50:
            self.direction='left'
        elif self.x<0:
            self.direction='right'
    def shedaodan(self):
        num=random.randint(1,100)
        if num==88:
            super().shedaodan()
#创建一个导弹类,继承自基类
class Misslis(Base):
    #重写基类的__init__方法
    def __init__(self,x,y,screen,planName):
        super().__init__(screen,planName)
        #根据飞机的名字，来选择导弹的类型，即哪个飞机发射的，还要设置子弹飞行的方向
        if planName=='game':
            imageName='./feiji/bullet-3.gif'
            self.x=x+40
            self.y=y-20
        elif planName=='enemy':
            imageName='./feiji/bullet-1.gif'
            self.x=x+30
            self.y=y+30
        self.image=pygame.image.load(imageName).convert()
    #导弹的移动方法
    def move(self):
        if self.name=='game':
            self.y-=2
        elif self.name=='enemy':
            self.y+=2
    #导弹的显示方法
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    #判断导弹是否超出屏幕范围
    def judge(self):
        if self.y>890 or self.y<0:
            return True
        else:
            return False


if __name__=='__main__':
    #创建一个窗口，用来显示内容
    screen=pygame.display.set_mode((480,890),0,32)
    #创建一个和窗口大小一样的图片，用来充当背景
    background=pygame.image.load('./feiji/background.png').convert()
    #创建一个玩家飞机对象
    gamePlan=GamePlan(screen,'game')
    #创建一个敌人飞机对象
    enemyPlan=EnemyPlan(screen,'enemy')
    #把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))
        gamePlan.display()
        enemyPlan.move()
        enemyPlan.shedaodan()
        enemyPlan.display()
        #判断是否点击了退出按钮
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            elif event.type==KEYDOWN:
                #控制飞机让其向左移动
                if event.key==K_a or event.key==K_LEFT:
                    gamePlan.moveLeft()
                #控制飞机让其向右移动
                elif event.key==K_d or event.key==K_RIGHT:
                    gamePlan.moveRight()
                #控制飞机让其发射导弹
                elif event.key==K_SPACE:
                    gamePlan.shedaodan()
        pygame.display.update()
