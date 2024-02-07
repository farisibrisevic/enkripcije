import random

def simple_encrypt_password(password):
    encrypted_password = ""
    for char in password:
        encrypted_char = chr(ord(char) + 1)
        encrypted_password += encrypted_char
    return encrypted_password

def complicated_encrypt_password(password):
    encrypted_password = ""
    for char in password:
        ascii_value = ord(char)
        encrypted_ascii_value = ascii_value + 3
        if 32 <= ascii_value <= 126:  
            if char.isalpha():
                if char.islower():
                    if encrypted_ascii_value > ord('z'):
                        encrypted_ascii_value -= 26
                elif char.isupper():
                    if encrypted_ascii_value > ord('Z'):
                        encrypted_ascii_value -= 26
                encrypted_ascii_value -= 8
            else:
                if encrypted_ascii_value > 126:
                    encrypted_ascii_value -= 94
        else:  
            if encrypted_ascii_value > 1114111:
                encrypted_ascii_value -= 1113981
        encrypted_password += chr(encrypted_ascii_value)
    return encrypted_password

def random_encrypt_password(password):
    encrypted_password = ""
    for char in password:
        if char.isalnum():  
            if char.isalpha():
                if char.islower():
                    unicode_value = ord(char) + random.randint(1, 100)  
                    encrypted_password += chr(unicode_value)
                elif char.isupper():
                    
                    combinations = [
                        char * 3,
                        ''.join(random.sample(char * 3, 3)),
                        ''.join(random.sample(char * 3, 3))
                    ]
                    encrypted_password += random.choice(combinations)
            else:
                
                encrypted_number = str(int(char) + random.randint(1, 100))
                encrypted_password += encrypted_number
        else:
            
            unicode_value = ord(char) + random.randint(1, 100)
            encrypted_password += chr(unicode_value)
    return encrypted_password

def main():
    while True:
        print("1. Jednostavna enkripcija")
        print("2. Komplikovana enkripcija")
        print("3. Nasumična enkripcija")
        print("4. Izlaz")

        choice = input("Unesi izbor: ")

        if choice == "1":
            password = input("Unesi šifru: ")
            encrypted_password = simple_encrypt_password(password)
            print("Enkriptovana šifra:", encrypted_password)
        elif choice == "2":
            password = input("Unesi šifru: ")
            encrypted_password = complicated_encrypt_password(password)
            print("Enkriptovana šifra:", encrypted_password)
        elif choice == "3":
            password = input("Unesi šifru: ")
            encrypted_password = random_encrypt_password(password)
            print("Enkriptovana šifra:", encrypted_password)
        elif choice == "4":
            print("Izlaz.")
            break
        else:
            print("Neispravan izbor.")

        encrypt_another = input("Da li želiš enkriptovati još jednu šifru? (da/ne): ")
        if encrypt_another.lower() != "da":
            print("Izlazak iz programa.")
            break


if __name__ == "__main__":
    main()
