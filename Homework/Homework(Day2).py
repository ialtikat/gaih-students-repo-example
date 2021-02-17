import random 
asal=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97) #asal sayılar listemiz
liste=[[random.choice(asal) for x in range(3)] for x in range(3)] #Matrisi oluşturma
for i in range(3):
    print(liste[i]) #Matrisi yazdırma
    
