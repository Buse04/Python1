#dosyayı aç ve f olarak isimlendir dedik.

with open("text.txt","r") as f:
    icerik=f.read()
    print(icerik)

#bu yaptıklarımız dosya.py ile aynı şeyler.
#tek fark bu şekilde kullanımda dosyayı manuel olarak kapatmamıza gerek yok. 
