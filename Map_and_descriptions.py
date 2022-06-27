#Pour tester le jeu, c'est RPG.py qu'il faut lancer.


#Cette fonction vérifie si quelquechose est dans une liste. Ici, elle sert à la fois à vérifier la présence d'un objet dans l'inventaire et à voir si la position du joueur déclenche un évènement particulier, une description, un combat, ...
def is_it_in_the_list(position,list):
    if list == [] :
        return False
    i = 0
    while i < len(list):
        if position == list[i]:
            return True
        else:
            i = i + 1
    return False

cases_montagne = [[0,8],[1,7],[1,8],[2,6],[2,7],[2,10],[2,16],[3,5],[3,6],[3,8],[3,10],[3,11],[3,16],[3,17],[4,4],[4,5],[4,8],[4,11],[4,17],[5,4],[5,6],[5,7],[5,8],[5,11],[5,12],[5,13],[5,14],[5,15],[5,16],[5,17],[6,4],[6,6],[6,16],[7,1],[7,2],[7,3],[7,4],[7,6],[7,9],[7,10],[7,16],[7,17],[7,18],[7,19],[8,4],[8,5],[8,6],[8,7],[8,8],[8,9],[8,16],[8,19]]
cases_montagne_ennemis = [[2,16],[5,8],[7,4],[7,9],[7,17]]
cases_montagne_objets = [[2,10],[3,8],[7,1],[7,10],[8,19]]
montagne_boss = [0,8]                       #Zeus

cases_foret = [[9,0],[9,1],[9,2],[9,6],[9,10],[9,11],[9,14],[9,15],[9,16],[9,17],[9,18],[10,0],[10,1],[10,2],[10,3],[10,4],[10,5],[10,6],[10,7],[10,8],[10,9],[10,10],[10,11],[10,12],[10,14],[10,15],[10,16],[10,17],[10,18],[10,19],[11,3],[11,4],[11,5],[11,6],[11,7],[11,8],[11,9],[11,10],[11,11],[11,12],[11,14],[11,15],[11,16],[11,17],[11,18],[11,19],[12,3],[12,4],[12,5],[12,6],[12,7],[12,8],[12,9],[12,10],[12,11],[12,12],[12,15],[12,16],[12,17],[12,18],[12,19],[13,6],[13,7],[13,8],[13,9],[13,10],[13,11],[13,12],[13,13],[13,15],[13,16],[13,17],[13,18],[13,19],[14,7],[14,8],[14,9],[14,10],[14,11],[14,12],[15,7],[15,8],[15,9],[15,10],[15,11],[16,7],[16,8],[16,9],[16,10],[17,6],[17,7],[17,8],[17,9],[18,7],[18,8]]
foret_sombre = [[9,0],[9,1],[9,2],[9,6],[9,10],[9,11],[10,0],[10,1],[10,2],[10,3],[10,4],[10,5],[10,6],[10,7],[10,8],[10,9],[10,10],[10,11],[10,12],[11,3],[11,4],[11,5],[11,6],[11,7],[11,8],[11,9],[11,10],[11,11],[11,12],[12,3],[12,4],[12,5],[12,6],[12,7],[12,8],[12,9],[12,10],[12,11],[12,12],[13,6],[13,7],[13,8],[13,9],[13,10],[13,11],[13,12],[13,13],[14,7],[14,8],[14,9],[14,10],[14,11],[14,12],[15,7],[15,8],[15,9],[15,10],[15,11],[16,7],[16,8],[16,9],[16,10],[17,6],[17,7],[17,8],[17,9],[18,7],[18,8]]
foret_lumineuse = [[9,14],[9,15],[9,16],[9,17],[9,18],[10,14],[10,15],[10,16],[10,17],[10,18],[10,19],[11,14],[11,15],[11,16],[11,17],[11,18],[11,19],[12,15],[12,16],[12,17],[12,18],[12,19],[13,15],[13,16],[13,17],[13,18],[13,19]]

cases_riviere_ocean = [[1,9],[2,9],[3,9],[4,9],[4,10],[5,10],[6,10],[6,11],[7,11],[7,12],[8,12],[9,12],[9,13],[10,13],[11,13],[12,13],[12,14],[13,14],[14,14],[15,14],[15,14],[15,15],[15,16],[15,17],[15,18],[15,19],[16,12],[16,13],[16,19],[17,13],[17,15],[17,16],[17,17],[17,19],[18,10],[18,11],[18,12],[18,13],[18,14],[18,15],[18,17],[18,19],[19,12],[19,19],[20,9],[20,10],[20,11],[20,12],[20,13],[20,14],[20,15],[20,16],[20,17],[20,18],[20,19]]
pont = [11,13]
cases_riviere_ocean_ennemis = [[15,18],[17,13],[18,10],[20,11]]
cases_riviere_ocean_objets = [[16,12],[20,9]]
riviere_ocean_boss = [18,17]                #Poséidon

cases_enfer = [[11,1],[12,1],[13,0],[13,1],[13,2],[14,0],[14,2],[14,3],[14,4],[14,5],[15,0],[15,3],[15,5],[16,0],[16,2],[16,5],[17,0],[17,2],[17,4],[18,0],[18,1],[18,2],[18,3],[18,4],[19,0],[19,4],[19,6],[20,0],[20,2],[20,3],[20,4],[20,5],[20,6]]
cases_enfer_ennemis = [[13,1],[15,3],[20,0]]
cases_enfer_objets = [[16,5],[19,6]]        #Hadès
enfer_boss = [20,2]

Rive_ouest_riviere = [[1,8], [3,8], [4,8], [7,10], [9,11], [10,12], [12,12]]
Rive_est_riviere = [[2,10], [3,10], [4,11], [5,11], [9,14], [10,14], [12,15]]
Riviere = [[1,9],[2,9],[3,9],[4,9],[4,10],[5,10],[6,10],[6,11],[7,11],[7,12],[8,12],[9,12],[9,13],[10,13],[12,13],[12,14]]
Embouchure_ouest = [13,13]          #parce que les embouchures seront les seuls accès à la rivière, même une fois qu'on aura la barque.
Embouchure_est = [13,15]

def map(player_position):
    carte_joueur = []
    carte_reference = []
    i = 0
    while i < 21 :
        carte_joueur.append("")
        carte_reference.append([])
        j = 0
        while j < 20 :
            if player_position == [i,j]:
                carte_joueur[i] = carte_joueur[i] + " X"
                carte_reference[i].append("J")
            elif is_it_in_the_list([i,j],cases_foret):
                carte_joueur[i] = carte_joueur[i] + " ^"
                carte_reference[i].append("F")
            elif is_it_in_the_list([i,j],cases_montagne):
                carte_joueur[i] = carte_joueur[i] + " ."
                carte_reference[i].append("M")
            elif is_it_in_the_list([i,j],cases_riviere_ocean):
                carte_joueur[i] = carte_joueur[i] + " ~"
                carte_reference[i].append("R")
            elif is_it_in_the_list([i,j],cases_enfer):
                carte_joueur[i] = carte_joueur[i] + " _"
                carte_reference[i].append("E")
            else :
                carte_joueur[i] = carte_joueur[i] + "  "
                carte_reference[i].append("V")          #vide
            j = j + 1
        i = i + 1
    return (carte_joueur,carte_reference)
    

def show_map(player_position):
    (carte_a_afficher,autre_carte) = map(player_position)       #on n'utilise pas la 2e carte que renvoit map
    print("Légende : \n. : montagne \n^ : forêt \n_ : souterrain \n~ : eau \nX : votre position")
    print("Les zones noires ne sont pas accessibles.")
    print("________________________________________")
    i = 0
    while i < len(carte_a_afficher) :
        print("|" + carte_a_afficher[i] + "|")
        i = i + 1
    print("|________________________________________|")
    return "done"





def Move(position_joueur,inventaire):
    (carte_joueur,carte_de_reference) = map(position_joueur)    #on n'utilise pas la 1e carte que renvoit map
    ligne_j = int(position_joueur[0])
    colonne_j = int(position_joueur[1])
    directions_possibles = ["N","S","E","O"]
    i = 0
    if ligne_j == 0 or (ligne_j > 0 and carte_de_reference[ligne_j - 1][colonne_j] == "V") :
        del directions_possibles[i]                 #Le nord est bloqué.
    elif position_joueur == [1,8] and not is_it_in_the_list("Clé de l'Olympe",inventaire) : #On ne peut pas aller voir Zeus sans la clé.
        del directions_possibles[i]                 #Le nord est bloqué.
    elif position_joueur == [13,14] or position_joueur == [11,13] :                 #On ne peut pas remonter la rivière, ni se jeter à l'eau depuis le pont.
        del directions_possibles[i]                 #Le nord est bloqué.
    elif ligne_j > 0 and is_it_in_the_list([ligne_j - 1, colonne_j],Riviere) :      #On ne peut pas se jeter à l'eau vers le nord quand on est à un coude de la rivière.
        del directions_possibles[i]                 #Le nord est bloqué.
    else :
        i = i + 1
    if ligne_j == 20 or (ligne_j < 20 and carte_de_reference[ligne_j + 1][colonne_j] == "V") :
        del directions_possibles[i]                 #Le sud est bloqué.
    elif position_joueur == [11,13] :               #On ne peut pas se jeter à l'eau depuis le pont.
        del directions_possibles[i]                 #Le sud est bloqué.
    elif ligne_j < 20 and is_it_in_the_list([ligne_j + 1, colonne_j],Riviere) :      #On ne peut pas se jeter à l'eau vers le sud quand on est à un coude de la rivière.
        del directions_possibles[i]                 #Le sud est bloqué.
    else :
        i = i + 1
    if colonne_j == 19 or (colonne_j < 19 and carte_de_reference[ligne_j][colonne_j + 1] == "V") :
        del directions_possibles[i]                 #L'est est bloqué.
    elif position_joueur == Embouchure_ouest and not is_it_in_the_list("Barque de Charon",inventaire) : #On ne peut pas aller sur la rivière sans la barque.
        del directions_possibles[i]                 #L'Est est bloqué.
    elif is_it_in_the_list(position_joueur,Rive_ouest_riviere) :
        del directions_possibles[i]                 #L'est est bloqué.
    else :
        i = i + 1
    if colonne_j == 0 or (colonne_j > 0 and carte_de_reference[ligne_j][colonne_j - 1] == "V") :
        del directions_possibles[i]                 #L'Ouest est bloqué.
    elif position_joueur == Embouchure_est and not is_it_in_the_list("Barque de Charon",inventaire) : #On ne peut pas aller sur la rivière sans la barque.
        del directions_possibles[i]                 #L'Ouest est bloqué.
    elif is_it_in_the_list(position_joueur,Rive_est_riviere) :
        del directions_possibles[i]                 #L'ouest est bloqué.
    
    print("Où voulez-vous aller ? Les directions suivantes sont disponibles :",directions_possibles,"(N : nord, S : sud, E : est, O : ouest)")
    direction_choisie = input()
    direction_choisie = direction_choisie.upper()
    while not is_it_in_the_list(direction_choisie,directions_possibles) :
        print("Il est impossible d'aller dans cette direction.")
        print("Où voulez-vous aller ? Les directions suivantes sont disponibles :",directions_possibles,"(N : nord, S : sud, E : est, O : ouest)")
        direction_choisie = input()
        direction_choisie = direction_choisie.upper()
    if direction_choisie == "N" :
        ligne_j = ligne_j - 1
    elif direction_choisie == "S" :
        ligne_j = ligne_j + 1
    elif direction_choisie == "E" :
        colonne_j = colonne_j + 1
    elif direction_choisie == "O" :
        colonne_j = colonne_j - 1
    return [ligne_j,colonne_j]




import time

def description_case(position_du_joueur,position_precedente):
    if position_du_joueur == [11,12] and position_precedente != [11,13] :
        print("Un pont de bois permet de traverser la gorge vers l'Est. Il a l'air solide.")
        time.sleep(2)
    elif position_du_joueur == [11,14] and position_precedente != [11,13] :
        print("Un pont de bois permet de traverser la gorge vers l'Ouest. Il a l'air solide.")
        time.sleep(2)
    elif is_it_in_the_list(position_du_joueur,Rive_ouest_riviere) and position_du_joueur[0] > 8 :   #La 2e condition évite d'afficher ces messages dans la montagne, car ils s'affichaient plusieurs fois, ce qui était désagréable.
        if is_it_in_the_list(position_precedente,Rive_ouest_riviere) :
            print("Vous longez la rive Ouest de la rivière. La gorge est trop profonde pour traverser.")
            time.sleep(3)
        else :
            print("Vous vous trouvez au bord d'une gorge au fond de laquelle coule une rivière. Elle vous coupe la route à l'Est tandis que l'eau s'écoule tranquillement vers le sud en scintillant sous le soleil. La forêt sur l'autre rive est plus lumineuse que celle où vous vous trouvez.")
            time.sleep(5)
    elif is_it_in_the_list(position_du_joueur,Rive_est_riviere) and position_du_joueur[0] > 8 :     #La 2e condition évite d'afficher ces messages dans la montagne, car ils s'affichaient plusieurs fois, ce qui était désagréable.
        if is_it_in_the_list(position_precedente,Rive_est_riviere) :
            print("Vous longez la rive Est de la rivière. La gorge est trop profonde pour traverser.")
            time.sleep(5)
        else :
            print("Vous vous trouvez au bord d'une gorge au fond de laquelle coule une rivière. Elle vous coupe la route à l'Ouest tandis que l'eau s'écoule tranquillement vers le sud en scintillant sous le soleil. La forêt sur l'autre rive est plus sombre que celle où vous vous trouvez.")
            time.sleep(5)
    #jonction montagne ouest // forêt sombre
    elif position_du_joueur == [8,6] :
        if position_precedente == [9,6] :
            print("Vous vous engagez sur le chemin rocailleux de la plus haute montagne. L'ascension promet d'être longue.")
            time.sleep(3)
        else :
            print("Vous êtes arrivés au pied de la montagne. Devant vous s'étend une forêt lugubre. Aucun sentier ne se dessine entre les arbres immenses.")
            time.sleep(5)
    elif position_du_joueur == [9,6] :
        if position_precedente == [8,6] :
            print("Vous vous engagez dans la pénombre inquiétante de la forêt. La végétation dense ne vous permet pas de voir très loin. Le danger peut être partout dorénavant.")
            time.sleep(5)
        else :
            print("Le sentier s'éclaire devant vous. Vous êtes arrivé en bordure de la forêt. Devant vous, au Nord, commencent les contreforts de montagnes imposantes, qui dressent leurs sommets déchiquetés vers le ciel.")
            time.sleep(5)
    #jonction montagne est // forêt lumineuse
    elif position_du_joueur == [8,16] :
        if position_precedente == [9,16] :
            print("Vous entamez l'ascension de la montagne la plus proche par un chemin bordé de fleurs qui s'élève en pente douce vers le sommet.")
            time.sleep(4)
        else :
            print("Vous êtes de retour au pied de la montagne. Devant vous s'étend une forêt luxuriante, parcourue de nombreux sentiers et baignée d'une douce lumière.")
            time.sleep(5)
    elif position_du_joueur == [9,16] :
        if position_precedente == [8,16] :
            print("Vous vous engagez sous les frondaisons. L'air frais embaume et vous voyez des écureuils bondir dans les arbres au milieu des chants d'oiseaux.\nCependant, vous restez sur vos gardes : qui sait quels monstres peuvent se cacher dans la végétation luxuriante ?")
            time.sleep(5)
        else :
            print("Vous parvenez à la lisière de la forêt. De majestueuses montagnes s'élèvent devant vous, au Nord.")
            time.sleep(3)
    elif position_du_joueur == [10,1] :
        if position_precedente == [11,1] :
            print("Vous vous engagez dans la pénombre inquiétante de la forêt. La végétation dense ne vous permet pas de voir très loin. Le danger peut être partout dorénavant.")
            time.sleep(5)
        else :
            print("L'entrée d'une grotte se dessine soudain derrière les arbres. Elle provoque chez vous une sensation de profond malaise qui ne permet aucun doute. Ce n'est pas une simple grotte. C'est l'entrée du royaume des Enfers.")
            time.sleep(5)
    elif position_du_joueur == [11,1] :
        if position_precedente == [10,1] :
            print("Vous pénétrez dans la grotte. Le passage est d'abord étroit et vous n'y voyez rien mais il s'élargit rapidement et s'éclaire peu à peu de mousses bioluminescentes, diffusant une étrange lueur verdâtre.\nBien qu'elles accentuent encore votre sensation de malaise, elles vous permettent au moins de voir à quelques pas.")
            time.sleep(5)
        else :
            print("Vous quittez enfin les enfers, mais votre soulagement est de courte durée. Devant vous s'étend une forêt lugubre. Aucun sentier ne se dessine entre les arbres immenses.")
            time.sleep(5)
    elif position_du_joueur == [13,14] :
        if position_precedente == [14,14] :
            print("Vous laissez derrière vous le royaume de Poséidon et retrouvez les eaux paisibles de la rivière.\nLes rives s'élèvent rapidement et la rivière s'enfonce dans une gorge. Vous devez regagner la terre ferme maintenant.\nDeux forêts encadrent le cours d'eau. Celle à l'Est est aérée et pleine de vie. Celle à l'Ouest est dense et ténébreuse.")
            time.sleep(5)
        else :
            print("Vous mettez votre barque à l'eau à l'embouchure du fleuve. Au Sud, la mer semble s'étendre à l'infini, miroitant sous le soleil.")
            time.sleep(4)
    elif position_du_joueur == [14,14] :
        if position_precedente == [13,14] :
            print("À l'instant où vous prenez le large, le vent se lève, les vagues se font plus violentes, et de lourds nuages noirs s'amoncellent à l'horizon.\nLe message est clair : Poséidon sait que vous êtes là, et vous n'êtes pas le bienvenu en son royaume.")
            time.sleep(5)
        else :
            print("Alors que vous commenciez à désespérer de quitter un jour la mer déchaînée, les vagues s'apaisent et vous apercevez enfin au Nord la côte et l'embouchure de la rivière.")
            time.sleep(5)
    return "description finie"





from random import randint
def evenement_case(case,liste):         #liste dans RPG.py, où on a stocké les cases des combats, pour ne pas se battre deux fois sur la même case
    if is_it_in_the_list(case,liste):
        if is_it_in_the_list(case,cases_enfer_ennemis):
            print("\nDes bruits étranges résonnent dans le tunnel. Vous vous arrêtez pour tendre l'oreille. Le son se précise et se rapproche.\nVous regardez fébrilement autour de vous à la recherche d'une cachette, mais il n'y en a aucune. Trop tard : l'ennemi est là.")
            action = "combat"
        elif is_it_in_the_list(case,cases_riviere_ocean_ennemis):
            print("\nLa tempête fait rage. Vous faites de votre mieux pour maintenir le cap, conscient qu'une barque ordinaire aurait déjà chaviré depuis longtemps.\nSoudain, un frisson vous parcourt l'échine. Il vous a semblé entendre un rugissement qui n'était pas celui du vent. Alors que vous pensez l'avoir imaginé, vous atteignez la crête d'une vague, et votre ennemi apparaît.")
            action = "combat"
        elif is_it_in_the_list(case,cases_montagne_ennemis):
            print("\nVous vous accroupissez derrière un rocher, aux aguets. Des pierres ont bougé à quelques pas de là, vous en êtes sûr.\nTrop tard : vous avez dû être repéré car le bruit se rapproche. Vous vous relevez, prêt à faire face. Le combat est à présent inévitable.")
            action = "combat"
        elif case == enfer_boss :
            print("\nSur le sol et les murs, la pierre brute a laissé la place à du marbre noir veiné d'argent.\nLe passage s'élargit pour devenir une salle immense, dont les murs répercutent le bruit de vos pas en échos inquiétants. Les ombres semblent gagner du terrain. Devant vous, où il n'y avait rien un instant auparavant, se dessine à présent un trône de marbre noir plus haut que trois hommes. Le trône semble vide mais votre instinct vous dit qu'il n'en est rien. En son centre, l'obscurité semble se solidifier.")
            action = "combat"
        elif case == riviere_ocean_boss :
            print("\nLe vent s'arrête brusquement, les vagues se calment, la mer devient d'huile, mais pas un rayon de soleil ne perce les nuages.\nLe silence se fait oppressant. À quelques mètres à peine de votre embarcation, la mer se met à bouillonner. Une silhouette se forme au centre du phénomène : une ombre immense, armée d'un trident de bronze.")
            action = "combat"
    else :
        if is_it_in_the_list(case,cases_riviere_ocean_objets):
            print("\nAu milieu de la tempête, une vague énorme s'abat sur votre esquif. Lorsqu'elle se retire, vous découvrez un objet au fond de la coque.")
            action = "objet"
        elif is_it_in_the_list(case,cases_enfer_objets):
            print("\nLes tunnels se ressemblent tous, les mêmes moussent verdâtres, quelques cristaux colorés, parfois un trou dans un mur laisse entrevoir un filet de lave.\nMais quelque chose attire votre attention : quelque chose brille dans une anfractuosité de la roche.")
            action = "objet"
        elif is_it_in_the_list(case,cases_montagne_objets):
            print("\nLes graviers qui couvrent le chemin roulent sous vos pieds, rendant l'ascension encore plus pénible sous le soleil qui vous assome.\nLe sommet vous paraît encore tellement loin. Vous marchez sur quelque chose qui roule et vous tombez brutalement. Vous regardez de plus près de quoi il s'agit car, cette fois, ce n'était pas un gravier.")
            action = "objet"
        elif is_it_in_the_list(case,foret_sombre):
            hasard = randint(1,100)
            if hasard > 90 :
                print("\nLe soleil s'apprête à disparaître derrière les arbres, plongeant encore un peu plus la forêt dans la pénombre.\nTous vos nerfs sont à vifs, et les corbeaux de plus en plus nombreux dans les arbres environnants n'arrangent rien. Soudain, tous s'envolent en même temps. Un instant plus tard, une ombre se dessine entre les troncs distordus.")
                action = "combat"
            elif hasard > 80 :
                print("\nLe jour se lève. Vous avez passé la nuit roulé en boule entre les racines d'un arbre mort.\nVous êtes fatigué et pensez ne jamais sortir de cette forêt. Mais vous reprenez un peu espoir en levant les yeux : le petit jour éclaire un objet dans un arbre creux en face de vous.")
                action = "objet"
            else :
                action = "rien"
        elif is_it_in_the_list(case,foret_lumineuse):
            hasard = randint(1,100)
            if hasard > 90 :
                print("\nDepuis un moment, vous vous sentez comme un intrus au milieu de cette beauté luxuriante.\nVous écartez une liane qui pend en travers du passage et, brusquement, vous vous figez. Vous avez compris la source de votre malaise : la forêt s'est tue. Alors même que vous réalisez ce que cela signifie, un bruit vous fait vous retourner.")
                action = "combat"
            elif hasard > 80 :
                print("\nLe soleil est bas sur l'horizon lorsque vous trouvez enfin une clairière où passer la nuit.\nLa forêt vous a fourni tout ce dont vous pouviez avoir besoin : de l'eau, de la nourriture, et toutes les herbes médicinales nécessaires à la préparation d'un remède, ou peut-être même d'un nectar.")
                action = "objet"
            else :
                action = "rien"
        elif case == montagne_boss :
            print("\nUn brouillard épais s'est installé et vous ne voyez pas à plus de quelques pas devant vous.\nIl se dissipe peu à peu, révélant une allée de marbre blanc bordée de colonnes. Le ciel au-dessus de vous est chargé de lourds nuages noirs. Vous vous avancez entre les colonnes. Venu de nulle part, un éclair frappe le sol quelques mètres plus loin, éclatant le marbre et soulevant un nuage de fumée. Le coup de tonnerre est si puissant qu'il vous sonne et vous fait chuter à quatre pattes sur le sol. Alors que vous vous relevez avec difficulté, le maître des lieux émerge du nuage de poussière.")
            action = "combat"
        else :
            action = "rien"
    return action





def ennemi_case(case):      #je renvoie l'indice de l'ennemi dans liste_ennemies (Ennemies.py)
    if case == riviere_ocean_boss :
        return 18   #"Poséidon"
    elif case == enfer_boss :
        return 17   #"Hadès"
    elif case == montagne_boss :
        return 19   #"Zeus"
    elif case == [7,4] :
        return 14   #"Arès"
    elif case == [15,18] :
        return 15   #"Dyonisos"
    elif case == [13,1] :
        return 16   #"Perséphone"
    elif is_it_in_the_list(case,[[2,16],[5,8],[7,9],[7,17]]) :      #aléatoire montagne
        monstre_hasard = randint(1,4)
        if monstre_hasard == 1 :
            return 0    #"Harpie"
        elif monstre_hasard == 2 :
            return 1    #"Cyclope"
        elif monstre_hasard == 3 :
            return 5    #"Gryffon"
        else :
            return 13   #"Apollon"
    elif is_it_in_the_list(case,[[15,3],[20,0]]) :      #aléatoire enfers
        monstre_hasard = randint(1,2)
        if monstre_hasard == 1 :
            return 3    #"Cerbère"
        else :
            return 7    #"Sphinx"    
    elif is_it_in_the_list(case,[[17,13],[18,10],[20,11]]) :      #aléatoire océans
        monstre_hasard = randint(1,4)
        if monstre_hasard == 1 :
            return 4    #"Lamia"
        elif monstre_hasard == 2 :
            return 11   #"Aphrodite"
        else :
            return 6    #"Sirènes"                #1 chance sur 2
    elif is_it_in_the_list(case,foret_sombre) or is_it_in_the_list(case,foret_lumineuse) :
        monstre_hasard = randint(1,18)
        if monstre_hasard <= 2 :
            return 2    #"Minotaure"
        elif monstre_hasard <= 4 :
            return 8    #"Lion de Némée"
        elif monstre_hasard <= 6 :
            return 9    #"Méduse"
        elif monstre_hasard <= 8 :
            return 12   #"Artémis"
        elif monstre_hasard <= 10 :
            return 10   #"Athéna"
        elif monstre_hasard == 11 :
            return 0    #"Harpie"
        elif monstre_hasard == 12 :
            return 1    #"Cyclope"
        elif monstre_hasard == 13 :
            return 5    #"Griffon"
        elif monstre_hasard == 14 :
            return 13   #"Apollon"
        elif monstre_hasard == 15 :
            return 3    #"Cerbère"
        elif monstre_hasard == 16 :
            return 7    #"Sphinx"
        elif monstre_hasard == 17 :
            return 4    #"Lamia"
        elif monstre_hasard == 18 :
            return 11   #"Aphrodite"
        