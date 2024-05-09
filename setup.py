import os

from config import SESSIONS_DIR, PHONE_CSV

# Check if the directory exists, if not, create it
os.makedirs(SESSIONS_DIR, exist_ok=True)

# Create the phone.csv file if it doesn't exist
if not os.path.exists(PHONE_CSV):
    with open(PHONE_CSV, 'a'):
        pass

print("Done")
