import sys
import os
from rsagestion import RsaGestion

rsa_obj = RsaGestion()

rsa_obj.generation_clef("public.pem","private.pem", 2048)

rsa_obj.chargement_clefs("public.pem","private.pem")

message = "Bonjour RSA"

encrypted = rsa_obj.chiffrement_rsa(message)
print(f"Message chiffre : {encrypted}")

decrypted = rsa_obj.dechiffrement_rsa(encrypted)
print(f"message dechiffre : {decrypted}")



