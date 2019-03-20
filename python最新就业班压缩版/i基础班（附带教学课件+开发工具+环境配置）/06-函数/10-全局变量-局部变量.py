age = 18

def A():
    age = 100
    print(age)

def B():
    global age
    age = 200 #此时把全局的age改为了200 
    print(age)

def C():
    print(age)

A()
B()
C()

# 打印
# 100
# 200
# 200
