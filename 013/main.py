"""
Tovabbfejlesztjuk az elozo dolgot. 

Most atirjuk a kiirato fuggvenyt ugy, hogy kap egy dictionary-t is, amiben benne van a jatekos karakterunk a kovetkezo modon:

character = {
    "name" : "Dark Wanderer",
    "position" : {
        "x" : 4 ,
        "y" : 2 
    }
}


Az eredmenye a kiiratasnak a korabbi peldaterkepen igy nezne ki:

████████████████████████████
██░░░░░░░░░░░░██████████████
██░░░░░░🧙‍░░░░██████░░░░░░██
██░░░░██████████████░░██░░██
██░░░░██░░░░░░░░░░██░░██░░██
██░░░░░░░░░░░░██░░██░░██░░██
██████████░░░░██░░██░░██░░██
██░░░░░░░░░░░░██░░░░░░██░░░░
████████████████████████████

Ket dolog valtozott meg:
 - Az eddigi █ es ░ karaktereket mindig duplan rajzoljuk ki, hogy korulbelul negyzet alaku legyen egy mezo.
 - A karakterunk helyere 🧙‍-t irunk ki.



"""

def initialize_map (width, height):
    # ide masold be a helyes megoldasodat a multkorirol
    lista = [width * ["██"]]

    for x in range(height-2):
        sor = []
        for y in range(width):
            sor.append("░░")
        sor[0] = "██"
        sor[-1] = "██"
        lista.append(sor)
    lista.append(width*["██"])

    return lista

def pretty_map_print(map, character):
    # Ide masold be a multkorit, a fenti modositasokkal. 
    # Ha a karakter pozicioja a palyan kivul lenne, egyszeruen ne jelenjen meg
    x = character["position"]["x"]
    y = character["position"]["y"]
    width = len(map[1])
    height = len(map)

    if (x <= width - 1 and x >= 0) and (y <= height - 1 and y >= 0): 
        map[y][x] = "🧙"

    for a in range(len(map)):
        for b in range(len(map[a])):
            print(map[a][b],end="")
        print()

###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


def initialize_character():
    x=int(input())
    y=int(input())
    return {"name": "Placeholder name", "position" : {"x":x,"y":y} }

width=int(input())
height=int(input())
map=initialize_map(width,height)

character=initialize_character()

pretty_map_print(map,character)
