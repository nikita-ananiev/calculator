from calculate import *
from tkinter import *

win = Tk()
win.title('Calculator')
win.geometry('490x500')
win.resizable(False, False)

line = Entry(win, font=("Courier New", 30))
line.grid(row=0, column=0, columnspan=4)

def button1pressed():
    line.insert(len(line.get()), '1')
button1 = Button(win, text='1', font=("Courier New", 30, 'bold'), command=button1pressed)
button1.grid(row=1, column=0)

def button2pressed():
    line.insert(len(line.get()), '2')
button2 = Button(win, text='2', font=("Courier New", 30, 'bold'), command=button2pressed)
button2.grid(row=1, column=1)

def button3pressed():
    line.insert(len(line.get()), '3')
button3 = Button(win, text='3', font=("Courier New", 30, 'bold'), command=button3pressed)
button3.grid(row=1, column=2)

def buttonPluspressed():
    line.insert(len(line.get()), '+')
buttonPlus = Button(win, text='+', font=("Courier New", 30), command=buttonPluspressed)
buttonPlus.grid(row=1, column=3)

def button4pressed():
    line.insert(len(line.get()), '4')
button4 = Button(win, text='4', font=("Courier New", 30, 'bold') ,command=button4pressed)
button4.grid(row=2, column=0)

def button5pressed():
    line.insert(len(line.get()), '5')
button5 = Button(win, text='5', font=("Courier New", 30, 'bold'), command=button5pressed)
button5.grid(row=2, column=1)

def button6pressed():
    line.insert(len(line.get()), '6')
button6 = Button(win, text='6', font=("Courier New", 30, 'bold'), command=button6pressed)
button6.grid(row=2, column=2)

def buttonMinuspressed():
    line.insert(len(line.get()), '-')
buttonMinus = Button(win, text='-', font=("Courier New", 30), command=buttonMinuspressed)
buttonMinus.grid(row=2, column=3)

def button7pressed():
    line.insert(len(line.get()), '7')
button7 = Button(win, text='7', font=("Courier New", 30, 'bold'), command=button7pressed)
button7.grid(row=3, column=0)

def button8pressed():
    line.insert(len(line.get()), '8')
button8 = Button(win, text='8', font=("Courier New", 30, 'bold'),command=button8pressed)
button8.grid(row=3, column=1)

def button9pressed():
    line.insert(len(line.get()), '9')
button9 = Button(win, text='9', font=("Courier New", 30, 'bold'), command=button9pressed)
button9.grid(row=3, column=2)

def buttonMulpressed():
    line.insert(len(line.get()), '*')
buttonMul = Button(win, text='*', font=("Courier New", 30), command=buttonMulpressed)
buttonMul.grid(row=3, column=3)

def buttonDecimalpressed():
    line.insert(len(line.get()), '.')
buttonDecimal = Button(win, text='.', font=("Courier New", 30), command=buttonDecimalpressed)
buttonDecimal.grid(row=4, column=0)

def button0pressed():
    line.insert(len(line.get()), '0')
button0 = Button(win, text='0', font=("Courier New", 30, 'bold'), command=button0pressed)
button0.grid(row=4, column=1)

def buttonResultpressed():
    expression = line.get()
    line.delete(0, last=END)
    line.insert(0, calculate(expression))
buttonResult = Button(win, text='=', font=("Courier New", 30), command=buttonResultpressed)
buttonResult.grid(row=4, column=2)

def buttonDivpressed():
    line.insert(len(line.get()), '/')
buttonDiv = Button(win, text='/', font=("Courier New", 30), command=buttonDivpressed)
buttonDiv.grid(row=4, column=3)

win.mainloop()

