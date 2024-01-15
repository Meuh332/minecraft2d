import pygame
from pomme import *
from serpent import *
from grille import *
from random import *
from time import *
pygame.init()
display.set_caption("snake")
screen = display.set_mode((1080, 720))

false = False
true = True

on = True

xs = 0
ys = 0
rs = "w"

def aff():
    yp = 0
    for ya in jeu:
        yp += 1
        xp = 0
        for xa in ya:
            xp += 1
            if xa == 1:
                s1 = S1(xp, yp)

                screen.blit(s1.image, s1.rect)
            if xa == 2:
                s2 = S2(xp, yp)

                screen.blit(s2.image, s2.rect)
            if xa == 3:
                s3 = S3(xp, yp)

                screen.blit(s3.image, s3.rect)
            if xa == 4:
                s4 = S4(xp, yp)

                screen.blit(s4.image, s4.rect)
            if xa == 5:
                s5 = S5(xp, yp)

                screen.blit(s5.image, s5.rect)
            if xa == 6:
                s6 = S6(xp, yp)

                screen.blit(s6.image, s6.rect)
            if xa == 7:
                s7 = S7(xp, yp)

                screen.blit(s7.image, s7.rect)
            if xa == 8:
                s8 = S8(xp, yp)

                screen.blit(s8.image, s8.rect)
            if xa == 9:
                s9 = S9(xp, yp)

                screen.blit(s9.image, s9.rect)
            if xa == 10:
                s10 = S10(xp, yp)

                screen.blit(s10.image, s10.rect)
            if xa == 11:
                s11 = S11(xp, yp)

                screen.blit(s11.image, s11.rect)
            if xa == 12:
                s12 = S12(xp, yp)

                screen.blit(s12.image, s12.rect)
            if xa == 13:
                s13 = S13(xp, yp)

                screen.blit(s13.image, s13.rect)
            if xa == 14:
                s14 = S14(xp, yp)

                screen.blit(s14.image, s14.rect)

s = mixer.Sound('snack_song.mp3')
m = mixer.Sound('mort_snack.mp3')
p = mixer.Sound('pomme_snack.mp3')

s.play()
a = 0


def setup():
    screen.fill((20, 90, 50))
    a = 1080
    b = 720
    c = 160*4
    d = 64
    vertclaire = Rect((a - (c - 64)) / 2, (b - (c - 64)) / 2, c - 64, c - 64)
    draw.rect(screen, (39, 174, 96), vertclaire)
    for y in range(5):
        for x in range(5):
            vertfonce = Rect((a - (c - 64)) / 2 + d * 2 * y, (b - (c - 64)) / 2 + d * 2 * x, d, d)
            draw.rect(screen, (25, 111, 61), vertfonce)
    for y in range(4):
        for x in range(4):
            vertfonce = Rect((a - (c - 64)) / 2 + d * 2 * y + 64, (b - (c - 64)) / 2 + d * 2 * x + 64, d, d)
            draw.rect(screen, (25, 111, 61), vertfonce)


def t(t):
    for u in keys:
        if t == u:
            return true
    return false

def pommee():
    pokey = true
    pommex = 1
    pommey = 1
    while pokey:
        pommex = randint(1, 9)
        pommey = randint(1, 9)
        if jeu[pommey - 1][pommex - 1] == 0:
            pokey = false
    return Pomme(pommex, pommey)

setup()
keys = []
foufé = false
dep = "w"
pomme = pommee()
pomme.truc2()
c = 0
while on:
    foufé = false
    a += 1
    if a == 97:
        a = 0
        s.play()
    for event in pygame.event.get():
        if event.type == QUIT:
            on = False
        if event.type == KEYDOWN:
            keys.append(event.key)
        if event.type == KEYUP:
            for k in keys:
                if k == event.key:
                    keys.remove(event.key)
    screen.blit(pomme.image, pomme.rect)
    aff()
    display.flip()
    setup()

    if dep == "w" and t(K_s):
        keys.remove(K_s)
    if dep == "a" and t(K_d):
        keys.remove(K_d)
    if dep == "s" and t(K_w):
        keys.remove(K_w)
    if dep == "d" and t(K_a):
        keys.remove(K_a)


    if t(K_w):
        dep = "w"
    if t(K_s):
        dep = "s"
    if t(K_d):
        dep = "d"
    if t(K_a):
        dep = "a"

    yp = 0
    yb = 0
    xb = 0
    for ya in jeu:
        yp += 1
        xp = 0
        for xa in ya:
            xp += 1
            if xa == 1:
                xs = xp - 1
                ys = yp - 1
                rs = "w"
                if yp == pomme.y and xp == pomme.x:
                    foufé = true
                    pomme = pommee()
                    p.play()
                    c += 1
                    print(c)
            if xa == 2:
                xs = xp - 1
                ys = yp - 1
                rs = "s"
                if yp == pomme.y and xp == pomme.x:
                    foufé = true
                    pomme = pommee()
                    p.play()
                    c += 1
                    print(c)
            if xa == 3:
                xs = xp - 1
                ys = yp - 1
                rs = "d"
                if yp == pomme.y and xp == pomme.x:
                    foufé = true
                    pomme = pommee()
                    p.play()
                    c += 1
                    print(c)
            if xa == 4:
                xs = xp - 1
                ys = yp - 1
                rs = "a"
                if yp == pomme.y and xp == pomme.x:
                    foufé = true
                    pomme = pommee()
                    p.play()
                    c += 1
                    print(c)



            if xa == 7:
                xq = xp - 1
                yq = yp - 1
                rq = "w"
            if xa == 8:
                xq = xp - 1
                yq = yp - 1
                rq = "s"
            if xa == 9:
                xq = xp - 1
                yq = yp - 1
                rq = "d"
            if xa == 10:
                xq = xp - 1
                yq = yp - 1
                rq = "a"


            if xa == 5:
                xb = xp - 1
                yb = yp - 1
                rb = "v"
            if xa == 6:
                xb = xp - 1
                yb = yp - 1
                rb = "h"

            if jeu[yb + 1][xb] == 5 and jeu[yb][xb - 1] == 4:
                jeu[yb][xb] = 14

            if jeu[yb][xb + 1] == 6 and jeu[yb - 1][xb] == 1:
                jeu[yb][xb] = 12

            if jeu[yb + 1][xb] == 5 and jeu[yb][xb + 1] == 3:
                jeu[yb][xb] = 11

            if jeu[yb][xb - 1] == 6 and jeu[yb - 1][xb] == 1:
                jeu[yb][xb] = 13


            if jeu[yb + 1][xb] == 2 and jeu[yb][xb - 1] == 6:
                jeu[yb][xb] = 14

            if jeu[yb][xb + 1] == 3 and jeu[yb - 1][xb] == 5:
                jeu[yb][xb] = 12

            if jeu[yb + 1][xb] == 2 and jeu[yb][xb + 1] == 6:
                jeu[yb][xb] = 11

            if jeu[yb][xb - 1] == 4 and jeu[yb - 1][xb] == 5:
                jeu[yb][xb] = 13


            if jeu[yb + 1][xb] == 8 and jeu[yb][xb - 1] == 6:
                jeu[yb][xb] = 14

            if jeu[yb][xb + 1] == 9 and jeu[yb - 1][xb] == 5:
                jeu[yb][xb] = 12

            if jeu[yb + 1][xb] == 8 and jeu[yb][xb + 1] == 6:
                jeu[yb][xb] = 11

            if jeu[yb][xb - 1] == 10 and jeu[yb - 1][xb] == 5:
                jeu[yb][xb] = 13


            if jeu[yb + 1][xb] == 5 and jeu[yb][xb - 1] == 10:
                jeu[yb][xb] = 14

            if jeu[yb][xb + 1] == 6 and jeu[yb - 1][xb] == 7:
                jeu[yb][xb] = 12

            if jeu[yb + 1][xb] == 5 and jeu[yb][xb + 1] == 9:
                jeu[yb][xb] = 11

            if jeu[yb][xb - 1] == 6 and jeu[yb - 1][xb] == 7:
                jeu[yb][xb] = 13


    if foufé == true:
        rq = ""

    if rq == "s" and jeu[yq - 1][xq] == 11:
        jeu[yq][xq] = 0
        jeu[yq - 1][xq] = 10
    if rq == "s" and jeu[yq - 1][xq] == 14:
        jeu[yq][xq] = 0
        jeu[yq - 1][xq] = 9
    if rq == "s" and jeu[yq - 1][xq] == 5:
        jeu[yq][xq] = 0
        jeu[yq - 1][xq] = 8

    if rq == "d" and jeu[yq][xq - 1] == 12:
        jeu[yq][xq] = 0
        jeu[yq][xq - 1] = 8
    if rq == "d" and jeu[yq][xq - 1] == 11:
        jeu[yq][xq] = 0
        jeu[yq][xq - 1] = 7
    if rq == "d" and jeu[yq][xq - 1] == 6:
        jeu[yq][xq] = 0
        jeu[yq][xq - 1] = 9

    if rq == "a" and jeu[yq][xq + 1] == 14:
        jeu[yq][xq] = 0
        jeu[yq][xq + 1] = 7
    if rq == "a" and jeu[yq][xq + 1] == 13:
        jeu[yq][xq] = 0
        jeu[yq][xq + 1] = 8
    if rq == "a" and jeu[yq][xq + 1] == 6:
        jeu[yq][xq] = 0
        jeu[yq][xq + 1] = 10

    if rq == "w" and jeu[yq + 1][xq] == 12:
        jeu[yq][xq] = 0
        jeu[yq + 1][xq] = 10
    if rq == "w" and jeu[yq + 1][xq] == 13:
        jeu[yq][xq] = 0
        jeu[yq + 1][xq] = 9
    if rq == "w" and jeu[yq + 1][xq] == 5:
        jeu[yq][xq] = 0
        jeu[yq + 1][xq] = 7


    if dep == "w" and jeu[ys - 1][xs] != 0:
        on = False
    if dep == "a" and jeu[ys][xs - 1] != 0:
        on = False
    if dep == "s" and jeu[ys + 1][xs] != 0:
        on = False
    if dep == "d" and jeu[ys][xs + 1] != 0:
        on = False


    if dep == "w" and ys != 0:
        jeu[ys][xs] = 5
        jeu[ys - 1][xs] = 1
    if dep == "a" and xs != 0:
        jeu[ys][xs] = 6
        jeu[ys][xs - 1] = 4
    if dep == "s" and ys != 8:
        jeu[ys][xs] = 5
        jeu[ys + 1][xs] = 2
    if dep == "d" and xs != 8:
        jeu[ys][xs] = 6
        jeu[ys][xs + 1] = 3


    if dep == "w" and ys == 0:
        on = False
    if dep == "a" and xs == 0:
        on = False
    if dep == "s" and ys == 8:
        on = False
    if dep == "d" and xs == 8:
        on = False


    sleep(1/8)
m.play()
sleep(2)