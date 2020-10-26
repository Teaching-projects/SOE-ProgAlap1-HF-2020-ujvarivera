szamla=[]
listaperc = []
listasms = []
honap = 0

while honap != 12:
    perc = int(input("Hány percet telefonáltunk?"))
    listaperc.append(perc)
    sms = int(input("Hány sms-t küldtünk?"))
    listasms.append(sms)
    honap += 1

havidij = int(input())
percdij = int(input())
smsdij = int(input())

total = 0
for i in range(len(listaperc)):
    havitel = listaperc[i] * percdij
    havisms= listasms[i] * smsdij
    if havitel + havisms < havidij:
        szamla.append(havidij)
        total += havidij
    else:
        szamla.append(havitel + havisms)
        total +=(havitel + havisms)

print(szamla)
print(total)


