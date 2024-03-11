from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import  ImportContactsRequest
from telethon.tl.types import InputPhoneContact
import sys
import csv
import time
import random
import pyfiglet

from colorama import init, Fore
import os

init()

r = Fore.RED
g = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, g, w, ye, cy]
info = g + '[' + w + 'i' + g + ']' + rs
attempt = g + '[' + w + '+' + g + ']' + rs
sleep = g + '[' + w + '*' + g + ']' + rs
error = g + '[' + r + '!' + g + ']' + rs
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('palayeshkood')
    print(random.choice(colors) + logo + rs)
    print(f'{info}{g} user adder bot{rs}')
    print(f'{info}{g} Author: aliashtab | starkteam{rs}\n')

def clscreen():
    os.system('cls')

clscreen()
banner()
api_id = int(sys.argv[1])
api_hash = str(sys.argv[2])
phone = str(sys.argv[3])
file = str(sys.argv[4])
x = str(sys.argv[5])
print(file)
messagetosend = ""
with open(x, "r", encoding="UTF-8") as fim:
    messagetosend = fim.readline().strip()


print(messagetosend)
def update_list(lst, temp_lst):
    count = 0
    while count != len(temp_lst):
        del lst[0]
        count += 1
    return lst
users = []
with open(file, encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=',', lineterminator='\n')
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        users.append(user)


print(f"try do tasks withs {phone}")
client = TelegramClient(f'sessions{phone}', api_id, api_hash)
client.connect()
print(f'{info}{g}sending --->  {messagetosend}{rs}\n')
n = 0
added_users = []
for user in users:
    n += 1
    added_users.append(user)
    if n % 20 == 0:
        print(f'{sleep}{g} Sleep 2 min to prevent possible account ban{rs}')
        time.sleep(120)
    try:
        x = str(user['username'])
        if x.isdigit():
            contact = InputPhoneContact(client_id=0, phone=f"+{x}", first_name="hello", last_name="fe")
            result = client(ImportContactsRequest([contact]))
            try:
                print(f"send message to --> +{x}")
                client.send_message(f"+{x}", messagetosend)
                time.sleep(5)
            except:
                print("something went wrong try on next user")
                continue

        else:
            try:
                print(f"send message to --> @{x}")
                client.send_message(f"@{x}", messagetosend)
                time.sleep(5)
            except:
                print("something went wrong try on next user")
                continue


    except:
        print("something went wrong try on next user")
        continue

#os.system(f'del {file}')
input(f'{info}{g}Adding complete...Press enter to exit...')
sys.exit()
