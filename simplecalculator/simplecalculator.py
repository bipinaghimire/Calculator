from tkinter import *
main = Tk()
main.title('CALCULATOR')
main.configure(bg='red')
main.iconbitmap('C:/Users/user/Desktop/calculator.ico')

e = Entry(main, width= 50, borderwidth=7, bg='yellow', fg='black')
e.grid(row=0, column=0, columnspan=4, padx=15, pady=20)
def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_clear():
    e.delete(0, END)
def button_add():
    first_number= e.get()
    global f_num
    global a
    a= 'add'
    f_num= float(first_number)
    e.delete(0, END)
def button_sub():
    first_number= e.get()
    global f_num
    global a
    a= 'sub'
    f_num= float(first_number)
    e.delete(0, END)
def button_mul():
    first_number= e.get()
    global f_num
    global a
    a= 'mul'
    f_num= float(first_number)
    e.delete(0, END)
def button_div():
    first_number= e.get()
    global f_num
    global a
    a='div'
    f_num= float(first_number)
    e.delete(0, END)
def button_power():
    first_number = e.get()
    global f_num
    global a
    a = 'power'
    f_num = float(first_number)
    e.delete(0, END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if a == 'add':
        e.insert(0, f_num + int(second_number))
    elif a=='sub':
        e.insert(0, f_num - int(second_number))
    elif a=='mul':
        e.insert(0, f_num * int(second_number))
    elif a=='div':
        e.insert(0, f_num / int(second_number))
    elif a== 'power':
        e.insert(0, f_num ** int(second_number))
def button_delete():
    length= len(e.get())
    e.delete(length-1, 'end')


button_1=Button(main, text="1", padx=38, pady=20, fg='white', bg='black', command=lambda: button_click(1))
button_2=Button(main, text="2", padx=38, pady=20, fg='white', bg='black', command=lambda: button_click(2))
button_3=Button(main, text="3", padx=39, pady=20, fg='white', bg='black', command=lambda: button_click(3))
button_4=Button(main, text="4", padx=38, pady=20, fg='white', bg='black', command=lambda: button_click(4))
button_5=Button(main, text="5", padx=38, pady=20, fg='white', bg='black', command=lambda: button_click(5))
button_6=Button(main, text="6", padx=39, pady=20, fg='white', bg='black', command=lambda: button_click(6))
button_7=Button(main, text="7", padx=38, pady=20, fg='white', bg='black', command=lambda: button_click(7))
button_8=Button(main, text="8", padx=38, pady=20, fg='white', bg='black', command=lambda: button_click(8))
button_9=Button(main, text="9", padx=39, pady=20, fg='white', bg='black', command=lambda: button_click(9))
button_0=Button(main, text="0", padx=38, pady=20, fg='white', bg='black',command=lambda: button_click(0))
button_decimal= Button(main, text='.', padx=39, pady=20, fg="yellow", bg="black",command=lambda: button_click('.'))
button_add=Button(main, text='+', padx=41, pady=20, fg='yellow', bg='black', command=button_add)
button_sub=Button(main, text='-', padx=42, pady=20, fg='yellow', bg='black', command=button_sub)
button_mul=Button(main, text='*', padx=42, pady=20, fg='yellow', bg='black', command=button_mul)
button_div=Button(main, text='/', padx=42, pady=20, fg='yellow', bg='black',  command=button_div)
button_equal=Button(main, text='=', padx=41, pady=20, fg='yellow', bg='black', command=button_equal)
button_clear=Button(main, text='Clear', padx=75, pady=20, fg='yellow', bg='black', command=button_clear)
button_del=Button(main, text='Del', padx=33, pady=20, fg='yellow', bg='black',command=button_delete)
button_power=Button(main, text='^', padx=38, pady=20, fg='yellow', bg='black',command=button_power)

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_equal.grid(row=5, column=3)
button_decimal.grid(row=4, column=1)
button_del.grid(row=5,column=0)
button_power.grid(row=4,column=2)

main.mainloop()
