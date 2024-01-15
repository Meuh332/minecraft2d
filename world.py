import blocklistfile

print("importation des module dans world")
from blocklistfile import blockattr, blocklist, blockattrlist
print("importation des module dans world terminé")
print("initialisation de la carte")
w = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],

]
xl=0
yl=0
blocklistfile.check_mod()
for i in w:
    for i2 in i:
        try:
            w[yl][xl] = blockattrlist[blocklist[w[yl][xl]]]
        except Exception as e:
            print(f"Erreur lors du chargement d'un bloc de la map : {e}")
            print(blocklist[len(blocklist) - 1])
            w[yl][xl] = blockattrlist["air"]
        if w[yl][xl] == 0:
            print("non")
        xl += 1
    yl += 1
    xl = 0
print("initialisation de la carte terminée")
def visible_blocks(camerax, cameray, screen_width, screen_height):
    # Calculez les indices de début et de fin en fonction de la position de la caméra
    world = w
    start_x = camerax // 44  # 44 est la taille d'un bloc
    start_y = cameray // 44
    end_x = start_x + (screen_width // 44) + 2  # +2 pour inclure un peu plus que ce qui est visible
    end_y = start_y + (screen_height // 44) + 2

    # Assurez-vous que les indices de fin ne dépassent pas les limites de la matrice "w"
    end_x = min(end_x, len(world[0]))
    end_y = min(end_y, len(world))

    # Créez la sous-matrice "visible_blocks"
    visible_blocks = []
    for row in range(start_y, end_y):
        visible_row = []
        for col in range(start_x, end_x):
            if 0 <= col < len(world[0]) and 0 <= row < len(world):
                visible_row.append(world[row][col])
        visible_blocks.append(visible_row)

    return visible_blocks

# 0 = air
# 1 = dirt
# 2 = grass_block
# 3 = stone
# 4 = coblestone
# 0 =
# 0 =
# 0 =
# 0 =
# 0 =