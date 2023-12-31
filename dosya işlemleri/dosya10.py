with open ("text.txt",) as okunacak:
    with open ("text2.txt", "w") as yazilacak:
        for satir in okunacak:
            yazilacak.write(satir)
            