from aesgestion import AesGestion

aes = AesGestion();
aes.generate_aes_key();
aes.load_aes_key_from_file('aes_keys.bin');
aes.decrypt_file("test_crypting.txt","test_decrypting.txt");

