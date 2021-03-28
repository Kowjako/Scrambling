import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCoder:
    def __init__(self, key):
        self.block_size = AES.block_size   #block size of AES = 128 bits 4x4 gdzie 1 komorka zajmuje 1 bajt
        self.key = hashlib.sha256(key.encode()).digest() #generujemy hash na podstawie klucza
        
    def __pad(self, text):
        numOfBytes = self.block_size - len(text) % self.block_size #ilosc bajtow ktora trzeba dodac aby dlugosc byla podzielna przez 128
        asciiLetter = chr(numOfBytes)  #konwertujemy liczbe na tekst (ASCII)
        paddingStr = numOfBytes * asciiLetter #dodajemy potrzebna ilosc symboli
        paddedTxt = text + paddingStr    #uzupelniamy tekst
        return paddedTxt
    
    def __unpad(self,text):  #usuniecie dodanych elemntow w __pad
        lastLetter = text[len(text) - 1] #zwraca ostatni symbol
        removeCounter = ord(lastLetter)    #funkcja dzialajaca odwrotnie do chr zwraca kod symbolu
        return text[:-removeCounter]    #obcina od konca
    
    def encode(self, text): 
        paddedTxt = self.__pad(text) #uzupelniamy do dlugosci podzelnej przez 128
        vectorCode = Random.new().read(self.block_size) #wektor do szyfrowania 
        cipher = AES.new(self.key, AES.MODE_CBC, vectorCode) #tworzenie szyfru
        encodedTxt = cipher.encrypt(paddedTxt.encode()) #encrypt text converted to bits    
        return b64encode(vectorCode+encodedTxt).decode("utf-8") #konwertujemy w normalna postac
    
    def decode(self, encodedtext):
        encodedtext = b64decode(encodedtext)    #kowertujemy na bity
        vectorCode = encodedtext[:self.block_size]  #wyodrebniamy wektor kodowy ktory dodalismy w linijce 29
        cipher = AES.new(self.key, AES.MODE_CBC,vectorCode) 
        decodedText = cipher.decrypt(encodedtext[self.block_size:]).decode("utf-8") #dekodujemy zacynajac od pozycji po wektorze
        return self.__unpad(decodedText)    #usuwamy symbole ktore byly dodane przez __pad

sygnalToCode = '0000000110100101010'
print(sygnalToCode)
cipher = AESCoder('AesTestKey') 
encoded = cipher.encode(sygnalToCode)
decoded = cipher.decode(encoded)

print(encoded)
print(decoded)