import subprocess
from pip._vendor.colorama import Fore
import threading
import time
import os
#import layn


subprocess.call('start https://discord.gg/DDcXf472BF', shell=True)
subprocess.call('start https://github.com/DiabloAkar', shell=True)

#diabloakar
bammer = '''

████████▄   ▄█     ▄████████ ▀█████████▄   ▄█        ▄██████▄  
███   ▀███ ███    ███    ███   ███    ███ ███       ███    ███ 
███    ███ ███▌   ███    ███   ███    ███ ███       ███    ███ 
███    ███ ███▌   ███    ███  ▄███▄▄▄██▀  ███       ███    ███ 
███    ███ ███▌ ▀███████████ ▀▀███▀▀▀██▄  ███       ███    ███ 
███    ███ ███    ███    ███   ███    ██▄ ███       ███    ███ 
███   ▄███ ███    ███    ███   ███    ███ ███▌    ▄ ███    ███ 
████████▀  █▀     ███    █▀  ▄█████████▀  █████▄▄██  ▀██████▀  
                                          ▀                    

'''

print()
print(Fore.RED+bammer)
print(Fore.WHITE+'|'+Fore.GREEN+'1'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Http'+Fore.WHITE+'|')
print(Fore.WHITE+'|'+Fore.GREEN+'2'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Socks4'+Fore.WHITE+'|')
print(Fore.WHITE+'|'+Fore.GREEN+'3'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Socks5'+Fore.WHITE+'|')
print()
site = input(Fore.WHITE+'|'+Fore.GREEN+'Proxy Tür Seçimini Yap'+Fore.WHITE+'| > ')

if site == '1':
    print()
    print(Fore.WHITE+'|'+Fore.GREEN+'1'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Tümü'+Fore.WHITE+'|')
    print(Fore.WHITE+'|'+Fore.GREEN+'2'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Elit'+Fore.WHITE+'|')
    print(Fore.WHITE+'|'+Fore.GREEN+'3'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Anonim'+Fore.WHITE+'|')
    print(Fore.WHITE+'|'+Fore.GREEN+'3'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Seffaf'+Fore.WHITE+'|')
    print()
    Anonimlik = input(Fore.WHITE+'|'+Fore.GREEN+'Proxy Özellik Seçimini Yap'+Fore.WHITE+'| > ')
    if Anonimlik == '1':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all&simplified=true")
    if Anonimlik == '2':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=elite&simplified=true")
    if Anonimlik == '3':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=anonymous&simplified=true")
    if Anonimlik == '4':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=transparent&simplified=true")

if site == '2':
    print()
    print(Fore.WHITE+'|'+Fore.GREEN+'1'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Tümü'+Fore.WHITE+'|')
    print(Fore.WHITE+'|'+Fore.GREEN+'2'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Turkey'+Fore.WHITE+'|')
    print(Fore.WHITE+'|'+Fore.GREEN+'3'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' United State of America'+Fore.WHITE+'|')
    print(Fore.WHITE+'|'+Fore.GREEN+'3'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' GER'+Fore.WHITE+'|')
    print()
    Ulke = input(Fore.WHITE+'|'+Fore.GREEN+'Ülke Seçimini Yap'+Fore.WHITE+'| > ')
    if Ulke == '1':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all&simplified=true")
    if Ulke == '2':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=5000&country=TR&simplified=true")
    if Ulke == '3':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=5000&country=US&simplified=true")
    if Ulke == '4':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=5000&country=ger&simplified=true")


if site == '3':
    print()
    print(Fore.WHITE+'|'+Fore.GREEN+'1'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Tümü'+Fore.WHITE+'|')
    print(Fore.WHITE+'|'+Fore.GREEN+'2'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Turkey'+Fore.WHITE+'|')
    print(Fore.WHITE+'|'+Fore.GREEN+'3'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' United State of America'+Fore.WHITE+'|')
    print(Fore.WHITE+'|'+Fore.GREEN+'3'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' GER'+Fore.WHITE+'|')
    print()
    Ulke = input(Fore.WHITE+'|'+Fore.GREEN+'Ülke Seçimini Yap'+Fore.WHITE+'| > ')
    if Ulke == '1':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=5000&country=all&simplified=true")
    if Ulke == '2':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=5000&country=TR&simplified=true")
    if Ulke == '3':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=5000&country=US&simplified=true")
    if Ulke == '4':
        os.system("start https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=5000&country=ger&simplified=true")

else:
    print('Yanlış tuşlama yaptınız program kendisini 5 saniye sonra kapatacaktır!')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('5')
    time.sleep(1)
    print(Fore.RED+'PROGRAM KENDİNİ KAPATIYOR')
    time.sleep(3)

    
#diabloakar
