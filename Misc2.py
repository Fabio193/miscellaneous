### INCOMPLETO
import random 
import time 
import sys 
import os 
import string

os.system("cls")
os.system('color 2')

print("-" * 40)
print("                TOOL")
print("-" * 40)


class password:
    def __init__(self):
        pass
    def password(caratteri):
        x = caratteri
        lettere = []
        numeri = []
        resto = x % 2
        if resto != 0: 
            for i in range(x//2):
                n = random.randint(1, 9)
                numeri.append(n)
                lettera = random.choice(string.ascii_uppercase or string.ascii_lowercase)
                lettere.append(lettera)
        else:
            for i in range(x//2):
                n = random.randint(1, 9)
                numeri.append(n)
                lettera = random.choice(string.ascii_letters)
                lettere.append(lettera)
        password = lettere + numeri 
        for i in range(len(password)):
           print(random.choice(password), end='')
        while True:
            r = str(input('\n[+] Riprovare?[Y/N]: '))
            if r == str('Y'):
                for i in range(len(password)):
                    print(random.choice(password), end='')
            elif r == str('N'): 
                sys.exit()
            else:
                sys.exit()
class indovino:
    def __init__(self):
        pass        
    def indovina():
        intervallo = []
        for i in range(1, 101):
            intervallo.append(i)
        numero = random.choice(intervallo)
        print('[+] Il tuo numero è',numero,'?')
        r = str(input("[Y/N]: "))
        if r == str('Y'):
            print("Acqua o Fuoco?")
            r = str(input("[ACQUA/FUOCO]: "))
            if r == str("ACQUA"):
                pass
class griglia:
    def __init__(self, x, y):
        x = self.x
        y = self.y
    def matrice(self):
        matrix = []
        for i in range(self.x):
            n = []
            for j in range(self.y):
                a = "-"
                n.append(i, a)
            matrix.append(n)
        print(matrix)
            


        



try:
    s = ''
    print(s)
    print("[1] Generatore Password Sicura")
    print("[2] Indovino")
    print("[3] Stampa Griglia")
    print(s)
    print("-" * 40)
    opera = int(input("[*] Operazione: "))
    if opera < 1 or opera > 3:
        print("[+] Operazione non valida!")
        while True:
            opera = int(input('Operazione: '))
            if opera < 1 or opera > 3:
                print("[+] Operazione non valida!")
            else:
                break
    print('-' * 40)


    if opera == 1:
        print(s)
        caratteri = int(input(("[*] Caratteri della password(MIN: 4, MAX: 10): ")))
        if caratteri < 4 or caratteri > 10:
            print("[+] Lunghezza non valida!")
            while True:
                carattere = int(input("[*] Caratteri della password(MIN: 4, MAX: 10): "))
                if caratteri < 4 or caratteri > 10:
                    print("[+] Lunghezza non valida!")
                else:
                    break
        a = password
        a.password(caratteri)
    elif opera == 2:
        print(s)
        print("Pensa ad un numero")
        b = indovino
        b.indovina()
except KeyboardInterrupt:
    print("[+]Aborto")