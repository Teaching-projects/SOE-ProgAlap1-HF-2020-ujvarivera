"""
Tovabbfejlesztjuk az elozo dolgot. 

Most megirunk egy "szepen kiirato" fuggvenyt, ami megkap egy map-et, es az alabbi formaban kiirja a kimenetre:

██████████████
█░░░░░░███████
█░░░░░░███░░░█
█░░███████░█░█
█░░█░░░░░█░█░█
█░░░░░░█░█░█░█
█████░░█░█░█░█
█░░░░░░█░░░█░░
██████████████


ha ez volt a bemenet:

terkep = [
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","░","░","░","█"],
    ["█","░","░","█","█","█","█","█","█","█","░","█","░","█"],
    ["█","░","░","█","░","░","░","░","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","█","░","█","░","█"],
    ["█","█","█","█","█","░","░","█","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","░","░","█","░","░"],
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"]
]

tehat pl egy initialize_map(10,6) altal adott terkepet ha kiiratunk, az igy nezzen ki:
██████████
█░░░░░░░░█
█░░░░░░░░█
█░░░░░░░░█
█░░░░░░░░█
██████████

"""

def initialize_map (width, height):
    # ide masold be a helyes megoldasodat mult hetrol
    lista = [width * ["█"]]

    for x in range(height-2):
        sor = []
        for y in range(width):
            sor.append("░")
        sor[0] = "█"
        sor[-1] = "█"
        lista.append(sor)
    lista.append(width*["█"])

    return lista

def pretty_map_print(map):
    # Ide ird meg az uj fuggvenyt, ami a fentiek szerint generalja a kimenetet
    """
    print("█"*width)
    if height !=2 and height != 3:
        for kulonsor in initialize_map(width,height-2):
            kulonsor = "█" + (width-2) * "░" + "█"
            print(kulonsor)
    if height == 3:
        kulonsor = "█" + (width-2) * "░" + "█"
        print(kulonsor)
    print("█"*width)
    """
    for a in range(len(map)):
        for b in range(len(map[a])):
            print(map[a][b],end="")
        print()

###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


width=int(input())
height=int(input())
pretty_map_print(initialize_map(width,height))
