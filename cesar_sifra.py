def caesar_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + key) % 26
            encrypted_char = chr(ord('a') + shift)
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, key):
    return caesar_cipher_encrypt(encrypted_text, -key)

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

message = get_hidden_input("Unesi poruku: ")
key = get_hidden_input("Unesi ključ za enkripciju: ")

encrypted_message = caesar_cipher_encrypt(message, int(key))
print("Enkriptovana poruka:", encrypted_message)

decrypt_key = get_hidden_input("Unesi ključ za dekripciju: ")
decrypted_message = caesar_cipher_decrypt(encrypted_message, int(decrypt_key))
print("Dekriptovana šifra:", decrypted_message)
