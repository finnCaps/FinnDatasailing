#run
from gpxcalculator2 import gpxdatareading
from gpxcalculator_twd_vmg import dcourses
from config import dconfig
from rander import manuMap
from rander import plot
import os

def main():
    os.system("cls")
    n,nWD,ta,gpx,s=dconfig()
    da1out,data1=gpxdatareading(n,gpx,s)
    da2,toC,twd,twde=dcourses(n,nWD,ta,da1out) # out: toC
    #print("Kurs",da2[6])
    #print("Heading [deg]",da2[2])
    print("Time of Calculation[min]:",toC)
    #print("True Wind direction [deg]:",twd)
    #manuMap(data1, da2,n,twd)
    plot(da2,twd,twde,n)

if __name__=="__main__":
    main()
