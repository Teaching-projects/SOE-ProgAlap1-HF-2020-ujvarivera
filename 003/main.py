"""
Irj programot, mely beker egy egesz szamot: n. Feltetelezhetjuk, hogy ez pozitiv. 

Ezt kovetoen kerjen be egesz szamokat addig, amig n db nemnegativ szamot nem kapott. 
A program a futasa vegen irja ki egy listaban ezeket a szamokat.

Pelda bemenet:
3
1
2
3
Pelda kimenet:
[1, 2, 3]

Pelda bemenet:
3
-1
0
-44
35
-19
-35
1
Pelda kimenet:
[0, 35, 1]

"""

szam = int(input())
index = 0
lista=[]

while index != szam:
    szam2 = int(input())
    if szam2 < 0:
        index -=1
    if szam2 > 0:
        lista.append(szam2)
    index +=1
print(lista)
