""" Игра камень, ножницы, бумага """
import random
from tkinter import *


data = {'1': 'Камень',
        '2': 'Ножницы',
        '3': 'Бумага'}


def pk_choice():
    choice = random.randint(1, 3)
    return choice


def comparison(user, pk):
    """ Результат выбора """
    result = user - pk
    if result == 0:
        score(1, 1)
        return 'НИЧЬЯ'
    elif result in (2, -1):
        score(1, 0)
        return 'ПОБЕДА'
    else:
        score(0, 1)
        return 'ПОРАЖЕНИЕ'


def to_start():
    """Обнуление результатов"""
    global user_score
    global pk_score
    user_score = 0
    pk_score = 0
    label_score['text'] = f'{user_score} - {pk_score}'
    label_result['text'] = ''


def score(user, pk):
    """ Подсчет очков """
    global user_score
    global pk_score
    user_score += user
    pk_score += pk
    label_score['text'] = f'{user_score} - {pk_score}'


def btn_command(value):
    users_choice = int(value)
    pk_ch = pk_choice()
    result = comparison(users_choice, pk_ch)
    label_result['text'] = result


window = Tk()
window.geometry('350x200')
window.title('Камень, ножницы, бумага')
window.resizable(width=False, height=False)

user_score = 0
pk_score = 0

label = Label(text='Сыграем в игру. Делай свой выбор', font=('Arial Bold', 14))
label.pack(padx=3, pady=3)

label_result = Label(text='', fg='green', bg='black', font='Arial 14', height='2', width=20, justify=CENTER)
label_result.pack(padx=3, pady=3)

label_score = Label(text='0 - 0', justify=CENTER)
label_score.pack(padx=3, pady=3)


def buttons():
    frame = Frame()
    frame.pack(padx=3, pady=3, fill=BOTH)
    for key, value in data.items():
        cmd = lambda x=key: btn_command(x)
        btn = Button(text=value, command=cmd, width=9, justify=CENTER, height=2, master=frame)
        btn.pack(pady=3, padx=7, side=LEFT)


btn_start = Button(text='Начать с начала', command=to_start)
btn_start.pack(padx=3, pady=3)


def main():
    buttons()
    window.mainloop()


main()
