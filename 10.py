import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton 
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import Menu

def operation():
    a=int(f_int.get())
    b=int(s_int.get())
    c=combo.get()

    if   c=='+':
        calc=a + b
    elif c=='-':
        calc=a - b
    elif c=='*':
        calc=a * b
    elif c=='/':
        calc=a / b

    res=f"= {calc}"
    lbl.configure(text=res)

def clicked():                                                                  
    rbutton=var.get()                                                          
    if rbutton==1:
        text="первый"
    elif rbutton==2:
        text="второй"
    elif rbutton==3:
        text="третий"
    return messagebox.showinfo("Вариант", f'Вы выбрали {text} вариант')

def open_file():
    with open ('loadtext.txt', 'r', encoding='utf-8-sig') as file:
        scroll.insert('1.0', file.readlines())


root=Tk()                                                                         
root.title("Кустов Александр Викторович")                                      
root.geometry('360x240')                                                        

menu=Menu(root)
new_item=Menu(menu, tearoff=0)
new_item.add_command(label='Открыть файл', command=open_file)
menu.add_cascade(label='Файл', menu=new_item)
root.config(menu=menu)

tab_control=ttk.Notebook(root)                                                  
tab1=ttk.Frame(tab_control)                                                     
tab2=ttk.Frame(tab_control)                                                     
tab3=ttk.Frame(tab_control)                                                     

tab_control.add(tab1, text='Первая')                                           
tab_control.add(tab2, text='Вторая')                                           
tab_control.add(tab3, text='Третья')                                           


# frame 1
f_int=Entry(tab1, width=4)
s_int=Entry(tab1, width=4)
combo=Combobox(tab1, width=2)
combo['values'] = ('+', '-', '*', '/')
combo.current(0)                                                               
lbl=Label(tab1, text='=')
btn=Button(tab1, text='Вычислить', command=operation)
f_int.grid(column=1, row=0)
combo.grid(column=2, row=0)
s_int.grid(column=3, row=0)
lbl.grid(column=4, row=0)
btn.grid(column=5, row=1)


# frame 2
var=IntVar()

rad1=Radiobutton(tab2, text='Первый', variable=var, value=1, command=clicked)  
rad2=Radiobutton(tab2, text='Второй', variable=var, value=2, command=clicked)  
rad3=Radiobutton(tab2, text='Третий', variable=var, value=3, command=clicked)  
rad1.grid(column=0, row=0)  
rad2.grid(column=1, row=0)  
rad3.grid(column=2, row=0)  

# frame 3
scroll=scrolledtext.ScrolledText(tab3)
scroll.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')                                       

root.mainloop()
