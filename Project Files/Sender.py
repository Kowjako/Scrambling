import time
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import Channel
import numpy as np
from random import shuffle
from tkinter.filedialog import askopenfilename


class sender:
    def __init__(self):
        window = tk.Tk()    #generowanie okna
        window.title("Nadawca sygnalu")
        window.geometry("310x500")
        window.resizable(False, False)

        def imgfromfile():  # wczytanie obrazu z pliku i konwertowanie do tablicy bitow
            filename = askopenfilename(initialdir="/", title="Wybierz plik")
            image = Image.open(filename).resize((250, 250)) #dostosowanie obrazu do ramki
            image = image.convert('1')  #konwertowanie na czarno-bialy
            photo = ImageTk.PhotoImage(image)
            
            global imgLabel
            #Tworzenie obrazu 
            imgLabel = Label(image=photo, borderwidth=2, relief="groove")
            imgLabel.image = photo
            imgLabel.place(x = 30, y = 50)
    
            img = Image.open(filename).convert('1') #konwertowanie na czarno-bialy
            arrImage = np.array(img)  #tworzenie tablicy na podstawie obrazu
            
            bitTable = []   #tabela do przechowywania bitow obrazu
            for x in np.nditer(arrImage):
                bitTable.append(x)    #generowanie tablicy na podstawie bitow obrazu
            for x in range(len(bitTable)):
                if bitTable[x]:       #kodowanie z postaci True-false na postac zero-jedynkowa
                    bitTable[x] = 1
                else:
                    bitTable[x] = 0
            global signal
            signal = bitTable

        def send(algorytm):  #przeslanie do odbiorcy
            
            #Channel.Channel(signal, selectedAlgorithm)
        
        algorytm = IntVar() #zmienna do przechowywania wybranego algorytmu

        #Generowanie napisu twoj obrazek
        imageLabel = tk.Label(text="Twoj obrazek", fg="black", width=28, anchor="center",font=('Times New Roman', 12))
        imageLabel.place(x = 30, y = 10)
        
        #Generowanie przycisku wybierz zdjecie
        button1 = tk.Button(text="Wybierz obraz", height = 3, width = 15,font=('Times New Roman', 10), command=lambda: imgfromfile())
        button1.place(x = 30, y = 340)
        
        #Generowanie przycisku wyslij
        button4 = tk.Button(text="Wyslij obraz", height = 3, width = 15,font=('Times New Roman', 10), fg="#123456", command=lambda: send(algorytm))
        button4.place(x = 160, y = 340)

        #Generowanie napisu wybory typu scramblingu
        scramblingType = tk.Label(text="Wybierz typ scramblingu: ", fg="black", width=30, anchor="w", font=('Times New Roman', 10))
        scramblingType.place(x = 30, y = 420)
        
        #Generowanie przycisku algorytmu B8ZS 
        button2 = tk.Radiobutton(text="B8ZS", variable=algorytm, value=0, anchor="w", height=2)
        button2.place(x = 30, y = 440)
        
        #Generowanie przycisku algorytmu HDB3
        button3 = tk.Radiobutton(text="HDB3", variable=algorytm, value=1, anchor="w", height=2)
        button3.place(x = 100, y = 440)
        
        

        window.mainloop() #wyswietlenie okna
 