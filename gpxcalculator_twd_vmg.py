#Einlesen der Daten
import numpy as np

#nWD=100  #grobe(nearly) Windrichtung [deg]
#ta=90         #tacking angle/ Wendewinkel [deg]


def dcourses(n,nWD,ta,da1out):
    #Auswählen der Werte für einen up an down
    v=0
    da2 = np.zeros((8,n))                    #0time 1Speed 2heading 3countercathode dlongitude 4adjacent leg dlatitude 5delta time  6: 1=Amwind pt 2=Amwind sbt 3=Halbwind(ablauftonne) 4=Vorwind 7:dZeit über ganze berechnung
    da2[0]=da1out[0]
    da2[1]=da1out[1]
    da2[2]=da1out[2]
    da2[3]=da1out[3]
    da2[4]=da1out[4]
    da2[5]=da1out[5]


    while v<n:
        
        if ((nWD+(ta/2)+30) % 360) >= da1out[2,v] and da1out[2,v]>=nWD:   #Amwind pt 
            da2[6,v]=1
        elif (nWD-((ta/2)+30)) %360 <= da1out[2,v] and da1out[2,v]<=nWD:     #Amwind sbt
            da2[6,v]=2
        elif (nWD-80) % 360>=da1out[2,v] and da1out[2,v] >=(nWD-110) % 360:      #Halbwind(ablauftonne)
            da2[6,v]=3
        elif (nWD-160) % 360 >=da1out[2,v] and da1out[2,v]  >=(nWD+160) % 360:
            da2[6,v]=4    #Vorwind
        v=v+1
    
    
    toC=(da1out[5,n]-da1out[5,0])/60


    #print("Kurs",da2[6])
        
    #return da2
    return da2, toC

    #Berechne von TWD

    #Berechnen von VMG

    #Ausgabe