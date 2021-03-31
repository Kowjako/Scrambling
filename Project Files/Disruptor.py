class Disruptor:
    def disruption(sig, dist): 
        distSig = sig
        i = 0
        while i < len(distSig.signal) - 1:
            # Lista ktora bedzie zawierac losowo miejsca zaklocen sygnalu
            distIndexList = []
            prob = 0.039        #z czego to jest? idk

            start = i       #początek ciągu tych samych znaków
            while distSignal.voltage[i] == distSignal.voltage[i + 1] and distSignal.voltage[i] == 'Z':
                i += 1
                if i >= len(distSignal.signal) - 1:
                    break
            end = i         #koniec ciągu tych samych znaków`

            if (dist == "B8ZS"):
                x = 4
            else:
                x = 3
            
            fragmentSize = end - start + 1  #długość ciągu tych samych znaków

            if fragmentSize >= x:  
                j = 0
                while j <= fragmentSize - x:  
                    j += 1
                
                prob = prob + j * 0.000012  #co to za stałe prob
                prob = math.ceil(prob * fragmentSize)
                j = 0
                while j < prob:
                    distIndexList.append(random.randint(start, end))
                    j += 1
                
                for j in range(len(distIndexList)):
                
                    if distSig.signal[distIndexList[j]] == 1:
                        distSig.voltage[distIndexList[j]] = 'Z'
                    
                    elif distSig.signal == 0 and distSig.voltage[j - 1] == 'H':
                        distSig.voltage[distIndexList[j]] = 'L'
                    
                    else:
                        distSig.voltage[distIndexList[j]] = 'H'
                    
                    distSig.signal[distIndexList[j]] = (distSig.signal[distIndexList[j]] + 1) % 2
            i+=1    #if problems occur delete that -
        return distSig


    def disruption2(sig, dist): 

        distSig=sig
        for x in signal:
            distSig.append(x)

        while i <len(distSig) -1:
            distIndexList = []
            prob = 0.039       #prawdopodobienstwo zakłócenia
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
                prob=prob+j*0.000013 #some weird probability?
                prob = math.ceil(prob*fragmentSize)
                j=0
                while j<prob:
                    distIndexList.append(random.randint(start,end))
                    j+= 1
                for j in range(len(distIndexList)):
                    distSig[distIndexList[j]] = int(not distSig[distIndexList[j]])
            i+=1
        return distSig
