from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("300x300")

firs_num = Text(window,width = 5,height = 3)
firs_num.place(x = 30, y = 10)

radio_state = IntVar
znak1 = Radiobutton(text = "+", value = 1,variable = radio_state)
znak2 = Radiobutton(text = "-", value = 2,variable = radio_state)
znak3 = Radiobutton(text = "*", value = 3,variable = radio_state)
znak4 = Radiobutton(text = "/", value = 4,variable = radio_state)

window.mainloop()
