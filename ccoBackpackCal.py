import tkinter as tk

bg_color = '#1E1E1E'
win = tk.Tk()
win.geometry('350x300+400+280')
win.config(bg=bg_color)

win.iconbitmap('backpack.ico')
win.title('背包!')

packs = [
    # [[0]name,[1]color]
    ['自主儲存單位', '#ff2059'],
    ['公事包', '#e730c0'],
    ['探險家背包', '#ccc541'],
    ['腰包', '#f3f5f4'],
    ['老舊袋子', '#8a8c8b'],
    ['科技碎片', '#afd0c9']
]
items = []


class Items:
    def __init__(self, name, main_color):
        self.name = name
        self.main_color = main_color


# --
for i in packs:
    item = Items(name=i[0], main_color=i[1])
    items.append(item)

for i in items:
    print(i.name)

win.mainloop()
