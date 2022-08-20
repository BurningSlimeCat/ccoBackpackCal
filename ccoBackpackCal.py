packs = [
    # 物品總資料
    # [0]編號, [1]簡稱, [2]名稱, [3]英文, [4]權重, [5]擁有數量, [6]差額
    [0, '紅包', '自主儲存單位', 'ASU', 7500000, 0, 0],
    [1, '紫包', '公事包    ', 'EOC', 300000, 0, 0],
    [2, '黃包', '探險家背包', 'Dora', 15000, 0, 0],
    [3, '白包', '腰包      ', 'Fanny', 1000, 0, 0],
    [4, '灰包', '老舊袋子  ', 'OldPouch', 100, 0, 0],
    [5, '科碎', '科技碎片  ', 'TS', 1, 0, 0]
]

# 包包換算器
print('---歡迎使用包包換算器---')
for item_num in range(5):
    print(f'[{packs[item_num][0]}]\t{packs[item_num][1]}\t{packs[item_num][2]}\t{packs[item_num][3]}')

# 輸入目標
check_1 = False
while not check_1:
    input_goal = input('輸入目標種類[0~4]：')
    if input_goal.isdigit():
        if int(input_goal) in range(5):
            choice = int(input_goal)
            check_1 = True
        else:
            print('請輸入對應數字')
    else:
        print('請輸入對應數字')
print()
# -----------------------------------------------------
print(f'---目標：{packs[choice][1]}---')
goal = goal_total = packs[choice][4]
weight = 0

# 輸入持有物品數量
print('輸入持有物品數量')

for i in range(choice + 1, len(packs)):
    input_have = input(f'{packs[i][1]}：')
    while not input_have.isdigit():
        input_have = input(f'請輸入數字\n{packs[i][1]}：')
    packs[i][5] = int(input_have)
print()
# -----------------------------------------------------
# 計算目標差額
for i in range(choice + 1, len(packs)):
    weight += packs[i][4] * packs[i][5]
    goal -= packs[i][4] * packs[i][5]

# 計算各物品差額
if goal <= 0:
    print('---目標達成度： 100%---')
else:
    print('---目標達成度：{:.0%}---'.format(weight / goal_total))
    for i in range(choice + 1, len(packs)):
        packs[i][6] = goal // packs[i][4]
        goal %= packs[i][4]
        print(f'{packs[i][1]} 還需要 {packs[i][6]}')
        if goal == 0:
            break
# -----------------------------------------------------
