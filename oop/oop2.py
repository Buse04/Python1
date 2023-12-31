class calisan: 
    def __init__(self,a,b,c):
        self.name=a
        self.surname=b
        self.age=c

    def show_info(self):
        print(f"Ad:{self.name}  Soyad:{self.surname} Yaş:{self.age}")

calisan1=calisan("ali", "veli", 20)
calisan2=calisan("buse", "zeynep", 19)

calisan1.show_info()
calisan2.show_info()

    


