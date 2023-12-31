from datetime import date

class kisi:
    def __init__(self, isim,yas):
        self.name=isim
        self.age=yas

    @classmethod
    def dogum_yılı_ile_hesapla(cls, isim, dogum_yılı):
        return cls(isim, date.today().year - dogum_yılı)
    
kisi1=kisi.dogum_yılı_ile_hesapla("buse", 1996)
print(kisi1.name, kisi1.age)












