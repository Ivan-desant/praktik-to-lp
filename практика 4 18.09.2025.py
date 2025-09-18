# №1
a=int(input('a: '))
b=int(input('b: '))
if a<=b:
    for i in range(a, b+1):
        print(i, end=' ')
else:
    print('A должно быть <= B')
print()

# №6
n=int(input('Введите значение числа n: '))
def fac(x):
    result=1
    for i in range(1, x+1):
        result*=i
    return result
print(fac(n))



