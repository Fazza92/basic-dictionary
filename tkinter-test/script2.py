from tkinter import *

window = Tk()


def kg_to_gpo():
  grams= (e1_value.get())*1000
  pounds = float(e1_value.get())*2.20462
  ounces = float(e1_value.get())*35.274
  t1.insert(END, grams,pounds,ounces)


b1 = Button(window, text="Kg")
b1.grid(row=0, column=1)

b2 = Button(window)
b2.grid(row=0, column=2)

b3=Button(window,text="Convert",command=kg_to_gpo)
b3.grid(row=0,column=3)


e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
