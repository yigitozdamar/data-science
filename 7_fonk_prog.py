
#pure functions

a=5

def impure_carp(b):
    return b*a

def pure_carp(a,b):
    return a*b

impure_carp(6)
pure_carp(4,6)


a = 9

#vectorized operations

a= [1,2,3,4]
b= [2,3,4,5]


ab= []

for i in range(0,len(a)):
    ab.append(a[i] * b[i])

ab

import numpy as np

a = np.array([1,2,3,4])
b= np.array([2,3,4,5])

a*b


# isimsiz fonksiyonlar

def eski_carp(a,b):
    return a*b

eski_carp(1,3)

yeni_carp = lambda a,b : a*b

yeni_carp(1,3)


sirasiz_liste = (['b',3],['a',8],['d',12],['c',1])

sorted(sirasiz_liste,key = lambda x: x[1])


#map 

v = [1,2,3,4,5]

list(map(lambda x: x +10, v))

#filter


v= [1,2,3,4,5,6,7,8,9]

list(filter(lambda x:x%2==0, v))


#reduce

from functools import reduce


v= [1,2,3,4,5,6,7,8,9]

reduce(lambda a,b : a+b,v)

reduce(lambda x: x%2 == 0,v)
































