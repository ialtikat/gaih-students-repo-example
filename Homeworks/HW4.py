import random

class HangmanGame:
    def __init__(self):
        self.giris = True
        word_list= ["Samsun", "ATATÜRK", "Python", "Cyber", "Yazılım"]
        self.word_list=[item.lower() for item in word_list]
        self.kesi=[]
        self.hak =5
        return None
    
    def random_word(self):
        kelime= random.choice(self.word_list)
        self.kelime=kelime

    def sekil(self):
        listsekil=['-,' for i in range(len(self.kelime))]
        print("Kelime de {0} harf var".format(len(self.kelime)))
        print(''.join(listsekil))
        self.listsekil=listsekil
        return None
    
    def sayac(self):
        if self.hak != 1:
            print("{0} canınız var".format(self.hak))
        else:
            print("{0} canınız var.".format(self.hak))
        return self.hak
    
    def karakter(self):
        krktr = input("Cevap giriniz: ")
        krktr = krktr.lower()
        self.krktr=krktr

        return None

    def oyun(self):
        if len(self.krktr) > 1 or len(self.krktr) == 0:
            print("Yanlızca bir harf girmelisiniz... ")
            self.hak=self.hak - 1
        elif (self.krktr).isalpha() == False:
            print("Alfabede bulunmayan bir karakter girdiniz...")
            self.hak=self.hak - 1
        elif self.krktr not in self.kelime:
            print("Girilen cevap kelimede yok...")
            self.hak=self.hak - 1
        else:
            for i in range(len(self.kelime)):
                if self.krktr == self.kelime[i]:
                    self.listsekil[i] = self.krktr
        print(''.join(self.listsekil))
        return None
    
    def win(self):
        if '-,' not in self.listsekil:
            print("Kazandınız. Tebrikler. Kelime: {0} ".format(self.kelime))
            if self.kelime not in self.kesi:
                (self.kesi).append(self.kelime)
            return True
    
    def loss(self):
        if '-,' in self.listsekil:
            print("Kaybettin")
        
    def bul(self):
        if self.kelime in self.kesi:
               print("Daha önce bu kelimeyi tahmin etmiştin") 
        if len(self.kesi) > 0:
                print("Şuana kadar keşfedilen kelimeler: {0}".format(' '.join(self.kesi)))
    
    def tekrar():
        try:
            cevap=input("Tekrar oynayalım mı? E/H  ")
            cevap.upper
            if cevap == "E":
                return True
            elif cevap == "H":
                print("Tekrar görüşmek üzere...")
                return False
            else:
                print("Geçerli bir cevap giriniz:")
                return HangmanGame.tekrar()
        except:
            print("Geçerli bir cevap giriniz:")
            return HangmanGame.tekrar()
    
    def statu(self):
        self.giris= HangmanGame.tekrar()
        return self.giris

hangman= HangmanGame()
while hangman.giris == True:
    hangman.random_word()
    hangman.bul()
    hangman.sekil()
    hangman.sayac()

    while(hangman.hak) > 0:
        hangman.karakter()
        hangman.oyun()
        hangman.sayac()
        
        if hangman.win() == True:
            break

    hangman.loss()
    hangman.statu()
