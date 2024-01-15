print("importation du module pour la gestion des block")
import os
print("importation du module pour la gestion des block terminé")

print("intialisation des calsse requise pour la gestion des blocs")
class blockattr:
    def __init__(self, block, recup, typeb, resistance, handrecup, itemgrouprecup, imagegname, gui=False, cassable=True, copyrecup=False):
        self.block = block
        self.recup = recup
        self.type = typeb
        self.resistance = resistance
        self.handrecup = handrecup
        self.itemgrouprecup = itemgrouprecup
        self.gui = gui
        self.cassable=cassable
        self.imagename = imagegname
        self.copyrecup = copyrecup


class itemattr:
    def __init__(self, item):
        self.item = item
        self.enchant = {}


print("intialisation des calsse requise pour la gestion des blocs terminée")
print("initialistaion des blocs")

blockattrlist = {
    "air": blockattr(0, [0, "air"], "air", 0, False, "hand", "air"),
    "dirt": blockattr(1, [1, "dirt"], "dirt", 1, True, "shovel", "dirt"),
    "grass_block": blockattr(2, [1, "dirt"], "dirt", 1, True, "shovel", "grass_block"),
    "stone": blockattr(3, [4, "cobblestone"], "stone", 50, False, "picaxe", "stone"),
    "cobblestone": blockattr(4, [4, "cobblestone"], "stone", 50, False, "picaxe", "cobblestone"),
    "bedrock": blockattr(5, [4, "cobblestone"], "stone", 100000, False, "picaxe", "bedrock", cassable=False),
    "craftingtable": blockattr(6, [6, "craftingtable"], "wood", 13, True, "axe", "craftingtable", True)
}

blocklist = [
    "air",
    "dirt",
    "grass_block",
    "stone",
    "cobblestone",
    "bedrock",
    "craftingtable"
]

print("initialistaion des blocs terminé")


def check_mod():
    global blocklist
    print("importaion et initialisation d(u,es) mod(s)")

    modfile = open("mods/parameter.config", "r")
    listn1 = modfile.read().split("\n")
    modload = {}
    for i in listn1:
        nt = i.split("=")
        modload[nt[0]] = nt[1]
    if modload["active"] == "True":
        for file in os.listdir("mods/mods"):
            try:
                if file.endswith(".py"):  # S'assure que le fichier est un script Python
                    module_name = file[:-3]  # Retire l'extension .py
                    mod = __import__("mods.mods." + module_name, fromlist=[''])
                    if mod.active:
                        battrsupmod, blistsupmod = mod.get_blocks()
                        blockattrlist.update(battrsupmod)
                        blocklist += blistsupmod
            except Exception as e:
                print(f"Erreur lors du chargement du module {file}: {e}")
    print("importaion et initialisation d(u,es) mod(s) terminé")
