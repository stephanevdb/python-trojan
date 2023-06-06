from cryptography.fernet import Fernet


def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    decrypted_file_path = encrypted_file_path[:-4]  # Remove the '.enc' extension
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    print("File decrypted successfully.")