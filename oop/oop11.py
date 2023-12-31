class kisi: 
    kisi_sayisi=0
    def __init__(self, isim,yas):
        self.name=isim
        self.age=yas
        kisi.kisi_sayisi += 1
    
    def bilgilerini_söyle(self):
      return  f"Ad: {self.name}  Yaş:{self.age}"


kisi1=kisi("ali", 20)
kisi2=kisi("veli", 30)
kisi3=kisi("buse", 40)

print(kisi1.bilgilerini_söyle())
