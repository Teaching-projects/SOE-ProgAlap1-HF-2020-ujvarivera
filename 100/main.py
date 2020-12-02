"""
Ebben a perogramban a celunk egy futasok adatait rogzito fajlok statisztikainak kiiratasa.

Az alap adatszerkezetunke gy ilyen dictionary:

{"position":(x,y), "timestamp":ts, "elavation:e}

ahol:
 - x es y meterben megadott koordinatak egy alap viszonyitasi ponthoz kepest
 - ts egy egesz timestamp, ami masodpercben mondja meg, mennyi ido telt el ejfel ota
 - e pedig egy folytonos, meterben mert ertek a tengerszint feletti magassagrol


egy gpx track nem mas, mint ilyen adatpontoknak egy listaja.

A feladatban tobb, esetenkent egymasra epulo fuggvenyt kell megirni, melyek errol a trackrol arulnak el informaciokat.

"""

# Ez a fugggveny adja meg ket position kozotti legvonalbeli tavolsagot meterben. 
# p1 es p2 is (x,y) tuple-ok
def position_distance(p1,p2):
    x = p1[0] - p2[0] 
    y = p1[1] - p2[1]
    tav = (x**2 + y**2) ** 0.5
    return tav

# Ez a fuggveny egy gpx-et var, ami a fent leirt pontokbol allo lista.
# A fuggveny adja meg a track teljes hosszat, ami a pontok kozotti legvonalbeli tavolsagok osszege.
# Nem kell foglalkozni 3d tavolsaggal, csak a "felulnezeti tavolsaggal".
def total_distance(gpx):
    teljeshossz = 0
    for i in range(len(gpx)-1):
        teljeshossz += position_distance(gpx[i]["position"], gpx[i+1]["position"])
    return teljeshossz

# Ez adja meg maasodpercben, milyen hosszan futottunk
def total_time(gpx):
    osszido = 0
    for i in range(len(gpx)-1):
        osszido += gpx[i+1]["timestamp"] - gpx[i]["timestamp"]
    return osszido

# Ez a fuggveny adja meg masodpercben, hogy a futas soran hany masodpercig alldogaltunk csak futas helyett.
# Alldogalasnak szamit, ha ket meresi pont kozott nem valtozik a pozicio
def idle_time(gpx):
    alldogalasi_ido = 0
    for i in range(len(gpx)-1):
        if gpx[i]["position"] == gpx[i+1]["position"]:
            nemfutottunk = gpx[i+1]["timestamp"] - gpx[i]["timestamp"]
            alldogalasi_ido += nemfutottunk
    return alldogalasi_ido

# Ez a fuggveny adja vissza masodpercben, hogy mennyit mozogtunk
def moving_time(gpx):
    osszido = total_time(gpx)
    alldogalasi_ido = idle_time(gpx)
    mozgasi_ido = osszido - alldogalasi_ido
    return mozgasi_ido


# Ez a fuggveny adjon vissza egy stringet, amiben "szepen" benne van egy eltelt ido, amit masodpercben kapunk meg
# Szep alat mm:ss formatumot ertjuk, ha nem volt legalabb egy ora, es hh:mm:ss formatumot, ha igen.
# Mindket esetben a legelso tag (mm vagy hh) eseteben nem szukseges a 2 szeles kiiras 0-val paddingolva, a tobbi pozicion viszont igen.
# Jo peldak: 3:14, 12:23:05, 1:00:01
# Rossz peldak: 03:14, 12:23:5, 1:0:1
def pretty_time(seconds):
    ora = seconds // 3600   # pl. 3800 // 3600 = 1(.055555556)
    perc = (seconds // 60) - ora * 60  # 3800 seconds esetén 63,3333 - 1* 60 = 3(,3333)
    mp = seconds - (ora*3600 + perc*60)  # 3800 esetén 20

    if perc < 10:
        perc = "0"+str(perc)
    if mp < 10:
        mp = "0"+str(mp)

    if seconds < 3600: # 1 ora = 3600 mp
        prettytime =  "{}:{}".format(perc,mp)
    else: prettytime =  "{}:{}:{}".format(ora,perc,mp)

    return prettytime

# Ez a fuggveny szamolja ki, hogy mennyi volt az osszes emelkedes, azaz hany metert mentunk felfele
def total_ascent(gpx):
    osszemelkedes = 0

    for i in range(len(gpx)-1):
        if gpx[i+1]["elavation"] > gpx[i]["elavation"]:
            osszemelkedes += (gpx[i+1]["elavation"] - gpx[i]["elavation"])
        
    return osszemelkedes

# Ez a fuggveny keresse meg a gpx track elejen azt a legrovidebb reszt, ami mar atlepi a megadott tavolsagot, majd errol a reszrol adjon vissza egy masolatot.
# A fuggveny adjon vissza egy ures tracket, ha az egesz gpx track nincs olyan hosszu, mint a megadott tavolsag.
def chop_after_distance(gpx, distance):
    track = []
    ossztav = 0

    if total_distance(gpx) < distance:
        return track
    else:
        for i in range(len(gpx)-1):
            ossztav += position_distance(gpx[i]["position"], gpx[i+1]["position"])
            if ossztav > distance:
                track.append(gpx[i])
        return track


# Ez a fuggveny keresse meg a leggyorsabb, legalabb 1 km-es szakaszt a trackben, es adjon vissza rola egy masolatot
def fastest_1k(gpx):
    lista = chop_after_distance(gpx,1000)
    minimum = lista[1]["timestamp"]
    fastest = []
    for i in range(len(lista)):
        if lista[i]["timestamp"] < minimum:
            minimum = lista[i]["timestamp"]
    for j in range(len(lista)):
        if lista[j]["timestamp"] == minimum:
            fastest.append(lista[j])
    return fastest


# Az alabbi reszek betoltenek egy ilyen pickle fajlt, es kiirjak a statisztikakat megformazva
import pickle

infile=open(input(),"rb")
gpx=pickle.load(infile)
infile.close()

print("Run statistics:")
print(" - Total distance: {:.2f} km".format(total_distance(gpx)/1000))
print(" - Total time    : {}".format(pretty_time(total_time(gpx))))
print(" - Total time    : {}".format(pretty_time(moving_time(gpx))))
print(" - Total ascent  : {:.0f} m".format(total_ascent(gpx)))
print(" - Fastest 1k    : {}".format(pretty_time(total_time(fastest_1k(gpx)))))

