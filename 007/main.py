
egyenleg = 0
szamldij = 2000
kamat = 1.1  #ha az egyenleg negativ
megtakaritas = 1.05 # ha pozitiv
osszeg = 0

penzmozgas = int(input()) 
egyenleg += penzmozgas  #januarban nincs szamldij
osszeg += penzmozgas

if egyenleg > 0:
  egyenleg *= megtakaritas
else:
  egyenleg *= kamat
egyenleg = int(egyenleg)

i = 0

while i < 11:
    penzmozgas = int(input())
    osszeg += penzmozgas
    egyenleg -= szamldij
    egyenleg +=penzmozgas
    if egyenleg > 0:
        egyenleg *= megtakaritas  
    else:
        egyenleg *= kamat
    egyenleg = int(egyenleg)
    i += 1

print(egyenleg)
print(osszeg)