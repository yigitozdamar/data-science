import random

def isim_olustucu():
    isim = ['Ali','Veli','Can','Merve','Gozde','Cansu']
    soyisim = ['Demir','Ozturk','Kaya','Bozkurt','Ozdemir','Karagol']
    return '{} {}'.format(random.choice(isim),random.choice(soyisim))

for i in range(6):
    print(isim_olustucu())