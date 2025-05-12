while True:
    try:
        n = int(input("输入需要打印的杨辉三角行数 :"))
        assert n > 0, "请输入正整数！"
        break
    except (ValueError, AssertionError) as e:
        print(f"输入无效: {e}，请重新输入！")

list1 = []
for i in range(n):
    list2 = []
    if i == 0:
        list2 = [1]
    elif i == 1:
        list2 = [1, 1]
    else:
        for j in range(i + 1):
            if j == 0 or j == i:
                list2.append(1)
            else:
                list2.append(list1[i - 1][j - 1] + list1[i - 1][j])
    list1.append(list2)

space = len(list1[-1])
for i in list1:
    print(' ' * (space * 4 // 2), end='')
    for j in i:
        print(f"{j:<4}", end='')
    print()
    space -= 1

print("杨辉三角打印完成！")
