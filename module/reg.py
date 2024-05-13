from telethon.sync import TelegramClient
import os

api_id = 6539950
api_hash = '111b6f6f44ba09b5858f9fee99a97322'
csv_filename = 'src/phone.csv'


def login(phone_number):
    client = TelegramClient(f"src/sessions/{phone_number}", api_id, api_hash)
    client.start(phone_number)


def main():
    if not os.path.isfile(csv_filename):
        with open(csv_filename, 'w'):
            pass

    while True:
        print("Enter 'x' to exit.")
        phone_number = str(input("Number: ")).strip()
        if phone_number.lower() == "x":
            break

        if not phone_number.startswith("+"):
            phone_number = "+" + phone_number

        if login(phone_number):
            with open(csv_filename, 'a') as f:
                f.write(f"{phone_number}\n")
            print("Login successful!")
        else:
            print("Login failed.")


if __name__ == "__main__":
    main()
