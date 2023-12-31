import time

baslangıc= time.time()

list= []

for i in range(10000000):
    list.append(i)

bitis= time.time()

print(bitis-baslangıc)



