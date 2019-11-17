
# sinif ve sinif ozellikleri
class VeriBilimci():
    print('Bu bir siniftir')
    bolum = ''
    deneyim_yili = 0
    sql = 'Evet'
    bildigi_diller = []

#orneklendirme

    
VeriBilimci.sql = 'Hayir'

VeriBilimci.sql

Ali = VeriBilimci()

Ali.sql

Ali.bildigi_diller.append('Python')

Ali.bildigi_diller

Veli = VeriBilimci()

Veli.bildigi_diller

#ornek ozellikleri

class VeriBilimci():
    def __init__(self):
        self.bildigi_diller = []
        
ali = VeriBilimci()
veli = VeriBilimci()


ali.bildigi_diller.append('R')
ali.bildigi_diller


veli.bildigi_diller.append('Python')
veli.bildigi_diller

class VeriBilimci():
    bildigi_diller = ['R','Python','SQL']
    def __init__(self):
        self.bildigi_diller = []
        
VeriBilimci.bildigi_diller

ali = VeriBilimci()
ali.bildigi_diller

ali.bildigi_diller.append('R')
ali.bildigi_diller

#ornek metodlari

class VeriBilimci():
    def __init__(self):
        self.bildigi_diller = []
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

VeriBilimci.dil_ekle

ali.dil_ekle('R')
ali.bildigi_diller

veli.dil_ekle('Python')
veli.bildigi_diller





























