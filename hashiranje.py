import hashlib

def hash_text(text):
    # Konvertiraj tekst u bytes format prije hashiranja
    text_bytes = text.encode('utf-8')
    
    # Stvori objekt hash funkcije (ovdje koristimo SHA-256)
    hash_object = hashlib.sha256()
    
    # Dodaj tekst u hash objekt
    hash_object.update(text_bytes)
    
    # Izračunaj hash vrijednost
    hash_value = hash_object.hexdigest()
    
    return hash_value

# Primjer korištenja
print("Unesite tekst koji želite hashirati:")
text = input()
hashed_text = hash_text(text)
print("Originalni tekst:", text)
print("Hash vrijednost:", hashed_text)
