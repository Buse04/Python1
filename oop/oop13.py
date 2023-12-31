class calisan:
    def __init__(self,isim,soyisim,maaş):
        self.name=isim
        self.surname=soyisim
        self.salary=maaş
        self.email=isim + soyisim + "@sirket.com"
    def bilgileri_göster(self):
        return "Ad: {} Soyad: {} Maaş: {} Email: {}".format(self.name, self.surname, self.salary, self.email)

calisan1=calisan("veli", "ali", 2000)
calisan2=calisan("ahmet", "celi", 3000)

class yazilimci(calisan):
    def __init__(self,isim,soyisim,maaş, dil):
        super().__init__(isim,soyisim,maaş)
        self.dil=dil
    def bilgileri_göster(self):
        return "Ad: {} Soyad: {} Maaş: {} Email: {} Dİl:{}".format(self.name, self.surname, self.salary, self.email, self.dil)
    def dili_söyle(self):
        return f"Bildiğim dil {self.dil}"

yazilimci1=yazilimci("ayşe", "yıldız", 4000, "java")
print(yazilimci1.bilgileri_göster())
print(yazilimci1.dili_söyle())

class yönetici(calisan):
    def __init__(self,isim,soyisim, maaş, çalisanlar= None):
        super().__init__(isim,soyisim,maaş)
        if çalisanlar == None:
            self.çalisanlar=[]
        else:
            self.çalisanlar = çalisanlar

    def calisan_ekle(self,çalisan):
        if çalisan not in self.çalisanlar:
            self.çalisanlar.append(çalisan)

    def calisan_sil(self,çalisan):
        if çalisan in self.çalisanlar:
            self.çalisanlar.remove(çalisan)

    def calisanları_göster(self):
        for çalisan in self.çalisanlar:
            print(çalisan.bilgileri_göster())

yönetici1= yönetici("metin", "ali", 5000)
yönetici1.calisan_ekle(calisan1)
yönetici1.calisanları_göster()

yönetici2=yönetici("mehmet", "ahmet", 6000, [yazilimci1,calisan1])
yönetici2.calisanları_göster()



