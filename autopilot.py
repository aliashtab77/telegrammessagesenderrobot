
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError

import sys
from telethon.tl.functions.channels import JoinChannelRequest
import csv
import time
import keyboard
import random
import pyfiglet
from colorama import init, Fore
import os
import pickle
'''
try:
    import beepy
except ImportError:
    if os.name == 'nt':
        os.system('pip install beepy')
    else:
        pass
'''
init()

r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '(' + w + 'i' + lg + ')' + rs
error = lg + '(' + r + '!' + lg + ')' + rs
success = w + '(' + lg + '*' + w + ')' + rs
INPUT = lg + '(' + cy + '~' + lg + ')' + rs
plus = lg + '(' + w + '+' + lg + ')' + rs
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('palayeshkood')
    print(random.choice(colors) + logo + rs)
    print(f'{r}   Version: {w}0.0 {r}| Author: {w}aliashtab | starkteam{rs}')


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clr()
banner()
users = []
input_file = 'members\\members.txt'
with open(input_file, 'r',) as f:
    for i in f:
        users.append(i.strip())


accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break
print('\n' + info + lg + ' Creating sessions for all accounts...' + rs)
for a in accounts:
    iD = int(a[0])
    Hash = str(a[1])
    phn = str(a[2])
    clnt = TelegramClient(f'sessions{phn}', iD, Hash)
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            code = input(f'{INPUT}{lg} Enter code for {w}{phn}{cy}[s to skip]:{r}')
            if 's' in code:
                accounts.remove(a)
            else:
                clnt.sign_in(phn, code)
        except PhoneNumberBannedError:
            print(f'{error}{w}{phn} {r}is banned!{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print('\n'+info+lg+'Banned account removed'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print(info+' Sessions created!')
time.sleep(2)
print(f'{info}{lg} Joining from all accounts...{rs}')
time.sleep(2)
clr()
number = len(accounts)
print(f'{info}{lg} Total accounts: {w}{number}')
print(f'{info}{lg} If you have more than 10 accounts then it is recommended to use 10 at a time')
a = int(input(f'{plus}{lg} Enter number of accounts to use: {r}'))
to_use = []
print(f'\n{info}{lg} Distributing CSV files...{rs}')
time.sleep(2)
for i in accounts[:a]:
    done = []
    to_use.append(i)
    file = 'members\\members' + str(accounts.index(i)) + '.csv'
    with open(file, 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(['username'])
        for user in users[:30]:
            writer.writerow([user])
            done.append(user)
    del_count = 0
    while del_count != len(done):
        del users[0]
        del_count += 1
    if len(users) == 0:
        break
if not len(users) == 0:
    with open('members\\membersbaghimand.txt', 'w', encoding='UTF-8') as f:
        for user in users:
            f.write(f"{user}\n")
    m = str(len(users))
    print(f'{info}{lg} Remaining {m} users stored in {w}membersbaghimand.txt')
for acc in to_use:
    accounts.remove(acc)
with open('vars.txt', 'wb') as f:
    for acc in accounts:
        pickle.dump(acc, f)
    for k in to_use:
        pickle.dump(k, f)
    f.close()

print(f'{info}{lg} txt file distribution complete{rs}')
time.sleep(2)
clr()
if not os.name == 'nt':
    print(f'{error}{r} Automation supports only Windows systems')
    sys.exit()



messagetosend = input(f'{info}{lg} please insert your message to send:{rs}')

with open("message.txt", "w", encoding="UTF-8") as file:
    file.write(messagetosend)

program = 'messagesender.py'
o = str(len(to_use))
print(f'\n{info}{r} This will be fully automated.')
print(f'{info}{r} Don\'t touch the keyboard until cmd window pop-up stops')
input(f'\n{plus}{lg} Press enter to continue...{rs}')
print(f'\n{info}{lg} Launching from {o} accounts...{rs}\n')
for i in range(5, 0, -1):
    print(random.choice(colors) + str(i) + rs)
    time.sleep(1)
for account in to_use:
    api_id = str(account[0])
    api_hash = str(account[1])
    phone = str(account[2])
    file = 'members\\members' + str(to_use.index(account)) + '.csv'
    os.system('start cmd')
    time.sleep(1.5)
    keyboard.write('python' + ' ' + program + ' ' + api_id + ' ' + api_hash + ' ' + phone + ' ' + file + ' ' + 'message.txt' + ' ')
    keyboard.press_and_release('Enter')
    print(f'{plus}{lg} Launched from {phone}')
#beepy.beep(sound='ping')
