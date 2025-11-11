import gpxpy
import numpy as np
import math
import datetime
from config import dconfig
import matplotlib.pyplot as plt



def gpxdatareading(s,n,gpx):
    with open(gpx,"r",encoding="utf-8") as gpx_file:                #einlesen der gpx datei s:Startzeitpunkt n:rechenschritte gpx:GPXDaten   with open(gpx,"r",encoding="utf-8") as gpx_file:
        gpx=gpxpy.parse(gpx_file)

        
        data1=np.zeros((6, n)) #0:time (1: time (datetime)) 2:latitude 3:longitude 4:heading 5:speed
        count=0

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points[s:]:
                if count >= n:
                    break


                data1[0,(count)]= point.time.timestamp()
                #data1[1,count]=point.time         
                data1[2,(count)]= point.latitude
                data1[3,(count)]= point.longitude
                count+=1

            if count >= n:
                break
        if count >= n:
            break
    return data1


def gpxheadingspeed(s,n,data1):#berechnen: heading, speed

    
    cc=np.zeros(n)
    al=np.zeros(n)
    dt=np.zeros(n)
    lat_rad=np.zeros(n)

    for i in range(n-2):
        lat_rad[i]=math.radians(data1[1,i])
        cc[i]=((data1[3,i+1]-data1[3,i])*math.cos(lat_rad[i]))   #countercathode longitude
        al[i]=(data1[2,i+1]-data1[2,i])                          #adjacent leg latitude
        
        if al[i]==0 and cc[i]<=0:
            data1[4,i]=270
        elif al[i]==0 and cc[i]>=0:
            data1[4,i]=90
        else:
            if cc[i]>=0 and al[i]>=0:                                 #heading in [deg]
                data1[4,i]=(math.degrees(math.atan(cc[i]/al[i]))) % 360   #0-90deg         
            elif cc[i]>=0 and al[i]<=0:                             #90-180deg
                data1[4,i]=180+(math.degrees(math.atan(cc[i]/al[i])))
            elif cc[i]<=0 and al[i]<=0:                                 #180-270deg
                data1[4,i]=180+(math.degrees(math.atan(cc[i]/al[i])))
            elif cc[i]<=0 and al[i]>=0:
                data1[4,i]=360+(math.degrees(math.atan(cc[i]/al[i])))   #270-360deg
        
        dt[i]=abs(data1[0,i+1]-data1[0,i])                          #delta time
        data1[5,i]=math.sqrt(cc[i]**2+al[i]**2)*60*3600/dt[i]
    
   
    
    mDa=np.zeros((8, n))  #0time 1Speed 2heading 3countercathode dlongitude 4adjacent leg dlatitude 5delta time  6: 1=Amwind pt 2=Amwind sbt 3=Halbwind(ablauftonne) 4=Vorwind 7:dZeit über ganze berechnung        
    mDa[0]=data1[0]
    mDa[1]=data1[5]
    mDa[2]=data1[4]
    mDa[3]=cc
    mDa[4]=al
    mDa[5]=dt
    
    toC=(mDa[0,n-1]-mDa[0,0])/60            #time of calculation in minutes
    print("Time of Calculation[min]:",toC)


    return mDa

    #Auswerten von cc und al (Gegen kathete und ankathete)
    xpoints = np.array(((data1[0,0:n])-data1[0,0])/60)
    y1points = np.array(cc)
    y2points=np.array(al)

    
    plt.figure(1)
    fig, ax1 =plt.subplots()
    ax1.plot(xpoints,y1points, color='blue',label='cc')
    ax1.set_xlabel("Zeit [min]")
    ax1.set_ylabel("degree",color='blue')

    ax1.plot(xpoints,y2points,color='purple',label='al')  
    plt.grid(True) 
    plt.legend()
    
    

    




