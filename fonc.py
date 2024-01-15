from world import w


def toutchp(x, y):
    x = int(x / 44) * 44
    y = int(y / 44) * 44

    # Convertir les coordonnées en indices de la matrice
    x = x // 44
    y = y // 44

    # Vérifier si la case dans la matrice est différente de zéro (si c'est un bloc)
    if x > -1 and y > -1:
        try:
            return w[y][x]
        except IndexError:
            return 0
    else:
        return 0


def t(t, keys):
    for u in keys:
        if t == u:
            return True
    return False
