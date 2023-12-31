
with open("text.txt") as f:
    icerik= f.readlines()
    print(icerik)

    for satir in icerik:
        print(satir, end="")