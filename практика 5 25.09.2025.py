# 6
stroka=input('Введите строку содержащую букву а: ')
count_a=stroka.count('а')
result=stroka.replace('а', '')
print('Результат: ' + result, '.', 'Количество удаленных букв а: ', count_a)

# 11
isxod=input('Введите строку с восклицательными знаками: ').lower()
isxod=isxod.replace('!', '.')
m=k=l=0
for r in range(0, len(isxod)-1):
    if isxod[r]=='н' and isxod[r+1]=='н':
        k+=1
        m=max(k, m)
    else:
        k=0
print(f'Новая строка: {isxod}, самая длинная последовательность из "н": {m+1}')

