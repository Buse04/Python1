#dosyanın çok büyük olması durumunda part part yazdırmak için kullanılır.
#eğer hala okunacak miktar varsa yeniden okur.

with open ("text.txt") as f:
    okunacak_miktar=10
    icerik= f.read(okunacak_miktar)
    while len(icerik) > 0:
        print(icerik, end="")
        icerik=f.read(okunacak_miktar)

#png dosyalarıyla işlem yapılacaksa wb veya rb komutu kullanılır.



    