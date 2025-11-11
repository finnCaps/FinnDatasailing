#Konfigurations file
def dconfig():
    s=int(input("Startzeitpunkt ="))
    n=int(input("Anzahl der Rechenschritte = "))
    nWD=int(input("Grobe Windrichtung [deg] = "))
    ta=100  
    gpx="Data/2025-08-29_track.gpx"
    #2025-08-29_track.gpx 2025-06-01 h-boatworlds_p.gpx
    return n, nWD,ta,gpx,s