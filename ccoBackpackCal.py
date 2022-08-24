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
win.geometry('350x300+400+280')
win.config(bg=bg_color)

win.iconbitmap('backpack.ico')
win.title('!背包')


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
        self.light.config(bg='yellow')

        total_amount = 0
        goal = self.weight
        for i in items:
            if i.en.get().isdigit():
                i.amount = int(i.en.get())
                total_amount += i.amount * i.weight

        if total_amount > goal:
            print('畢業了')
        else:
            goal_need = goal - total_amount
            for i in range(self.index + 1, len(items)):
                items[i].need = goal_need // items[i].weight
                items[i].lab.config(text=f'{items[i].need}')
                goal_need %= items[i].weight


# -創建物件實體-
for i in packs:
    item = Items(index=i[0], name=i[1], main_color=i[2], weight=i[3])
    item.create_item()
    items.append(item)

# -確認用-
for i in items:
    print(i.index, i.name, i.main_color, i.weight)

win.mainloop()