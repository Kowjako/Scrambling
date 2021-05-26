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
        window.geometry("860x320")

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

        def receive_puresignaldisrupted(disruptedSignal):  # wyplenienie miejsca na signal zaklocony niescramblowany
            for i in range(len(disruptedSignal)):
                disruptedSignal[i] = int(disruptedSignal[i])
                
        def receive_descrambledSygnal(descrambledSygnal):  # wypelnienie miejsca na sygnal po descramblingu
            sygnal = descrambledSygnal.signal
            for i in range(len(sygnal)):
                sygnal[i] = int(sygnal[i])
                
        #Odebranie wszystkich trzech sygnalow
        receive_puresignal(puresignal)
        receive_puresignaldisrupted(puresignaldisrupted)
        receive_descrambledSygnal(descrambledSygnal)
        
        disruptedBitsDiscrambled = comparePureToDescrambled(puresignal, descrambledSygnal)
        disruptedBits = comparePureToDisrupted(puresignal, puresignaldisrupted)
        percentage = disruptedBits * 100 / len(puresignal)
        scramblingPercentage = disruptedBitsDiscrambled * 100 / len(puresignal)

        label4 = tk.Label(text="Dlugosc odebranego sygnalu: " + str(len(puresignal)) + " bitow", width = 40, font=('Times New Roman', 10))
        label4.place(x = 0, y = 50)     
        
        label5 = tk.Label(text="Ilosc znieksztalconych bitow: " + str(disruptedBits),width = 33, font=('Times New Roman', 10))
        label5.place(x = 0, y = 70)
        
        label6 = tk.Label(text="Wynosi to " + str(round(percentage,4)) + " % sygnalu",  width = 29, font=('Times New Roman', 10))
        label6.place(x = 0, y = 90)

        label7 = tk.Label(text="Metoda scramblingu: " + algorythm, width = 28, font=('Times New Roman', 10))
        label7.place(x = 0, y = 130)
        
        label8 = tk.Label(text="Ilosc znieksztalconych bitow: " + str(disruptedBitsDiscrambled), width = 33, font=('Times New Roman', 10)) 
        label8.place(x = 0, y = 150)

        label9 = tk.Label(text="Wynosi to " + str(round(scramblingPercentage,4)) + " % sygnalu",  width = 29, font=('Times New Roman', 10))
        label9.place(x = 0, y = 170)
        
        label10 = tk.Label(text="Jakosc obrazka poprawiona scramblingiem wynosi " + str(round(percentage - scramblingPercentage, 5)) + " %", width=100, font=('Times New Roman', 10))
        label10.place(x = 200, y = 100)

        window.mainloop()
