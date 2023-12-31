class fakülte:
    def __init__(self, isim, soyisim, yas, bölüm):
        self.name=isim
        self.surname=soyisim
        self.age=yas
        self.department=bölüm

    def show_info(self):
        print(f"Ad:{self.name} Soyad:{self.surname} Yaş:{self.age} Bölüm:{self.department}")

ögrenci1=fakülte("buse", "yağmur", 20, "matematik")
ögrenci2=fakülte("elif", "yılmaz", 18, "hukuk")

ögrenci1.show_info()
ögrenci2.show_info()


