def caesar_cipher_encrypt(text, key):
    if key < 1 or key > 25:
        print("Neispravan unos! Ključ mora biti u rasponu od 1 do 25.")
        return None
    
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + key) % 26
            encrypted_char = chr(ord('a') + shift)
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        elif char.isdigit():
            encrypted_char = str((int(char) + key) % 10)
            encrypted_text += encrypted_char
        else:
            shift = (ord(char) + key) % 128
            encrypted_char = chr(shift)
            encrypted_text += encrypted_char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') - key) % 26
            decrypted_char = chr(ord('a') + shift)
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        elif char.isdigit():
            decrypted_char = str((int(char) - key) % 10)
            decrypted_text += decrypted_char
        else:
            shift = (ord(char) - key) % 128
            decrypted_char = chr(shift)
            decrypted_text += decrypted_char
    return decrypted_text

def get_hidden_input(prompt):
    import msvcrt
    print(prompt, end='', flush=True)
    password = ''
    while True:
        char = msvcrt.getch()
        char = char.decode('utf-8')
        if char == '\r':
            print()
            return password
        elif char == '\b':
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)

def get_valid_key_input(prompt):
    while True:
        key = get_hidden_input(prompt)
        if key.isdigit() and 1 <= int(key) <= 25:
            return int(key)
        else:
            print("Neispravan unos! Ključ mora biti cijeli broj u rasponu od 1 do 25.")

message = get_hidden_input("Unesi poruku: ")
key = get_valid_key_input("Unesi ključ za enkripciju (1-25): ")

while key is None:
    message = get_hidden_input("Unesi poruku: ")
    key = get_valid_key_input("Unesi ključ za enkripciju (1-25): ")

encrypted_message = caesar_cipher_encrypt(message, key)
print("Enkriptovana poruka:", encrypted_message)

decrypt_key = get_hidden_input("Unesi ključ za dekripciju: ")
decrypted_message = caesar_cipher_decrypt(encrypted_message, int(decrypt_key))
print("Dekriptovana šifra:", decrypted_message)

def main():

    while True:
        print("1. Enkripcija")
        print("2. Izlaz")

        choice = input("Unesi izbor: ")

        if choice == "1":
            message = get_hidden_input("Unesi poruku: ")
            key = get_valid_key_input("Unesi ključ za enkripciju (1-25): ")
            while key is None:
                message = get_hidden_input("Unesi poruku: ")
                key = get_valid_key_input("Unesi ključ za enkripciju (1-25): ")
            encrypted_message = caesar_cipher_encrypt(message, key)
            print("Enkriptovana poruka:", encrypted_message)
        elif choice == "2":
            print("Izlaz.")
            break
        else:
            print("Neispravan izbor! Pokušaj ponovo.")

if __name__ == "__main__":
    main()
    
