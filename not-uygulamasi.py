def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    ogrenciAdi=liste[0]
    notlar=liste[1].split(",")
    
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])

    ortalama=(not1+not2+not3)/3

    if ortalama>95 and ortalama<=100:
        harf="A+"
    elif ortalama>=90 and ortalama<=94:
        harf="A"
    elif ortalama>=85 and ortalama<=89:
        harf="B+"
    elif ortalama>=75 and ortalama<=84:
        harf="B"
    elif ortalama>=65 and ortalama<=74:
        harf="C+" 
    elif ortalama>=55 and ortalama<=64:
        harf="C"
    elif ortalama>=45 and ortalama<=54:
        harf="D+"
    elif ortalama>=40 and ortalama<=44:
        harf="D"                          
    else:
        harf="F"

    return ogrenciAdi+": "+ harf + "\n"                


def ortalamalari_oku():
    with open("harf_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad=input("Öğrenci adı: ")
    soyad=input("Öğrenci soyadi: ")
    not1=input("Not 1: ")
    not2=input("Not 2: ")
    not3=input("Not 3: ")

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")
        

def notlari_kayitet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste=[]

        for i in file:
            liste.append(not_hesapla(i))

    with open("harf_notlari.txt","w",encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)        


while True:
    islem=input("1-Harf Notunu Göster\n2-Öğrenci Notlarını Gir\n3-Notları Kayıt Et\n4-Cıkış\n")

    if islem=="1":
        ortalamalari_oku()

    elif islem=="2":
        not_gir()    

    elif islem=="3":
        notlari_kayitet()

    else:
        break    