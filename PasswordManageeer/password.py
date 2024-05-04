# from cryptography.fernet import Fernet
# """
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)"""

# def load_key():
#     file = open("key.key","rb")
#     key = file.read()
#     file.close()
#     return key

# master_pwd = input("Enter the master password: ").lower()
# key = load_key() + master_pwd.encode()
# fer = Fernet(key)




# def view():
#     with open("pswd.txt",'r') as f:
#         for i in f.readlines():
#             name, pwd  = (i.rstrip()).split("|")
#             print(f"name: {name} , password: {fer.decrypt(pwd.encode())}")
    

# def add():
#     name = input("Account name: ")
#     pwd =input("Enter the password: ")
#     with open("pswd.txt",'a') as f:
#         f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +'\n')

#     pass


# while True:
#     mode = input("Enter the mode you want 1.view 2. add and 3. q for exit: ").lower()

#     if mode =="q":
#         break

#     if mode == "1":
#         view()
#     elif mode == "2":
#         add()
#     else :  
#         print("invalid choice:  ")
#         continue
    
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode
import os

def generate_key_from_password(password: str) -> Fernet:
    salt = os.urandom(16)  # Ideally, save this salt somewhere to reuse when decrypting
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = urlsafe_b64encode(kdf.derive(password.encode()))
    return Fernet(key), salt

def load_key_and_salt() -> (bytes, bytes):
    with open("key.key", "rb") as key_file:
        key = key_file.read(32)
        salt = key_file.read(16)
    return key, salt

def get_fernet(master_pwd: str, salt: bytes) -> Fernet:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = urlsafe_b64encode(kdf.derive(master_pwd.encode()))
    return Fernet(key)

def view(fer: Fernet):
    try:
        with open("pswd.txt",'r') as f:
            for line in f.readlines():
                name, pwd  = line.strip().split("|")
                try:
                    decrypted_pwd = fer.decrypt(pwd.encode()).decode()
                    print(f"Account: {name}, Password: {decrypted_pwd}")
                except Exception as e:
                    print(f"Error decrypting password for {name}: {str(e)}")
    except FileNotFoundError:
        print("Password file not found.")

def add(fer: Fernet):
    name = input("Account name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open("pswd.txt", 'a') as f:
        f.write(name + "|" + encrypted_pwd + '\n')

master_pwd = input("Enter the master password: ")
# Initialize Fernet key
fer, salt = generate_key_from_password(master_pwd)

while True:
    mode = input("Enter the mode you want (1.view 2.add 3.q to quit): ").lower()
    if mode == "q":
        break
    elif mode == "1":
        view(fer)
    elif mode == "2":
        add(fer)
    else:
        print("Invalid choice.")
