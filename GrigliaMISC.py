###  Griglia
import time 
import datetime
import random
import os 
os.system('cls')
os.system('color 2')

class gioco:
    def __init__(self):
        pass
    def matrice(self, x, y):
        matrice = []
        self.matrice = matrice
        for i in range(x):
            n = []
            for j in range(y):
                numero = "  |"
                n.insert(i, numero)
            matrice.append(n)
        return matrice 
    def griglia(self,x, y):
        matrice = self.matrice(x, y)
        s = ''
        bordo = "+" + "---+" * y                            
        for i in range(len(matrice)):
            print(bordo)
            print("|", end='')
            for j in range(len(matrice[i])):
                print(self.matrice[i][j], end ='')
            print()
        print(bordo) 
        self.place(x, y)
    def place(self, x, y):
        posizioni = []
        matrice = self.matrice(x, y)
        for x in range(len(matrice)):
            for y in range(len(matrice)):
                posizioni.append((x, y))
        scegli = random.sample(posizioni, k=2)
        for r, c in scegli:
            self.matrice[r][c] = f" {random.randint([0,2])} |"
    def popola(self, x, y):
        self.griglia(x, y)
    
x = int(input("Riga: "))
y = int(input("Colonna: "))
g = gioco()
print(g.griglia(x, y))

