#Algorytm powraca zamienione zera
class Descrambler:
    def __init__(self, sygnal, algorithm):
        self.descrambledsygnal = sygnal
        if algorithm == "HDB3":
            print("DESCRAMBLING WITH HDB3")
            i = 0 # aktualna pozycja w sygnale
            j = 0 # ilosc jedynek w poprzednim ciagu
            while i < len(self.descrambledsygnal.signal) - 3:  #ze wzgledu ze maska wyglada B00V lub 000V wiec ostatnie sprawdzenie bedzie na dlugosci -3
                if self.descrambledsygnal.signal[i] == 1:
                    j += 1
                if j % 2 == 0 and self.descrambledsygnal.voltage[i] == 'B': #maska byla B00V wiec wracamy zera na pozycjach B oraz V = i, i+3
                    self.descrambledsygnal.voltage[i] = 'Z'
                    self.descrambledsygnal.voltage[i+3] = 'Z'
                    j = 0
                elif j % 2 == 1 and self.descrambledsygnal.voltage[i] == 'V': #maska byla 000V bo jedynek nieparzysta liczba wiec wracamy zero na pozycji i
                    self.descrambledsygnal.voltage[i] = 'Z'
                    j = 0
                i += 1
        elif algorithm == "B8ZS":
            print("DESCRAMBLING WITH B8ZS")
            i = 0
            while i < len(self.descrambledsygnal.signal) - 4:  #ze wzgledu ze maska wyglada 000VB0VB wiec ostatnie sprawdzenie bedzie na dlugosci -4
                if self.descrambledsygnal.voltage[i] == 'V':
                    self.descrambledsygnal.voltage[i] = 'Z'
                    self.descrambledsygnal.voltage[i + 1] = 'Z'
                    self.descrambledsygnal.voltage[i + 3] = 'Z'
                    self.descrambledsygnal.voltage[i + 4] = 'Z'
                i += 1
                
    def toZeroOneRepresentation(self):
        i = 0
        while i < len(self.descrambledsygnal.signal):
            if self.descrambledsygnal.voltage[i] == 'H' or self.descrambledsygnal.voltage[i] == 'L':
                self.descrambledsygnal.signal[i] = 1
            else:
                self.descrambledsygnal.signal[i] = 0
            i += 1
            
    def getDescrambledSygnal(self):
        return self.descrambledsygnal