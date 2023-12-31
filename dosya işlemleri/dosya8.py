#r modu dosya yoksa hata verir.
#w modu dosya yoksa oluşturur.

with open ("text2.txt", "w") as f:
    f.write("Buse")

#w modunda yeni text dosyası oluştururken tırnak içindeki ifade her seferinde değişir.
#a modunda yeni text dosyası oluştururken tırnak içindeki ifade her seferinde eklenir.
