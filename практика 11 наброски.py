from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.ttk import Combobox
root=Tk()
root.title('Ижокин Иван Евгеньевич')
root.geometry('450x360')

style=ttk.Style()
style.configure('TNotebook', tabposition='n')
style.configure('TNotebook.Tab', padding=[20, 10, 20, 10], width=150, anchor='center')

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
            try:
                res=eval(f'{num1}{znak}{num2}')
                labelres.configure(text=res)
            except:
                messagebox.showerror('Ошибка математика', 'ЛЕЕЕ на 0 делить нельзя')
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
    var_var=[]
    if c1.get()==1:
        var_var.append('первый вариант')
    if c2.get()==1:
        var_var.append('второй вариант')
    if c3.get()==1:
        var_var.append('третий вариант')
    if var_var:
        result=', '.join(var_var)
        lblres.configure(text=f'Вы выбрали: {result}')
    else:
        lblres.configure(text='Неее, сначала выбери что-нибудь!')


lblres=Label(tab2, text='')
butprov=Button(tab2, text='Проверка', command=butprovfunc)
c1=IntVar()
c2=IntVar()
c3=IntVar()
chk1=Checkbutton(tab2, text='Первый вариант', variable=c1)
chk2=Checkbutton(tab2, text='Второй вариант', variable=c2)
chk3=Checkbutton(tab2, text='Третий вариант', variable=c3)
chk1.grid(column=0, row=0)
chk2.grid(column=0, row=1)
chk3.grid(column=0, row=2)
butprov.grid(column=0, row=3)
lblres.grid(column=3, row=4)

#3
def dopfunc():
    field_txt.delete('1.0', END)
    field_txt.insert('1.0', 'УПС, пока не придумал')
def loadfile():
    f=filedialog.askopenfilename()
    if f:
        file_input=''
        with open(f, 'r') as files:
            for i in files:
                file_input+=i
        field_txt.delete('1.0', END)
        field_txt.insert('1.0', file_input)
menur=Menu(root)
new_item=Menu(menur)
new_item.add_command(label='Загрузить', command=loadfile)
new_item.add_separator()
new_item.add_command(label='Еще', command=dopfunc)
menur.add_cascade(label='Файл', menu=new_item)
root.config(menu=menur)
field_txt=Text(tab3, width=200, height=100, bg='white', fg='black', wrap='word')
field_txt.pack()
root.mainloop()
