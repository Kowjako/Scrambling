from Disruptor import Disruptor
from Scrambler import Scrambler
import Receiver
from Descrambler import Descrambler

#Klasa przedstawiajaca kanal transmisyjny dla sygnalu scramblowanego/niescramblowanego
class Channel:
    def __init__(self, sygnal, algorythm):
        disrupter = Disruptor(sygnal)   #tworzenie zaklocenia na podstawie sygnalu poczatkowego
        scrambler = Scrambler(sygnal)   #tworzenie scramblera na podstawie sygnalu
        
        signal1 = disrupter.disruption2(algorythm)  #zaklocenie sygnalu bez scramblowania
        
        signal2 = scrambler.scramble(algorythm)  #wykonanie scramblingu na sygnale zadanym algorytmem
        
        disrupter2 = Disruptor(signal2) #utworzenie disruptora na podstawie skramlowanego sygnalu
        
        signal3 = disrupter2.disruption(algorythm) #zaklocenie skramblowanego sygnlau
        
        descr = Descrambler(signal3) #tworzenie descramblera na podstawie zakloconego skramblowanego sygnalu
        signal4 = descr.descramble(algorythm)
            
        Receiver.receiver(sygnal, signal1, signal4, algorythm, signal2, signal3) #wysylka wszystich sygnalow