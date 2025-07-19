from base64 import b64decode
from Crypto.Cipher import DES3

# 24-byte DES-EDE3 key (config.inc.php)
key = KEY

# Encrypted values in base64 (session)
data = {
    'password': 'PASSWORD',
    'auth_secret': 'AUTH_SECRET',
    'request_token': 'REQUEST_TOKEN'
}

def decrypt_des3_cbc(value, key):
    try:
        raw = b64decode(value)
        iv = raw[:8]
        cipher_text = raw[8:]
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        decrypted = cipher.decrypt(cipher_text)

        decrypted = decrypted.rstrip(b'\x00')[:-1]
        return decrypted.decode(errors='replace')
    except Exception as e:
        return f"[ERROR] {e}"

# Show decrypted password, show all values
for k, v in data.items():
    result = decrypt_des3_cbc(v, key)
    print(f"[+] Decrypted {k}: {result}")
  
