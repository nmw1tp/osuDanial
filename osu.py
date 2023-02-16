from tkinter import *

from random import *

window = Tk()

window.geometry(f"1024x768+0+0") # Размеры и положение

window.title("Поймай шарик")

c=Canvas(window, width=600, height=600, bg='lightblue')

p=Canvas(window, width=600, height=100, bg='lightgreen')

c.pack();  p.pack()

colors=['green', 'red', 'blue', 'orange', 'yellow','purple']

words=['Лови','Ну же','Ты можешь','Давай еще',

       'Ты точно туда нажал?','Ты чемпион',

       'Да левая клавиша а не правая ;)']

k=0

def ball():

    global k

    c.delete(ALL)

    x=randint(10, 580)

    y=randint(10, 580)

    r=randint(5, 50)

    new_ball=c.create_oval(x, y, x+r, y+r, fill=choice(colors))

    c.tag_bind(new_ball, '<Button-1>', click)

    window.after(4000-k*50, ball)

    c.create_text(250, 15, font='Arial 18', text=choice(words))

def click(event):

    global k

    k= k + 1

    p.delete(ALL)

    p.create_text(80,30,font='Arial 18',text='Попаданий: '+str(k))

    if k>30:

        p.create_text(200,50,font='Arial 16',text='Уже сложнее? ;)')

    if k>50:

        p.create_text(200,70,font='Arial 14',text='Спорим что не наберешь 80? ;)')

ball()

p.create_text(200,30,font='Arial 18',text='Нажимай на шарик и выигрывай')

window.mainloop()
