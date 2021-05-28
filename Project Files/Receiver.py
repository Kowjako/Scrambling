import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import math
import numpy as np

class receiver:
    def __init__(self, puresignal, puresignaldisrupted, descrambledSygnal, algorythm):
        
        window = tk.Tk() #tworzenie okna glownego
        window.title("Odbiorca sygnalu")
        window.resizable(False, False)
        window.geometry("860x550")

        def comparePureToDescrambled(puresignal, descrambledSygnal):  # zestawienie dwoch sygnalow, pokazanie roznic
            descrambledSygnal = descrambledSygnal.signal
            counter = 0
            for i in range(len(puresignal)):
                if (puresignal[i] != descrambledSygnal[i]):
                    counter += 1
            return counter

        def comparePureToDisrupted(array1, array2):  # zestawienie dwoch sygnalow, pokazanie roznic
            counter = 0
            for i in range(len(array1)):
                if (array1[i] != array2[i]):
                    counter += 1
            return counter

        def receive_puresignal(pureSignal):  # wypelnienie miejsca na sygnal wysylany
            sygnal = []
            for i in range(len(pureSignal)):
                sygnal.append(pureSignal[i])
            plt.imsave('pure.png', np.array(sygnal).reshape(int(math.sqrt(len(sygnal))), int(math.sqrt(len(sygnal)))))  #zapisanie pliku
            image = Image.open("pure.png").resize((250, 250))   #otwarcie pliku
            
            photo = ImageTk.PhotoImage(image)   #generowanie obrazku na podstawie pliku
            label1 = Label(image=photo, borderwidth=2)
            label1.image = photo
            label1.place(x = 20, y = 20)

        def receive_puresignaldisrupted(disruptedSignal):  # wyplenienie miejsca na signal zaklocony niescramblowany
            for i in range(len(disruptedSignal)):
                disruptedSignal[i] = int(disruptedSignal[i])
            
            plt.imsave('withoutScrambling.png', np.array(disruptedSignal).reshape(int(math.sqrt(len(disruptedSignal))), int(math.sqrt(len(disruptedSignal)))))
            image = Image.open("withoutScrambling.png").resize((250, 250))
            
            photo = ImageTk.PhotoImage(image)
            label2 = Label(image=photo, borderwidth=2)
            label2.image = photo
            label2.place(x = 300, y = 20)

        def receive_descrambledSygnal(descrambledSygnal):  # wypelnienie miejsca na sygnal po descramblingu
            sygnal = descrambledSygnal.signal
            for i in range(len(sygnal)):
                sygnal[i] = int(sygnal[i])
            
            plt.imsave('withScrambling.png', np.array(sygnal).reshape(int(math.sqrt(len(sygnal))), int(math.sqrt(len(sygnal))))) 
            image = Image.open("withScrambling.png").resize((250, 250))
            
            photo = ImageTk.PhotoImage(image)
            label3 = Label(image=photo, borderwidth=2)
            label3.image = photo
            label3.place(x = 580, y = 20)
                
        def compareScrambledToPure(pureSignal, descrambledSygnal):
            narzut = 0
            sygnal = descrambledSygnal.signal   #sygnal po scramblowaniu
            for i in range(len(sygnal)):
                sygnal[i] = int(sygnal[i])
            
            sygnal1 = []                        #oryginal
            for i in range(len(pureSignal)):
                sygnal1.append(pureSignal[i])
                
            for i in range(len(pureSignal)):
                if(sygnal1[i]==0 and sygnal[i]==1):     #sprawdzamy ile jedynek wstawiono zamiast zer
                    narzut+=1
                
            original = 0
            for i in range(len(pureSignal)):
                if(sygnal1[i]==1):     #sprawdzamy ile jedynek w oryginalu
                    original+=1
                
            return ((original+narzut)/original)*100 - 100  #procentowa wartosc narzutu
            
        #Odebranie wszystkich trzech sygnalow
        
        receive_puresignal(puresignal)
        receive_puresignaldisrupted(puresignaldisrupted)
        receive_descrambledSygnal(descrambledSygnal)
        
        disruptedBitsDiscrambled = comparePureToDescrambled(puresignal, descrambledSygnal)
        disruptedBits = comparePureToDisrupted(puresignal, puresignaldisrupted)
        percentage = disruptedBits * 100 / len(puresignal)
        scramblingPercentage = disruptedBitsDiscrambled * 100 / len(puresignal)
        
        narzut = compareScrambledToPure(puresignal,descrambledSygnal)

        label1 = tk.Label(text="Obraz poczatkowy",width = 20, font=('Times New Roman', 10))
        label1.place(x = 80, y = 290)
        
        label2 = tk.Label(text="Obrazek zaklocony bez scramblowania",width = 40, font=('Times New Roman', 10))
        label2.place(x = 290, y = 290)
        
        label3 = tk.Label(text="Obrazek scramblowany",width = 40, font=('Times New Roman', 10))
        label3.place(x = 570, y = 290)
        
        label4 = tk.Label(text="Dlugosc odebranego sygnalu: " + str(len(puresignal)) + " bitow", width = 40, font=('Times New Roman', 10))
        label4.place(x = 0, y = 350)     
        
        label5 = tk.Label(text="Ilosc znieksztalconych bitow: " + str(disruptedBits),width = 33, font=('Times New Roman', 10))
        label5.place(x = 0, y = 370)
        
        label6 = tk.Label(text="Wynosi to " + str(round(percentage,4)) + " % sygnalu",  width = 29, font=('Times New Roman', 10))
        label6.place(x = 0, y = 390)

        label7 = tk.Label(text="Metoda scramblingu: " + algorythm, width = 28, font=('Times New Roman', 10))
        label7.place(x = 0, y = 430)
        
        label8 = tk.Label(text="Ilosc znieksztalconych bitow: " + str(disruptedBitsDiscrambled), width = 33, font=('Times New Roman', 10)) 
        label8.place(x = 0, y = 450)

        label9 = tk.Label(text="Wynosi to " + str(round(scramblingPercentage,4)) + " % sygnalu",  width = 29, font=('Times New Roman', 10))
        label9.place(x = 0, y = 470)
        
        label10 = tk.Label(text="Jakosc obrazka poprawiona scramblingiem wynosi " + str(round(percentage - scramblingPercentage, 5)) + " %", width=100, font=('Times New Roman', 10))
        label10.place(x = 200, y = 400)
        
        label11 = tk.Label(text="Narzut scramblingiem wynosi: " + str(round(narzut, 5)) + " %", width=100, font=('Times New Roman', 10))
        label11.place(x = 200, y = 450)
        window.mainloop()
