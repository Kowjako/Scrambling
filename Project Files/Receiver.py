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
        window.geometry("860x520")

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