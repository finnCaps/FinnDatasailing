#Einlesen der Daten
import numpy as np

#nWD=100  #grobe(nearly) Windrichtung [deg]
#ta=90         #tacking angle/ Wendewinkel [deg]
#n=10

#print("test")

def dcourses(n,nWD,ta,da1out,r):
    #Auswählen der Werte für einen up an down
    v=0
    da2 = np.zeros((8,n))                    #0time 1Speed 2heading 3countercathode dlongitude 4adjacent leg dlatitude 5delta time  6: 1=Amwind pt 2=Amwind sbt 3=Halbwind(ablauftonne) 4=Vorwind 7:dZeit über ganze berechnung
    da2[0]=da1out[0]
    da2[1]=da1out[1]
    da2[2]=da1out[2]
    da2[3]=da1out[3]
    da2[4]=da1out[4]
    da2[5]=da1out[5]

    #Große heading änderungen werden nicht akzeptiert
    """
    mean = np.mean(da1out[2,:])
    std = np.std(da1out[2,:])


    grenze_unten = mean - 2 * std
    grenze_oben = mean + 2 * std

    

    filtered = da1out[(da1out >= grenze_unten) & (da1out <= grenze_oben)]

    da2[2, :] = np.pad(filtered, (0, n - len(filtered)), constant_values=np.nan)
    """
    #da2[2,0]=da1out[2,0]
    """
    v=1
    while v<n:
        if (da1out[2,v]-da1out[2,v-1])% 360 >20:
            da2[2,v]=da1out[2,v-1]    
        elif (da1out[2,v]+da1out[2,v-1])% 360 >20:
            da2[2,v]=da1out[2,v-1]    
        else:
            da2[2,v]=da1out[2,v]
        v=v+1

    
    """

    v=0
    while v<n:
        
        if nWD+(da1out[2,v]-nWD) % 360 <= nWD+(ta/2)+20:   #Amwind pt 
            da2[6,v]=1
        elif (nWD-(nWD-da1out[2,v]) % 360)  >= (nWD-((ta/2)+20)):     #Amwind sbt
            da2[6,v]=2
        elif (nWD-((ta/2)+21)) % 360>=da1out[2,v] and da1out[2,v] >=(nWD-129) % 360:      #Halbwind(ablauftonne)
            da2[6,v]=3
        elif (nWD+129) % 360 >=da1out[2,v] and da1out[2,v]  >=(nWD+((ta/2)+21)) % 360:
            da2[6,v]=3
        elif (nWD-130) % 360 >=da1out[2,v] and da1out[2,v]  >=(nWD+130) % 360:
            da2[6,v]=4    #Vorwind
        v=v+1
    
    
    toC=(da1out[0,n-1]-da1out[0,0])/60

    twde=np.zeros(n)   #true wind direction exact
    v=0
    while v<n:
        if da2[6,v]==1:
            twde[v]=(da2[2,v]-(ta/2))%360
        elif da2[6,v]==2:
            twde[v]=(da2[2,v]+(ta/2))%360
        v=v+1

    
    twd=np.zeros(n)   #true wind direction
    k=np.convolve(twde, np.ones(r)/r, mode='valid')
    twd=[0]*(r-1)+list(k)
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