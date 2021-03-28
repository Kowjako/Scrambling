import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AES:
    def __init__(self, key):
        self.block_size = AES.block_size    #block size of AES = 128 bits 4x4 gdzie 1 komorka zajmuje 1 bajt
        self.key = hashlib.sha256(key.encode().digest()) #generujemy hash na podstawie klucza
        
    def __pad(self, text):
        number_of_bytes_to_pad = self.block_size - len(text) % self.block_size #ilosc bajtow ktora trzeba dodac aby dlugosc byla podzielna przez 128
        ascii_string = chr(number_of_bytes_to_pad)  #konwertujemy liczbe na tekst (ASCII)
        padding_str = number_of_bytes_to_pad * ascii_string #dodajemy potrzebna ilosc symboli
        padded_text = text + padding_str    #uzupelniamy tekst
        return padded_text
    
    
    def encode(self, text):
        
        
       

print(encoded)
print(decoded)