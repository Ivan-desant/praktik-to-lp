import random
#6.1
def nod(x, y):
    if x>y:
        while y:
            x, y=y, x%y
        return x
    else:
        while x:
            y, x=x, y%x
        return y
def nok(a, b):
    return (a*b)/nod(a, b)
print(nok(10, 20))
print()
#6.2
def area(x, y, a, b, d1):
    if d1<=(x+y) and d1<=(a+b):
        p1=(x+y+d1)/2
        p2=(a+b+d1)/2
        s1=(p1*(p1-x)*(p1-y)*(p1-d1))**0.5
        s2=(p2*(p2-a)*(p2-b)*(p2-d1))**0.5
        result=s1+s2
    else:
        result='Некорректные данные для расчета'
    return result
print(area(5, 4,6, 7, 9))
print()



#9.1
def kul(n, k=0):
    if n!=0:
       ns=[int(f) for f in str(n)]
       return kul(n-sum(ns), k+1)
    else:
        return k
print(kul(11))
print()

#9.2
def pr(ls1, ls2, ls3):
    r1=r2=r3=1
    for i in ls1:
        r1=r1*i
    for j in ls2:
        r2=r2*j
    for k in ls3:
        r3=r3*k
    return (f'Произведение чисел массива {ls1}={r1},\n'
            f'Произведение чисел массива {ls2}={r2}, \n'
            f'Произведение чисел массива {ls3}={r3}')

def sumer(ls1, ls2, ls3):
    return (f'Среднее арифметическое значение чисел массива {ls1}={sum(ls1)/len(ls1)}, \n'
            f'Среднее арифметическое значение чисел массива {ls2}={sum(ls2)/len(ls2)}, \n'
            f'Среднее арифметическое значение чисел массива {ls3}={sum(ls3)/len(ls3)}, \n')
t=[x for x in range(1, 10)]
p=[2, 10, 30]
l=[random.randint(10, 100) for i in range(5)]
print(pr(t, p, l))
print()
print(sumer(t, p, l))






