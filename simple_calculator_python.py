import tkinter as tk
from tkinter import Button, Entry
window = tk.Tk()

def cal ():
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        amal1 = amal.get()
        if amal1 == "+":
            jame= num1 + num2
            print(jame)
        elif amal1 == "-":
           menha=num1 - num2
           print(menha)
        elif amal1 == "*":
           zarb= num1 * num2
           print(zarb)
        elif amal1 == "/":
           tagsim= num1 / num2
           print(zarb)
        else:
           print("error")

entry1 = Entry(window)
entry1.pack()

amal = Entry(window)
amal.pack()

entry2 = Entry(window)
entry2.pack()

button1=Button(window, text="calculate")
button1.config(command=cal)
button1.pack()

window.mainloop()
