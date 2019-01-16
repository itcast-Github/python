'''
g_a = 100

g_list = [11,22]

def A():
    global g_a
    print(g_a)

    #global g_list
    g_list.append(33)
    print(g_list)


def B():
    print(g_list)

A()
B()
'''



def A(a,b):
    print("------A-------")



def A():
    print("------B-----")




A(11,22)







