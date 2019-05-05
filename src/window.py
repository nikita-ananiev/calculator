from calculate import *
from run import *
import tkinter as tk
from tkinter import messagebox


# Создание главного окна
win = tk.Tk()
win.title('Мой калькулятор')
win.resizable(False, False)

# Создание строки ввода выражения
line = tk.Entry(win, font=("Courier New", 24))
line.pack(fill=tk.X)
line.focus_set()

# Создание области кнопок
frame = tk.Frame(win)
frame.pack(expand=True)

# Юникод-символы backspace и смены знака
bsp = '\u232B'
sig = '\u00B1'

# Тексты кнопок
buttons = [
    bsp, 'C', '(', ')', '?',
    '7', '8', '9', '/', '%',
    '4', '5', '6', '*', '^',
    '1', '2', '3', '-', '!',
    sig, '0', '.', '+', '='
]


# Функция проверки: является ли символ цифрой или десятичным разделителем
def is_digit_or_decimal(c):
    return c.isdigit() or c == '.'


# Функция-обработчик нажатия (большинства) кнопок
def common_pressed(text):
    cursor_position = line.index(tk.INSERT)
    line.insert(cursor_position, text)


# Функция-обработчик нажатия кнопки результата (=)
def result_pressed():
    expression = line.get()
    line.delete(0, last=tk.END)
    line.insert(0, calculate(expression))


# Функция-обработчик нажатия кнопки очистки выражения (С)
def clean_pressed():
    line.delete(0, last=tk.END)


# Функция-обработчик нажатия кнопки справки (?)
def about_pressed():
    messagebox.showinfo(
        "Авторы", "Модуль расчета:\nАнаньев Никита"
        "\n-----------------------------------\n"
        "Оконное приложение:\nМихайлова Александра")


# Функция-обработчик нажатия кнопки backspace
def bs_pressed():
    cursor_position = line.index(tk.INSERT)
    line.delete(cursor_position - 1, cursor_position)


# Функция-обработчик нажатия кнопки смены знака
def sign_pressed():
    expression = line.get()
    cursor_position = line.index(tk.INSERT)
    number = ''
    i = cursor_position
    while i > 0 and is_digit_or_decimal(expression[i-1]):
        number = expression[i-1] + number
        i -= 1
    first = i
    i = cursor_position
    while i < len(expression) and is_digit_or_decimal(expression[i]):
        number = number + expression[i]
        i += 1
    if len(number) == 0:
        return
    last = i
    if first > 1 and last < len(expression) and expression[first-2:first] == "(-" and expression[last] == ")":
        line.delete(first-2, last+1)
        line.insert(first-2, number)
    else:
        line.delete(first, last)
        line.insert(first, "(-" + number + ")")
        line.icursor(last + 2)


# Функция-обработчик (верхнего уровня) нажатия кнопки
def on_pressed(text):
    if text == '=':
        result_pressed()
    elif text == 'C':
        clean_pressed()
    elif text == '?':
        about_pressed()
    elif text == bsp:
        bs_pressed()
    elif text == sig:
        sign_pressed()
    else:
        common_pressed(text)


# Функция-обработчик выбора функции (и вставка ее в выражение)
def insert_function(function):
    arg_count = funccountarg[function]
    cursor_position = line.index(tk.INSERT)
    if arg_count > 0:
        line.insert(cursor_position, function +
                    "(" + "," * (arg_count-1) + ")")
        line.icursor(cursor_position + len(function) + 1)
    else:
        line.insert(cursor_position, function)
        line.icursor(cursor_position + len(function))


# Создание кнопок
for i in range(len(buttons)):
    text = buttons[i]
    row = i // 5 + 1
    column = i % 5
    button = tk.Button(frame, width=3, text=text, font=(
        "Courier New", 30, 'bold'), command=lambda t=text: on_pressed(t))
    button.grid(row=row, column=column)
    if text == '=':
        default_button = button
# Привязка кнопки '=' к нажатию ENTER
win.bind('<Return>', (lambda e, b=default_button: b.invoke()))


# Создание меню вставки функций
func_list = funccountarg.keys()
functions = tk.Menubutton(win, text="Вставить функцию...",
                          font=("Courier New", 20, 'bold'))
functions.pack(fill=tk.X)
menu = tk.Menu(functions, tearoff=False, font=("Courier New", 20, 'bold'))
for func_name in func_list:
    menu.add_command(
        label=func_name, command=lambda text=func_name: insert_function(text))
functions['menu'] = menu


# Запуск оконного приложения
win.mainloop()
