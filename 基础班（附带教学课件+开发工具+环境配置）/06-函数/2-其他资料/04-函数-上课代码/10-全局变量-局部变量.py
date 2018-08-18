age = 18

def A():
    age = 100
    print(age)



def B():
    global age
    age = 200
    print(age)

def C():
    print(age)

B()
A()
C()
