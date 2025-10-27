#daten einlesen
import gpxpy
import numpy as np
import math
import datetime
from config import dconfig
import matplotlib.pyplot as plt



def gpxdatareading(n,gpx,s):
    with open(gpx,"r",encoding="utf-8") as gpx_file:
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



#berechnen: heading, speed

    
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
        data1[5,i]=math.sqrt(cc[i]**2+al[i]**2)*60*3600/dt[i]          #speed in[knt]   
    
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
    
            
#Daten Speichern im Array

    da1out=np.zeros((6, n))                    #0time 1Speed 2heading 3countercathode dlongitude 4adjacent leg dlatitude 5delta time 
    da1out[0]=data1[0]
    da1out[1]=data1[5]
    da1out[2]=data1[4]
    da1out[3]=cc
    da1out[4]=al
    da1out[5]=dt



#ausgabe
    return da1out, data1

    print("lat",data1[2])
    print("time",data1[0])

    print("Time:",da1out[0])
    print("speed",da1out[1])
    print("heading",da1out[2])
    print("3countercathode",da1out[3])
    print("adjacent leg",da1out[4])
#print("delta time",da1out[5])


