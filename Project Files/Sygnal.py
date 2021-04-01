#Klasa reprezentujaca sygnal w postaci napieciowej oraz zero-jedynkowej
class Sygnal:
    def __init__(self,signal):      #konstruktor klasy Sygnal
        self.signal = list(signal)  #postac zero-jedynkowa
        self.voltage = ['Z']*len(signal) #na poczatku sygnal jest wypelniony zerami - reprezentacja napieciowa
        counter = 0
        for i in self.signal:
            if i == 1 and counter == 0: #poczatek sygnalu
                self.voltage[counter] = 'H'
            elif i == 1 and self.voltage[counter-1]=='H':
                self.voltage[counter] = 'L'
            elif i == 1:
                self.voltage[counter] = 'H'
            counter +=1
    