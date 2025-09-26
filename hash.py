from hashgestion import HashGestion  

h = HashGestion()

fichier = "message.txt"  
empreinte = h.calculate_file_sha256(fichier)

print(f"SHA256 de {fichier} : {empreinte}")
