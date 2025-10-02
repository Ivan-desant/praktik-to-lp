# 6.1
from random import *
lists=[randint(10, 30) for i in range(10)]

print(max(lists), '\n',
      f'Количество чисел меньше максимального: {len(lists)-1} \n',
      f'Количество чисел больше максимального: {len([x for x in lists if x>max(lists)])}')
print()
#6.2
ls1=[4, 6, 7, 12, 3, 10, 4, 22, 3, 1]
result=sum(j for j in ls1 if j>5)
print(f'Сумма чисел больших 5: {result}')
print()

#11.1
ex1=[randint(10, 100) for i in range(10)]
resl=0
for k in ex1:
    if k%2==0:
        resl=max(resl, k)
print(f'Максимальный элемент списка({ex1}) делящийся на два без остатка: {resl}')
print()

#11.2
ex2=[randint(1, 20) for i in range(10)]
print(ex2)
rs2=[x for x in ex2 if x<10 and x%2==0]
print(rs2)
if len(rs2) >0:
    rs2.sort(reverse=False)
    print(f'Новый массив {rs2}')
else:
    print('Таких чисел в исходном массиве нет')

