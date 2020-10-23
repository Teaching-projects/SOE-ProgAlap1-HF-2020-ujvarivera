
egyenleg = 0
szamldij = 2000
kamat = 1.1  #ha az egyenleg negativ
megtakaritas = 1.05 # ha pozitiv
zaroegyenleg = 0

penzmozgas = int(input()) 
egyenleg += penzmozgas  #januarban nincs semmi levonas
if egyenleg > 0:
  egyenleg *= 1.05
else:
  egyenleg *= 1.1
egyenleg = int(egyenleg)
# print(egyenleg)

i = 0

while i < 2:
    penzmozgas = int(input())
    if penzmozgas > 0:
        egyenleg -= szamldij   #honap eleje
        egyenleg += penzmozgas
        egyenleg *= 1.05  #honap vege
        egyenleg = int(egyenleg)
        # print(egyenleg)
    else:
        egyenleg -= szamldij 
        egyenleg += penzmozgas
        egyenleg *= 1.1
        egyenleg = int(egyenleg)
        # print(egyenleg)

    i += 1

print(egyenleg)