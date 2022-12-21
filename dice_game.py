""" Игра в кости """
from tkinter import *
import random

dices = {'1': '''
   
 * 
   ''',
         '2': """
  *
   
*  """,
         '3': """
*  
 * 
  *""",
         '4': '''
* *
   
* *''',
         '5': '''
* *
 * 
* *''',
         '6': '''
***
   
***'''}


def roll():
    dice_1 = str(random.randint(1, 6))
    dice_2 = str(random.randint(1, 6))
    dice_label_1['text'] = dices[dice_1]
    dice_label_2['text'] = dices[dice_2]


window = Tk()
window.title('Игра в кости')
window.geometry('250x150')
window.resizable(width=False, height=False)

label = Label(text='Брось кости', justify=CENTER, font='Arial 14')
label.pack(pady=3, padx=3)

frame = Frame(bg='black')
frame.pack(padx=3, pady=3)

dice_label_1 = Label(text='', justify=CENTER, fg='white', master=frame, bg='black', width=15, height=3)
dice_label_1.pack(pady=3, padx=3, side=LEFT)
dice_label_2 = Label(text='', justify=CENTER, fg='white', master=frame, bg='black', width=15, height=3)
dice_label_2.pack(pady=3, padx=3, side=LEFT)

button = Button(text='Бросить', command=roll)
button.pack(padx=3, pady=3)


window.mainloop()
