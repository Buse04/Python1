#girilmedi yazılan yerlerde eğer veri girilmemişse girilmedi yazar.

class sinif:
    def __init__(self,ad="girilmedi", soyad="girilmedi", bölüm="girilmedi", obp=0):
        self.name=ad
        self.surname=soyad
        self.department=bölüm
        self.obp=obp

    def show_info(self):
        print(f"Ad:{self.name} Soyad:{self.surname} Bölüm:{self.department} OBP:{self.obp}")

ogrenci1=sinif("buse", "baylav", "matematik")
ogrenci2=sinif("demet", "baylav", 3.7)

ogrenci1.show_info()
ogrenci2.show_info()


#böyle girildiğinde demetin bölümü ve obp si yanlış oldu. Doğrusu oop5.py dosyasında



