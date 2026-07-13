from getpass import getpass
from werkzeug.security import generate_password_hash
import os

# If .env file doesn't exist, create it, otherwise write generated password
if not os.path.exists('.env'):
    with open('.env', 'w') as f:
        pw = getpass('Set a new password: ')
        if pw == '':
            print("Password cannot be empty. Please try again.")
            exit()
        f.write(f"PASSWORD={generate_password_hash(pw)}\n")
        os.chmod('.env', 0o600) # Set file permissions to read/write for owner only
        print("Password set successfully.")
else:
    with open('.env', 'r') as f:
        lines = f.readlines()
    with open('.env', 'w') as f:
        for line in lines:
            if line.startswith('PASSWORD='):
                pw = getpass('Set a new password: ')
                if pw == '':
                    print("Password cannot be empty. Please try again.")
                    exit()
                f.write(f"PASSWORD={generate_password_hash(pw)}\n")
                break
            else:
                f.write(line)
    os.chmod('.env', 0o600)  # Set file permissions to read/write for owner only
    print("Password set successfully.")
