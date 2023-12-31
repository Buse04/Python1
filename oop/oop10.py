class kisi: 
    kisi_sayisi=0
    def __init__(self, isim,yas):
        self.name=isim
        self.age=yas
        kisi.kisi_sayisi += 1

print(kisi.kisi_sayisi)
kisi1=kisi("ali", 20)
kisi2=kisi("veli", 30)
kisi3=kisi("buse", 40)
print(kisi.kisi_sayisi)