#6.1
n=3
f=open('ИжокинИванЕвгеньевич_УБ51_vvod.txt', 'r').readlines()
a=[]
res=''
for i in f:
    i=i.replace('\n', ' ')
    i=i.split(' ')
    b=[]
    for j in i:
        if len(j)>0:
            b.append(int(j))
    a.append(b)
print(a)
file=open('ИжокинИванЕвгеньевич_УБ51_vivod.txt', 'w')
file.write('№6.1 \n')
for i in range(len(a)):
    file.writelines(f'Макс. число в строке {i+1} = {max(a[i])}\n')
for i in range(n):
    file.writelines(f'Мин. число в столбце {i} = {min(a[0][0+i], a[1][0+i], a[2][0+i])}\n')
file.close()
print()

#6.2
n=3
f=open('ИжокинИванЕвгеньевич_УБ51_vvod.txt', 'r').readlines()
a=[]
res=''
for i in f:
    i=i.replace('\n', ' ')
    i=i.split(' ')
    b=[]
    for j in i:
        if len(j)>0:
            b.append(int(j))
    a.append(b)
print(a)
di=[]
for i in range(n):
        di.append(a[i][i])
for j in range(n):
        di.append(a[j][2-j]) # [0;2][1;1][2;0]
print(di)
a[n//2][n//2]=max(di)
new_f=open('ИжокинИванЕвгеньевич_УБ51_vivod.txt', 'w')
for i in a:
    for j in i:
        new_f.write(f'{j} ')
    new_f.write('\n')
new_f.close()