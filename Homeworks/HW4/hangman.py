import random
from grafik import man

class GameHang:
    def __init__(self):
        self.adam=0
        self.hak=7
        wordlist=["Samsun", "ATATÜRK", "Python", "Cyber", "Yazılım"]
        self.wordlist=[item.upper() for item in wordlist]

    def random_word(self):
        kelime= random.choice(self.wordlist)
        self.kelime=kelime

    def giris(self):
        listgiris=['-,' for i in range(len(self.kelime))]
        print("Kelime de {0} harf var".format(len(self.kelime)))
        print(''.join(listgiris))
        self.listgiris=listgiris
        return None
    def can(self):
        if self.hak != 1:
            print("{0} canınız var".format(self.hak))
        else:
            print("{0} canınız var.".format(self.hak))
        return self.hak
    def cevap(self):
        cvp = input("Harf tahmini giriniz: ")
        cvp = cvp.upper()
        self.cvp=cvp

    def oyun(self):
        if len(self.cvp) > 1 or len(self.cvp) == 0:
            print("Yanlızca bir harf girmelisiniz... ")
            self.hak=self.hak - 1
            print(man[self.adam])
            self.adam=self.adam+1
        elif (self.cvp).isalpha() == False:
            print("Alfabede bulunmayan bir karakter girdiniz...")
            self.hak=self.hak - 1
            print(man[self.adam])
            self.adam=self.adam+1
        elif self.cvp not in self.kelime:
            print("Girilen cevap kelimede yok...")
            self.hak=self.hak - 1
            print(man[self.adam])
            self.adam=self.adam+1
        else:
            for i in range(len(self.kelime)):
                if self.cvp == self.kelime[i]:
                    self.listgiris[i] = self.cvp
            print("Doğru cevap ")
        print(''.join(self.listgiris))

    def win(self):
        if '-,' not in self.listgiris:
            print("Kazandınız. Tebrikler. Kelime: {0} ".format(self.kelime))
            self.hak=0

    def loss(self): 
        if '-,' in self.listgiris:
            print("Kaybettin....")

while True:
    try:
        print("----------------------------------------------------------------------------------------------------------")
        print("HangGame Oyununa hoşgeldiniz...\nToplam 7 hakkınız bulunmaktadır.\nBaşarılar\nOyuna başlamak için 1 yazınız\nÇıkış yapmak için 0 yazınız")
        basla=int(input("=> "))
        if basla == 1:
            game= GameHang()
            game.random_word()
            game.giris()
            game.can()
            while game.hak > 0:
                game.cevap()
                game.oyun()
                game.can()
                if game.win()== True:
                    break
            game.loss()
        elif basla == 0:
            print("Tekrar görüşmek üzere...")
            break
    except:
        print("Hatalı bir giriş yaptınız.")