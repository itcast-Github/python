import os
'''
#1. 获取制定路径下 的所有文件名
allFileName = os.listdir("./test")
print(allFileName)

#2. 循环的方式 依次进行重命名
for name in allFileName:
    os.rename("./test/"+name,"./test/"+"[东京出品]-"+name)
'''

#0. 提示并获取一个要重命名的文件夹
needRenameFile = input("请输入要批量重命名的文件夹：")

#1. 获取制定路径下 的所有文件名
allFileName = os.listdir("./"+needRenameFile)
print(allFileName)

#2. 循环的方式 依次进行重命名
for name in allFileName:
    os.rename("./"+needRenameFile+"/"+name,"./"+needRenameFile+"/"+"[东京出品 QILEI TEST]-"+name)
