from telethon.sync import TelegramClient
import csv
from telethon import utils, errors
import time

phonecsv = "phone"

with open(f'{phonecsv}.csv', 'r') as f:
    phlist = [row[0] for row in csv.reader(f)]

print('Jami📝: '+str(len(phlist)))

prchk = 'y'
channel = str(input("kanal [@ qo'shmang]:"))
idl = int(input("id [postni id raqamini yozing]:"))
butt = int(input("button raqami:(1 2 yoki 3 4 chi orni bo'yicha kiriting:)"))
limit = int(input("limit kiritin har bosishdagi to'xtash vaqti:"))

indexx = 0
print("tuzuvchi: t.me/al_haq_jaloliddin")
for phone in phlist:
    indexx += 1
    phone = utils.parse_phone(phone)
    print(f"Login {phone}")
    client = TelegramClient(f"sessions/{phone}", 6383658, '02f94e696f8230da8ca6d93aad570e08')
    client.start(phone)
    print(f'Index : {indexx}')
    if prchk.lower() == 'y':
        try:
            time.sleep(limit)
            msg = client.send_message(channel, '/start')
            msg.click(butt-1)
        except errors.MessageNotModifiedError:
            print("Button not found, skipping...")
            continue
        except Exception as e:
            print("Error:", e)
            print("Continuing with the next session...")
            continue
