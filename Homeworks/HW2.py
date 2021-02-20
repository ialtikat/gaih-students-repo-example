i=0
average=[]
ogrenci=[]
info={}
while i<5:
    name=input("Öğrenci adını giriniz: ")
    surname=input("Öğrenci soyadını giriniz: ")
    if name != "" and surname != "":
        vize=float(input("Vize notunu giriniz: "))
        final=float(input("Final notunu giriniz: "))
        proje=float(input("Proje notunu giriniz: "))
        if vize >=0 and final >=0  and proje >=0 and vize <= 100 and final <= 100 and proje <= 100:
            ogrenci.append(name+" "+surname)
            average.append((vize+final+proje)/3)
            i+=1
        else:
            print("Sınav ve ödev notlatları 0 dan küçük ve 100 den büyük olamaz!!!")
            break
    else:
        print ("Lütfen öğrenci ad ve soyadlarını boş geçmeyiniz!!!")
        break
        

for i in range(len(average)):
    info[ogrenci[i]]= average[i]
print(info)  
storted_info=storted_info=sorted(info, key=info.__getitem__, reverse=True)
print(storted_info)
print(storted_info[0], " En yüksek ortalama ile birinci olmuştur tebrikler...")


"""
items = [(v, k) for k, v in info.items()]
items.sort()
items.reverse() 
items = [(k, v) for v, k in items]
=> Dictionari içerisindeki elemanları küçükten büyüğe sıralar reverse() fonksiyonu ile ters çevirir.


storted_info=sorted(info, key=info.__getitem__, reverse=True) => Büyükten küçüğe sıralar ve storted_info listine ekler, value değerlerini listeye almaz.

"""

"""
OUTPUT:

{'İbrahim ALTIKAT': 90.0, 'Ali VELİ': 63.333333333333336, 'Kemal SUNAL': 100.0, 'Jonny Mon': 45.0, 'Mehmet Mehmet': 37.333333333333336}
['Kemal SUNAL', 'İbrahim ALTIKAT', 'Ali VELİ', 'Jonny Mon', 'Mehmet Mehmet']
Kemal SUNAL  En yüksek ortalama ile birinci olmuştur tebrikler...


"""