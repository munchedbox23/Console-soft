from tkinter import *

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

window = Tk()
window.config(padx=50,pady=50,bg = YELLOW)
window.title("BMI Calculator")
window.geometry("600x600")
window.resizable(False,False)

photo = PhotoImage(file = "bmi calc/bmi calc.png")
canvas = Canvas(bg =YELLOW,width=photo.width(),height=photo.height())
canvas.create_image(photo.width()/2,photo.height()/2,image = photo)
canvas.image = photo
canvas.place(x = 150,y = 0)


def calc():
    weight_value = float(weight.get())
    height_value = float(height.get())
    imt_value = weight_value // height_value**2
    bmi = Label(text = round(imt_value,1),font = ("Arial",30,"bold"),bg = YELLOW)
    bmi.place(x = 355,y = 354)


lang = StringVar(value="Мужчина")

manbutton = Radiobutton(bg = YELLOW,text="Мужчина",value="Мужчина",variable=lang,font = ("Arial",12,"bold"))
manbutton.place(x = 55,y = 305)

womanbutton = Radiobutton(bg = YELLOW,text="Женщина",value="Женщина",variable=lang,font = ("Arial",12,"bold"))
womanbutton.place(x = 145,y = 305)

# Labels
your_danie = Label(text = "Данные про вас",bg = "#FFA07A",font = ("Arial",17,"bold"))
your_danie.place(x = 20,y = 250)
pol = Label(text = "Пол:",font = ("Arial",17,'bold'),bg = YELLOW)
pol.place(x = 0,y = 300 )
wight_label = Label(text = "Вес: ",font = ("Arial",17,"bold"),bg = YELLOW)
wight_label.place(x = 0, y = 350)
height_label = Label(text = "Рост: ",font = ("Arial",17,"bold"),bg = YELLOW)
height_label.place(x = 0, y = 400)
kg = Label(text = "кг ",font = ("Arial",17,"bold"),bg = YELLOW)
kg.place(x = 100, y = 350)
m = Label(text = "метра",font = ("Arial",17,"bold"),bg = YELLOW)
m.place(x = 110, y = 400)
age = Label(text = "Возраст:",font = ("Arial",17,"bold"),bg = YELLOW)
age.place(x = 0, y = 450)


# Entries
weights = Entry(window,width=5)
weights.place(x=60, y=360)
heights = Entry(window,width=5)
heights.place(x=70, y=410)

age_txt = Entry(width=5)
age_txt.place(x = 110,y = 460)


weight = Entry(width=5)
weight.place(x=60, y=360)
height = Entry(width=5)
height.place(x=70, y=410)



your_bmi = Label(text = "Ваш Имт",bg = "#FFA07A",font = ("Arial",17,"bold"))
your_bmi.place(x = 350,y = 320)

calc_button = Button(text = "Рассчитать",bd = 5,font = ("Arial",15,"bold"),command=calc,bg="#00FF7F")
calc_button.place(x = 0, y = 500)

window.mainloop()
