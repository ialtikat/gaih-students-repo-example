def prime_first(self):
    for i in range(2, self):
        if self % i == 0:
            return False
    return True

def prime_second(self):
    for i in range(2, self):
        if self % i == 0:
            return False
    return True

for i in range(2,1000):
    if i <= 500:
        if prime_first(i):
            print("Asal sayı: ",i)
             #listilk.append(i) => Tanımlama yaparak liste içerisine yazdırabiliriz.
    else:
        if prime_second(i):
            print("Asal sayı: ",i)
            #listson.append(i) => Tanımlama yaparak liste içerisine yazdırabiliriz.


"""
 0-500 Arasındaki asal sayıları prime_first fonksiyonu listeliyor. 500-1000 Arasındaki asal sayıları ise pirem_second fonksiyonu listeliyor.
"""
