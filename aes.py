from aesgestion import AesGestion

aes = AesGestion();
aes.generate_aes_key(); 
aes.save_aes_key_to_file("aes_key.bin")

aes.encrypt_file("message.txt", "message_chiffre.txt");
aes.load_aes_key_from_file("aes_key.bin");
aes.decrypt_file("message_chiffre.txt", "message_dechiffre.txt"); 


