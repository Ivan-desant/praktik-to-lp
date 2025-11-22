
import requests
from tkinter import *
from tkinter import messagebox
import json

window=Tk()
window.title('Получение JSON')
window.geometry('400x400')

def zapros():
    repo=ent.get()
    user = 'flutter'
    url=f'https://api.github.com/repos/{user}/{repo}'
    r=requests.get(url)
    if r:
        messagebox.showinfo('Проверка', 'Соединение установлено!')
        r=r.json()
        r.setdefault('email', None)
        r.setdefault('company', None)
        ls = {'company': r['company'], 'created_at': r['created_at'], 'email': r['email'], 'id': r['id'],
              'name': r['name'], 'url': r['url']}
        with open('vivod.json', 'w', encoding='utf-8') as f:
            json.dumps(ls)
            h = json.dumps(ls, indent=6)
            f.write(h)
        messagebox.showinfo('Состояние файла', 'Информация добавлена')
    else:
        messagebox.showinfo('Проверка', 'Увы, ошибка 404')

frame = Frame(window)
frame.pack(expand=True)
label = Label(frame, text='Введи имя репозитория')
ent = Entry(frame, width=20)
but = Button(frame, text='Получить информацию', command=zapros)
label.pack(pady=10)
ent.pack(pady=5)
but.pack(pady=10)

window.mainloop()
