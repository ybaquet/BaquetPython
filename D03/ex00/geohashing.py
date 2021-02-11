import antigravity
import sys

def geohashing(lat, long, datedow):
    antigravity.geohash(lat, long, datedow.encode('ascii'))

def usage():
    print("Usage is 'python3.8 geohashing.py {latitude} {longitude} {date (yyyy-mm-dd)} {indice Dow-Jones}")

if __name__ == '__main__':
    if 5 == len(sys.argv):
        try:
            latitude = float(sys.argv[1])
            longitude = float(sys.argv[2])
            date = sys.argv[3]
            dow = float(sys.argv[4])
            datedow = date + '-' + str(dow)
            geohashing(latitude, longitude, datedow)
        except ValueError:
            print("Type error")
            usage()
    else:
        usage()