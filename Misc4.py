from anonBrowser import *
import requests
import sys
import requests
import http.cookiejar
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

os.system('cls' if os.name == 'nt' else 'clear')


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

### aggiumgere proxy e user agent nella lista 
try:
    print("+" * 60)
    print("[1] Print HTML code")
    print("[2] Port Scanning")
    print("[3] Proxy Verification")
    print("[4] TCP client")
    print("+" * 60)

    print("")
    print("-" * 60)
    response = input("↳ ")
    print("-" * 60)
    print("")

    print("+" * 60)
    if response == str(1):
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
                url = str(input("↳ Select an url: "))
                page = browser.open(url)
                print("")
                print("Printing HTML..")
                print("")
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
                    print("")
                    print("Printing HTML..")
                    print("")
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
            source_code = page.read().decode('utf-8', errors='replace')
            print(source_code.encode(sys.stdout.encoding or 'utf-8', errors='replace').decode())
            print("")
            print("Printing HTML..")
            print("")
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
        print("+" * 60)
        print("             !!! WORKING IN PROGRESS !!!")
        print("+" * 60)
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

        

        def test_proxy(proxy_address):
            print(f"Proxy Test: {proxy_address}")
            options = Options()
            options.add_argument('--headless')
            options.add_argument(f'--proxy-server={proxy_address}')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')

            try:
                driver = webdriver.Chrome(options=options)
                driver.set_page_load_timeout(10)
                driver.get("https://httpbin.org/ip")
                time.sleep(2)  # Attendi risposta
                ip_text = driver.find_element(By.TAG_NAME, "body").text
                print(f"Work! Response: {ip_text}")
                driver.quit()
                return True
    
            except (WebDriverException, TimeoutException) as e:
                print(f"Failed: {e.__class__.__name__}")
                try:
                    driver.quit()
                except:
                    pass
                return False
            


        print("↳ Select proxy for the testing (format IP:PORTA), one for line. Write 'END' to finsh:")
        proxy_list = []

        while True:
            p = input("Proxy: ")
            if p.lower().strip() == 'fine':
                break
        proxy_list.append(p.strip())

        print("")
        print("Starting Test...")
        validi = []

        for proxy in proxy_list:
         if test_proxy(proxy):
            validi.append(proxy)


        print("Test Complete.")
        print("")
        print(f" Proxy valid ({len(validi)}):")
        for vp in validi:
            print(f" - {vp}")
    elif response == str("4"):

        
        target = input("↳ Target Host: ")
        port = input("↳ Target Port: ")
        target_port = int(port)
        target_host = str(target) 
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       ### Socket.AF_INET = classic Ipv4 address. SOCK_STREAM = TCP port
        client.connect((target_host, target_port))    
        target_host = target.encode()
        request = ("\bGET / HTTP/1.1\r\nHost: {0}\r\n\r".format(target))          ###Send dsome date 
        client.send(request.encode())             

        respose = client.recv(4096)     
        print(response) 
    elif response == str("5"):
        target = input(" ↳ Target Host: ")
        port   = input(" ↳ Target Port: ")
        target_host = str(target)
        target_port = int(port)
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        request = ('AAABBBCCC',(target_host, target_port))
        client.sendto(str(request).encode())
        data, addr = client.recvfrom(4096)
        print(data)
except KeyboardInterrupt:
    print('Abort')




