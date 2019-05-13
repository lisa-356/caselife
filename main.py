'''Case Life
Developers: Savenkova Liza(60%), Slobodchikov Stepan (40%)'''

from tkinter import *
from random import randint
from time import sleep
from tkinter import messagebox

from class1 import *
from local import *

print(HELLO)

SIZE = 0
rectangle_size, x, y = 10, 10, 10

tags = []
grid = []


# Main Tkinter window -------------------------------------------------

def main():
    global tags, grid, SIZE, x, y, rectangle_size

    def find_rect_coordinates(x, y):
        """Найти координаты прямоугольника, который был нажат"""
        return x - x % 10, y - y % 10

    def change_color(event):
        """ Изменение цвета нажатой сетки и изменение состояния ячейки в сетке"""

        x, y = find_rect_coordinates(event.x, event.y)
        try:
            iy = int(x / 10 - 1)
            ix = int(y / 10 - 1)
            if ix == -1 or iy == -1:
                raise IndexError
            if grid[ix][iy].isAlive:
                canvas.itemconfig(tags[ix][iy], fill="black")
            else:
                canvas.itemconfig(tags[ix][iy], fill="green")
            grid[ix][iy].changeStatus()
        except IndexError:
            return

    def paint_grid():
        for i in grid:
            for j in i:
                if j.nextStatus != j.isAlive:
                    x, y = j.position_matrix
                    if j.nextStatus:
                        canvas.itemconfig(tags[x][y], fill="green")
                    else:
                        canvas.itemconfig(tags[x][y], fill="black")
                    j.changeStatus()

    def changeInStatus(cell):
        ''' Если состояние ячейки изменяется в следующем поколении, возвращаем True, иначе False'''
        num_alive = 0
        x, y = cell.position_matrix
        for i in (x - 1, x, x + 1):
            for j in (y - 1, y, y + 1):
                if i == x and j == y:
                    continue
                if i == -1 or j == -1:
                    continue
                try:
                    if grid[i][j].isAlive:
                        num_alive += 1
                except IndexError:
                    pass
        if cell.isAlive:
            return not (num_alive == 2 or num_alive == 3)
        else:
            return num_alive == 3

    def begin_game():
        for i in grid:
            for j in i:
                if changeInStatus(j):
                    j.nextStatus = not j.isAlive
                else:
                    j.nextStatus = j.isAlive
        paint_grid()
        global begin_id
        begin_id = root.after(200, begin_game)

    def stop_game():
        root.after_cancel(begin_id)

    root = Tk()
    root.title("LIFE")

    frame = Frame(root, width=SIZE, height=SIZE)
    frame.pack()

    canvas = Canvas(frame, width=SIZE, height=SIZE)
    canvas.pack()

    for i in range(int(SIZE / rectangle_size)):
        tags.append([])
        grid.append([])
        for j in range(int(SIZE / rectangle_size)):
            tag = canvas.create_rectangle(x, y,
                                          x + rectangle_size,
                                          y + rectangle_size,
                                          fill='black')
            tags[i].append(tag)
            grid[i].append(Cell(x, y, i, j))
            x += rectangle_size
        x = rectangle_size
        y += rectangle_size

    start = Button(root, text="Start!", command=begin_game)
    start.pack(side=LEFT)
    stop = Button(root, text="Stop!", command=stop_game)
    stop.pack(side=RIGHT)
    canvas.bind('<Button-1>', change_color)
    root.mainloop()


def ask():
    """Размер поля"""
    global SIZE

    def choice(event):

        global SIZE
        SIZE = size_entry.get()

        try:
            SIZE = int(SIZE)
        except ValueError:
            messagebox.showinfo('Ошибка', 'Данные введены некорректно!\nРазмер поля по умолчанию: 500x500.')
            SIZE = 500
        root.destroy()
        main()

    root = Tk()

    root.title('LIFE')
    root["bg"] = '#d8c2ff'
    root.geometry('450x100')
    label = Label(root, text="Задайте ширину поля(>100):", bg='#d8c2ff',
                  fg='#3d2859', font="Arial 16")
    message_button = Button(text="START", width=10, height=2, bg='#1476ff',
                            fg='#ffffff')
    size_entry = Entry(root, width=13)

    label.grid(row=0, column=0, padx=5, sticky="w")
    size_entry.grid(row=0, column=1, padx=5, pady=5)
    message_button.grid(row=1, column=1, padx=5, pady=10)

    message_button.bind("<Button-1>", choice)

    root.mainloop()



ask()


