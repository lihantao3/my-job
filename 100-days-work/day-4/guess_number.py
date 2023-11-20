import random


answer = random.randint(1,100)
res = int(input('你猜测的数字是： '))
counter = 0
while res != answer:
    counter += 1
    if res > answer:
        res = int(input("再小一点，你的下一个答案是： "))
    else:
        res = int(input("再大一点，你的下一个答案是： "))
print('恭喜你回答正确，你一共猜错了%d次答案。' % counter)
