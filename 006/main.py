"""
Kerj be egesz szamokat addig, amig 0-t nem kapsz.
A vegen irj ki minden bekert szamot, de mindgyiket csak egyszer, es abban a sorrendben, ahogy az elso elofordulas tortent.

pl:

Bemenet:
1
2
3
4
3
2
4
7
5
6
7
0
Kimenet:
1
2
3
4
7
5
6
"""

szam = int(input())
lista =[]

while szam !=0:
    if szam not in lista:
        lista.append(szam)
    szam=int(input())
# print(lista)

for i in range(len(lista)):
    print(lista[i])
