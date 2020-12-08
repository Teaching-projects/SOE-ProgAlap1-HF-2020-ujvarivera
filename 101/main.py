from typing import Dict, List

Tippek=List[str]
"""Leadott tippek, azaz betűk listájának típusa."""

def kozte_van(betu:str, betuk:Tippek) -> bool:
    """Megadja, hogy a listában már benne van-e a megadott betű, vagy sem.

    Args:
        betu (str): a keresett betű
        betuk (Tippek): betűk listája

    Returns:
        bool: `True` ha benne van, `False` ha nincsen.
    """
    if betu in betuk:
        return True
    else: return False

"""
betuk = ["a","b","c", "M"]
print(kozte_van("d",betuk)) # False
print(kozte_van("a",betuk)) # True
print(kozte_van("b",betuk)) # True
print(kozte_van("m",betuk)) # False
mukodik
"""

specialis_karakterek=[' ','.',',','!','?',':','-']

def megjelenites(szo:str, betuk:Tippek) -> str:
    """Visszaad egy olyan szót, amiben a `betuk`-ben lévő betűk látszanak, minden más helyére `_` kerül, kivéve néhány speciális karaktert, amik megjelennek változtatás nélkül. Ezen karakterek listája a `specialis_karakterek` globális listában adott.

    Kis és nagy betűket megkülönbözteti a függvény.

    Args:
        szo (str): a szó, aminek megjelenített változatát meg szeretnénk kapni. 
        betuk (Tippek): Egy karakterből, betűkből álló lista, amit már tippeltünk

    Returns:
        str: a megjelenített változata a szónak
    """
    string = ""
    for betu in szo:
        if kozte_van(betu,betuk+specialis_karakterek):
            string += betu
        else: string += "_"
    return string

"""
betuk = ["a","b","c", "M"]
szo = "Hal"
print(megjelenites(szo,betuk))  # _a_
szo = "Maci"
print(megjelenites(szo,betuk)) #Maci
szo = "maci"
print(megjelenites(szo,betuk)) #_aci
szo = "I'll be back!"
betuk = ["I", "l", "a", "k"]
print(megjelenites(szo,betuk)) # I_ll __ _a_k!

mukodik
"""

def megfejtett(szo:str, betuk:Tippek) -> bool:
    """Megadja, hogy sikerült-e már megfejtenünk a szót, azaz minden benne levő betű már a tippjeink között van.

    Args:
        szo (str): a kitalálandó szó
        betuk (Tippek): az eddig tippelt betűk

    Returns:
        bool: `True` ha teljesen megfejtettük a szót, `False` különben
    """
    osszeg = 0
    for betu in szo:
        if betu in betuk or betu in specialis_karakterek:
            osszeg += 1
    if osszeg == len(szo):
        return True
    else: return False

"""
szo= "ab"
betuk = ["a", "c"]
print(megfejtett(szo,betuk)) # False
betuk = ["a", "b"]
print(megfejtett(szo,betuk)) # True
betuk = ["b", "a"]
print(megfejtett(szo,betuk)) # True
szo= "alma!"
betuk = ["a", "l","m","a"]
print(megfejtett(szo,betuk)) # True
mukodik
"""

def tartalmazza(szo:str, betu:str) -> bool:
    """Megadja, hogy a megaadott betű szerepel-e a megadott szóban.

    Args:
        szo (str): a szó
        betu (str): a betű, amit keresünk, feltételezhető, hogy 1 karakter hosszú

    Returns:
        bool: `True` ha szerepel, `False` ha nem    
    """
    if betu in szo:
        return True
    else: 
        return False

"""
print(tartalmazza("alma","a")) #True
print(tartalmazza("alma","b")) #False
print(tartalmazza("alma","A")) #False

mukodik

"""

def rossz_tippek(szo:str, betuk:Tippek) -> int:
    """Megadja, hogy hány rossz betűt tippeltünk eddig.

    Args:
        szo (str): a kitalálandó szó
        betuk (Tippek): az eddigi betű tippjeink

    Returns:
        int: a rossz tippek száma
    """
    rossz = 0
    for i in betuk:
        if i not in szo:
            rossz += 1
    return rossz
"""
betuk = ["a","b","c","d"]
szo = "abgh"
print(rossz_tippek(szo,betuk)) #2

betuk = ["a","b","c"]
szo = "abg"
print(rossz_tippek(szo,betuk)) #1

mukodik
"""

def eletek(osszes:int,elhasznalt:int)->str:
    """Visszaad egy olyan szöveget, ami egy indikátor arra, hány életünk van még.

    A szöveg elején van annyi 😄 ahány életünk még maradt, majd annyi 💀 ahányat már "eljátszottunk".

    Args:
        osszes (int): az összes életünk száma
        elhasznalt (int): az eljátszott életek (rossz betű tippek) száma

    Returns:
        str: 😄😄😄💀💀 formátumú indikátor (a példa adatai: 5 összes, 2 elhasznált)
    """
    eletek = (osszes - elhasznalt) * "😄"
    elhasznaltelet = elhasznalt * "💀"
    maradek = eletek + elhasznaltelet
    return maradek
"""
print(eletek(4,1)) #😄😄😄💀
print(eletek(4,2)) #😄😄💀💀
print(eletek(4,3)) #😄💀💀💀
mukodik
"""

def akasztofa(szo:str,osszes_elet:int) -> None:
    """Végigvisz egy akasztófa játékot, ahol a megadott szót kell kitalálni, és `osszes_elet` rossz tipp után vesztettünk.

    A játék minden körben először írja ki, hogy mit látunk a megfejtendő szóból, alá egy indikátort arról, hogy hány életünk van még, majd végül a tippelt karakterek listáját a tippek sorrendjében.

    Ezt követően az "Adja meg a kovetkezo betut: " kiírással kérjünk be egy betűt. Ellenőrzés nem szükséges se arra, hogy egyetlen betűt adtunk-e meg, se arra, hogy volt-e már korábban ez a betű. A megadott betűt irassuk is rögtön ki. (Szimplán, egymagában. Ennek pusztán annyi célja van, hogy nyomon követhetőbbek legyenek az out fájlok.)

    Más kiiratás nem történik, a játék logikája egyértelmű: addig adunk le tippeket betűkre, amíg vagy meg nem fejtődik a szó, vagy el nem fogynak az életeink. Többször leadhatjuk ugyanazt a tippet, de ez rossz, akkor több életet is vesz el. A kiíratott listában is jelenjen meg duplán akkor ez a betű.

    Ha nyertünk, még kerüljön kiírásra a megfejtett szó, valamint alá egy olyan szöveg, hogy "Gratulalok, nyertel, es meg X eleted maradt!", ahol X értelemszerűen a megmaradt életek száma.

    Ha vesztettünk, akkor egy "Sajnalom, nem nyertel, ez lett volna a megoldas: MEGOLDAS".

    Példakimenetek adottak.
    

    Args:
        szo (str): a megfejtendő szó
        osszes_elet (int): az életeink száma, azaz hány rossz tipp után vesztettünk
    """
    
    tippek = []
    elhasznalt = 0

    while True:
        print(megjelenites(szo,tippek))
        print(eletek(osszes_elet,elhasznalt))
        print(tippek)
        betu = input("Adja meg a kovetkezo betut: ")
        tippek.append(betu)
        if not tartalmazza(szo,betu):
            elhasznalt += 1
        if megfejtett(szo,tippek):
            print("Gratulalok, nyertel, es meg {} eleted maradt!".format(osszes_elet-elhasznalt))
            break
        if osszes_elet == elhasznalt:
            print("Sajnalom, nem nyertel, ez lett volna a megoldas: ", szo)
            break
    



# Ez alatt ne tessek modositani.

szo=input()
maxelet=int(input())
akasztofa(szo,maxelet)





