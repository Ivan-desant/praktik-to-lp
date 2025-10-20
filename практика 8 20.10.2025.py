#6.1
import random
a=[]
n=3
for i in range(n):
    b=[]
    for i in range(n):
        b.append(random.randint(1, 10))
    a.append(b)
print(a)
for i in range(len(a)):
    print(f'Макс. число в строке {i+1} = {max(a[i])}')
for i in range(n):
    print(f'Мин. число в столбце {i} = {min(a[0][0+i], a[1][0+i], a[2][0+i])}')
print()
#6.2
n=int(input('Введите нечетное число: '))
if n%2!=0 and n>1:
    a=[]
    while len(a)!=n:
        b=[random.randint(-n*n, n*n+10) for i in range(n*n)]
        if len(set(b))==n*n:
            k=0
            for i in range(n):
               c=[]
               while len(c)!=n:
                    c.append(b[k])
                    k+=1
               a.append(c)
    print(a)
    di=[]
    for i in range(n):
        di.append(a[i][i])
    for j in range(n):
        di.append(a[j][2-j]) # [0;2][1;1][2;0]
    print(di)
    a[n//2][n//2]=max(di)
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
print()

#9.1
k=3
n=3
a=[]
res=[]
for i in range(n):
    b=[]
    for j in range(n):
        b.append(random.randint(1, 100))
    a.append(b)
print(a)
for i in a:
    for m in i:
        if m%3==0:
            res.append(m)
print(f'Число элементов в матрице кратных k = {len(res)}, максимальное из них = {max(res)}')
print()

#9.2
n=int(input('Введите нечетное число: '))
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        b.append(random.randint(-10, 10))
    a.append(b)
print(a)
res=[]
for i in a:
    for j in i:
        res.append(abs(j))
mx=max(res)
it=0
jt=0
f=False
for i in range(n):
    for j in range(n):
        if abs(a[i][j])==mx:
            it,jt=i,j
            f=True
            break
    if f:
        break
jop=[]
for i in range(len(a)):
    for j in range(len(a)):
        k=a[i][j]
        if k not in a[it] and j!=jt:
            jop.append(k)
new_a=[]
l=0
for i in range(n-1):
    c=[]
    while len(c)!=n-1:
        c.append(jop[l])
        l+=1
    new_a.append(c)
print(new_a)


