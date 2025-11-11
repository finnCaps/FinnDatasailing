#run
from config import dconfig
from gpxcalculator2 import gpxdatareading
from gpxcalculator2 import gpxheadingspeed
from gpxcalculator_twd_vmg import dcourses
from gpxcalculator_twd_vmg import exactwinddirection
from rander import manuMap
from rander import plot
import os

def main():
    os.system("cls")
    s,n,gpx,nWD,ta=dconfig()        #s:startzeitounkt n:rechenschritte gpx:gpx datei nWD:ungefähreWindrichtung ta:tacking angle
    data1=gpxdatareading(s,n,gpx)
    mDa=gpxheadingspeed(s,n,data1)
    mDa=dcourses(n,nWD,ta,mDa) #Einteilen des heading für einen up an down
    twde=exactwinddirection(n,ta,mDa)   #true wind direction exact  
    
    plot(n,mDa,twde)
    print("branch: version_two")

if __name__=="__main__":
    main()
