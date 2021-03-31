from Disruptor import Disruptor
from Scrambler import Scrambler

#Klasa przedstawiajaca kanal transmisyjny dla sygnalu scramblowanego/niescramblowanego
class Channel:
    def __init__(self, sygnal, algorythm):
        scrambler = Scrambler(sygnal)   #tworzenie scramblera na podstawie sygnalu
        disrupter = Disruptor(sygnal)   #tworzenie descramblera na podstawie sygnalu
        signal1 = disrupter.disruption(sygnal, algorythm)  #sygnal zaklocony bez scramblowania
        signal2 = scrambler.scramble(algorythm)  #wykonanie scramblingu na sygnale
        disrupter2 = Disruptor(signal2.getDescrambledSygnal()) #utworzenie disruptora na podstawie skramlowanego sygnalu
        signal3 = disrupter2.disruption(algorythm) #zaklocenie skramblowanego sygnlau