from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# check if key exists --> if not, create it
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
else:
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

cipher = Fernet(key)

choice = int(input("Welcome to the Encrypter. Would you like to encrypt or decrypt?\n 1. Encrypt\n 2. Decrypt\n"))

if choice == 1:
    message = input("Enter the message you want to encrypt: ")
    ciphertext = cipher.encrypt(message.encode())
    print(f"\nEncrypted:\n{ciphertext.decode()}")

elif choice == 2:
    message = input("Enter the message you want to decrypt: ").strip()

    try:
        decrypted_message = cipher.decrypt(message.encode()).decode()
        print(f"\nDecrypted:\n{decrypted_message}")
    except Exception:
        print("\nError: Invalid key or message. Make sure you used the same key and a valid ciphertext.")

else:
    print("ERROR! Use only values 1 or 2.")
