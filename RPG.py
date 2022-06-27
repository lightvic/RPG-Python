#C'est bien ce fichier qu'il faut lancer pour tester le jeu.
#Rappel des membres du groupe 17 (tous W1 groupe 2) : GUILLERD Victorien, JIN Loïc, LEFEBVRE Valentine, MOHAMED Mia

from random import randint
import os
import time

from os import system
from Menu import *
from Combat import *
from perso_stat import *
from Map_and_descriptions import *
from Ennemies import *

def game():
    token = 3
    a = menu(token) 
    if a == "Jeu" :     #nouvelle partie
        
        Liste_armes_2_etoiles = ["une épée courte en acier", "un arc en bois"]
        Liste_armes_3_etoiles = ["une épée longue en bronze céleste", "un grand arc à flèches de bronze"]
        Liste_armures_1_etoile = ["des gantelets", "des brassards", "des jambières"]
        Liste_armures_2_etoiles = ["une cotte de mailles", "une cuirasse", "un casque"]

        liste_cases_combat = [[2,16],[5,8],[7,4],[7,9],[7,17],[15,18],[17,13],[18,10],[20,11],[13,1],[15,3],[20,0],[18,17],[20,2]]  #Ce sont les cases où un combat peut avoir lieu, en-dehors de la forêt.
        jeu_en_cours = 1
        Niveau_joueur = 1
        mana_max = magic_point(Niveau_joueur)
        mana = mana_max
        XP_base = 0
        position_initiale_joueur = [12,5]
        time.sleep(2)
        os.system("cls")
        print("...")
        time.sleep(1)
        print("Fatigué...")
        time.sleep(1)
        print("Vous êtes réveillé mais vous n'ouvrez pas tout de suite les yeux. Vous êtes allongé à même le sol couvert de feuilles mortes. Des racines vous labourent le dos et vous poussent à vous asseoir en vous frottant les yeux.")
        time.sleep(5)
        print("Vous vous trouvez dans une forêt lugubre, au pied d'un arbre aux branches et au tronc distordus. Les arbres autour de vous, tous semblables, sont hauts et rapprochés. Leurs feuilles noires forment une canopée qui ne laisse presque aucune lumière filtrer. Il ne fait pas nuit mais l'heure est impossible à déterminer précisément.")
        time.sleep(7)
        print("Qu'est-ce que vous faites là ? Vous ne vous souvenez de rien...")
        time.sleep(3)
        print("Vous vous décidez finalement à vous lever et à explorer les environs. Rester inactif dans un endroit pareil vous met mal à l'aise.")
        time.sleep(4)
        print("Une odeur nauséabonde flotte dans l'air. Vous hésitez à partir dans la direction opposée mais vous devez en avoir le coeur net.")
        time.sleep(4)
        print("Quelle horreur ! Vous avez découvert un cadavre en décomposition. Vous vous couvrez le nez avec votre col. En observant les alentours plus attentivement, vous remarquez des traces de combat. Cette personne n'est pas morte de cause naturelle.")
        time.sleep(6)
        print("Il vous en coûte d'agir ainsi mais, si ce qui l'a tué rode encore dans les parages, il faut que vous puissiez vous défendre. Vous lui volez donc ses armes.")
        time.sleep(5)
        position_joueur = position_initiale_joueur
        inventory = ["une épée rouillée", "un vieil arc tordu"]
        print("\nOBTENU : une épée rouillée et un vieil arc tordu")
        time.sleep(2)
        print("\nEn vous penchant pour ramasser les armes, un pendentif est sorti de votre col et s'est balancé au bout de sa chaine. Vous n'aviez même pas remarqué que vous portiez ce bijou autour du cou.")
        time.sleep(6)
        print("C'est un petit pendentif doré ovale. En l'ouvrant, vous découvrez le portrait d'une jeune fille souriante, et tous vos souvenirs reviennent brutalement, accompagnés d'une grande colère. Car il s'agit de votre soeur, et Zeus l'a enlevée.")
        time.sleep(6)
        print("Vous vous rappelez le défi qu'il vous a lancé : vous devez le vaincre, ainsi que ses frères, et tous les monstres et dieux qui se trouveront sur votre route. Si vous y parvenez, elle vous sera rendue saine et sauve. Mais quel crédit accorder à la parole d'un dieu capable d'une telle félonie ? Il n'y a pas une seconde à perdre.")
        time.sleep(7)
        while jeu_en_cours == 1 :
            ancienne_position = position_joueur
            show_map(position_joueur)                               #On affiche la carte avec la position du joueur avant de lui demander où il veut aller.
            position_joueur = Move(ancienne_position,inventory)
            os.system("cls")
            description_case(position_joueur,ancienne_position)     #Certaines cases affichent des descriptions pour entrer un peu dans l'univers du jeu.
            evenement = evenement_case(position_joueur,liste_cases_combat)  #Cette fonction détermine si on déclenche un combat, si on trouve un objet, ou s'il ne se passe rien.
            if evenement == "objet":
                objet = randint(1,10)                               #Lorsqu'on trouve un objet, il y a 80% de chances pour que ce soit un remède et 20% de chances pour que ce soit un nectar.
                if objet < 8 :
                    inventory.append("remède")
                    print("\nOBTENU : un remède. Vous pourrez le boire pour récupérer quelques points de vie en cas de besoin.\n")
                    time.sleep(4)
                else :
                    inventory.append("nectar")
                    print("\nOBTENU : un nectar. Vous pourrez le boire pour régénérer votre mana en cas de besoin.\n")
                    time.sleep(4)
                pass
            elif evenement == "combat":
                numero_ennemi = ennemi_case(position_joueur)        #En fonction d'où on se trouve sur la carte (forêt ou emplacement précis des autres zones), les ennemis ne sont pas les mêmes. Cette fonction nous donne le numéro de l'ennemi à affronter.
                ennemi = Liste_ennemis[numero_ennemi]               #On stocke la liste que nous renvoie la fonction de l'ennemi (avec notemment ses statistiques, son nom, les messages à afficher en début et fin de combat, ...)
                attaque_joueur = atk(Niveau_joueur)
                defense_joueur = defense(Niveau_joueur)
                PV_joueur = pv(Niveau_joueur)
                mana_max = magic_point(Niveau_joueur)
                mana = mana_max
                base_def = defense_joueur
                atk_base = attaque_joueur
                pv_max = PV_joueur
                esq_player = dodge(Niveau_joueur)
                liste_attaques_joueur = list_attack_per_level(Niveau_joueur)    #Le niveau auquel le joueur apprend une attaque est prédéfini donc sa liste d'attaques dépend uniquement de son niveau.
                attack_player = 0
                resultat_combat = combat(Niveau_joueur,pv_max,PV_joueur,atk_base,attaque_joueur,base_def,defense_joueur,esq_player,inventory,mana,mana_max,ennemi,liste_attaques_joueur,attack_player)
                if resultat_combat == "game over" :
                    print("~~~ FIN DU JEU ~~~ VOUS AVEZ PERDU ~~~")
                    jeu_en_cours = 0
                elif resultat_combat == "gagné" :
                    if Niveau_joueur != 10:
                        print("Vous avez gagné",ennemi[6],"points d'expérience.")
                        XP_base = XP_base + ennemi[6]
                        print("Vous avez en tout",XP_base,"points d'expérience.")
                        Niveau_joueur = level_up(XP_base,Niveau_joueur)
                        print("Vous êtes niveau",Niveau_joueur,".\n")
                    if numero_ennemi == 17 :        #Après le combat contre Hadès.
                        inventory.append("Barque de Charon")
                        print("\nOBTENU : Barque de Charon. Vous pouvez à présent rejoindre la mer depuis l'embouchure de la rivière.\n")
                    elif numero_ennemi == 18 :      #Après le combat contre Poséidon.
                        inventory.append("Clé de l'Olympe")
                        print("\nOBTENU : Clé de l'Olympe. Vous pouvez à présent atteindre le sommet de la plus haute montagne.\n")
                    elif numero_ennemi == 19 :      #Après le combat contre Zeus, le jeu est fini.
                        os.system("cls")
                        print("Un énorme bruit métallique retentit. Il vous fait penser à une grille, alors vous courrez dans sa direction. Après ce qui vous paraît une éternité, vous arrivez enfin devant un immense bâtiment de pierre.")
                        time.sleep(6)
                        print("À l'intérieur, d'innombrables cellules sont alignées, mais une seule est ouverte, et une jeune fille se tient dans l'entrée, sans oser sortir. Elle vous aperçoit, crie votre nom et court vers vous.")
                        time.sleep(6)
                        print("C'est votre soeur, terrifiée et amaigrie, mais vivante. Vous avez réussi. Vous allez enfin pouvoir rentrer chez vous.\n")
                        time.sleep(4)
                        print("~~~ FIN DU JEU ~~~ VOUS AVEZ GAGNÉ ~~~")
                        jeu_en_cours = 0
                        time.sleep(4)
                        credit(token)
                    else :
                        objets_disponibles = Liste_armes_2_etoiles + Liste_armes_3_etoiles + Liste_armures_1_etoile + Liste_armures_2_etoiles
                        if objets_disponibles != [] :
                            proba_butin = randint(1,4)          #On a 1 chance sur 4 de trouver un objet après avoir vaincu un ennemi (autre que les 3 grands dieux).
                            if proba_butin == 1 :               
                                loot = 1
                            else :
                                loot = 0
                            if loot == 1:
                                loot_list = liste_butin(Liste_armes_2_etoiles,Liste_armes_3_etoiles,Liste_armures_1_etoile,Liste_armures_2_etoiles)
                                if loot_list == Liste_armes_2_etoiles :
                                    (inventory,Liste_armes_2_etoiles) = butin(inventory,Liste_armes_2_etoiles)
                                elif loot_list == Liste_armes_3_etoiles :
                                    (inventory,Liste_armes_3_etoiles) = butin(inventory,Liste_armes_3_etoiles)
                                elif loot_list == Liste_armures_1_etoile :
                                    (inventory,Liste_armures_1_etoile) = butin(inventory,Liste_armures_1_etoile)
                                elif loot_list == Liste_armures_2_etoiles :
                                    (inventory,Liste_armures_2_etoiles) = butin(inventory,Liste_armures_2_etoiles)
                            objets_disponibles = Liste_armes_2_etoiles + Liste_armes_3_etoiles + Liste_armures_1_etoile + Liste_armures_2_etoiles
                    if liste_cases_combat.count == 1 :
                        liste_cases_combat.remove(position_joueur)  #évite d'avoir deux combats sur la même case (quand c'est sur un chemin et qu'on doit y passer deux fois)
                    time.sleep(3)               #sinon, on ne voit pas tout ce qui s'affiche à la fin du combat (xp, etc) parce que la map s'affiche tout de suite
                elif resultat_combat == "fuite" :
                    position_joueur = ancienne_position             #Puisque certaines cases déclenchent automatiquement un combat, la fuite nous renvoie à la case précédente pour éviter de relancer le combat (ou qu'on puisse échapper à un combat obligatoire en fuyant, et continuer à avancer).

game()