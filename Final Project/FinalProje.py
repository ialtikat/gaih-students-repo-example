class Food: 
    def __init__(self,name): 
        self.name=name
  
    def pisir(self, name): 
        if self.name == "Kavurma":
            print("Pişmesi için 75 DK bekleyelim")
        elif self.name=="Pilav":
            print("Pişmesi için 40 DK bekleyelim")
  
    def karistir(self): 
        print("Karıştırmayı unutmayalım :)")
    
    def urun(self,name):
        print("<Malzemeler>")
        for i in range(len(name)):
                print("> {}".format(name[i]))

    def yemek(self):
        print("Afiyet olsun.")

class Kavurma(Food): 
    def __init__(self,name, malzeme): 
        self.name = name
        self.malzeme=malzeme
        print("<------------------------Bu Günün Menüsü------------------------------>")
        print("Yemeğimiz: {}".format(self.name))
        self.urun(self.malzeme)
        self.pisir(self.name)
        self.karistir()
        self.yemek()
  
  
class Pilav(Food): 
    def __init__(self,name, malzeme): 
        self.name = name
        self.malzeme=malzeme
        print("<------------------------Bu Günün Menüsü------------------------------>")
        print("Yemeğimiz: {}".format(self.name))
        self.urun(malzeme)
        self.pisir(self.name)
        self.karistir()
        self.yemek()
  
  
class Cacik(Food): 
    def __init__(self,name, malzeme): 
        self.name = name
        self.malzeme=malzeme
        print("<------------------------Bu Günün Menüsü------------------------------>")
        print("Yemeğimiz: {}".format(self.name))
        self.urun(malzeme)
        self.pisir(self.name)
        self.karistir()
        self.yemek()
  

if __name__ == "__main__": 
    kavurma = Kavurma("Kavurma", ["Et","1 Adet Soğan", "2 Yemek Kaşığı Yağ ", "1 Tatlı Kaşığı Tuz", "1 Çay Kaşığı Kekik", "1 Çay Kaşığı Karabiber", "1 Bardak Sıcak Su"] ) 
    pilav = Pilav("Pilav",["2 su bardağı pirinç", "2 yemek kaşığı tereyağı","2 yemek kaşığı sıvıyağ","1 çay kaşığı tuz","4 yemek kaşığı tel şehriye ","3 su bardağı sıcak su","1 adet tavuk suyu"]) 
    cacik= Cacik("Cacık",["3 su bardağı yoğurt","1,5 su bardağı soğuk su","4 adet orta boy salatalık", "2 diş sarımsak","1 çay kaşığı tuz"])
  