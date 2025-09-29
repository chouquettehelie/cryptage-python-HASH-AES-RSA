from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import base64


k = RSA.generate(2048); pub, priv = k.publickey(), k

aes = get_random_bytes(16)
aes = PKCS1_OAEP.new(priv).decrypt(PKCS1_OAEP.new(pub).encrypt(aes))

msg = b"Hello hybride !"


c = AES.new(aes, AES.MODE_EAX); ct, tag = c.encrypt_and_digest(msg)
open("message.txt","w").write(base64.b64encode(c.nonce+tag+ct).decode())

d = base64.b64decode(open("message.txt").read())
m = AES.new(aes,AES.MODE_EAX,nonce=d[:16]).decrypt_and_verify(d[32:],d[16:32])
print(m.decode())
