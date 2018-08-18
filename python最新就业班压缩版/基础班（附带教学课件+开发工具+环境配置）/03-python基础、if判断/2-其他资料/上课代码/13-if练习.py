
#1. 请输入你当前的分数
#scoreInput = input("请输入当前驾驶证的分数:")
#score = int(scoreInput)
score = int(input("请输入当前驾驶证的分数:"))


#2. 请输入你违反的交通规则序号（1：闯红灯，2：违章停车）
#guizeInput = input("请输入你违反的交通规则序号（1：闯红灯，2：违章停车）")
#guize = int(guizeInput)
guize = int(input("请输入你违反的交通规则序号（1：闯红灯，2：违章停车）"))

#3. 扣分
if guize==1:
    score -= 6
if guize==2:
    score -= 3

#4. 显示当前的分数，以及显示是否需要参加学习
print("你的剩余分数为：%d"%score)
if score<=0:
    print("你需要参加学习")
else:
    print("你不需要参加学习，你剩余的分数是：%d"%score)
