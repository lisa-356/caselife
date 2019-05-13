from tkinter import *


class Cell:
    def __init__(self, x, y, i, j):
        self.isAlive = False
        self.nextStatus = None
        self.position_screen = (x, y)
        self.position_matrix = (i, j)

    def __str__(self):
        return str(self.isAlive)

    def __repr__(self):
        return str(self.isAlive)

    def changeStatus(self):
        self.isAlive = not self.isAlive


"""
class Rectangle():


    def __init__(self, canvas, tag, count_click):

        self.canvas = canvas
        self.tag = tag
        self.count_click = count_click

    def color(self, event):
        self.canvas.itemconfig(self.tag, fill='green')



class Board():

    def __init__(self, root, size):

        self.root = root
        self.height = size
        self.width = size
        self.step = 20
        self.show_board()

    def show_board(self):

        return canvas

"""
