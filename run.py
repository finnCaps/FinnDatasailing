#run
from config import dconfig
from gpxcalculator2 import gpxdatareading
from gpxcalculator2 import gpxheadingspeed
from gpxcalculator_twd_vmg import dcourses
from rander import manuMap
from rander import plot
import os

def main():
    os.system("cls")
    s,n,gpx,nWD,ta=dconfig()        #s:startzeitounkt n:rechenschritte gpx:gpx datei nWD:ungefähreWindrichtung ta:tacking angle
    data1=gpxdatareading(s,n,gpx)
    data1,da1out=gpxheadingspeed(s,n,data1)
    da2,toC,twd,twde=dcourses(n,nWD,ta,da1out) # out: toC
    #print("Kurs",da2[6])
    #print("Heading [deg]",da2[2])
    print("Time of Calculation[min]:",toC)
    #print("True Wind direction [deg]:",twd)
    #manuMap(data1, da2,n,twd)
    plot(da2,twd,twde,n)
    print("branch: version_two")

if __name__=="__main__":
    main()
