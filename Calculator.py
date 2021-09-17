from tkinter import *


def updateTextFill(num):
    global text_string
    text_string += str(num)
    text_label.set(text_string)

def equal():
    global text_string
    try:
        total = str(eval(text_string))
        text_string = total
        text_label.set(text_string)
        text_string = ""
    except SyntaxError:
        text_string = ""
        text_label.set(text_string)
    except ZeroDivisionError:
        text_string = ""
        text_label.set("ERROR")

def delete():
    global text_string
    text_string = ""
    text_label.set(text_string)

window = Tk()
text_string = ""
text_label = StringVar()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int(screen_width / 2 - 500/2);
window_y = int(screen_height / 2 - 500/2);
window.geometry("315x447+{}+{}".format(str(window_x), str(window_y)))
window.title("Calculator")
textLabel = Label(window, textvariable = text_label,  bg = "white", font = ("Arial", 30, "bold"), width = 50)
textLabel.pack()

frame = Frame(window)
frame.pack()

but1 = Button(frame, text = "1", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill(1))
but1.grid(row = 0, column = 0)
but2 = Button(frame, text = "2", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill(2))
but2.grid(row = 0, column = 1)
but3 = Button(frame, text = "3", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill(3))
but3.grid(row = 0, column = 2)
but4 = Button(frame, text = "4", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill(4))
but4.grid(row = 1, column = 0)
but5 = Button(frame, text = "5", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill(5))
but5.grid(row = 1, column = 1)
but6 = Button(frame, text = "6", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill(6))
but6.grid(row = 1, column = 2)
but7 = Button(frame, text = "7", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill(7))
but7.grid(row = 2, column = 0)
but8 = Button(frame, text = "8", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill(8))
but8.grid(row = 2, column = 1)
but9 = Button(frame, text = "9", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill(9))
but9.grid(row = 2, column = 2)
but0 = Button(frame, text = "0", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill(0))
but0.grid(row = 3, column = 0)
butPlus = Button(frame, text = "+", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill("+"))
butPlus.grid(row = 0, column = 3)
butSub = Button(frame, text = "-", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill("-"))
butSub.grid(row = 1, column = 3)
butMulti = Button(frame, text = "*", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill("*"))
butMulti.grid(row = 2, column = 3)
butDiv = Button(frame, text = "/", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill("/"))
butDiv.grid(row = 3, column = 3)
butEqual = Button(frame, text = "=", font = ("Arial", 30), width = 3, height = 1, command = equal)
butEqual.grid(row = 4, column = 3)
butDot = Button(frame, text = ".", font = ("Arial", 30), width = 3, height = 1, command = lambda: updateTextFill("."))
butDot.grid(row = 3, column = 1)
butDel = Button(frame, text = "Del", font = ("Arial", 30), width = 3, height = 1, command = delete)
butDel.grid(row = 3, column = 2)




window.mainloop()