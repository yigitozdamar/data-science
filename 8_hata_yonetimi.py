
A = 1
B = 0

A / B

try:
    print(A/B)
except ZeroDivisionError:
    print('Paydada 0 olur mu')
    
a = 1
b = '2'

a/b

try:
    print(a/b)
except TypeError:
    print('Sayi girmelisin')