from datetime import *

dogum = datetime.strptime(input('Dogum tarihinizi giriniz (Gun.Ay.Yil) :'),'%d.%m.%Y')
yas = datetime.now() - dogum

print(f"{yas} saniyedir yasiyorsunuz")