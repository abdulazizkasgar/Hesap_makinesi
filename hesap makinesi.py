while(True):
    i = 0
    if i == 0:
        print("HESAP MAKINESINE HOSGELDINIZ\nYapmak istediginiz islemleri girebilirsiniz")
    while(True):
        if i >= 1:
            print("TEKRAR HOS GELDINIZ")
        sayi1 = float(input("birinci sayiyi girin:"))
        while(True):
            islem = str(input("Bir islem secin\n+  -\nx  /\n"))
            sayi2 = float(input("ikinci sayiyi girin:"))
            sonuc1 = sayi1 + sayi2
            sonuc2 = sayi1 - sayi2
            sonuc3 = sayi1 * sayi2
            sonuc4 = sayi1 / sayi2
            if islem == "+":
                print("sonuc", sonuc1)
                break
            elif islem == "-":
                print("sonuc", sonuc2)
                break
            elif islem == "x":
                print("sonuc", sonuc3)
                break
            elif islem == "/":
                print("sonuc", sonuc4) 
                break   
            else :
                print("GECERSIZ KOMUT TEKRAR DENEYIN!")    
                continue
        i = i + 1
        while(True):
            sonuc = str(input("BASKA BIR ISLEMINIZ VARMI?\nevt / hyr :"))
            if sonuc == "evt" :
                break
            elif sonuc == "hyr" :
                print("yine bekleriz :)")
                break
            else :
                print("GECERSIZ KOMUT TEKRAR DENEYIN!")
                continue   
        if sonuc == "evt":
            continue
        elif sonuc =="hyr":
            break    
    if sonuc == "hyr":
        break    