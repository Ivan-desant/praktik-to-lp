from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
root=Tk()
root.title('Ижокин Иван Евгеньевич')
root.geometry('450x360')

style=ttk.Style()
style.configure('TNotebook', tabposition='n')
style.configure('TNotebook.Tab', padding=[49, 0, 49, 0])

tab_control=ttk.Notebook(root, style='TNotebook')
tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab3=ttk.Frame(tab_control)
tab_control.add(tab1, text='№1')
tab_control.add(tab2, text='№2')
tab_control.add(tab3, text='№3')
tab_control.pack(expand=1, fill='both')

#1
def butfunc():
    num1=ent1.get()
    num2=ent2.get()
    znak=combo.get()
    try:
        num1=int(num1)
        num2=int(num2)
        if znak in '+-/*':
            res=eval(f'{num1}{znak}{num2}')
            labelres.configure(text=res)
        else:
            labelres.configure(text='Выберите оператор')
    except ValueError:
        labelres.configure(text='Введите числа!')


ent1=Entry(tab1, width=5)
ent2=Entry(tab1, width=5)
labelres=Label(tab1, text='')
resbut=Button(tab1, text='Запуск', command=butfunc)
combo=Combobox(tab1, width=3)
combo['values']=('+', '-', '/', '*', '')
combo.current(4)
labelrv=Label(tab1, text='=')
ent1.grid(column=0, row=0)
ent2.grid(column=3, row=0)
combo.grid(column=2, row=0)
labelrv.grid(column=4, row=0)
labelres.grid(column=5, row=0)
resbut.grid(column=3, row=3)

#2
def butprovfunc():
    txt=selected.get()
    lblres.configure(text=f'Вы выбрали {txt}')

lblres=Label(tab2, text='')
butprov=Button(tab2, text='Проверка', command=butprovfunc)
selected=StringVar()
chk1=Radiobutton(tab2, text='Первый', value='Первый вариант', variable=selected)
chk2=Radiobutton(tab2, text='Второй', value='Второй вариант', variable=selected)
chk3=Radiobutton(tab2, text='Третий', value='Третий вариант', variable=selected)
chk1.grid(column=0, row=0)
chk2.grid(column=0, row=1)
chk3.grid(column=0, row=2)
butprov.grid(column=0, row=3)
lblres.grid(column=3, row=4)

#3
def input_file():
    tfile=entfi.get()
    text_file=''
    try:
        with open(tfile, 'r') as f:
            for i in f:
                text_file+=i
        window=Toplevel()
        window.title('Содержимое файла')
        label_input=Label(window, text=text_file)
        label_input.pack()
    except:
        messagebox.showerror('Ошибка', 'Такого файла нет')
def help_menu():
    lbl_help.config(text='Упс, пока не придумал')
def menuframe():
    but1=Button(tab3, text='Вывести содержимое', command=input_file)
    but1.grid(column=0, row=3)
    but2=Button(tab3, text='Еще', command=help_menu, width=18)
    but2.grid(column=0, row=4)
    def delet():
        but1.grid_forget()
        but2.grid_forget()
        but3.grid_forget()
        lbl_help.config(text='')
        entfi.delete(0, 'end')
    but3=Button(tab3, text='Выйти', command=delet, width=18)
    but3.grid(column=0, row=5)
entfi=Entry(tab3)
lbl_file=Label(tab3, text='Файл:')
butmenu=Button(tab3, text='Меню', command=menuframe, width=18)
lbl_help=Label(tab3, text='')
lbl_file.grid(column=0, row=0)
entfi.grid(column=1, row=0)
butmenu.grid(column=0, row=2)
lbl_help.grid(column=0, row=6)
root.mainloop()
