from Disruptor import Disruptor
from Scrambler import Scrambler
import Receiver
from Descrambler import Descrambler
#Klasa przedstawiajaca kanal transmisyjny dla sygnalu scramblowanego/niescramblowanego
class Channel:
    def __init__(self, sygnal, algorythm):
        scrambler = Scrambler(sygnal)   #tworzenie scramblera na podstawie sygnalu
        
        disrupter = Disruptor(sygnal)   #tworzenie descramblera na podstawie sygnalu poczatkowego
        
        signal1 = disrupter.disruption2(sygnal, algorythm)  #zaklocenie sygnalu bez scramblowania
        
        signal2 = scrambler.scramble(algorythm)  #wykonanie scramblingu na sygnale zadanym algorytmem
        
        disrupter2 = Disruptor(signal2.getDescrambledSygnal()) #utworzenie disruptora na podstawie skramlowanego sygnalu
        
        signal3 = disrupter2.disruption(algorythm) #zaklocenie skramblowanego sygnlau
        
        descram = Descrambler(signal3,algorythm) #tworzenie descramblera na podstawie zakloconego skramblowanego sygnalu
        
        signal4 = descram.getDescrambledSygnal() #descramblowanie sygnalu
        
        tab1 = list(Receiver.signalhistogram(signal2).keys())
        tab2 = list(Receiver.signalhistogram(signal2).values())
        
        Receiver.receiver(sygnal, signal1, signal4, algorythm, signal2, signal3, tab1, tab2)