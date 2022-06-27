#Pour tester le jeu, c'est RPG.py qu'il faut lancer.


from random import randint
import os
from Map_and_descriptions import is_it_in_the_list
import time

def player_attaque(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player) : #action du joueur
    i = 0
    bonus_atk = 1
    bonus_epee = 1
    bonus_arc = 1
    if is_it_in_the_list("une épée courte en acier",inventory):
        bonus_epee = 1.5                        #les armes 2 étoiles augmentent seulement l'attaque de l'arme concernée (bonus non cumulable avec celui d'une arme 3 étoiles)
    if is_it_in_the_list("une épée longue en bronze céleste",inventory):
        bonus_epee = 2                          #les armes 3 étoiles augmentent l'attaque de l'arme concernée (bonus non cumulable avec celui d'une arme 2 étoiles)
        bonus_atk = bonus_atk * 1.1             #les armes 3 étoiles augmentent aussi l'attaque générale de 10% (bonus cumulable si deux armes 3 étoiles dans l'inventaire)
    if is_it_in_the_list("un arc en bois",inventory):
        bonus_arc = 1.5                         #les armes 2 étoiles augmentent seulement l'attaque de l'arme concernée (bonus non cumulable avec celui d'une arme 3 étoiles)
    if is_it_in_the_list("un grand arc à flèches de bronze",inventory):
        bonus_arc = 2                           #les armes 3 étoiles augmentent l'attaque de l'arme concernée (bonus non cumulable avec celui d'une arme 2 étoiles)
        bonus_atk = bonus_atk * 1.1             #les armes 3 étoiles augmentent aussi l'attaque générale de 10% (bonus cumulable si deux armes 3 étoiles dans l'inventaire)

    print("Sélectionnez le NUMÉRO de l'attaque.")
    print("Vous avez ",mana,"de mana.")
    while i < len(liste_attack) :               #liste des attaques et de leur coût en mana
        if i == 0 :
            print(liste_attack[i],"| ",round(atk_p * bonus_atk), "dégâts","| coût : 0 mana")                            #bonus_atk : le bonus obtenu lorsqu'on a une arme 3 étoiles
            print(" ")
        elif i == 1 :
            print(liste_attack[i],"| ",round((300 + atk_p) * bonus_atk * bonus_epee), "dégâts","| coût : 5 manas")      #bonus_epee : le bonus obtenu lorsqu'on a une épée 2 ou 3 étoiles (c'est-à-dire pas celle du départ)
            print(" ")
        elif i == 2 :
            print(liste_attack[i],"| ",round((500 + atk_p) * bonus_atk * bonus_arc), "dégâts","| coût : 10 manas")      #bonus_arc : le bonus obtenu lorsqu'on a un arc 2 ou 3 étoiles (c'est-à-dire pas celui du départ)
            print(" ")
        elif i == 3 :
            print(liste_attack[i],"| ",round((1500 + atk_p) * bonus_atk), "dégâts","| coût : 30 manas")
            print(" ")
        elif i == 4 :
            print(liste_attack[i],"| ",round((2000 + atk_p) * bonus_atk), "dégâts","| coût : 75 manas")
            print(" ")
        elif i == 5 :
            print(liste_attack[i],"| ",round((3500 + atk_p) * bonus_atk), "dégâts","| coût : 150 manas")
            print(" ")
        elif i == 6 :
            print(liste_attack[i],"| ",round((6666 + atk_p) * bonus_atk), "dégâts","| coût : 200 manas")
            print(" ")
        elif i == 7 :
            print(liste_attack[i],"| ",round((30000 + atk_p) * bonus_atk), "dégâts","| coût : 500 manas")
            print(" ")
        i = i + 1
    print("quitter")
    choice = input()                  #choix de l'attaque du joueur
    os.system("cls")
    
    if choice == "1" :
            print("Vous utilisez attaquer à mains nues.")                  
            attack_player = round(atk_p * bonus_atk)
    elif choice == "2" :
            print("Vous utilisez attaquer à l'épée.")
            attack_player = round((300 + atk_p) * bonus_atk * bonus_epee)
            mana = mana - 5
    elif choice == "3" :
            print("Vous utilisez tir à l'arc.")
            attack_player = round((500 + atk_p) * bonus_atk * bonus_arc)
            mana = mana - 10
    elif choice == "4" :
            if liste_attack.count("4 : Orage") == 1 :
                print("Vous utilisez orage.")
                attack_player = round((1500 + atk_p) * bonus_atk)
                mana = mana - 30
            else :
                print("Vous n'avez pas encore appris ce sort !")
                return combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
    elif choice == "5"  :
            if liste_attack.count("5 : Glaciation") == 1 :
                print("Vous utilisez glaciation.")
                attack_player = round((2000 + atk_p) * bonus_atk)
                mana = mana - 75
            else :
                print("Vous n'avez pas encore appris ce sort !")
                return combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
    elif choice == "6"  :
            if liste_attack.count("6 : Seisme") == 1 :
                print("Vous utilisez séisme.")
                attack_player = round((3500 + atk_p) * bonus_atk)
                mana = mana - 150
            else :
                print("Vous n'avez pas encore appris ce sort !")
                return combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
    elif choice == "7" :
            if liste_attack.count("7 : Inferno") == 1 :
                print("Vous utilisez inferno.")
                attack_player = round((6666 + atk_p) * bonus_atk)
                mana = mana - 200
            else :
                print("Vous n'avez pas encore appris ce sort !")
                return combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
    elif choice == "8" :
            if liste_attack.count("8 : Big Bang") == 1 :
                print("Vous utilisez big bang.")
                attack_player = round((30000 + atk_p) * bonus_atk)
                mana = mana - 500
            else :
                print("Vous n'avez pas encore appris ce sort !")
                return combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
    elif choice == "quitter" :
            attack_player = 0
            os.system("cls")
            combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
        
    else :
            attack_player = 0
            os.system("cls")
            print("Erreur : recommencez le tour.")
            return combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
   
    
    return attack_player,mana,choice

def player_obj(inventory) :         #utilisation de l'inventaire du joueur
    i = 0
    remede = 0
    nectar = 0
    while i < len(inventory) :      #On compte le nombre de remèdes et de nectars dans l'inventaire du joueur pour le lui afficher. Ce sont les seuls objets utilisables en combat et donc les seuls que l'on affiche.
        if inventory[i] == "remède" :
            remede = remede + 1
        elif inventory[i] == "nectar" :
            nectar = nectar + 1
        i = i + 1 
    print("nectars :",nectar)
    print("remèdes :",remede)
    print("quitter")
    print("Quel objet voulez-vous utiliser ? 1 : nectar (régénère le mana), 2 : remède (régénère les PV), 3 : quitter")
    choice = input()
    if choice == "nectar" or choice == "1" :
        os.system("cls")
        return 0
    if choice == "remède" or choice == "2" :
        os.system("cls")
        return 1
    elif choice == "quitter" or choice == "3" :
        os.system("cls")
        return 2
    else :
        os.system("cls")
        print("Erreur : recommencez le tour.")
        return 3





Epees = ["une épée rouillée","une épée courte en acier","une épée longue en bronze céleste"]
Arcs = ["un vieil arc tordu", "un arc en bois", "un grand arc à flèches de bronze"]
liste_armures_1_etoile = ["des gantelets", "des brassards", "des jambières"]
liste_armures_2_etoiles = ["une cotte de mailles", "une cuirasse", "un casque"]


def liste_butin(armes_2_etoiles,armes_3_etoiles,armures_1_etoile,armures_2_etoiles):           #Cette fonction détermine seulement dans quelle liste d'armes / armures sera prélevé le butin quand on bat un monstre.
    objets_disponibles = armes_2_etoiles + armes_3_etoiles + armures_1_etoile + armures_2_etoiles
    if objets_disponibles == [] :
        print("\nAucun objet à trouver : il doit rester quelque chose à corriger dans RPG pour que la fonction loot ne soit pas appelée à ce moment-là.\n")
    else :
        liste_objet = []
        compteur = 0
        while liste_objet == [] and compteur < 3:
            arme_ou_armure = randint(0,1)                               #On a une chance sur deux d'obtenir une arme et une chance sur deux d'obtenir une armure (du moins au départ, puisque ces probabilités changeront lorsqu'une liste sera vide).
            if arme_ou_armure == 0 :                                    #On obtiendra une arme.
                random_rarity = randint(1,10)
                if random_rarity < 3 and armes_3_etoiles != [] :        #Au début, on a 3 chances sur 10 d'avoir une arme 3 étoiles, mais cela peut changer.
                    liste_objet = armes_3_etoiles                       #la liste dans laquelle sera pioché l'objet trouvé
                elif random_rarity < 3 and armes_3_etoiles == [] :      #Il n'y a plus d'arme 3 étoiles donc on trouve une arme 2 étoiles.
                    if armes_2_etoiles != [] :
                        liste_objet = armes_2_etoiles
                    else :
                        arme_ou_armure = 1                  #Il n'y a plus d'arme donc on trouve une pièce d'armure.
                        compteur = compteur + 1
                else :                                      #random_rarity >= 3. Au début, on a 7 chances sur 10 d'avoir une arme 2 étoiles, mais cela peut changer.
                    if armes_2_etoiles != [] :
                        liste_objet = armes_2_etoiles
                    else :
                        if armes_3_etoiles != [] :          #Il n'y a plus d'arme 2 étoiles donc on trouve une arme 3 étoiles.
                            liste_objet = armes_3_etoiles
                        else :
                            arme_ou_armure = 1              #Il n'y a plus d'arme donc on trouve une pièce d'armure.
                            compteur = compteur + 1
            if arme_ou_armure == 1 :                        #On obtiendra une pièce d'armure.
                random_rarity = randint(1,10)
                if random_rarity < 3 and armures_2_etoiles != [] :      #Au début, on a 3 chances sur 10 d'avoir une armure 2 étoiles, mais cela peut changer.
                    liste_objet = armures_2_etoiles                     #la liste dans laquelle sera pioché l'objet trouvé
                elif random_rarity < 3 and armures_2_etoiles == [] :    #Il n'y a plus d'armure 2 étoiles donc on trouve une armure 1 étoile.
                    if armures_1_etoile != [] :
                        liste_objet = armures_1_etoile
                    else :
                        arme_ou_armure = 0                  #Il n'y a plus d'armure donc on trouve une arme.
                        compteur = compteur + 1
                else :                                      #random_rarity >= 3. Au début, on a 7 chances sur 10 d'avoir une armure 1 étoile, mais cela peut changer.
                    if armures_1_etoile != [] :
                        liste_objet = armures_1_etoile
                    else :
                        if armures_2_etoiles != [] :        #Il n'y a plus d'armure 1 étoile donc on trouve une armure 2 étoiles.
                            liste_objet = armures_2_etoiles
                        else :
                            arme_ou_armure = 0              #Il n'y a plus d'armure donc on trouve une arme.
                            compteur = compteur + 1
        return liste_objet

def butin(inventaire,liste):           #Cette fonction prélève le butin (dans la liste définie par la fonction précédente) et l'ajoute à l'inventaire.
    numero_objet = randint(0,len(liste)-1)      #L'objet est choisi au hasard dans la liste en paramètre.
    objet = liste[numero_objet]
    inventaire.append(objet)
    print("\nOBTENU :", objet)
    if objet == "une épée courte en acier" and not is_it_in_the_list("une épée longue en bronze céleste",inventaire):
        print("Votre attaque à l'épée infligera davantage de dégâts, à présent.\n")
    elif objet == "une épée courte en acier" and is_it_in_the_list("une épée longue en bronze céleste",inventaire):
        print("Cette épée ne vous sert pas vraiment. Votre épée longue en bronze céleste est plus puissante.\n")
    elif objet == "une épée longue en bronze céleste" :
        print("Votre attaque à l'épée infligera davantage de dégâts, à présent. La magie présente dans l'épée augmente aussi votre attaque.\n")
    elif objet == "un arc en bois" and not is_it_in_the_list("un grand arc à flèches de bronze",inventaire):
        print("Votre tir à l'arc infligera davantage de dégâts, à présent.\n")
    elif objet == "un arc en bois" and is_it_in_the_list("un grand arc à flèches de bronze",inventaire):
        print("Cet arc ne vous sert pas vraiment. Votre grand arc à flèches de bronze est plus puissant.\n")
    elif objet == "un grand arc à flèches de bronze":
        print("Votre tir à l'arc infligera davantage de dégâts, à présent. La magie présente dans l'arc augmente aussi votre attaque.\n")
    elif is_it_in_the_list(objet,liste_armures_1_etoile) :
        print("Vous serez un peu mieux protégé des attaques, à présent.\n")
    elif is_it_in_the_list(objet,liste_armures_2_etoiles) :
        print("Vous serez bien mieux protégé des attaques, à présent !\n")
    del(liste[numero_objet])            #on supprime l'objet obtenu de la liste d'où il provient, afin de ne pas trouver deux fois le même.
    time.sleep(3)
    return(inventaire,liste)


def player_escape() : #Lorsque le joueur choisit de fuir
    escape = randint(0,10)
    if escape <= 8 :
        escape_result = "fuite"
        os.system("cls")
        print("Vous réussisez à fuir.")
        time.sleep(1)
    else :
        escape_result = "fail"
        os.system("cls")
        print("Vous n'arrivez pas à fuir.")
        time.sleep(1)
    return escape_result

def monster(ennemy) :  #L'attaque de l'ennemi est décidée aléatoirement parmi ses deux attaques.

    choice = randint(7,8)           #L'ennemi a autant de chances d'utiliser son attaque faible ou son attaque puissante.
    print("L'adversaire utilise ",ennemy[choice])
    return ennemy[choice + 2]

def critique(attaque,name) :        #Cette fonction détermine s'il y a coup critique (2 chances sur 10). Elle sert à la fois au joueur et à l'ennemi.
    chance = randint(1,10)
    if chance <= 2 :
        attaque = attaque * 2 
        if name =="vous" :
            print("Vous faites un coup critique.")
        else :
            print(name,"fait un coup critique.")
    return attaque

def dodge(esq,attaque,name):        #Cette fonction détermine si quelqu'un esquive. Elle sert à la fois au joueur et à l'ennemi.
    chance = randint(1,10)
    if esq > 4 :                    #Le joueur a au maximum 4 chances sur 10 d'esquiver.
        esq = 4
    if esq  <= chance :
        return attaque
    else :
        if name == "vous" :
            print("Vous esquivez.")
        else :
            print(name,"esquive.")
        return 0

def combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player):
    print(ennemy[11])                       #C'est la description de début de combat. Elle est unique à chaque ennemi.
    if niveau_player < ennemy[1] :
        print("\nCet ennemi est meilleur que vous ! La fuite est fortement conseillée !\n")     #Comme les ennemis apparaissent beaucoup aléatoirement, on prévient le joueur lorsqu'un ennemi est trop dangereux pour lui.
    pv_monster = ennemy[2]
    print("\n","Vous avez",pv_player,"point(s) de vie.\n")
    print("\n",ennemy[0],"a",ennemy[2],"point(s) de vie.\n")
   
    while ennemy[2] > 0 and pv_player > 0 :
        atk_player = 0
        atk_monster = 0
        def_player = 0
        def_monster = 0
        i = 0
        j=0
        remede = 0
        nectar = 0

        escape= str()
        print("Que voulez-vous faire ?")
        print("1.attaquer")
        print("2.défendre |",def_base,"points de défense")
        print("3.utiliser un objet")
        print("4.fuir")
        action=input()
        action=action.lower()                         
        os.system("cls")
        if action == "attaquer" or action == "1" :   #le joueur choisit d'attaquer
            atk_player,mana,choice = player_attaque(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
            j=1
            if choice != "1" :
                if mana < 0 :  #utilisation de mana
                    print("Vous n'avez plus de mana !")
                    combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
            atk_player = critique(atk_player,"vous")                                    #test de coup critique du joueur
            atk_player = dodge(ennemy[5],atk_player,ennemy[0])                          #test d'esquive du monstre    
            
        elif action == "defendre" or action == "défendre" or action == "2" :            #Le joueur choisit de se défendre.
            bonus_def = 1       #Les bonus de défense des pièces d'armures sont tous cumulables. Armure 1 étoile : +5%, armure 2 étoiles : +10%. Le bonus maximum est d'environ 54%.
            print("Vous vous défendez.")
            if is_it_in_the_list("des gantelets",inventory):
                bonus_def = bonus_def * 1.05
            if is_it_in_the_list("des brassards",inventory):
                bonus_def = bonus_def * 1.05
            if is_it_in_the_list("des jambières",inventory):
                bonus_def = bonus_def * 1.05
            if is_it_in_the_list("une cotte de mailles",inventory):
                bonus_def = bonus_def * 1.1
            if is_it_in_the_list("une cuirasse",inventory):
                bonus_def = bonus_def * 1.1
            if is_it_in_the_list("un casque",inventory):
                bonus_def = bonus_def * 1.1
            def_player = round(def_base * bonus_def)
            

        elif action == "objet" or action == "utiliser un objet" or action == "3" :        #Le joueur choisit d'utiliser un objet.
            j = 1
            i = 0
            while i < len(inventory) :
                if inventory[i] == "remède" :
                     remede = remede + 1
                elif inventory[i] == "nectar" :
                    nectar = nectar + 1
                i = i + 1 
            obj = player_obj(inventory)
            if obj == 0 :
                if nectar != 0 :
                    if mana == mana_max :
                        print ("Vous n'avez pas besoin de ça !")
                        return combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
                    mana = mana_max
                    inventory.remove("nectar")                  #suppression d'un nectar de l'inventaire
                    
                    print("Votre mana a été restauré !")
                else :
                    os.system("cls")
                    print("Vous n'avez plus de nectar.")        #si le joueur veut utiliser un nectar alors qu'il n'en a plus
                    
                    combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
            elif obj == 1 :
                if remede != 0 :
                    if pv_player == max_pv :
                        print ("Vous n'avez pas besoin de ça !")
                        return combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)              
                    regene = max_pv * 75
                    regene = round(regene / 100)
                    if regene > max_pv - pv_player :
                        regene = max_pv - pv_player
                    pv_player = pv_player + regene
                    inventory.remove("remède")                  #suppression d'un remède de l'inventaire.
                    
                    print("Vous avez récupéré", regene,"points de vie.")
                else :
                    os.system("cls")
                    print("Vous n'avez plus de remède.")        #si le joueur veut utiliser un remède alors qu'il n'en a plus.
                    
                    combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
            elif obj == 2 :
                combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
            elif obj == 3 :
                combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)

        
        elif action == "fuir" or action == "4" :        #Le joueur choisit de fuir.
            escape = player_escape()
        else :
            atk_p = atk_base
            def_player = 0
            combat(niveau_player,max_pv,pv_player,atk_base,atk_p,def_base,def_player,esq,inventory,mana,mana_max,ennemy,liste_attack,attack_player)
        if escape == "fuite" :                          #si la fuite réussit
            mana = mana_max
            ennemy[2] = pv_monster
            return "fuite"
        else :
            j = 1
        while j == 1 :
            action_monster = randint(1,10)      #action du monstre aléatoire
            if action_monster <= 8 :
                if atk_player >= ennemy[2] :
                    ennemy[2] = 0
                    print("Vous infligez",atk_player,"dégât(s).")
                    print("L'adversaire a",ennemy[2],"pv.")
                    ennemy[2] = pv_monster
                    print(ennemy[12])
                    return "gagné"
           
                atk_monster = monster(ennemy)
                atk_monster = critique(atk_monster,ennemy[0])               #test de coup critique du monstre
                atk_monster = dodge(esq,atk_monster,"vous")                 #test d'esquive du joueur
                print("L'adversaire vous inflige",atk_monster,"dégât(s).")
                j = 0
            else :
                def_monster = ennemy[4]                     #défense du monstre
                print("L'adversaire se défend. Il a",ennemy[4],"point(s) de défense.")
                j = 0
            if action == "attaquer" or action == "1" :      #Le joueur choisit d'attaquer.
                print("Vous infligez",atk_player,"dégât(s).")
        
        atk_player = atk_player - def_monster       #dégâts du joueur (défense du monstre prise en compte, s'il ne se défend pas la def est de 0)
        atk_monster = atk_monster - def_player      #dégâts du monstre (défense du joueur prise en compte, s'il ne se défend pas la def est de 0)
        def_monster = 0
        if atk_player < 0 :                         #ppour éviter que l'attaque soit négative
            atk_player = 0
        if atk_monster < 0 :
            atk_monster = 0
        ennemy[2] = ennemy[2] - atk_player          #dégâts infligés au monstre
        if ennemy[2] < 0 :
            ennemy[2] = 0
        pv_player = pv_player - atk_monster         #dégâts infligés au joueur
        if pv_player < 0 :
            pv_player = 0
        
        
        
        print("Il vous reste",pv_player,"pv.")
        print("L'adversaire a ",ennemy[2],"pv.")

    
    if ennemy[2] == 0 :
        print(ennemy[12])                   #texte de victoire
        time.sleep(4)
        mana = mana_max
        pv_player = max_pv
        ennemy[2] = pv_monster
        return "gagné"                      #L'ennemi est mort, le joueur peut rebouger.

    elif pv_player == 0 :                   #Le joueur est mort, il retourne alors au menu.
        print(ennemy[13])                   #texte de défaite
        time.sleep(4)
        print("GAME OVER")
        return "game over"

    

