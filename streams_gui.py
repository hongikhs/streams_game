from tkinter import *
import random

a = list(range(1,11))
b = list(range(11,20))
c = list(range(20,31))
j = ['*']
d = a + b + b + c + j
n = 1
print(d)
random.shuffle(d)
print(d)

def popNumber():
    global n
    if n < 20:
        num = d.pop(0)
        label['text'] = num
        n += 1
    button['text'] = str(n) + '번째 숫자 뽑기'

wd = Tk()
wd.title("스트림스")
label = Label(wd, text='준비', font='helvetica 100 bold')
button = Button(wd, text='1번째 숫자 뽑기', font='helvetica 40 bold', command=popNumber)

label.pack()
button.pack()
wd.mainloop()
