from telethon.sync import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError,
)


class TelethonSession:
    @staticmethod
    def session_file(api_id: int, api_hash: str, phone, password=None):
        """
        Create new telethon session file.
        :param api_id: Your api id.
        :param api_hash: Your api hash.
        :param phone: Your phone number.
        :param password: Optional if the account have 2FA enabled.
        """
        client = TelegramClient(f'{phone}.session', api_id, api_hash)
        try:
            client.start(phone, password)
        except ValueError:
            # If 2FA is enabled, Telegram requires the password
            password = input("Please enter your Telegram password: ")
            client.start(phone, password)
        print("\n🟢 Success!")
