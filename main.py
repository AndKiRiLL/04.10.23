# Задача «Делаем срезы»
'''
S1 = 'Hello'
print(S1[2])

S2 = 'Goodbay'
print(S2[-2])

S3 = 'Goodmorning'
print(S3[:5])

S4 = 'Night'
print(S4[:-2])

S5 = 'Advanced'
print(S5[1::2])

S6 = 'Clasic'
print(S6[0::2])

S7 = 'Ultimate'
print(S7[::-1])

S8 = 'Ultimate'
print(S8[::-2])

S9 = 'Python'
print('Lenght string:', len(S9))
'''

# Задача «Количество слов»

#S = 'Ware are you doing'
#print(S.count(' ') + 1)

# Задача «Две половинки»

'''
s = 'Wareareyoudoing'
s_1 = s[:round(len(s)/2)]
s_2 = s[len(s)//2:]
print(s_2, s_1)
'''

# Задача «Первое и последнее вхождения»
'''
//После изучения условий из презентации переделал задание
s = 'float file'

if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
'''

# Задача «Удаление фрагмента»
'''
s = 'one height hig'

h_1 = s.find('h')
h_2 = s.rfind('h')+1

print(s[:h_1],s[h_2:])
'''

# Задача «Замена подстроки»
'''
s = '1 day, 1 week, 1 year'
print(s.replace('1','one'))
'''

# Задача «Удаление символа»
'''
s = 'kirill@gmail.com@'
print(s.replace('@',''))
'''

# Задача «Замена внутри фрагмента»
'''
s = 'h one height hig'

h1 = s[:s.find('h') + 1]
h2 = s[s.find('h') + 1 : s.rfind('h')]
h3 = s[s.rfind('h'):]

s = h1 + h2.replace('h','H') + h3

print(s)
'''

# ///////////////////// Задачи на условия /////////////////////

#Задача «Минимум из двух чисел»
'''
x1 = 3
x2 = 5

if x1 < x2:
    print(x1)
else:
    print(x2)
'''

#Задача «Знак числа»
'''
x = int(input())

if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)
'''

# Задача «Шахматная доска»
'''
x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
'''

# Задача «Високосный год»
'''
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print('YES')
else:
    print('NO')
'''

# Задача «Сколько совпадает чисел»
'''
x1 = int(input())
x2 = int(input())
x3 = int(input())

if   x1 != x2 != x3:
    print('0')

elif x1 == x2 == x3:
    print('3')

else:
    print('2')
'''

# Задача «Ход ладьи»
'''
x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
'''

#Задача «Шоколадка»
'''
n = int(input())
m = int(input())
k = int(input())

if k < m * n and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
'''

# Задача «Яша плавает в бассейне»
'''
n = int(input())
m = int(input())
x = int(input())
y = int(input())

if x > n / 2:
    x = n - x

if y > m / 2:
    m = m - y

if x < y:
    print(x)
else:
    print(y)
'''