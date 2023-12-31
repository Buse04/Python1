class sınıf:
    def __init__(self, ad, soyad, bölüm="girilmedi", obp=0):
        self.name=ad
        self.surname=soyad
        self.department=bölüm
        self.obp=obp

    def show_info(self):
        print(f"Ad:{self.name} Soyad:{self.surname} Bölüm:{self.department} OBP:{self.obp}")

ogrenci1=sınıf("buse", "baylav", "matematik")
ogrenci2=sınıf("demet", "baylav", obp=4)

ogrenci1.show_info()
ogrenci2.show_info()

