nbr = 0
try:
    nbr = int(input("nbr:"))
except ValueError:
    print("veiller mettre un nombre la prochaine fois!")
    exit()

nbrd = 0
pol = ""
pol2 = ""
ecart = 1000
p1 = True
while not nbrd == nbr:
    print(nbrd)

    pol2 = pol
    pol = input("plus ou mois (p ou m)? :")

    if ecart > 1:
        if p1:
            if pol == "p":
                nbrd += ecart
            elif pol == "m":
                nbrd -= ecart
            else:
                print("p ou l !")
                exit()
            p1 = False

        else:
            if pol == "p":
                if pol2 == "m":
                    nbrd += ecart
                if pol2 == "p":
                    nbrd += ecart
            elif pol == "m":
                if pol2 == "p":
                    ecart //= 10
                    nbrd -= ecart
                if pol2 == "m":
                    nbrd -= ecart
            else:
                print("p ou l !")
                exit()
    else:
        if p1:
            if pol == "p":
                nbrd += ecart
            elif pol == "m":
                nbrd -= ecart
            else:
                print("p ou l !")
                exit()
            p1 = False
        else:
            if pol == "p":
                nbrd += ecart
            elif pol == "m":
                nbrd -= ecart
            else:
                print("p ou l !")
                exit()
print(nbrd)
