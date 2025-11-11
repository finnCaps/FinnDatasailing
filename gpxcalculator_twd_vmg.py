#Einlesen der Daten
import numpy as np

#nWD=100  #grobe(nearly) Windrichtung [deg]
#ta=90         #tacking angle/ Wendewinkel [deg]
#n=10

#print("test")

def dcourses(n,nWD,ta,mDa):   #  mDa:0time 1Speed 2heading 3countercathode dlongitude 4adjacent leg dlatitude 5delta time  6: 1=Amwind pt 2=Amwind sbt 3=Halbwind(ablauftonne) 4=Vorwind 7:dZeit über ganze berechnung
    #Einteilen des heading für einen up an down  

    v=0
    while v<n:
        
        if nWD+(mDa[2,v]-nWD) % 360 <= nWD+(ta/2)+20:   #Amwind pt 
            mDa[6,v]=1
        elif (nWD-(nWD-mDa[2,v]) % 360)  >= (nWD-((ta/2)+20)):     #Amwind sbt
            mDa[6,v]=2
        elif (nWD-((ta/2)+21)) % 360>=mDa[2,v] and mDa[2,v] >=(nWD-129) % 360:      #Halbwind(ablauftonne)
            mDa[6,v]=3
        elif (nWD+129) % 360 >=mDa[2,v] and mDa[2,v]  >=(nWD+((ta/2)+21)) % 360:
            mDa[6,v]=3
        elif (nWD-130) % 360 >=mDa[2,v] and mDa[2,v]  >=(nWD+130) % 360:
            mDa[6,v]=4    #Vorwind
        v=v+1
    return mDa
    
   
def exactwinddirection(n,ta,mDa):
    twde=np.zeros(n)   #true wind direction exact
    v=0
    while v<n:
        if mDa[6,v]==1:
            twde[v]=(mDa[2,v]-(ta/2))%360
        elif mDa[6,v]==2:
            twde[v]=(mDa[2,v]+(ta/2))%360
        v=v+1
    return twde     #true wind direction exact
    twd=1
    """
    twd=np.zeros(n)   #true wind direction
    k=np.convolve(twde, np.ones(r)/r, mode='valid')
    twd=[0]*(r-1)+list(k)
    """
    #v=0
    #twd=np.zeros(n-1)   #true wind direction
    #while v<n-5:
    #    twd[v+1]=(twde[v]+twde[v+1]+twde[v+2]+twde[v+3]+twde[v+4])/5
    #    v=v+1
    
    #print("Kurs",da2[6])
    
    #return da2
    return da2, toC,twd,twde

    #Berechne von TWD
    
    #Berechnen von VMG

    #Ausgabe