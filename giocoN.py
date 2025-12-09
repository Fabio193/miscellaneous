### Semplice programma che analizza i numeri naturali 


import os 
import sys 
import time 
import string

os.system('cls')
os.system('color 3')


def head():
    print('-' * 40)
    print('                FABIO')
    print('-' * 40)
def oprerazioni():
    print("[1] Numeri pari/dispari\n" \
    "[2] Somma dei numeri naturali (1+2+3+4+5+6+7...)\n" \
    "[3] Numeri primi")
    print('-' * 40)

class numeri:
    def __init__(self, numero):
        self.numero = numero
    def pari(self, numero):
        pari = []
        dispari = []
        for i in range(1, (numero+1)):
            if i % 2 == 0:
                pari.append(i)
            else:
                dispari.append(i)
        percpari = f"{(len(pari) * 100) / i}%"
        percdispari = f"{(len(dispari) * 100) / i}%"
        print("\n[*] Pari:", len(pari), "-", percpari)
        print("[*] Dispari:", len(dispari), '-', percdispari)
        while True:
            domanda = str(input("\n[+] Assegnare altro numero[Y/N]?: "))
            if domanda == str('Y') or str('y'):
                numero = int(input("[+] Numero da esaminare: "))
                pari = []
                dispari = []
                for i in range(1, (numero+1)):
                    if i % 2 == 0:
                        pari.append(i)
                    else:
                        dispari.append(i)
                percpari = f"{(len(pari) * 100) / i} %"
                percdispari = f"{(len(dispari) * 100) / i} %"
                print("\n[*] Pari:", len(pari), "-", percpari )
                print("[*] Dispari:", len(dispari), '-', percdispari)

            elif domanda == str('N') or str("n"):
                sys.exit()
            else:
                print("[*] Operazione non valida!")
    def serie(self, numero):
        numeri = []
        for i in range(1, (numero+1)):
            numeri.append(i)
        seire = sum(numeri)
        print("\n[*] La somma dei numeri natruali da 1 a", numero, ':', seire)
        while True:
            domanda = str(input('[+] Esaminare un altro numero[Y/N]: '))
            if domanda == str("Y") or str ("y"):
                numero = int(input("\n[+] Numero da esaminare: "))
                numeri = []
                for i in range(1, (numero+1)):
                    numeri.append(i)
                seire = sum(numeri)
                print("[*] La somma dei numeri natruali da 1 a", numero, ':', seire)
            elif domanda == str("N") or str('n'):
                sys.exit()
            else:
                print('[*] Operazione non valida!')
    def primi(self, numero):
        primi = []
        for num in range(2, (numero + 1)):
            primo = True
            for i in range(2, num):
                if num % i == 0:
                    primo = False
                    break
            if primo:
                primi.append(num)
        print("\n[*] Numeri primi: ", primi)
        print("[*] Totale numeri primi trovati: ", len(primi))
        print(f'[*] Percentuale: {(len(primi)*100)/numero}%')
        while True:
            domanda = str(input('\n[+] Esaminare un altro numero[Y/N]: '))
            if domanda == str('Y') or str('y'):
                numero = int(input("[+] Numero da esaminare: "))
                primi = []
                for num in range(2, (numero + 1)):
                    primo = True
                    for i in range(2, num):
                        if num % i == 0:
                            primo = False
                            break
                    if primo:
                        primi.append(num)
                print("\n[*] Numeri primi: ", primi)
                print("[*] Totale numeri primi trovati: ", len(primi))
                print(f'[*] Percentuale: {(len(primi)*100)/numero}%')
            elif domanda == str('N') or str('n'):
                print(sys.exit)
            else:
                print('[*] Operazione non valida!')
    
try:
    head()
    oprerazioni()
    x = int(input('[+] Operazione: '))
    if x == 1: 
        numero = int(input("[+] Numero da esaminare: "))
        a = numeri(numero) 
        a.pari(numero)
    elif x == 2: 
        numero = int(input("[+] Numero da esaminare: "))
        a = numeri(numero)
        a.serie(numero)
    elif x == 3:
        numero = int(input("[+] Numero da esaminare: "))
        a = numeri(numero)
        a.primi(numero)
    else:
        print('[*] Operazione non valida!')
except KeyboardInterrupt:
        print("[*] Aborto")
except SystemError as e:
    print("[*] Erorre!")


