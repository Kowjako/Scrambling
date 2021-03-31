import math
import random

class Disruptor:
    def __init__(self,sig): #dodanie konstruktora
        self.distSig = sig  #sygnal zaklocony
    def disruption(self,dist): #zaklocenie sygnalu scramblowanego
        i = 0
        while i < len(self.distSig.signal) - 1:
            # Lista ktora bedzie zawierac losowo miejsca zaklocen sygnalu
            distIndexList = []
            prob = 0.039        #prawdopodobienstwo zaklocenia

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
                
                prob = prob + j * 0.000015  #zwiekszenie prawdpodobienstwa wystapienia zaklocenia
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
            i+=1
        return self.distSig


    def disruption2(self,dist): 
        distSig= self.distSig
        i = 0
        while i <len(distSig) -1:
            distIndexList = []
            prob = 0.039       #prawdopodobienstwo zak³ócenia
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
