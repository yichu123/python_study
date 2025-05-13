import random

suits = ['♥', '♠', '♣', '♦']
cardstr = ['J', 'Q', 'K', 'A']
cardnum = [str(i) for i in range(2, 11)]
cardking = ['大王', '小王']

card = []
for suit in suits:
    for num in cardnum:
        card.append(suit + num)
    for str in cardstr:
        card.append(suit + str)
card = card + cardking
random.shuffle(card)
地主牌=random.sample(card,6)
x=random.choice(['A','B','C','D'])
for i in 地主牌:
    card.remove(i)
A = []
B = []
C = []
D = []
for i in range(len(card)):
    if i % 4 == 0:
        A.append(card[i])
    if i % 4 == 1:
        B.append(card[i])
    if i % 4 == 2:
        C.append(card[i])
    if i % 4 == 3:
        D.append(card[i])
eval(x).extend(地主牌)
print(f'地主牌是{地主牌}，地主是{x}')
print(f'A:{A}')
print(f'B:{B}')
print(f'C:{C}')
print(f'D:{D}')


# 第1行： 引入random模块
# 第3-6行： 将所有扑克牌中出现的数字及符号等作为列表列出
# 第8-14行： 根据刚刚的数字与符号的列表，将一副牌中的元素用列表列出
# 第15行： 使用random.shuffle方法将列表中的元素随机打乱，相当于洗牌
# 第16-19行： 随机选出六张牌作为地主牌，并从所有牌中去除这六张牌，并随机选择地主
# 第20-23行： 为ABCD四位角色创建列表，用于存放各位的牌
# 第24-32行： 由于之前的扑克牌已经随机打乱，模仿发牌的方式，将这些牌每四张分给同一个人
# 第33行： 为选择的地主加上地主牌
# 第34-38行： 打印地主、地主牌以及ABCD各位的牌