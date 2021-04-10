
import os
import subprocess
import sys
import pygeoip
import json 
import requests
from simple_geoip import GeoIP
from ipwhois import IPWhois
import nmap3

from colorama import init, Fore
init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE
PURP  = Fore.MAGENTA


def main():
    logo = (f"""{PURP}
                                                 
                                                                  
 __         ______     ______   __  __     ______    
/\ \       /\  ___\   /\__  _\ /\ \_\ \   /\  ___\   
\ \ \____  \ \  __\   \/_/\ \/ \ \  __ \  \ \  __\   
 \ \_____\  \ \_____\    \ \_\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_____/     \/_/   \/_/\/_/   \/_____/ 
                                                      

""")
    print(logo)
    print("""
    1. Information Gathering
    2. Vulnerability Analysis
    3. Exploiting
    4. Passwords/Hashes
    5. GeoIP
    
    """)
    choice = input("Please select a module: ")
    import os
    clear = lambda: os.system('cls')
    clear()
    
    if choice == "1":
        print(logo)
        print("What kind of scan would you like to conduct?")
        print("1. Whois Scan")
        print("2. Port Scan")
        print("3. Subdomain Scanner")
        print("4. Spider")
        print("5. OS fingerprinting")
        print("99. Back \n")
        infochoice = input("Please put in your choice: ")
        if infochoice == "1":
            clear = lambda: os.system('cls')
            clear()
            print(logo) 
            ip = input("What IP do you want to look up: ")
            obj = IPWhois(ip)
            res = obj.lookup_whois()
            from pprint import pprint
            pprint(res)
        if infochoice == "2":
            clear = lambda: os.system('cls')
            clear()
            os.system("python modules/port_scanner.py")
        if infochoice == "3":
            clear = lambda: os.system('cls')
            clear()
            os.system("python modules/subdomain_scanner.py")
        if infochoice == "4":
            os.system("python modules/spider.py") 
        if infochoice == "5":
            import nmap3
            nmap = nmap3.Nmap()
            os_results = nmap.nmap_version_detection(input("Please enter the IP you want to scan: "))
            print(os_results)

    if choice == "2":
        print(logo)
        print("You have selected the Vulnerability Analysis module")
        print("1. SQLI vulnerability scan")
        print("2. SSL vulnerability scan")
        print("99. Back")
        choice2 = input ("Please select a module: ")
        if choice2 == "1":
            clear = lambda: os.system('cls')
            clear()
            os.system("python modules/sqli.py")
        if choice2 =="2":
            import os
            server = input("please put in the domain: ")
            command = 'pysslscan scan --scan=server.ciphers --scan=vuln.heartbleed --report=term:rating=ssllabs.2009e ' + server
        os.system(command)
        clear = lambda: os.system('cls')
        clear()
    if choice == "3":
        print(logo)
        print("1. SQL injection")
        print("2. DOS")
        print("99. Back")
        exChoice = input("Select an attack module: ")
        if exChoice == "1":
            clear = lambda: os.system('cls')
            clear()
            domain = input("what is the domain: ")
            import os
            myCmd = 'sqlmap -u ' + domain
            os.system(myCmd)
        if exChoice == "2":
            print("Please select one")
            print("1. SlowLoris")
            print("2. SYN flood")
            doschoice = input(": ")
            if doschoice == "1":
                clear = lambda: os.system('cls')
                clear()             
                domain = input("What is the domain: ")
                import os
                myCmd = "slowloris -v " + domain
                os.system(myCmd)
            if doschoice == "2":
                from modules import syn_flood                 
    if choice == "4":
        print(logo)
        print("Lets crack some hashes")
        print("1. hashes")
        print("2. brute")
        print("99. Back")
        choice1 = input("select a module: ")
        if choice1 == "1":
            clear = lambda: os.system('cls')
            clear()
            print(logo)
            print("1. Hash identifier")
            print("2. Hash Cracking")
            print("99. Back")
            cryptographyc1 = input("Please put in your choice: ")
            if cryptographyc1 == "1":
                from modules import hash_identifier
            if cryptographyc1 == "2":
                print("""
                1. Hash database lookup
                2. Hash dictionary attack
                """)
                c = input("Please choose a module: ")
                if c == "1":
                    clear = lambda: os.system('cls')
                    clear()
                    from modules import hash_database
                if c == "2":
                    clear = lambda: os.system('cls')
                    clear()
                    from modules import hash_cracker2


        if choice1 == "2":
            clear = lambda: os.system('cls')
            clear()          
            print(logo)
            print("""
    Please choose a module
        1. SSH
        2. FTP

                """)
            c1 = input(": ")
            if c1 == "1":
                from modules import ssh_bruter
            if c1 == "2":
                from modules import ftp_cracker


    if choice == "5":
        clear = lambda: os.system('cls')
        clear()
        print(logo)
        adress = input("what ip do you want me to locate: ")
        import urllib.request
        import json
        with urllib.request.urlopen("https://geolocation-db.com/json/" + adress) as url:
            data = json.loads(url.read().decode())
            print(data)
    else:
        return
if __name__ == '__main__':
    main()
