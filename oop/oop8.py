class calisan:
    zam_orani=1.1 
    def __init__(self, ad, soyad, maaş):
        self.ad=ad
        self.soyad=soyad
        self.maaş=maaş
        self.email=ad + soyad + "@sirket.com"

    def show_info(self):
        return(f"Ad:{self.ad} Soyad:{self.soyad} Maaş:{self.maaş} Email:{self.email}")



calisan1= calisan("Ali", "Veli", 3000)


class yazılımcı(calisan):
    zam_oranı=1.3
    def __init__(self, ad, soyad, maaş, bildiği_dil):
        super().__init__(ad,soyad,maaş,)
        self.bildiği_dil=bildiği_dil

    def show_inf(self):
        return(f"Ad:{self.ad} Soyad:{self.soyad} Maaş:{self.maaş} Email:{self.email} Bildiği Dil:{self.bildiği_dil}")

yazılımcı1= yazılımcı("zeynep", "sadi", 4000, "İng")


print(show_info(calisan1))
print(show_inf(yazılımcı1))

class yönetici(calisan):
    def __init__(self, ad,soyad, maaş, calisanlar= None):
        if calisanlar== None:
            self.calisanlar=[]
        else:
            self.calisanlar= calisanlar

    def calisan_ekle(self, calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisan_sil(self, calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)

    def calisanlari_göster(self):
        for calisan in self.calisanlar:
            print(calisan.show_info()) 

yönetici1=yönetici("ahmet", "metin", 19000,)
yönetici1.calisan_ekle(calisan1)
yönetici1.calisan_ekle(yazılımcı1)
yönetici1.calisanlari_göster()