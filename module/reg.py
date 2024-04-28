from telethon.sync import TelegramClient
import os

api_id = 6539950
api_hash = '111b6f6f44ba09b5858f9fee99a97322'

while True:
    print("Bekor qilish uchun 'x'.")
    raqam = str(input("Number: "))
    if raqam.lower() == "x":
        break

    if not raqam.startswith("+"):
        number = "+" + raqam

    with open('phone.csv', 'r') as f:
        if any(raqam in line for line in f):
            print("Allaqachon bu raqam mavjud.")
        else:
            print(f"Login {raqam}")

    client = TelegramClient(f"sessions/{raqam}", api_id, api_hash)

    try:
        # noinspection PyTypeChecker
        client.start(raqam)
        with open('../module/phone.csv', 'a') as f:
            f.write(f"\n{raqam}" if os.path.getsize('../module/phone.csv') > 0 else raqam)
        client.disconnect()
        print("✅✅Tayyor!")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
