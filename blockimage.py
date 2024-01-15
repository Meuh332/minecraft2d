print("importation des module de l'affichage du monde")
from pygame import image
from blocklistfile import blocklist

print("importation des module de l'affichage du monde terminé")
print("initialisation de la fonction d'affichage de blocs")


def block(bn):
    try:
        return image.load("textures/blocks/" + bn.imagename + ".png"), True
    except Exception as er:
        print(f"un block non reconnu a été trouvé et remplacé par de l'air, Ereur: {er}, bn: {bn.imagename}")
        return image.load("textures/blocks/" + blocklist[0] + ".png"), False


print("initialisation de la fonction d'affichage de bloc terminé")
