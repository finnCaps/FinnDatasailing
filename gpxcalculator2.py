#daten einlesen
import gpxpy
import numpy as np
import math
import datetime
from config import dconfig
import pandas as pd
import time


def gpxdatareading(n,gpx):
    with open(gpx,"r",encoding="utf-8") as gpx_file:
        gpx=gpxpy.parse(gpx_file)

        
        data1=np.zeros((6, n)) #1:time 2: time (datetime) 3:latitude 4:longitude 5:heading 6:speed
        count=0

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if count >= n:
                    break


                data1[0,count]= point.time.timestamp()
                #data1[1,count]=point.time         
                data1[2,count]= point.latitude
                data1[3,count]= point.longitude
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

    for i in range(n-1):
        lat_rad[i]=math.radians(data1[1,i])
        cc[i]=abs((data1[3,i]-data1[3,i+1])*math.cos(lat_rad[i]))   #countercathode longitude
        al[i]=abs(data1[2,i]-data1[2,i+1])                          #adjacent leg latitude
        data1[4,i]=math.degrees(math.atan(cc[i]/al[i]))             #heading in [deg]
        dt[i]=abs(data1[0,i]-data1[0,i+1])                          #delta time
        data1[5,i]=math.sqrt(cc[i]**2+al[i]**2)*60*3600/dt[i]          #speed in[knt]   

            
#Daten Speichern im Array

    da1out=np.zeros((6, n))                    #0time 1Speed 2heading 3countercathode dlongitude 4adjacent leg dlatitude 5delta time 
    da1out[0]=data1[0]
    da1out[1]=data1[5]
    da1out[2]=data1[4]
    da1out[3]=cc
    da1out[4]=al
    da1out[5]=dt


#ausgabe
    return da1out

    print("lat",data1[2])
    print("time",data1[0])

    print("Time:",da1out[0])
    print("speed",da1out[1])
    print("heading",da1out[2])
    print("3countercathode",da1out[3])
    print("adjacent leg",da1out[4])
#print("delta time",da1out[5])


