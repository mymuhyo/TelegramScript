"""
    Create telegram sessions.
"""


# Import the necessary classes from the 'telegram' module
from telegram import TelethonSession

# Initialize instances TelethonSession and PyrogramSession
ts = TelethonSession()

# Define API credentials and user information
api_id = 25679717
api_hash = "0cdc672fddfe30f6065d95872fcb4cb6"
phone = input("Nomer: ")
password = input("Password: ")


ts.session_file(api_id, api_hash, phone, password)