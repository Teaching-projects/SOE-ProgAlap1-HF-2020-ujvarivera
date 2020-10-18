"""
Kerj be ket egesz szamot (feltetelezhetjuk, hogy pozitivak), es ird ki a 
legnagyobb kozos osztojukat, majd a legkisebb kozos tobbszorosuket.

pl:
Bemenet:
6
27
Kimenet:
3
54
"""

szam1 = int(input()) 
szam2 = int(input()) 
nagyobb = szam1 
kisebb = szam2 

if szam1 < szam2: 
    nagyobb = szam2 
    kisebb = szam1 

# legnagyobb közös osztó 

lnko = kisebb
while True:
    if szam1 % lnko ==0 and szam2 % lnko ==0:
        print(lnko)
        break
    lnko -= 1


#legkisebb közös többszörös

tobbszoros = 0
while True:
    tobbszoros += 1
    lkkt = nagyobb*tobbszoros 
    if lkkt % kisebb == 0:
        print(lkkt) 
        break
   



