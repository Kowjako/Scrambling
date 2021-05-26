import math
import random
from numpy.matlib import rand

class Disruptor:
    def __init__(self,sig): #dodanie konstruktora
        self.distSig = sig  #sygnal zaklocony
    def disruption(self,dist): #zaklocenie sygnalu scramblowanego
        i = 0
        while i < len(self.distSig.signal) - 1:
            # Lista ktora bedzie zawierac losowo miejsca zaklocen sygnalu
            distIndexList = []
            prob = 0.045       #prawdopodobienstwo zaklocenia

            start = i       #pocz¹tek ci¹gu tych samych znaków
            while self.distSig.voltage[i] == self.distSig.voltage[i + 1] and self.distSig.voltage[i] == 'Z':
                i += 1
                if i >= len(self.distSig.signal) - 1:   #koniec sygnalu
                    break
            end = i         #koniec ci¹gu tych samych znaków`

            if (dist == "B8ZS"):
                x = 4       #jaki musi byc ciag aby wystapilo zaklocenie
            else:
                x = 3
            
            fragmentSize = end - start + 1  #d³ugoœæ ci¹gu tych samych znaków

            if fragmentSize >= x:  
                j = 0
                while j <= fragmentSize - x:  
                    j += 1
                
                prob = prob + j * 0.00001  #zwiekszenie prawdpodobienstwa wystapienia zaklocenia
                prob = math.ceil(prob * fragmentSize)
                j = 0
                while j < prob:
                    distIndexList.append(random.randint(start, end))    #generowanie mejsc zaklocenia sygnalu
                    j += 1
                
                for j in range(len(distIndexList)):
                
                    if self.distSig.signal[distIndexList[j]] == 1:
                        self.distSig.voltage[distIndexList[j]] = 'Z'
                    
                    elif self.distSig.signal[distIndexList[j]] == 0 and self.distSig.voltage[j - 1] == 'H':
                        self.distSig.voltage[distIndexList[j]] = 'L'
                    
                    else:
                        self.distSig.voltage[distIndexList[j]] = 'H'
                    
                    self.distSig.signal[distIndexList[j]] = (self.distSig.signal[distIndexList[j]] + 1) % 2
            start = 0
            end = 0
            i+=1
        return self.distSig


    def disruption2(self,dist): 
        distSig = []
        for i in self.distSig:
            distSig.append(i)
        i = 0
        while i <len(distSig) -1:
            distIndexList = []
            prob = 0.055       #prawdopodobienstwo zak³ócenia
            start=i
            while distSig[i] == distSig[i+1] and distSig[i]==0:
                i+=1
                if i>= len(distSig) -1:
                    break
            end =i

            if(dist == 'B8ZS'):
                x= 4
            else:
                x=3
            fragmentSize = end - start +1
            if fragmentSize>= x:
                j=0
                while j<= fragmentSize - x:
                    j+=1
                prob = prob + j*0.000015    #zwiekszenie prawdopodobienstwa w przypadku dlugiego ciagu
                prob = math.ceil(prob*fragmentSize)
                j=0
                while j<prob:
                    distIndexList.append(random.randint(start,end))
                    j+= 1
                for j in range(len(distIndexList)):
                    distSig[distIndexList[j]] = int(not distSig[distIndexList[j]])
            i+=1
        return distSig
    
    def bscDistruption(self):
        distSig = []
        for i in self.distSig:
            distSig.append(i);
        i = 0
        p = 0.001 #prawdopodobienstwo odebrania niepoprawnego bitu
        for i in range(len(distSig)):
            if(random.randint(0, 100)==p*100):
                distSig[i] = int(not(distSig[i]))
        return distSig
    
    def gilbertDistruption(self):
        distSig = []
        for i in self.distSig:
            distSig.append(i);
        i = 0
        state = 'D'   #D - stan z ma³ym prawdopodobienstwem, Z - stan z duzym prawdopobienstwem
        pSmall = 0.01 #stan z malym prawdopodobienstwem
        pHuge = 0.1 #stan z duzym prawdopodbienstwem
        for i in range(len(distSig)):
            if(state == 'D'):
                if(random.randint(0,100) >= 100-pHuge*100):       #stan z malym p
                    distSig[i] = int(not(distSig[i]))
                if(random.randint(0,100) >= 100-pHuge*100):
                    state = 'Z'
            if(state == 'Z'):
                if(random.randint(0,100) >= 100-pSmall*100):       #stan z duzym p
                    distSig[i] = int(not(distSig[i]))
                if(random.randint(0,100) >= 100-pSmall*100):
                    state = 'D'
        return distSig
        
        
