class calisan:
    def __init__(self,isim, maaş):
        self.name=isim
        self.salary=maaş

calisan1=calisan("ali", 20000)
calisan2=calisan("veli", 30000)

print(calisan1.__dict__)
print(calisan2.__dict__)

#dictionary olarak yazdırdık.
