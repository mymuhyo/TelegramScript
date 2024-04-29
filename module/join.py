from telethon.sync import TelegramClient
import csv
import time
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import utils, errors

# Constants
PHONE_CSV = "src/phone.csv"


# Function to read phone numbers from CSV
def read_phone_numbers(filename):
    with open(filename, 'r') as file:
        return [row[0] for row in csv.reader(file)]


def main():
    # Read phone numbers from CSV
    phone_list = read_phone_numbers(PHONE_CSV)
    total_numbers = len(phone_list)
    print('Total Numbers: ', total_numbers)

    # Input private link or group username
    is_private = input('Is the group private? (Y/N): ').lower() == 'y'
    group_link = input('Enter the private link or group username: ')

    # Loop through phone numbers
    for index, phone_number in enumerate(phone_list, start=1):
        phone = utils.parse_phone(phone_number)
        print(f"Logging in {phone} (Index: {index}/{total_numbers})")

        # Initialize Telegram client
        client = TelegramClient(f"src/sessions/{phone}", 2152072, '004e98412f47431215095770454c9da4')
        client.start(phone)

        try:
            # Join group
            if is_private:
                client(ImportChatInviteRequest(group_link))
            else:
                client(JoinChannelRequest(group_link))

            print(f'Joined successfully: {group_link}')

            # Check if all numbers are processed
            if index >= total_numbers:
                print(f'All {total_numbers} numbers processed.')
                break

        except errors.FloodWaitError as e:
            print(f'Waiting {e.seconds} seconds before retrying...')
            time.sleep(e.seconds)
        except Exception as e:
            print(f'An error occurred: {e}')


if __name__ == "__main__":
    print("Starting the process...")
    main()
