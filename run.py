#run
from gpxcalculator2 import gpxdatareading
from gpxcalculator_twd_vmg import dcourses
from config import dconfig
def main():
    
    n,nWD,ta,gpx=dconfig()
    da1out=gpxdatareading(n,gpx)
    da2,toC=dcourses(n,nWD,ta,da1out)
    print("Kurs",da2[6])
    print ("Time of Calculation[sec]:",toC)

if __name__=="__main__":
    main()
