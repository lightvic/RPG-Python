#Pour tester le jeu, c'est RPG.py qu'il faut lancer.


from random import randint
def Search(X,List):
    i = 0 
    while i < len(List):
        if List[i] == X:
            return True
        i = i + 1
    return False

liste_attaque = ["1 : Attaquer à main nues","2 : Attaquer à l'épée","3 : Tir à l'arc"]

def max_exp(niveau):         #c'est le nombre de points d'expérience qu'on doit au minimum avoir pour augmenter de niveau.
    max_xp = 5 * niveau * 20
    return int(max_xp)

def level_up(barre_exp,niveau) :            #fonction pour voir si on augmente de niveau
    jauge_xp = max_exp(niveau)
    print("Vous devez avoir au moins",jauge_xp,"points d'expérience pour augmenter de niveau.")
    if barre_exp >= jauge_xp :
        niveau = niveau + 1
        print("Vous gagnez un niveau.")
        list_attack_per_level(niveau)
    return niveau

def atk(niveau) :                          #fonction qui augmente l'attaque en fonction du niveau
    attaque = 350 * niveau 
    return int(attaque)

def magic_point(niveau) :
    mana = 100 * niveau
    return mana

def defense(niveau) :              #fonction qui augmente la défense en fonction du niveau
    protect = 2500 * niveau 
    return int(protect)

def pv(niveau) :                   #fonction qui augmente les PV en fonction du niveau
    vie = 2500 * niveau 
    return int(vie) 

def dodge(niveau) :
    esq = niveau 
    return int(esq)

def list_attack_per_level(niveau) :             #fonction qui définit la liste d'attaques en fonction du niveau et affiche les nouvelles attaques apprises lors de la montée de niveau.

    if niveau >= 2 :
        if not Search("4 : Orage",liste_attaque):
            print("Vous avez appris l'attaque 'Orage' au niveau 2 !")
            liste_attaque.append("4 : Orage")
    if niveau >= 4 :
        if not Search("5 : Glaciation",liste_attaque):
            print("Vous avez appris l'attaque 'Glaciation' au niveau 4 !")
            liste_attaque.append("5 : Glaciation")
    if niveau >= 6 :
        if not Search("6 : Seisme",liste_attaque):
            print("Vous avez appris l'attaque 'Séisme' au niveau 6 !")
            liste_attaque.append("6 : Seisme")
    if niveau >= 8 :
        if not Search("7 : Inferno",liste_attaque):
            print("Vous avez appris l'attaque 'Inferno' au niveau 8 !")
            liste_attaque.append("7 : Inferno")
    if niveau == 10 :
        if not Search("8 : Big Bang",liste_attaque):
            print("Vous avez appris l'attaqe 'Big Bang' au niveau 10 !")
            liste_attaque.append("8 : Big Bang")
    return liste_attaque

