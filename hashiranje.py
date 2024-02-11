import hashlib

def hash_text(text):

    text_bytes = text.encode('utf-8')

    hash_object = hashlib.sha256()
    
    hash_object.update(text_bytes)
    
    hash_value = hash_object.hexdigest()
    
    return hash_value

print("Unesite tekst koji želite hashirati:")
text = input()
hashed_text = hash_text(text)
print("Originalni tekst:", text)
print("Hash vrijednost:", hashed_text)
