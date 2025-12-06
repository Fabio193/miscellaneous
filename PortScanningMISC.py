### Dal libro Pythob Guide. RandomStuff 
import psutil 
import socket 
import subprocess 
import sys 
import os
from datetime import *



### Pulire schermo 

os.system('cls' if os.name == 'nt' else 'clear')   ### Richiamo funzione con due parametri

### Richesta Input


head = str("""
 _   _    _    ____   ___  _     ___ ____  ___    _  _____ 
| \ | |  / \  |  _ \ / _ \| |   |_ _/ ___|/ _ \  / \|_   _|
|  \| | / _ \ | |_) | | | | |    | | |  _| | | |/ _ \ | |  
| |\  |/ ___ \|  __/| |_| | |___ | | |_| | |_| / ___ \| |  
|_| \_/_/   \_\_|    \___/|_____|___\____|\___/_/   \_\_|  

""")


print("-" * 60)
print("-" * 60)

print(head)

print("-" * 60)
print("-" * 60)
print("")
print("+" * 60)
print("             !!! WORKING IN PROGRESS !!!")
print("+" * 60)
print("")
server  = str(input("Enter a remote host to scan: "))
print("")
remoteServerIP = socket.gethostbyname(server)  ### funzione un parametro

### Banner estetico
print("+" * 60)
print("Please wait, scanning remote host", remoteServerIP)
portI = int(input("Select the first value port range(ES: 10, 200): "))
portF = int(input("Select the second value port range(ES: 10, 200): "))
print("+" * 60)
print("")
### Tempo impiegato dal tool

t1 = datetime.now()

openport = []


t1 = datetime.now()
### Scan di porte vulnerabili utilizzando il ciclo for. Porte da 1 a 1024

### Ripete il codice nel blocco try fino al termine delle operazioni. Se
try:      
 for port in range(portI, portF):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   ### SOCK_STREAM = tipo TCP socket, AF_INET = famiglia di appartenenza del sockrt
    result = sock.connect_ex((remoteServerIP, port))
    if result != 0:
       print("↳ Port {0}: Closed.".format(port))           ### Modifica apporttaa , check in corso
       sock.close()
    elif result == 0:
        print("↳ Port {0}: Open.".format(port))
        openport.append(port)
        sock.close()
        


### eccezioni del programma, degli avvisi per segnalere che non sta andando coome previsto
except KeyboardInterrupt:
   print("Abort: You pressed Ctrl+C")
   sys.exit()

except socket.gaierror:
   print("Hostname could not be resolved. Exiting")
   sys.exit()

except socket.error:
   print("Couldn't connect to server")
   sys.exit()

#### tempo fine esecuziione 
t2 = datetime.now()


### calcolo del tempo totale 
total = t2 - t1

print("")
print("+ Port Open:", openport)


print("Scanning complete in {0}".format(total))
