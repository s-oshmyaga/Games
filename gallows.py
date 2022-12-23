""" Виселица """
import random
from tkinter import *

stages = {0: ' ',
          1: '''
    
|     
|     
|     
|     
|   ''',
          2: '''
 ___
|    
|   
|
|
|    
''',
          3: '''
 ___
|   |
|   0
|    
|
|''',
          4: '''
 ___
|   |
|   0
|   |
|
|    ''',
          5: '''
 ___
|   |
|  \\0/
|   |
|
|    ''',
          6: '''
 ___
|   |
|  \\0/
|   |
|  / \\
|    ''',
          7: '''
 ___
|   |
|  \\0/
|   |
|  / \\
|  ...  '''}


words = 'болячка болото артистизм аспирантура арбитр аншлаг астроном выбоина грабитель ' \
        'гостиная грузовик заменитель зажим злоумышленник импровизация иллюзионист ' \
        'картон карман кастрюля категория лакомство лаборатория навигация нагрев общество ' \
        'олимпиец пахарь погрешность проект рыбалка рукопожатие смирение ' \
        'стрела страница тумбочка туман фальшивка фанатик ушиб хитрюга шахматист ' \
        'ширпотреб электричка янтарь ягуар якорь'.split()
user_mistakes = 0
result = []
word_choice = ''


def lbl_stages(mistake):
    """Изменения рисунков виселицы"""
    mistakes = f'Количество \n ошибок - {mistake}'
    stage_picture = stages[mistake]
    lbl_gallows['text'] = mistakes + '\n' + stage_picture


def start_game():
    """Вывод загаданного слова"""
    global user_mistakes
    global word_choice
    global result
    user_mistakes = 0
    word_choice = random.choice(words)
    result = ['_' for _ in range(len(word_choice))]
    lbl_word['text'] = ' '.join(result)
    lbl_stages(user_mistakes)
    enr_letter.delete(0, END)
    btn_enter.config(state='normal')


def check(character):
    global word_choice
    global result
    global user_mistakes
    if character in word_choice:
        for sign in range(len(result)):
            if word_choice[sign] == character:
                result[sign] = word_choice[sign]
                lbl_message['text'] = 'Есть такая буква'
                lbl_word['text'] = ' '.join(result)
        if '_' not in result:
            lbl_message['text'] = 'Ваша победа'
            btn_enter.config(state='disabled')
    else:
        lbl_message['text'] = 'Нет такой буквы'
        user_mistakes += 1
        if user_mistakes == 7:
            lbl_message['text'] = 'Вы проиграли'
            lbl_word['text'] = ' '.join(word_choice)
            btn_enter.config(state='disabled')
    lbl_stages(user_mistakes)
    enr_letter.delete(0, END)


def enter():
    letter = enr_letter.get().lower()
    if not letter:
        lbl_message['text'] = 'Вы ничего не ввели'
    elif len(letter) > 1:
        lbl_message['text'] = 'Введите одну букву'
    else:
        check(letter)


window = Tk()
window.title('Виселица')
window.resizable(width=False, height=False)


lbl_gallows = Label(text='', bg='black', fg='white', justify=LEFT, width=15)
lbl_gallows.grid(row=0, rowspan=6, column=0, sticky='ns')

lbl_title = Label(text='Введите букву', font=('Arial Bold', 12), justify=CENTER, width=17)
lbl_title.grid(row=0, column=1, columnspan=2)

lbl_word = Label(text='', font='Arial 12', width=17, height=2)
lbl_word.grid(row=1, column=1, columnspan=2)

lbl_message = Label(text='', font='Arial 11', justify=CENTER, width=19, fg='green')
lbl_message.grid(row=2, column=1, columnspan=2)

enr_letter = Entry(bg='black', fg='white', width=5, font='Arial 14', justify=CENTER)
enr_letter.grid(row=3, column=1, columnspan=2, sticky='ew')

btn_enter = Button(text='Ввод', command=enter)
btn_enter.grid(row=4, column=1, columnspan=2, sticky='ew')

btn_restart = Button(text='Начать сначала', command=start_game)
btn_restart.grid(row=5, column=1, columnspan=2, sticky='ew')

start_game()
window.mainloop()
