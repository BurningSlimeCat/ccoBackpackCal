import tkinter as tk

my_font = '微軟正黑體 15 bold'
bg_color = '#1E1E1E'
bgl_color = '#424242'
fg_color = '#afd0c9'
packs = [
    # [[0]index,[1]name,[2]color,[3]weight]
    [0, '自主儲存單位', '#ff2059', 7500000],
    [1, '公事包', '#e730c0', 300000],
    [2, '探險家背包', '#ccc541', 15000],
    [3, '腰包', '#f3f5f4', 1000],
    [4, '老舊袋子', '#8a8c8b', 100],
    [5, '科技碎片', '#afd0c9', 1]
]
items = []

# 視窗
win = tk.Tk()

screen_w = win.winfo_screenwidth()  # 輸出螢幕寬度
screen_h = win.winfo_screenheight()  # 輸出螢幕高度
win_w = 310
win_h = 315
win_x = (screen_w - win_w) / 2
win_y = (screen_h - win_h) / 2

win.geometry('%dx%d+%d+%d' % (win_w, win_h, win_x, win_y))
win.config(bg=bg_color)

win.title('我要大背包!!')


class Items:

    def __init__(self, index, name, main_color, weight):
        self.index = index
        self.name = name
        self.main_color = main_color
        self.btn = tk.Button()
        self.en = tk.Entry()
        self.lab = tk.Label()
        self.light = tk.Label()
        self.weight = weight
        self.amount = 0
        self.need = 0

    def create_item(self):
        self.light.config(bg=bg_color, width=1, height=1)
        self.light.grid(row=self.index, column=0)

        self.btn.config(text=self.name, bg=self.main_color,
                        font=my_font, width=10, command=self.choice_pack)
        self.btn.grid(row=self.index, column=1)

        self.en.config(bg=bgl_color, fg=fg_color,
                       font=my_font, width=5)
        self.en.grid(row=self.index, column=2)

        self.lab.config(bg=self.main_color, font=my_font, width=5)
        self.lab.grid(row=self.index, column=3)

    def choice_pack(self):
        for i in items:
            i.light.config(bg=bg_color)
        self.light.config(bg='skyblue')

        total_amount = 0
        goal = self.weight
        for i in items:
            if i.en.get().isdigit():
                i.amount = int(i.en.get())
                total_amount += i.amount * i.weight

        if total_amount > goal:
            lab_result.config(text='恭喜完成目標!!!')
            for i in range(0, len(items)):
                items[i].lab.config(text='')
        else:
            lab_result.config(text='進度達成 {:.0%}'.format(total_amount / goal))
            goal_need = goal - total_amount
            for i in range(0, self.index + 1):
                items[i].lab.config(text='')

            for i in range(self.index + 1, len(items)):
                items[i].need = goal_need // items[i].weight
                items[i].lab.config(text=f'{items[i].need}')
                goal_need %= items[i].weight


def reset():
    for i in range(len(items)):
        items[i].light.config(bg=bg_color)
        items[i].en.delete(0, "end")
        items[i].lab.config(text='')
        lab_result.config(text='歡 迎 使 用 !')
    pass


# -創建物件實體-
for i in packs:
    item = Items(i[0], i[1], i[2], i[3])
    item.create_item()
    items.append(item)

lab_result = tk.Label(bg=bgl_color, fg=fg_color, font=my_font, width=16,
                      text='歡 迎 使 用 !')
lab_result.grid(row=len(packs) + 1, column=1, columnspan=2)

btn_reset = tk.Button(bg=bgl_color, fg=fg_color, font=my_font, width=4, bd=0,
                      text='reset', command=reset)
btn_reset.grid(row=len(packs) + 1, column=3, columnspan=2)

win.mainloop()
