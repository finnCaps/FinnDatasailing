
import folium
from config import dconfig
from gpxcalculator2 import gpxdatareading
from gpxcalculator_twd_vmg import dcourses
import matplotlib.pyplot as plt
import numpy as np

def manuMap(data1, da2,n,twd):
    map = folium.Map(location=[data1[2,0], data1[3,0]], zoom_start=20)

    track_points=[data1[2,0:n-1],data1[3,0:n-1]]
    folium.PolyLine(track_points, color="blue", weight=5, opacity=0.8).add_to(map)
    map.save("track_map.html")


   #Plotten der Windrichtung
   
def plot(da2,twd,twde,n):
    
    xpoints = np.array(((da2[0,0:n])-da2[0,0])/60)
    xpoints3=np.array(((da2[0,0:n])-da2[0,1])/60)
    y1points = np.array(twd)        #true wind direction
    y2points=np.array((da2[6,0:n])*1)   #Kurs: pt=1,stbt=2,r=3,d=4
    y3points = np.array(twde)   #true wind direction exact
    y4points=np.array(da2[2,0:n])   #heading

    #plt.ion()
    plt.figure(2)
    fig, ax1 =plt.subplots()
    ax1.plot(xpoints,y1points, color='blue',label='true wind direction')
    ax1.set_xlabel("Zeit [min]")
    ax1.set_ylabel("degree",color='blue')

    ax1.plot(xpoints,y3points,color='purple',label='true wind direction exact') 
    ax1.plot(xpoints,y4points,color='green',label='heading')     
    plt.legend()

    ax2=ax1.twinx()
    ax2.plot(xpoints,y2points,color='red',label='Kurs:pt=1,stbt=2,r=3,d=4')
    ax2.set_ylabel("Kurs",color='red') 
    
   
    fig.tight_layout()

    plt.figtext(0.08,0.01,"1=port Tack, 2=starboard Tack, 3=reach, 4=downwind")
    plt.grid(True)
    plt.legend()
    plt.show() 
