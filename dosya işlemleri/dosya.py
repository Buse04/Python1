# r okuma
#r+ okuma ve yazma
#w yazma modu


f= open("text.txt","r")
icerik= f.read()
print(icerik)
f.close()

#f.close ile açılan dosya kapatılmazsa sorun çıkar.



