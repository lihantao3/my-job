"""
说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只
"""


for x in range(20):
    for y in range(33):
        z = 100 - y - x
        if x * 5 + y * 3 + z / 3 == 100:
            print('公鸡：%d只, 母鸡：%d只, 小鸡：%d只' % (x, y, z))


