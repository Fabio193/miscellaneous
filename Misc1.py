### Basato su Pyhton Guide for devs


import requests
import sys
import requests
from http.cookiejar import *
import urllib
import socket
from datetime import *
import subprocess 
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
import time
import mechanize
import threading
from geolite2 import *
import json
from geopy.geocoders import Nominatim
import geocoder

os.system('cls' if os.name == 'nt' else 'clear')

head = """

_   _    _    ____   ___  _     ___ ____  ___    _  _____ 
| \ | |  / \  |  _ \ / _ \| |   |_ _/ ___|/ _ \  / \|_   _|
|  \| | / _ \ | |_) | | | | |    | | |  _| | | |/ _ \ | |  
| |\  |/ ___ \|  __/| |_| | |___ | | |_| | |_| / ___ \| |  
|_| \_/_/   \_\_|    \___/|_____|___\____|\___/_/   \_\_|  



"""

print("-" * 80)
print("-" * 80)

print(head)

print("-" * 80)
print("-" * 80)

### aggiumgere proxy e user agent nella lista 
try:
    print("+" * 60)
    print("[1] Print HTML code")
    print("[2] Port Scanning")
    print("[3] Proxy Verification")
    print("[4] TCP Client")
    print("[5] UDP Client")
    print("[6] TCP Server")
    print("[7] UDP Server")
    print("[8] IP  Geolocalization ")
    print("+" * 60)

    print("")
    response = input("↳ ")
    print("")

    if response == str(1):
        print("-" * 60)
        print("PRINT HTML CODE(BETA)")
        print("-" * 60)
        print("")
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        cookie_jar = LWPCookieJar()
        browser.set_cookiejar(cookie_jar)
        user_agent = str(input("↳ Enter an user agent: "))
        browser.addheaders = [('User-agent', user_agent)]
        z = input("[+] Do you have a proxy? (Y/N): ")
        if z == str("N"):
            y = input("[+] Do you want continue without proxy? (Y/N):  ")
            if y == str("Y"):
                url = (input("↳ Select an url: "))
                page = browser.open(url)
                print("\nPrinting HTML..\n")
                time.sleep(5)
                
                source_code = page.read().decode('utf-8', errors='replace')
                print(source_code.encode(sys.stdout.encoding or 'utf-8', errors='replace').decode())
                time.sleep(5)
                print("")
               
                print("-" * 60)
                for cookie in cookie_jar:
                    print(f"Name: {cookie.name}")
                    print(f"Value: {cookie.value}")
                    print(f"Port: {cookie.port}")
                    print(f"Domain: {cookie.domain}")
                    print(f"Path: {cookie.path}")
                    print(f"Expires: {cookie.expires}")
                    print(f"Comment: {cookie.comment}")
                    print("-" * 40)
                    time.sleep(1)
                print("-" * 60)
                    
            elif y == str("N"):
                time.sleep(3)
                sys.exit()

        elif z == str("Y"):
            indirizzo = input("↳ Select a proxy: ")
            proxy = {
                "http": indirizzo,
                "https": indirizzo
             }
            print("→ Proxy configured:", proxy)
            try: 
                response = requests.get("http://example.com", proxies=proxy, timeout=10)
                print("[+] State:", response.status_code)
            except Exception as e:
                 print("↳ Error in the request", e)
                 x = str(input('[+] Continue? (Y/N): '))
                 if x == str("Y"):
                    url = str(input("↳ Select an url: "))
                    page = browser.open(url)
                    source_code = page.read().decode('utf-8', errors='replace')
                    print(source_code.encode(sys.stdout.encoding or 'utf-8', errors='replace').decode())
                    print("\nPrinting HTML..\n")
                    print(source_code)
                    time.sleep(5)
                    print("")
                   
                    print("-" * 60)
                    cookie_jar = LWPCookieJar()
                    browser.set_cookiejar(cookie_jar)
                    time.sleep(1)
                    for cookie in cookie_jar:
                        print(f"Name: {cookie.name}")
                        print(f"Value: {cookie.value}")
                        print(f"Port: {cookie.port}")
                        print(f"Domain: {cookie.domain}")
                        print(f"Path: {cookie.path}")
                        print(f"Expires: {cookie.expires}")
                        print(f"Comment: {cookie.comment}")
                        CookieJar.clear()
                    print("-" * 60)
                    time.sleep(1)
                
                   
                 elif x == str("N"):
                     sys.exit()
                 else:
                      sys.exit()

            browser.set_proxies(proxy)
            url = str(input("↳ Select an url: "))
            page = browser.open(url)
            source_code = page.read().decode('utf-8', errors='replace')
            print(source_code.encode(sys.stdout.encoding or 'utf-8', errors='replace').decode())
            print("\nPrinting HTML..\n")
            print(source_code)
            time.sleep(5)
            print("")
           
            print("-" * 60)
            for cookie in cookie_jar:
                print(f"Name: {cookie.name}")
                print(f"Value: {cookie.value}")
                print(f"Port: {cookie.port}")
                print(f"Domain: {cookie.domain}")
                print(f"Path: {cookie.path}")
                print(f"Expires: {cookie.expires}")
                print(f"Comment: {cookie.comment}")
                print("-" * 40)
                time.sleep(1)
            print("-" *60)
    elif response == str(""):
     sys.exit()
    elif response == str("2"):
        print("")
        print("-" * 60)
        print("PORT SCANNER(BETA)")
        print("-" * 60)
        print("")
        server  = str(input("Enter a remote host to scan: "))
        print("")
        remoteServerIP = socket.gethostbyname(server)  ### funzione un parametro


        print("+" * 60)
        print("Please wait, scanning remote host", remoteServerIP)
        portI = int(input("Select the first value port range(ES: 10, 200): "))
        portF = int(input("Select the second value port range(ES: 10, 200): "))
        print("+" * 60)
        print("")
        t1 = datetime.now()
        openport = []
        t1 = datetime.now()

        try:      
            for port in range(portI, portF):
             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   ### SOCK_STREAM = tipo TCP socket, AF_INET = famiglia di appartenenza del sockrt
             result = sock.connect_ex((remoteServerIP, port))
             if result != 0:
                    print("↳ Port {0}: Closed.".format(port))           
             elif result == 0:
                print("↳ Port {0}: Open.".format(port))
                openport.append(port)
                sock.close()
        except KeyboardInterrupt:
            print("Abort: You pressed Ctrl+C")
            sys.exit()
        except socket.gaierror:
            print("Hostname could not be resolved. Exiting")
            sys.exit()

        except socket.error:
            print("Couldn't connect to server")
            sys.exit()

        t2 = datetime.now()
        total = t2 - t1
        print("")
        print("+ Port Open:", openport)
        print("Scanning complete in {0}".format(total))     
    elif response == str("3"):
        socket.setdefaulttimeout(180)
        print("FROM https://github.com/ApsOps/proxy-checker")
        proxyList = []
        print("[+] Select a proxy (IP/PORT), write END to finish: ")
        while 1:
            p = input("↳ proxy: ")
            proxyList.append(p)
            if p == str('END'):
                break
        proxyList.remove('END')
        
        def is_bad_proxy(pip):    
            try:        
                proxy_handler = urllib.request.ProxyHandler({'http': pip})        
                opener = urllib.request.build_opener(proxy_handler)
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                urllib.request.install_opener(opener)        
                sock=urllib.request.urlopen('http://www.google.com')  # change the url address here
                #sock=urllib.urlopen(req)
            except urllib.error.HTTPError as e:        
                print('\n↳ Error code: ', e.code)
                return e.code
            except Exception as detail:
                print( "\n↳ ERROR:", detail)
                return 1
            return 0

        for item in proxyList:
            if is_bad_proxy(item):
                print ("\n↳ Bad Proxy", item)
            else:
             print("")
             print("↳", item, "is working") 
    elif response == str("4"):
        print("-" * 60)
        print("TCP CLIENT")
        print("-" * 60)
        try:
            target = input("↳ Target Host: ")
            port = input("↳ Target Port: ")
            target_port = int(port)
            target_host = str(target) 
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       ### Socket.AF_INET = classic Ipv4 address. SOCK_STREAM = TCP port
            client.connect((target_host, target_port))    
            target_host = target
            request = (input("\n↳ Data to sand:"))          ###Send dsome date  ###request = ("\bGET / HTTP/1.1\r\nHost: {0}\r\n\r".format(target)) 
            byte = int(input("↳ Bytes for response: "))
            client.send(request.encode("utf-8"))             

            response = client.recv(byte)
            if response == bytes(b''):
                print("\n[*] No bytes recived(", response, "). Connection closed!")
                sys.exit()
            print("\n↳ Recived bytes: ", response)
            print("↳ Recived str: ", response.decode('utf-8')) 
        except WindowsError:
            print("[*] Connection refused!")
    elif response == str("5"):
        print("-" * 60)
        print("UDP CLIENT")
        print("-" * 60)
        try:
            target = input("↳ Target Host: ")                   ### SERVER PER effettuare test echo.u-blox.com:8
            port   = input("↳ Target Port: ")
            target_host = str(target)
            target_port = int(port)
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                       ### sock_DGRAM = UDP port
            client.connect((target_host, target_port))                                         ### connesiione al client
            request = input("\n↳ Data to sand:  ")
            byte = int(input('↳ Bytes for reponse:'))                                                    ### Bytes da inviare al server. Scrivere qualcosa in str, poi viene converitito in bytes tramite modulo di codifica UTF-8, il server riceve la richesta, elabora, decide se rifiutare o accettare, manda output in byte, decodificazione byte in str leggibile. Se il byte = b'', il server NON RIceve TCP packest. OUTPUT OBBLIGATORIO
            client.send(request.encode("utf-8"))
            data, addr = client.recvfrom(byte)
            if data == bytes(b''):
                print("\n[*] No bytes recived(", data, "). Connection closed!")
            print("\n↳ Recived bytes: ", data)                                                          ### RICEZIONE di bytr
            print('↳ Recived str: ', data.decode("utf-8"))                                              ### decodificazione
        except WindowsError:
            print("[*] Connection refused")
        except KeyboardInterrupt:
            print("Abort")
    elif response == str("6"):
        print("-" * 60)
        print("TCP SERVER")
        print("-"* 60)
        try:
            ip = str(input("↳ Server ip: "))                                                                ### Input utenti
            port = int(input("↳ Server port: "))

            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((ip, port))                                                                     ### Inizializzazione server   
            server.listen(5)                                                                           ### Massimo 5 connessioni
            print("[*] Listening on {0}:{1}".format(ip, port))

            def handling_client(client_socket):                                                 ### gestione client
                 request = client_socket.recv(4096)
                 print("[*] Received: {0}".format(request))
                 print("[*] Sending response")
                 client_socket.send("Hello TCP client!".encode("utf-8"))                        ### Messaggio di default che il server manda al client. Codificato in utf-8
                 client_socket.close()

            while True:                                                                         ### Server in loop, aspettando le connessioni in entarta.
             client, addr = server.accept()                                                     ### Quando il client socket si connette, la variabile utente viene aggiunta alla variabile server client. Successivamente creiamo un thread per gestire le connessione in entarta e il loop è pronto per accettare nuovo connessioni.
             print("[+] Accepted connection from {0}:{1}".format(addr[0], addr[1]))             ### Inidirizzo di provenienza 
             client_handler = threading.Thread(target=handling_client,args=(client,))           
             client_handler.start()          
        except KeyboardInterrupt:
            print('Abort')
    elif response == str("7"):
        print("-" * 60)
        print("UDP SERVER")
        print("-"* 60)
        try:
            ip = str(input("↳ Server ip: "))
            port = int(input("↳ Server port: "))                                        ### input da utenti

            server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                      ### Inizializzazione soket
            server.bind((ip, port))                                                         ### Inizializzazione server
            print("[*] Listening on {0}:{1}".format(ip, port))                          
            while True:
                data, addr = server.recvfrom(1024)                                  # riceve fino a 1024 byte
                print(f"[+] Recived {addr}: {data.decode()}")                             ### inidrizzo di provenienza 
                server.sendto(data, addr)                                                ### Inizializzazione server
        except KeyboardInterrupt:
            print("Abort")
    elif response == str("8"):
        print("-" * 60)
        print("IP GEOLOCALIZATION")
        print("-"* 60)
        print("")
        host = str(input("↳ Select Target: "))
        ip_address = socket.gethostbyname(host)
        print("[*] ID: {0}".format(host))
        reader = geolite2.reader()
        response = reader.get(ip_address)
        continente = (json.dumps(response['continent']['names']['en'], indent = 4))
        country = (json.dumps(response['country']['names']['en'], indent = 4))
        y = (json.dumps(response['location']['latitude']))
        x = (json.dumps(response['location']['longitude']))
        
        print("[+] Continent: ", continente)
        print("[+] Country: ", country)
        print("[+] Latitude: ", y)
        print("[+] Longitude: ", x)

        geolocator = Nominatim(user_agent = "SborraSeriele80SchoolProject")

        location = geolocator.reverse((y, x), language='en')
        print('[+]', location.address)
        swat = input("[*] Swating? (Y/N): ")
        if swat == str("Y"):
            print("[*] Sending a request to the authorities")
            time.sleep(10)
            print("[+] Done!")
        elif swat == str("N"):
            sys.exit()



except KeyboardInterrupt:
    print('Abort')




