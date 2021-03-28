#V - takie same jak poprzedni niezerowy impuls
#B - oznacza napiecie przeciwne do poprzedzajacego niezerowego

class Scrambler:
    def __init__(self, sygnal):
        self.scrambledSignal = sygnal
    def scramble(self, algorithm):
        if algorithm == "HDB3":
            print("SCRAMBLING WITH HDB3")
            i = 0 # aktualna pozycja w sygnale
            j = 0 # ilosc jedynek w poprzednim ciagu
            while i < len(self.scrambledSignal.signal) - 3: #bo ostanio bedzie sprawdzana ciag o dlugosci cztery wiec odejmujemy 3
                if self.scrambledSignal.signal[i] == 1:
                    j += 1
                if self.zeroCount(i,4): #sprawdzanie czy wystepuje ciag 4 zer
                    if j % 2 == 0: #parzysta liczba jedynek poprzedzajacych
                        self.scrambledSignal.voltage[i] = 'B'
                        self.scrambledSignal.voltage[i+3] = 'V'
                        j = 0 #wyzerowanie jedynek
                        i += 3 #przejscie do kolejnych 4 pozycji
                    elif j % 2 == 1: #nieparzysta liczba jedynek poprzedzajacych
                        self.scrambledSignal.voltage[i+3] = 'V'
                        j = 0
                        i += 3
                i += 1        
        elif algorithm == "B8ZS": #North American T1
            print("SCRAMBLING WITH B8ZS")
            i = 0
            while i < len(self.scrambledSignal.signal) - 7: #bo bedzie sprawdzany ciag o dlugosci 8 wiec odejmujemy 3 
                if self.zeroCount(i, 8):
                    self.scrambledSignal.voltage[i+3]='V'
                    self.scrambledSignal.voltage[i+4]='B'
                    self.scrambledSignal.voltage[i+6]='B'
                    self.scrambledSignal.voltage[i+7]='V'
                    i += 7 #przejscie do nastpenych 8 symboli
                i+=1
    
    def getScrambledSignal(self):
        return self.scrambledSignal.voltage
                
    def zeroCount(self, startPos, countToCheck):
        for k in self.scrambledSignal.signal[startPos:startPos + countToCheck]: #sprawdzamy czy sa w ciagu okreslonej dlugosci jedynki
            if k == 1:
                return False    #znaczy w ciagu jest 1 i nie potrzebne kodowanie
        return True