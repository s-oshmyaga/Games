#!/usr/bin/env python3
""" Начальное окно с предложением выбрать игру """

from tkinter import *


def dices():
    root.destroy()
    import dice_game


def rps():
    root.destroy()
    import Rock_Paper_Scissors


def gallows():
    root.destroy()
    import gallows


root = Tk()
root.title('Мини-игры')
root.geometry('350x250')
root.resizable(width=False, height=False)

label_root = Label(text='''Добро пожаловать в мини-игры.
Выберите, в какую игру 
вы хотите сыграть''', font=('Arial Bold', 14))
label_root.pack(pady=5, padx=5)

btn_dice = Button(text='Игра в кости', command=dices, font='Arial 11')
btn_dice.pack(padx=3, pady=3)

btn_RPS = Button(text='Камень, ножницы, бумага', command=rps, font='Arial 11')
btn_RPS.pack(pady=3, padx=3)

btn_RPS = Button(text='Виселица', command=gallows, font='Arial 11')
btn_RPS.pack(pady=3, padx=3)

root.mainloop()


