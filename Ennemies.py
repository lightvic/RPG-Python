#Pour tester le jeu, c'est RPG.py qu'il faut lancer.


from random import randint
def Harpie():
    #lieu : montagne : aléatoire parmi [[2,16],[5,8],[7,9],[7,17]] + forêt
    Nom = "Harpie" 
    Niveau = 1
    Points_de_vie = 1000
    Points_attaque = 150
    Points_defense = 50
    Points_XP = 50

    Small_attack = Points_attaque
    Nom_small_attack = "Bourrasque"
    Big_attack = Points_attaque + 100
    Nom_Big_attack = "Serres acérées"
    esq = 2

    Description_debut = "\nEn quelques battements d'ailes, elle est devant vous. Les serres de la harpie raclent la pierre alors qu'elle se pose sur le rocher près de vous. Elle ne replie ses ailes qu'à demi et vous fixe de son regard perçant, prête à l'attaque.\n"
    Description_victoire = "\nLa harpie explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nLa harpie transperce votre chair jusqu'à vous déchiqueter et vous mettre en pièce.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Cyclope():
    #lieu : montagne : aléatoire parmi [[2,16],[5,8],[7,9],[7,17]] + forêt
    Nom = "Cyclope" 
    Niveau = 1
    Points_de_vie = 2000
    Points_attaque = 80
    Points_defense = 150
    Points_XP = 50
    esq = 2

    Small_attack = Points_attaque
    Nom_small_attack = "Écrasement"
    Big_attack = Points_attaque + 200
    Nom_Big_attack = "Chaudron"

    Description_debut = "\nD'un pas lourd, le cyclope s'avance en détruisant tout sur son passage, ne laissant derrière lui que le chaos et la destruction.\n"
    Description_victoire = "\nLe cyclope hurle et explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nLe cyclope vous arrache la tête, vous éventre de ses dents pointues et vous dévore.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Minotaure():
    #lieu : forêt
    Nom = "Minotaure" 
    Niveau = 1
    Points_de_vie = 1500
    Points_attaque = 30
    Points_defense = 100
    Points_XP = 50
    esq = 2

    Small_attack = Points_attaque
    Nom_small_attack = "Plaquage"
    Big_attack = Points_attaque + 420
    Nom_Big_attack = "Coup de corne"

    Description_debut = "\nUn corps d'homme surmonté d'une hideuse tête de taureau : le minotaure apparait entre les arbres et abaisse la tête, cornes en avant, prêt à charger.\n"
    Description_victoire = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nLe minotaure ne vous laisse aucune chance de survie : il vous a chargé et vous a empallé sur ses cornes.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Cerbere(): 
    #lieu : enfers : aléatoire parmi [[15,3],[20,0]] + forêt
    Nom = "Cerbère" 
    Niveau = 2
    Points_de_vie = 2500
    Points_attaque = 350
    Points_defense = 150
    Points_XP = 50
    esq = 2

    Small_attack = Points_attaque
    Nom_small_attack = "Combo griffes"
    Big_attack = Points_attaque + 150
    Nom_Big_attack = "Morsure"

    Description_debut = "\nUn grondement sourd se fait entendre un instant avant que vous ne distinguiez le monstre. C'est un cerbère : un chien énorme, haut comme au moins trois hommes, et pourvu de trois têtes qui vous regardent toutes en salivant.\n"
    Description_victoire = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nLe cerbère se jette sur vous et vous achève d'un coup de griffes avant que ses trois têtes se disputent pour vous dévorer.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Lamia():
    #lieu : océan : aléatoire parmi [[17,13],[18,10],[20,11]] + forêt
    Nom = "Lamia"
    Niveau = 2
    Points_de_vie = 2300
    Points_attaque = 370
    Points_defense = 120
    Points_XP = 50
    esq = 2

    Small_attack = Points_attaque
    Nom_small_attack = "Coup de natte"
    Big_attack = Points_attaque + 175
    Nom_Big_attack = "Morsure venimeuse"

    Description_debut = "\nLa lamia s'approche en faisant onduler son corps de serpent. Elle a un visage magnifique mais, lorsqu'elle sourit, elle dévoile ses longs crocs venimeux.\n"
    Description_victoire = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nLa créature s'approche tout doucement de vous et plante profondément ses crocs dans votre chair, son venin agit instantanément. Vous êtes paralysé mais toujours conscient. Votre agonie ne fait que commencer.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Griffon():
    #lieu : montagne : aléatoire parmi [[2,16],[5,8],[7,9],[7,17]] + forêt
    Nom = "Griffon" 
    Niveau = 3
    Points_de_vie = 5000
    Points_attaque = 450
    Points_defense = 300
    Points_XP = 50
    esq = 2

    Small_attack = Points_attaque
    Nom_small_attack = "Lacération"
    Big_attack = Points_attaque + 90
    Nom_Big_attack = "Serre d'aigle"

    Description_debut = "\nMi-rapace, mi-lion, le griffon vous fait face. Il se dresse sur ses pattes arrières en battant des ailes et pousse un cri strident avant de se jeter sur vous.\n"
    Description_victoire = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nLe griffon vous attaque de ses serres acérées et vous tue sur le coup.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Sirenes(): 
    #lieu : océan : aléatoire parmi [[17,13],[18,10],[20,11]]
    Nom = "Sirènes" 
    Niveau = 2
    Points_de_vie = 3000
    Points_attaque = 200
    Points_defense = 60
    Points_XP = 50
    esq = 2

    Small_attack = Points_attaque
    Nom_small_attack = "Chant ensorcelant"
    Big_attack = Points_attaque + 250
    Nom_Big_attack = "Eviscération"

    Description_debut = "\nPar quelque étrange sortilège, le chant des sirènes est parfaitement audible malgré le bruit de la tempête, et menace de vous faire perdre de vue la réalité. Vous devez à tout prix rester lucide si vous tenez à la vie.\n"
    Description_victoire = "\nLes sirènes explosent en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nUn instant d'inattention a suffit à sceller votre sort. Vous vous êtes laissé envoûter et les sirènes en ont profité pour vous déchiqueter.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Sphinx():
    #lieu : enfers : aléatoire parmi [[15,3],[20,0]] + forêt
    Nom = "Sphinx" 
    Niveau = 1
    Points_de_vie = 1300
    Points_attaque = 75
    Points_defense = 100
    Points_XP = 50
    esq = 2

    Small_attack = Points_attaque
    Nom_small_attack = "Griffures"
    Big_attack = Points_attaque + 375
    Nom_Big_attack = "Enigme mortelle"

    Description_debut = "\nCorps de lion, ailes d'oiseau et tête de femme, le sphinx vous fait face. Il se dresse sur ses pattes arrières en battant des ailes et pousse un hurlement de rage avant de se jeter sur vous.\n"
    Description_victoire = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nVotre destin a été décidé lorsque vous n'avez pas su répondre à l'énigme du sphinx. Vous tombez sous les coups de griffes de ses énormes pattes de lion.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Lion_de_Nemee():
    #lieu : forêt
    Nom = "Lion de Némée" 
    Niveau = 1
    Points_de_vie = 1000
    Points_attaque = 100
    Points_defense = 100
    Points_XP = 50
    esq = 2

    Small_attack = Points_attaque
    Nom_small_attack = "Peau d'acier"
    Big_attack = Points_attaque + 100
    Nom_Big_attack = "Déchiquetage"

    Description_debut = "\nUn lion d'or émerge d'entre les arbres : le lion de Némée. Rien ne peut transpercer sa peau et ses griffes sont plus acérées que n’importe quel glaive. Il se tapit près du sol, prêt à l'attaque.\n"
    Description_victoire = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nLe lion de Némée parvient à vous plaquer au sol et vous déchiquette.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Meduse():
    #lieu : forêt
    Nom = "Méduse" 
    Niveau = 3
    Points_de_vie = 4000
    Points_attaque = 500
    Points_defense = 200
    Points_XP = 50
    esq = 2

    Small_attack = Points_attaque
    Nom_small_attack = "Morsure de serpent"
    Big_attack = Points_attaque + 1000
    Nom_Big_attack = "Pétrification"

    Description_debut = "\nUne femme s'avance entre les arbres. Vous ne distinguez pas encore ses traits mais sa chevelure semble s'agiter malgré l'absence de vent et un étrange sifflement se fait entendre. Lorsque vous comprenez que sa chevelure est faite de serpents, vous détournez au plus vite la tête. Vous ne devez en aucun cas croiser le regard de Méduse.\n"
    Description_victoire = "\nMéduse hurle et explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nVous avez eu le malheur d'ouvrir les yeux. Vous sentez votre corps se changer en pierre. Déjà vous ne pouvez plus lever le bras qui tient votre épée. Méduse s'approche en riant. Son rire sadique vous poursuivra jusque dans la mort.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Deesse_Athena():
    #lieu : forêt
    Nom = "Athéna" 
    Niveau = 5
    Points_de_vie = 10000
    Points_attaque = 500
    Points_defense = 3000
    Points_XP = 50
    esq = 4

    Small_attack = Points_attaque
    Nom_small_attack = "Coup de bouquin"
    Big_attack = Points_attaque + 1500
    Nom_Big_attack = "Illumination"

    Description_debut = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais une déesse : Athéna, déesse de la guerre et de la sagesse.\n"
    Description_victoire = "\nLa déesse pousse un hurlement de rage. Elle émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, elle a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nVous n'avez rien vu venir. Athéna a eu raison de vous à l'instant même où vous pensiez que la victoire était assurée.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Deesse_Aphrodite():
    #lieu : océan : aléatoire parmi [[17,13],[18,10],[20,11]] + forêt
    Nom = "Aphrodite" 
    Niveau = 4
    Points_de_vie = 8000
    Points_attaque = 500
    Points_defense = 2500
    Points_XP = 50
    esq = 4

    Small_attack = Points_attaque
    Nom_small_attack = "Beauté fatale"
    Big_attack = Points_attaque + 1000
    Nom_Big_attack = "Tromperie"

    Description_debut = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais une déesse : Aphrodite, déesse de la beauté.\n"
    Description_victoire = "\nLa déesse pousse un hurlement de rage. Elle émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, elle a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nAphrodite vous a eu lâchement, mais, dans votre agonie, vous réalisez amèrement que l'honneur n'est d'aucun secours dans la mort.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]

def Deesse_Artemis():
    #lieu : forêt
    Nom = "Artémis" 
    Niveau = 6
    Points_de_vie = 10000
    Points_attaque = 1100
    Points_defense = 4000
    Points_XP = 100
    esq = 4

    Small_attack = Points_attaque
    Nom_small_attack = "Tir critique"
    Big_attack = Points_attaque + 3000
    Nom_Big_attack = "Un tir, un mort"

    Description_debut = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais une déesse : Artémis, déesse de la chasse.\n"
    Description_victoire = "\nLa déesse pousse un hurlement de rage. Elle émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, elle a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nLa forêt est son territoire. Vous n'aviez aucune chance. Artémis s'est fondue parmi les arbres avant de vous abattre d'une flèche.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Dieu_Apollon():
    #lieu : montagne : aléatoire parmi [[2,16],[5,8],[7,9],[7,17]] + forêt
    Nom = "Apollon" 
    Niveau = 6
    Points_de_vie = 15000
    Points_attaque = 650
    Points_defense = 5000
    Points_XP = 100
    esq = 4

    Small_attack = Points_attaque
    Nom_small_attack = "Cacophonie"
    Big_attack = Points_attaque + 1750
    Nom_Big_attack = "Eclipse"

    Description_debut = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais un dieu : Apollon, dieu du soleil et de la musique.\n"
    Description_victoire = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nVous avez oublié qu'Apollon était aussi dieu de la guérison. Ses blessures disparaissaient en quelques instant, tandis que les vôtres ne faisaient que se multiplier. Vous n'aviez aucune chance de sortir vivant de ce combat.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Dieu_Ares():
    #lieu : montagne : [7,4]
    Nom = "Arès" 
    Niveau = 8
    Points_de_vie = 35000
    Points_attaque = 2000
    Points_defense = 99999
    Points_XP = 100
    esq = 4

    Small_attack = Points_attaque
    Nom_small_attack = "Coup d'estoc"
    Big_attack = Points_attaque + 1000
    Nom_Big_attack = "Berserk"

    Description_debut = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais un dieu : Arès, dieu de la guerre.\n"
    Description_victoire = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nPenser vaincre le dieu de la guerre au combat était pure folie. Vous aurez l'éternité pour vous en repentir.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Dieu_Dionysos():
    #lieu : océan : [15,18]
    Nom = "Dionysos" 
    Niveau = 1
    Points_de_vie = 25000
    Points_attaque = 10
    Points_defense = 500
    Points_XP = 100
    esq = 4

    Small_attack = Points_attaque
    Nom_small_attack = "Enserrement de vigne"
    Big_attack = Points_attaque + 40
    Nom_Big_attack = "Supplice du tonneau"

    Description_debut = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais un dieu : Dyonisos, dieu du vin et de la folie.\n"
    Description_victoire = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nVous ne savez plus où vous êtes. La folie de Dyonisos a dû déteindre sur vous. Oui, vous devez être fou, ou vous ne verriez pas des nageoires à la place de vos bras. Avant de perdre définitivement toute pensée rationnelle, vous réalisez que le dieu ne vous a pas tué mais changé en dauphin. Et quelque part, au fond de vous, vous le remerciez de sa clémence.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Deesse_Persephone():
    #lieu : enfers : [13,1]
    Nom = "Perséphone" 
    Niveau = 2
    Points_de_vie = 4783
    Points_attaque = 250
    Points_defense = 1000
    Points_XP = 50
    esq = 4

    Small_attack = Points_attaque
    Nom_small_attack = "Allergies"
    Big_attack = Points_attaque + 100
    Nom_Big_attack = "Floraison infernale"

    Description_debut = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais une déesse : Perséphone, déesse du printemps et épouse d'Hadès.\n"
    Description_victoire = "\nLa déesse pousse un hurlement de rage. Elle émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, elle a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
    Description_defaite = "\nVous n'atteindrez jamais le dieu des enfers. Sa femme était trop puissante pour vous. Vous mourez transpercé de toutes parts par les tiges des fleurs qu'elle a fait pousser par magie.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Dieu_Hades(): 
    Nom = "Hadès" 
    Niveau = 4
    Points_de_vie = 9999
    Points_attaque = 666
    Points_defense = 9999
    Points_XP = 100
    esq = 4

    Small_attack = Points_attaque
    Nom_small_attack = "Hantise"
    Big_attack = Points_attaque + 666
    Nom_Big_attack = "Faux spectrale"

    Description_debut = "\nHadès, dieu des morts et des enfers, apparait dans toute sa terrifiante splendeur. Il porte une armure noire.\nElle ne brille pas mais semble absorber toute la lumière environnante. Il se lève et  son arme apparait dans sa main : une faux immense, plus grande encore que le dieux lui-même et dont l'énergie vous glace jusque dans votre âme.\n"
    Description_victoire = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu sans laisser de trace. Vous n'osez pas vous attarder sur les lieux.\nAu fond, derrière le trône, vous trouvez la barque de Charon qui gît abandonée. Vous décidez de l'emporter avec vous. Vous savez qu'après avoir vaincu Hadès, il vous faudra affronter ses frères. Et vous n'êtes pas encore prêt à faire face au seigneur des dieux.\n"
    Description_defaite = "\nVous êtes vaincu. Vous allez mourir, et vous savez que, pour l'avoir défié, Hadès ne vous réserve pas un sort favorable en son royaume.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Dieu_Poseidon(): 
    Nom = "Poséidon" 
    Niveau = 7
    Points_de_vie = 30000
    Points_attaque = 1200
    Points_defense = 99999
    Points_XP = 100
    esq = 4

    Small_attack = Points_attaque
    Nom_small_attack = "Coup de Trident"
    Big_attack = Points_attaque + 750
    Nom_Big_attack = "Tsunami"

    Description_debut = "\nPoséidon, dieu des océans, se tient devant vous. Et vous êtes sur son territoire. Il vous faudra plus que du courage pour espérer sortir victorieux de ce combat.\n"
    Description_victoire = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu, laissant une clé au fond de votre barque.\nDe l'objet émane une énergie phénoménale, presque effrayante, qui ne laisse aucun doute sur sa nature. Il s'agit de la clé qui ouvre les portes de l'Olympe. Il est temps pour vous maintenant d'affronter le plus puissant des dieux.\n"
    Description_defaite = "\nVous êtes soulevé dans les airs et votre barque rétrécit à vue d'oeil. Comment êtes-vous arrivé là-haut ?\nCe n'est qu'alors que vous remarquez que vous êtes empallé sur une des pointes du trident de Poséidon. Il vous en arrache et vous jette dans les flots déchaînés. Vous succombez heureusement rapidement, car les requins ne tardent pas à venir se disputer votre dépouille.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]


def Dieu_Zeus(): 
    Nom = "Zeus" 
    Niveau = 9
    Points_de_vie = 99999
    Points_attaque = 1700
    Points_defense = 99999
    Points_XP = 100
    esq = 4

    Small_attack = Points_attaque
    Nom_small_attack = "30 millions de volts"
    Big_attack = Points_attaque + 5000
    Nom_Big_attack = "Barrage orageux"

    Description_debut = "\nZeus se tient là, devant vous, son immense éclair à la main. A la pensée de ce qu'il a pu faire à votre soeur, vous manquez perdre toute contenance, mais vous vous ressaisissez à temps.\nCe n'est pas le moment de vous laisser aller. La colère donne de la force mais obscurcit le jugement. Vous devez rester maître de vous-même si vous voulez la sauver."
    Description_victoire = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu sans laisser de trace. Vous poussez un soupir de soulagement.\n"
    Description_defaite = "\nVous êtes à terre, incapable de vous relever. Vous avez échoué. Vous aller mourir sans avoir pu sauver votre soeur.\nEt vous vous maudirez éternellement pour cela. Zeus lève son éclair haut au-dessus de sa tête puis l'abat dans votre direction. Vous ne voyez que la lumière aveuglante de l'attaque, et c'est fini.\n"
    return [Nom, Niveau, Points_de_vie, Points_attaque, Points_defense,esq, Points_XP, Nom_small_attack, Nom_Big_attack, Small_attack, Big_attack, Description_debut, Description_victoire, Description_defaite]

Liste_ennemis = [Harpie(),Cyclope(),Minotaure(),Cerbere(),Lamia(),Griffon(),Sirenes(),Sphinx(),Lion_de_Nemee(),Meduse(),Deesse_Athena(),Deesse_Aphrodite(),Deesse_Artemis(),Dieu_Apollon(),Dieu_Ares(),Dieu_Dionysos(),Deesse_Persephone(),Dieu_Hades(),Dieu_Poseidon(),Dieu_Zeus()]
