from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from datetime import datetime

#define our data
data=b"SECRETDATA"


output = f"output/encryptedfile{datetime.now()}.bin"

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open(output, "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()

#################################################################

file_in = open(output, "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

#the person decrypting the message will need access to the key
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data.decode('UTF-8'))