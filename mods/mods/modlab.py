from blocklistfile import blockattr, blocklist
from pygame import *
import fonc

badded = 0
bladded = []
blockattrlist = {}
clicd = False
clicg = True
active = False
vanillablocklong = len(blocklist)
init = True


def mainf(p, var, screen):
    #print(var["cameray"])
    try:
        # print(fonc.toutchp(p.rect.x + p.rect.width // 2 + var["camerax"], p.rect.y + p.rect.height + 20 + var["cameray"]) == 7)
        if var["saut"] and fonc.toutchp(p.rect.x + p.rect.width // 2 + var["camerax"], p.rect.y + p.rect.height + 40 + var["cameray"]).block == vanillablocklong + badded and fonc.toutchp(p.rect.x + p.rect.width // 2 + var["camerax"], p.rect.y + p.rect.height - 44 * 6 + var["cameray"]).block == vanillablocklong + badded:
            var["cameray"] -= 300
            var["saut"] = False
        if fonc.t(K_LSHIFT, var["keys"]) and fonc.toutchp(p.rect.x + p.rect.width // 2 + var["camerax"], p.rect.y + p.rect.height + 20 + var["cameray"]).block == 7 and fonc.toutchp(p.rect.x + p.rect.width // 2 + var["camerax"], p.rect.y + p.rect.height + 44 * 7 + var["cameray"]).block == 7:
            var["cameray"] += 300
            var["saut"] = False
    except Exception as e:
        print("error :", e)
    finally:
        return var


def clicdf(item, pos, player, b, var):
    if b.block - vanillablocklong == 1:
        player.inv.give(2)


def clicgf(item, pos, player, b, var):
    if b.block - vanillablocklong == 1:
        player.inv.ungive((3, var["selectedslot"]))


def actublockadd():
    return vanillablocklong + badded


def get_blocks():
    global badded, bladded, blockattrlist, vanillablocklong, init

    new_block = blockattr(actublockadd(), [actublockadd(), "vert"], "stone", 10, True, "picaxe", "vert")
    blockattrlist.update({"vert": new_block})
    bladded.append("vert")
    vanillablocklong -= 1
    badded += 1
    if init:
        #vanillablocklong -= badded
        init = False

    return blockattrlist, bladded
