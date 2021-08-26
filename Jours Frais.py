print("sys:Démarrage...")
print("Importation des modules...")
from time import strftime
from tkinter.constants import FALSE
try:
    import time
except ModuleNotFoundError:
    print(":(")
    print("Une erreur est survenue: MODULE_NOT_FOUND_ERROR")
    print("Cet erreur est survenue car certain module n'ont pas été trouvé")
    print("Le module: TIME est introuvable et Jours Frais ne peut plus continuer à fonctionner")
    print("Le jeu va s'arrêter")
    time.sleep(15)
    sys.exit()
try:
    import os
except ModuleNotFoundError:
    print(":(")
    print("Une erreur est survenue: MODULE_NOT_FOUND_ERROR")
    print("Cet erreur est survenue car certain module n'ont pas été trouvé")
    print("Le module: OS est introuvable et Jours Frais ne peut plus continuer à fonctionner")
    time.sleep(15)
    sys.exit()
print("Vérification du système...")
if os.path.exists("/storage/emulated/0/Android"):
    print("Il à été détecté que votre jeu tourne sous le système d'exploitation Android")
    print("Ce système n'est cependant pas pris en charge par Jours Frais")
    print("Le jeu va s'arrêter")
    time.sleep(12)
    sys.exit()
try:
    import sys
except ModuleNotFoundError:
    print(":(")
    print("Une erreur est survenue: MODULE_NOT_FOUND_ERROR")
    print("Cet erreur est survenue car certain module n'ont pas été trouvé")
    print("Le module: SYS est introuvable et Jours Frais ne peut plus continuer à fonctionner")
    print("Le jeu va s'arrêter")
    time.sleep(15)
    sys.exit()
try:
    import subprocess
except ModuleNotFoundError:
    print(":(")
    print("Une erreur est survenue: MODULE_NOT_FOUND_ERROR")
    print("Cet erreur est survenue car certain module n'ont pas été trouvé")
    print("Le module: SUBPROCESS est introuvable.")
    input("Appuyer sur entrée pour continuer")
try:
    import locale
except ModuleNotFoundError:
    print(":(")
    print("Une erreur est survenue: MODULE_NOT_FOUND_ERROR")
    print("Cet erreur est survenue car certain module n'ont pas été trouvé")
    print("Le module: LOCALE est introuvable et Jours Frais ne peut plus continuer à fonctionner")
    print("Le jeu va s'arrêter")
    time.sleep(15)
    sys.exit()
try:
    import tkinter
    from tkinter import Label
except ModuleNotFoundError:
    print(":(")
    print("Une erreur est survenue: MODULE_NOT_FOUND_ERROR")
    print("Cet erreur est survenue car certain module n'ont pas été trouvé")
    print("Le module: SUBPROCESS est introuvable et Jours Frais ne peut plus continuer à fonctionner")
    print("Le jeu va s'arrêter")
    time.sleep(10)
    sys.exit()
try:
    import keyboard
    try:
        import mouse
        key = True
        clavier = True
    except ModuleNotFoundError:
        print("Le module MOUSE n'est pas installé, Jours Frais va l'installé")
        if os.name == 'nt':
            os.system('pip install mouse')
            print("L'extension est (normalement) installé")
            print("Le jeu va s'arrêter")
            time.sleep(5)
            sys.exit()
        else:
            os.system('pip3 install mouse')
            print("L'extension est (normalement) installé")
            print("Le jeu va s'arrêter")
            time.sleep(5)
            sys.exit()
except ModuleNotFoundError:
    print("Le module KEYBOARD n'est pas installé sur ce PC")
    print("Jours Frais utilise ce module pour rendre l'expérience de jeu plus attractive")
    print("Il est fortement recommandé d'installer ce module. Pour cela une page sur le site de Jours Frais à été écrite pour vous aider à l'installer")
    print("Lien du site de Jours Frais: tomtom67170.github.io")
    input("Appuyer sur entrée pour continuer...")
    key = False
    clavier = True
try:
    from random import *
except ModuleNotFoundError:
    print("Le module RANDOM est introuvable! Jours Frais est en train d'adapter les paramètres...")
    if clavier == True:
        clavier = False
        key = False
        print("Le module KEYBOARD à été désactivé")
if os.path.exists("E1.py"):
    print("Extension 1 trouvée!")
else:
    print("Echec de l'importation des modules!")
    fenetre = tkinter.Tk()
    fenetre.geometry("700x100")
    fenetre.title("Erreur")
    if os.path.exists("vcsconflicting_93497.ico"):
        fenetre.iconbitmap("vcsconflicting_93497.ico")
    texte1 = Label (fenetre, text="E1.py est introuvable")
    texte2 = Label (fenetre, text="Le fichier est disponible dans les dossiers GitHub. Il doit se trouver dans le même dossier que Jours Frais.py")
    texte1.pack()
    texte2.pack()
    fenetre.mainloop()
    sys.exit()
    prc_tot = 81
def prc (pourcent):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tomservice")
    print(pourcent,"%")
version_jeu = "0.2" #non Doit être changé à chaque MAJ
entré = 0 #non
essaie = 0 #non
partie = [0, 0, 0] #non
état_partie = 0 #oui 3
nbPartie = 0 #non
save = 0 #?
pseudo = 0 #oui 2
version = "0.2" #oui 1
salle = "Entré" #non
lit = 0 #oui 4
code = 0 #oui 5
exe = 0 #non
comm = [] #non
état_E1 = 0 #non
energie_sav = 0 #oui 6
energie = 0 #non
faim_sav = 0 #oui 7
faim = 0 #non
humeur_sav = 0 #oui 8
humeur = 0  #non
hygiène_sav = 0 #oui 9
hygiène = 0 #non
action = 0 #non
touche_nb = 0 #non
touche = 0 #non
argent = 0 #oui 10
ciné = True #oui 11
locale.setlocale(locale.LC_TIME,'') 
actuel = int(time.strftime("%M")) #non
if actuel >= 58:
    print("Impossible de démarrer Jours Frais! Veuillez réessayer plus tard...")
    time.sleep(10)
    sys.exit()
if os.path.exists("j.emvv"):
    print("Des fichier temporaires ont été trouvé! Jours Frais va les supprimer")
    os.remove("comm.emvv")
    os.remove("j.emvv")
prochain = actuel + 2 #non
ancien_j = 0 #non
j = 0 #non
def minuteur (minute, seconde):
    if clavier == False:
        while minute > -1:
            while seconde > 0:
                time.sleep(0.9)
                os.system('cls' if os.name == 'nt' else 'clear')
                seconde = seconde - 1
                print(minute,":", seconde)
            minute = minute - 1
            seconde = 60
    if clavier == True:
        global action
        action = True
        touche_nb = randint(1,4)
        touche = 0
        while minute > -1:
            while seconde > 0:
                time.sleep(0.9)
                os.system('cls' if os.name == 'nt' else 'clear')
                seconde = seconde - 1
                print(minute,":",seconde,"Restez appuyer sur C pour annulez")
                if seconde > 2:
                    if touche_nb == 1:
                        print ("Appuyer sur Z pour gagner 2 sec")
                        touche = 'z'
                    if touche_nb == 2:
                        print("Appuyer sur S pour gagner 2 sec")
                        touche = 's'
                    if touche_nb == 3:
                        print("Appuyer sur D pour gagner 2 sec")
                        touche = 'd'
                    if touche_nb == 4:
                        print("Appuyer sur Q pour gagner 2 sec")
                        touche = 'q'
                    if keyboard.is_pressed(touche):
                        seconde = seconde -2
                        touche_nb = randint(1,4)
                if keyboard.is_pressed('c'):
                    print("Action annulé!")
                    action = False
                    seconde = 0
                    minute = 0
            minute =  minute - 1
            seconde = 60
def demande():
    global entré
    global salle
    entré = input("["+salle+"] Que voulez vous faire?")
print("Prêt!")
time.sleep(1)
print("Jours Frais made in Python (Version ALPHA",version_jeu,")")
print("sys:Séléctionner une partie avec 1, 2 ou 3")
print("sys:Pour gérer les sauvegardes démarrer l'assistant de sauvegarde inclu avec l'archive .rar")
try:
    entré = int(input())
except ValueError:
    print("Une erreur est survenue: VALUE_ERROR")
    print("Cet erreur est survenue car vous avez entré autre chose qu'un chiffre! L'erreur n'est pas fatal et le jeu va reprendre!")
    time.sleep(5)
    entré = int(input("ATTENTION: Nous avons rattrapé le crash mais cette fois-ci, vous devez entrer un chiffre"))
try:
    if (entré == 1 or entré == 2 or entré == 3):
        print("sys:Chargement de la partie", entré)
    if entré == 1:
        with open("Sauvegarde 1.txt", 'r') as filin:
            partie = filin.read().splitlines()
        nbPartie = 1
    if entré == 2:
        with open("Sauvegarde 2.txt", 'r') as filin:
            partie = filin.read().splitlines()
        nbPartie = 2
    if entré == 3:
        with open("Sauvegarde 3.txt", 'r') as filin:
            partie = filin.read().splitlines()
        nbPartie = 3
    try:
        version = partie [0]
        print(partie)
    except TypeError:
        print(":(")
        print("Une erreur est survenue et le jeu ne peux plus fonctionner pour la raison suivante: TYPE_ERROR")
        print("Cet erreur est suvenue car votre sauvegarde est illisible ou corrompue! Veuillez supprimer la sauvegarde puis en recréer une!")
        print("Le jeu va s'arrêter")
        time.sleep(20)
        sys.exit()
    if version != version_jeu :
        print("Votre sauvegarde n'est pas conçu pour tourner sous cette version de Jours Frais.py veuillez supprimer cette sauvegarde puis en créer une dans l'assistant de sauvegarde")
        print("Le jeu va s'arrêter")
        time.sleep(10)
        sys.exit()
except FileNotFoundError:
    print(":(")
    print("Une erreur est survenue et le jeu ne peux plus fonctionner pour la raison suivante: FILE_NOT_FOUND")
    print("Les fichiers de sauvegardes sont introuvables, veuillez les crées dans l'assistant de sauvegarde")
    print("Le jeu va s'arrêter")
    time.sleep(20)
    sys.exit()
if entré == 4:
    print("???: Bienvenue dans l'assistant de mise à jour")
    time.sleep(5)
    print("sys: Vous avez découvert un easter-egg ATTENTION: Il va disparaître pour la 0.2")
    print("Après cette version, seul l'assistant de sauvegarde pourra mettre à jour vos sauvegardes")
    print("Tomservice à décidé de le supprimer car les méthodes de fonctionnement sont obsolètes")
    try:
        entré = int(input("Assistant de maj: Quel est le numéro de la sauvegarde que vous souhaiter convertir?"))
    except ValueError:
        print("Python: Vous n'avez pas entré un chiffre! S'il vous plaît, entrer de nouveau un chiffre entre 1 et 3")
        time.sleep(6)
        entré = int(input("ATTENTION: Nous avons rattrapé le crash mais cette fois-ci, vous devez entrer un chiffre"))
    if (entré >= 4 or entré <= 0):
        print("Assistant de maj: Numéro de sauvegarde invalide, vous allez quitter le logiciel")
        time.sleep(10)
        sys.exit()
    print("Assistant de maj: Nous allons procéder à la mise à jour de votre sauvegarde")
    time.sleep(6)
    input("étape 1: Aller dans le dossier de la version qui vous intéresse de Jours Frais, appuyer sur entré pour continuer...")
    input("étape 2: Renommer le fichier sauvegarde.txt correspondant à votre sauvegarde puis rennommer-le en ajoutant .old.(La copie est recommandé) appuyer sue entré pour continuer")
    input("Vérifiez que le fichier à un nom de ce style: Sauvegarde.old.txt (.txt correspond à l'extension de fichier, il est possible qu'il ne soit pas afficher selon vos paramètre, appuyer sur entrée pour continuer")
    input("étape 3: Déplacer (ou copier) le fichier dans le dossier de cette version")
    nbPartie = entré
    input("étape 4: La conversion va démarrer, les données présente dans la sauvegarde", entré," seront écrasées, voulez-vous continuer? (o/n)")
    if entré == "o":
        print("étape 5: Écrasement des données de la sauvegarde", entré,". Veuillez patientez...")
        try:
            if nbPartie == 1:
                with open("Sauvegarde 1.old.txt", 'r') as filin:
                    partie = filin.read().splitlines
                with open("Sauvegarde 1.old.txt", 'w') as fichier:
                    for partie in partie:
                        fichier.write(f'{partie}\n')
            if nbPartie == 2:
                with open("Sauvegarde 2.old.txt", 'r') as filin:
                    partie = filin.read().splitlines
                with open("Sauvegarde 2.txt", 'w') as fichier:
                    for partie in partie:
                        fichier.write(f'{partie}\n')
            if nbPartie == 3:
                with open("Sauvegarde 3.old.txt", 'r') as filin:
                    partie = filin.read().splitlines
                with open("Sauvegarde 3.txt", 'r') as filin:
                    for partie in partie:
                        fichier.write(f'{partie}\n')
        except FileNotFoundError:
            print("Python: Une erreur est survenue est la conversion n'a pas été réalisé! Vérifiez que tous les fichiers sont présent dans le dossier de ce jeu est vérifié que le nom est correct")
            print("Le jeu va s'arrêter...")
            time.sleep(15)
            sys.exit()
        print("Partie convertie avec succés le jeu va s'arrêter")
        time.sleep(5)
        sys.exit()
    else:
        print("Convertisseur de sauvegarde annulé par l'utilisateur! Le jeu va s'arrêter")
        time.sleep(8)
        sys.exit()
try:
    version = partie[0]
    pseudo = partie[1]
    état_partie = int(partie[2])
    lit = int(partie[3])
    code = int(partie[4])
    energie = int(partie [5])
    faim = int(partie [6])
    humeur = int(partie [7])
    hygiène = int(partie[8])
except IndexError:
    print(":(")
    print("Une erreur est survenue et le jeu ne peux plus continuer à fonctionner pour la raison suivante: INDEX_ERROR")
    print("Cette erreur est survenue car certaines informations n'ont pas été trouvé dans votre sauvegarde! N'oubliez pas de mettre à jour vos sauvegardes")
    print("Le jeu va s'arrêter")
    time.sleep(15)
    sys.exit()
except ValueError:
    print(":(")
    print("Une erreur est survenue: VALLUE_ERROR")
    print("Votre sauegarde à rencontré un problème! Certaines données sont invalides ou corrompus")
    print("Veuillez la recommencer dans l'assistant de sauvegarde.")
    print("Le jeu va s'arrêter")
    time.sleep(20)
    sys.exit()
print("sys:Partie chargé")
if état_partie == 1:
    print("Préparation en cours...")
    try:
        with open ("comm.emvv", 'w') as fichier:
            fichier.write('0\n')
            fichier.write(f'{energie}\n')
            fichier.write(f'{faim}\n')
            fichier.write(f'{humeur}\n')
            fichier.write(f'{hygiène}\n')
    except PermissionError:
        print(":(")
        print("Une erreur est survenue: PERMISSION_ERROR")
        print("Cette erreur est survenue car votre interpréteur Python n'a pas la permissions d'écrire dans le dossier de Jours Frais")
        print("Vérifiez que le dossier de Jours Frais n'est pas protégé en écriture!")
        time.sleep(15)
        sys.exit()
    filepath = 'E1.py'
    if os.name=='posix':
        os.system("gnome-terminal -x sh -c \"python3 E1.py; bash\"")
    else:
        os.startfile(filepath)
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    if état_partie == 0:
        print("sys:??? à rejoint la conversation")
        print("???:Bonjour, cet sauvegarde est vide! Nous allons créer une partie")
        time.sleep(5)
        pseudo = input("???:Comment vous appelez-vous?")
        print("???:Bonjour",pseudo,", je m'appelle John")
        time.sleep(4)
        print("John:John Business")
        time.sleep(3)
        print("John:Avant de continuer les présentation nous allons configurer la partie:")
        time.sleep(7)
        print("John:J'ai déjà pu connaitre votre pseudo")
        time.sleep(5)
        print("John:Il ne me reste plus qu'à connaitre le code de carte bancaire")
        time.sleep(6)
        print("Vous:Comment ça?! Je ne vais comme même pas vous donner mon code bancaire!")
        time.sleep(6)
        print("John: Non, je ne parle pas de votre carte présente dans la vie RÉELLE")
        time.sleep(6)
        print("John: Dans votre vie virtelle, vous posséder une carte qui seras votre seul moyen de paiement")
        time.sleep(7)
        print("John: Dans cette vie virtuelle, vous pouvez choisir votre code vous même!")
        time.sleep(4)
        code = input("Maintenant veuillez indiquer un code à 4 chiffres")
        if len(code) == 4:
            print("John: Merci, j'enregistre cela dans votre compte bancaire.")
        else:
            print("John: Vous vous moquer de qui",pseudo,"? Je vous ai demandé de me donner un code à 4 CHIFFRES!")
            time.sleep(9)
            print("John: Si vous commencer ainsi je vais devoir fermer votre vie virtuelle...")
            time.sleep(5)
            print("John: Je vais enclancher l'arrêt du jeu...")
            time.sleep(4)
            print("sys:John à quitté la conversation")
            print("sys: Arrêt enclanché par John Business, arrêt dans 5 secondes")
            time.sleep(5)
            sys.exit()
        print("John: Nous sommes fin prêt!")
        time.sleep(3)
        print("John:Je vais procéder à un tutoriel pour vous expliquer comment ce jeu fonctionne")
        time.sleep(7)
        print("John:Nous allons commencer par une expliquation de texte")
        time.sleep(5)
        print("[Entrée ] <--- Le mot encadré représente le nom de la pièce à laquelle vous êtes actuellement")
        time.sleep(8)
        print("John:La pièce [Entré] est la pièce par défault. Vous apparaisser ici et passer par celle-ci pour changer de pièce")
        time.sleep(10)
        print("John:Ici vous pouvez taper certaines commandes")
        time.sleep(4)
        print("John:Commandes de base:")
        print("save: Vous permet de sauvegarder votre partie")
        print("fin: Permet de fermer le jeu")
        time.sleep(12)
        input("John:Je vais désormais vous expliquer comment aller dans une pièce et y réaliser des action, appuyer sur entrée pour continuer...")
        print("John:Taper: chambre, puis valider avec entrée")
        while entré != "chambre":
            entré = input("[Entré]John:Que faire? Vos actions sont limité par le tutoriel")
            if entré != "chambre":
                print("Commande invalide: Vérifier que tout est en minuscule.")
        salle = "Chambre"
        print("[Chambre]John: Bien, en saisissant le nom de la pièce voulu, vous y êtes allé!")
        print("[Chambre]John: Dans la pièce [Entré], taper aide pour connaitre les différentes pièces")
        time.sleep(6)
        print("[Chambre]John: Et dans les autres pièces taper aide pour connaitre les différentes actions possibles")
        time.sleep(7)
        while entré != "aide":
            entré = input("[Chambre]John: Taper: aide pour connaitre les actions possible")
            if entré == "aide":
                print("sys: Actions disponibles:")
                print("Lit")
                print("Faire le lit(indisponible)")
            else:
                print("Commande invalide: Vérifier que tout est en majuscule")
        print("[Chambre]John: Maintenant vous savez comment connaitre les différentes actions pour les pièces")
        time.sleep(6)
        print("[Chambre]John: Les actions simples sont indiqué avec juste leurs nom")
        time.sleep(6)
        print("[Chambre]John: Vous avez probablement remarqué que l'action 2 était accompagné de (indisponible)")
        time.sleep(5)
        print("[Chambre]John: Cela signifie que l'objet n'est pas disponible pour le moment!")
        time.sleep(6)
        print("[Chambre]Vous: Sérieux?")
        time.sleep(3)
        if clavier == True:
            print("Pour réaliser une action, tapez le nom de l'action (si elle est disponible)")
            time.sleep(5)
            print("""Maintenant tapez "dormir" pour dormir""")
            while entré != "dormir":
                if entré == "dormir":
                    print("Avec le module KEYBOARD, vous pouvez gagnez des secondes en appuyat sur les touches demandés ou appuyer sur C pour annuler votre action!")
                    time.sleep(5)
                    minuteur(1,0)
        print("[Chambre]John: Maintenant taper entrée pour retourner à l'entrée")
        while entré != "entrée":
            entré = input("sys: Que faire? Vos actions sont limité par le tutoriel.")
            if entré =="entrée":
                salle = "Entrée"
            else:
                print("sys: Commande invalide! Vérifier que tout est en minuscule")
        print("[Entrée] John: Nous sommes de retour à l'entrée de chez vous!")
        time.sleep(4)
        print("[Entrée] John: Un peu de pratique...Taper la commande qui vous permet de connaitre les pièces disponible...")
        while (entré != "aide"):
            entré = input("sys:Que faire? Vos actions sont limité par le tutoriel")
            if entré != "aide":
               print("sys: Commande invalide! Vérifiez que tout est en minuscule!")
               essaie = essaie + 1
        if essaie == 3:
            print("sys: Nous avons remarqué que vous avez des difficultés à continuer, la bonne commande était aide! Retenez-le")
            time.sleep(8)
        print("sys:Pièces présent chez vous:")
        print("Chambre(indisponible)")
        print("Salon")
        print("Cuisine (indisponible)")
        print("Salle de bain (indisponible)")
        print("Télétravailler(indisponible)")
        print("Commande de base:")
        print("save: Sauvegarder")
        print("fin: Arrête le jeu")
        time.sleep(10)
        print("[Entré]John: Maintenant, rendez-vous dans la seul pièce disponible")
        essaie = 0
        while (entré != "salon"):
            entré = input("sys:Que faire? Vos actions sont limité par le tutoriel!")
            if entré != "salon":
                print("sys:Commande invalide! Vérifiez que tout est en minuscule!")
                essaie = essaie + 1
        if essaie == 3:
            print("sys: Nous avons remarqué que vous avez des difficultés à continuer, la bonne commande était salon! Retenez-le")
            essaie = 0
            time.sleep(8)
        print("[Salon]John: Bien maintenant taper la commande pour voir les différentes actions possibles de cette pièces")
        time.sleep(7)
        while (entré != "aide"):
            entré = input("sys:Que faire? Vos actions sont limité par le tutoriel!")
            if entré != "aide":
                print("Commande invalide! Vérifiez que tout est en minuscule!")
                essaie = essaie + 1
        if essaie == 3:
            print("sys: Nous avons remarqué que vous avez des difficultés à continuer, la bonne commande était aide! Retenez-le")
            essaie = 0
            time.sleep(8)
        print("sys:Actions possible dans le salon :")
        print("Télé $(indisponible)")
        print("Radio !(indisponible)")
        print("Dessiner $(indisponible)")
        print("Lire $(indisponible)")
        time.sleep(5)
        print("[Salon]John: Vous pouvez observer le fait que le 1er le 3ème et dernier choix possède un $")
        time.sleep(6)
        print("[Salon]John: Cela signifie que l'objet doit être acheté")
        time.sleep(5)
        print("[Salon]John:Vous pouvez également observer que la deuxième action possède un !")
        time.sleep(6)
        print("[Salon]John: Cela signifie que l'objet est acheté mais vous devez payé pour l'utiliser(souvent à cause d'un abonnement)")
        time.sleep(10)
        print("[Salon]John: Maintenant je vous ai présenté les différents façon dont les actions peuvent être exprimé, je vais vous présenter un endroit important")
        time.sleep(10)
        print("[Salon]John: S'il vous plait retournée à l'entrée.")
        time.sleep(4)
        while entré != "entrée":
            entré = input("sys: Que faire? Vos actions sont limités par le tutoriel.")
            if entré != "entrée":
                print("sys: Commande invalide! Vérifiez que tout est en minuscule!")
        salle = "entrée"
        print("[Entré]John je vais vous épargnez le besoin d'écrire aide pour connaitre les pièces disponibles.")
        time.sleep(7)
        print("Pièces présente chez vous:")
        print("Chambre (indisponible)")
        print("Salon (indisponible)")
        print("Cuisine (indiponible)")
        print("Salle de bain (indisponible)")
        print("Télétravailler")
        time.sleep(8)
        print("[Entrée]John: Vous pourrez remarquer que l'option télétravailler est désormais disponible!")
        time.sleep(6)
        print("[Entrée]John: Contrairement à ce que vous pouvez probablement croire, il ne faut pas dire Télétravailler mais démarrer pour accéder à cette pièce (qui n'est même pas une pièce)")
        time.sleep(7)
        print("[Entrée]John: En effet il ne s'agit pas d'une pièce mais d'une action spécifique à la salle Entrée")
        time.sleep(6)
        print("[Entrée]John: Cet action va démarrer votre ordinateur virtuelle de travail")
        time.sleep(5)
        while entré != "démarrer":
            entré = input("[Entrée]John: Taper démarrer pour accéder à votre PC de travail")
            if entré != "démarrer":
                print("Commande invalide! Vérifiez que tout est en minuscule!")
        print("...")
        time.sleep(3)
        print("Démarrage MS-DOS 6.22...")
        time.sleep(5)
        salle = "PC"
        print("[PC]PC: PC initialisé!")
        print("[PC]John: Bienvenue sur votre PC de travail!")
        time.sleep(4)
        print("[PC]Vous: OK John, mais à quoi ça sert d'être sur un PC de travail? Je ne vais pas pouvoir jouer...")
        time.sleep(6)
        print("[PC]John: Voyons", pseudo,", vous allez vite vous rendre compte que dans la vie, il vous faut de l'argent...")
        time.sleep(7)
        print("[PC]John: Ce PC, à l'aide de différent programme, va vous permettre de gagner de l'argent")
        time.sleep(6)
        print("[PC]John: Tout ces programmes, vont désormais vous servir à travailler pour moi!")
        time.sleep(5)
        print("[PC]Vous: Comment ça? Je n'ai jamais demandé à travailler pour vous!")
        time.sleep(4)
        print("[PC]John: Écoutez", pseudo,", Johnservice vous à trouvé un toit et les pièces qui vont avec, aviez-vous réellement cru que tout cela serait gratuit?")
        time.sleep(12)
        while entré != "o":
            entré = input("[PC]sys: Acceptez-vous cela? (o/n)")
            if entré != "o":
                print("[PC]John: Écouter", pseudo,", je comprends que cela soit bizarre pour vous mais vous devez accepter")
        print("[PC]John: Content que vous accepter de travailler pour moi")
        time.sleep(6)
        print("[PC]John: Maintenant que je vous ai expliqué pourquoi vous travaillé, revenons au commande de votre PC")
        time.sleep(7)
        print("[PC]John: Si vous connaissez déjà les commande DOS, cela devrait être facile pour vous d'apprendre à utiliser ce PC.")
        time.sleep(8)
        print("[PC]John: Taper dir pour connaitre les différent programmes présent sur votre ordinateur")
        time.sleep(5)
        while entré != "dir":
            entré = input("C: Tutoriel.exe est en cours d'éxecution")
            if entré != "dir":
                print("Commande invalide")
        print("Programme trouvé dans le lecteur C")
        print("Bouton.exe (crypté)")
        print("Calculatrice.exe (crypté)")
        print("Skype.exe")
        print("Arrêt.dll")
        time.sleep(8)
        print("[PC]John: Vous pouvez remarqué que certains logiciel sont crypté. Dans ces cas là, il est impossible de les ouvrir sans code")
        time.sleep(8)
        print("[PC]John: Pour démarrer un logiciel il suffit de simplement d'écrire son nom (sans le .exe). Je vais démarrer Skype pour vous montrer un exemple")
        time.sleep(10)
        print("[PC]John(contrôle votre PC): Skype")
        time.sleep(1.5)
        print("[PC]PC: Démarrage de Skype...")
        time.sleep(2)
        print("[PC]Skype: Fonction disponible sur Skype")
        print("1: Modifier les paramètres")
        print("2: Mode d'emploie des logiciels de votre PC")
        print("3: Appelez John")
        print("4: Connaitre mes informations")
        print("5: Afficher l'aide")
        print("6: Éxécuter arrêt.dll")
        time.sleep(15)
        print("[PC]John: Chaque programme possède un fichier arrêt.dll. Sur skype, il faut entrer 5 pour éxécuter arrêt.dll")
        time.sleep(10)
        print("[PC]John: Maintenant, arrêter Skype!")
        print("[PC]John: Les fichiers arrêt.dll vous permettent de quitter un programme ou alors d'éteindre votre PC si vous êtes sur l'invite de commande")
        time.sleep(15)
        try:
            while entré != 6:
                entré = int(input("Skype: Que voulez-vous faire? Action limité par tutoriel.exe"))
                if entré != 6:
                    print("Action invalide ou indisponible")
        except ValueError:
            print(":(")
            print("Une erreur est survenue et votre jeu ne plus fonctionner pour la raison: VALUE_ERROR")
            print("Cet erreur est survenue car vous avez entré autre chose qu'un chiffre")
            print("Le jeu va s'arrêter")
            time.sleep(15)
            sys.exit()
        print("[PC]John: Voila, le tutoriel est terminé! Je vais désactiver tutoriel.exe et ainsi, vous pourrez faire ce que vous voulez.")
        time.sleep(10)
        print("[PC]John: Je vous souhaite une bonne journée, si vous avez besoin d'aide, rendez-vous sur Skype")
        time.sleep(8)
        print("[PC]John: ATTENTION: Il s'agit du tutoriel de la version ALPHA",version_jeu,"IL EST INCOMPLET")
        time.sleep(7)
        print("[PC]John: Après chaque maj,lisez le texte qui est ajouté à côté de la version sur GitHub, il est recommandé de réaliser un tutoriel après chaque mise à jour")
        time.sleep(10)
        print("sys: John à quitté la conversation")
        print("sys: Le tutoriel est terminé! Jours Frais doit redémarrer!")
        time.sleep(3)
        salle = "entrée"
        exe = 1
        état_partie = 1
        print("Préparation à la sauvegarde...")
        print("Sauvegarde de la partie", nbPartie,", veuillez patientez...")
        partie[0] = version
        partie[1] = pseudo
        partie[2] = état_partie
        partie[3] = lit
        partie[4] = code
        partie[5] = energie
        partie[6] = faim
        partie[7] = humeur
        partie[8] = hygiène
        try:
            if nbPartie == 1:
                with open("Sauvegarde 1.txt", 'w') as fichier:
                    for partie in partie:
                        fichier.write(f'{partie}\n')
            if  nbPartie == 2:
                with open("Sauvegarde 2.txt", 'w') as fichier:
                    for partie in partie:
                        fichier.write(f'{partie}\n')
            if nbPartie == 3:
                with open("Sauvegarde 3.txt", 'w') as fichier:
                    for partie in partie:
                        fichier.write(f'{partie}\n')
            print("Partie Sauvegardé")
            print("Le jeu va s'arrêter")
            time.sleep(5)
            sys.exit()
        except PermissionError:
            print(":(")
            print("Une erreur est survenue: PERMISSION_ERROR")
            print("Cet erreur est survenue car Python ne possède pas les permissions pour modifier le fichier! Vérifiez que le fichier sauvegarde.txt n'est pas protégé en écriture")
            print("Les systèmes Linux ne sont pas compatibles pour le moment! Une future mise à jour rendra ces systèmes compatibles")
            print("Toutes les données enregistrées durant le tuto seront perdu!")
            time.sleep(10)
            sys.exit()
    else:
        locale.setlocale(locale.LC_TIME,'') 
        actuel = int(time.strftime("%M"))
        if actuel >= prochain:
            try:
                with open ("j.emvv", 'r') as filin:
                    lol = filin.read().splitlines()
                    j = int(lol[0])
                if ancien_j < j:
                    ancien_j = j
                    demande()
                    if actuel <=58:
                        prochain = actuel + 2
                    else: 
                        if actuel == 58:
                            prochain = 0
                        else:
                            prochain = 1
                else:
                    print("Il à été détecté que E1.py ne fonctionne plus correctement!")
                    print("Le jeu va s'arrêter! Les données non sauvegardés seront perdu!")
                    with open ("comm.emvv", 'w') as fichier:
                        fichier.write('1')
                    time.sleep(10)
                    sys.exit()
            except FileNotFoundError:
                print("Le fichier j.emvv à rencontré un problème! Jours Frais ne peut continuer de fonctionner")
                print("Le jeu va s'arrêter! Toutes les données non sauvegardés seront perdu!")
                with open ("comm.emvv", 'w') as fichier:
                    fichier.write('1')
                time.sleep(10)
                sys.exit
        else:
            demande()
        try:
            with open ("comm.emvv", 'r') as filin:
                comm = filin.read().splitlines()
            état_E1 = int(comm[0])
            energie = int(comm[1])
            faim = int(comm[2])
            humeur = int(comm [3])
            hygiène = int(comm [4])
        except FileNotFoundError:
            print(":(")
            print("Le fichier comm.emvv à rencontré un problème")
            print("Jours Frais doit s'éteindre, toutes les données non sauvegardés seront perdu!")
            time.sleep(10)
            sys.exit()
        except IndexError:
            print(":(")
            print("Le fichier comm.emvv à rencontré un problème")
            print("Jours Frais doit s'éteindre, toutes les données non sauvegardés seront perdu!")
            time.sleep(10)
            sys.exit()
        if entré == "save":
            exe = 1
            print("sys: La fonction save est désactivé car un bug est présent mais aucune solution n'à été trouvé pour le moment. L'équipe de dev de Tomservice enquête actuellement sur ce bug")
            print("sys: La fonction fin vous permettra de sauvegarder et de quitter le jeu")
            #print("Sauvegarde de la partie",nbPartie,"Veuillez ne pas toucher les fichier .txt")
            #try:
                #if nbPartie == 1:
                    #partie[0] = état_partie
                    #partie[1] = pseudo
                    #with open("Sauvegarde 1.txt", 'w') as fichier:
                        #for partie in partie:
                            #fichier.write(f'{partie}\n')
                #if  nbPartie == 2:
                    #partie[0] = état_partie
                    #with open("Sauvegarde 2.txt", 'w') as fichier:
                        #for partie in partie:
                            #fichier.write(f'{partie}\n')
                #if nbPartie == 3:
                    #partie[0] = état_partie
                    #with open("Sauvegarde 3.txt", 'w') as fichier:
                        #for partie in partie:
                            #fichier.write('f{partie}\n')
                #print("Partie Sauvegardé")
            #except FileNotFoundError:
                #print("Une erreur est survenue: FILE_NOT_FOUND")
                #print("Cet erreur est survenue car le fichier de sauvegarde est introuvable! Vérifiez qu'il est présent dans le dossier sous un nom de sauvagarde[chiffre].txt")
            #except PermissionError:
                #print("Une erreur est survenue: PERMISSION_ERROR")
                #print("Cet erreur est survenue car Python ne possède pas les permissions pour modifier le fichier! Vérifier que le fichier sauvegarde.txt n'est pas protégé en écriture")
        if entré == "fin":
            entré = input("Voulez quitter et sauvegardée la partie?(o/n)")
            if entré =="o":
                print("Sauvegarde de la partie", nbPartie,", veuillez patientez...")
                with open ("comm.emvv", 'r') as filin:
                    comm = filin.read().splitlines()
                comm[0] = "1"
                energie = int(comm[1])
                faim = int(comm [2])
                humeur = int(comm[3])
                hygiène = int(comm[4])
                partie[0] = version
                partie[1] = pseudo
                partie[2] = état_partie
                partie[3] = lit
                partie[4] = code
                partie[5] = energie
                partie[6] = faim
                partie[7] = humeur
                partie[8] = hygiène
                with open ("comm.emvv", 'w') as fichier:
                    for comm in comm:
                        fichier.write(f'{comm}\n')
                try:
                    if nbPartie == 1:
                        with open("Sauvegarde 1.txt", 'w') as fichier:
                            for partie in partie:
                                fichier.write(f'{partie}\n')
                    if  nbPartie == 2:
                        with open("Sauvegarde 2.txt", 'w') as fichier:
                            for partie in partie:
                                fichier.write(f'{partie}\n')
                    if nbPartie == 3:
                        with open("Sauvegarde 3.txt", 'w') as fichier:
                            for partie in partie:
                                fichier.write(f'{partie}\n')
                    print("Partie Sauvegardé")
                    print("Le jeu va s'arrêter")
                    time.sleep(5)
                    sys.exit()
                except PermissionError:
                    print("Une erreur est survenue: PERMISSION_ERROR")
                    print("Cet erreur est survenue car Python ne possède pas les permissions pour modifier le fichier! Vérifiez que le fichier sauvegarde.txt n'est pas protégé en écriture")
            if entré =="n":
                print("Arrêt annulé par l'utilisateur")
            else:
                print("Une autre réponse que {o} ou {n} à été répondu! Arrêt annulé par Jours Frais.py")
            exe = 1
        if entré == "aide":
            print("sys: Pièces présente chez vous:")
            print("Chambre")
            print("Salon (indisponible")
            print("Cuisine (indisponible)")
            print("Salle de bain (indisponible)")
            print("Commande de base:")
            print("save (indisponible): Permet de sauvegarder")
            print("fin: Permet de sauvegarder la partie et quitter le jeu")
            print("démarrer: Démarre le PC de travail")
            time.sleep(5)
            exe = 1
        if entré == "chambre":
            salle = "Chambre"
            while entré != "entrée":
                demande()
                if entré == "aide":
                    print("Action possible dans cette pièce")
                    print("Dormir")
                    print("Faire le lit")
                    exe = 1
                if entré == "dormir":
                    print("Vous allez dormir...")
                    if lit == 0:
                        print("Votre lit n'est pas fait, vous avez du mal à dormir car vous n'êtes pas à l'aise")
                        minuteur(5,0)
                    else:
                        print("Votre lit est fait, vous êtes à l'aise")
                        minuteur(2,0)
                    if action == True:
                        energie = 100
                        with open ("comm.emvv", 'r') as filin:
                            comm = filin.read().splitlines()
                        comm[1] = 100
                        with open ("comm.emvv", 'w') as fichier:
                            for comm in comm:
                                fichier.write(f'{comm}\n')
                        lit = 0
                        print("Vous avez dormi")
                    exe = 1
                if entré == "faire le lit":
                    if lit == 0:
                        print("Vous allez faire votre lit")
                        minuteur(1,0)
                        if action == True:
                            ("Votre lit est fait")
                            lit = 1
                    else:
                        print("Votre lit à déjà été fait, inutile de le refaire mais je connais une personne qui sera content de dormir")
                    exe = 1
                if entré == "entrée":
                    exe = 1
                if exe == 0:
                    print("Commande invalide. Vérifiez que tout est en minuscule.")
                exe = 0
            salle = "Entrée"
            exe = 1
        if entré == "démarrer":
            if energie >= 10:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Démarrage de MS-DOS 6.22...")
                if ciné == True:
                    time.sleep(1)
                salle = "PC"
            while entré != "Arrêt":
                if energie >= 10:
                    entré = input("C:\\")
                else:
                    entré = "Arrêt"
                    print("Vous êtes trop fatigué pour travailler! Dormez puis réessayé")
                    if ciné == True:
                        time.sleep(2)
                if entré == "dir":
                    print("Programme présent dans le disque C:")
                    print("Bouton.exe")
                    print("Calculatrice.exe")
                    print("Skype.exe")
                    print("Arrêt.dll")
                    exe = 1
                if entré == "aide":
                    print("Commande DOS")
                    print("dir: Connaitre les programmes présent")
                    print("[NomDeProgramme]: Lance le programme (ne rajoutez pas le .exe)")
                    print("cls: Efface le contenue de l'écran")
                    print("Arrêt: Arrête le PC de travail")
                    exe = 1
                if entré == "cls":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    exe = 1
                if entré == "Skype" or entré== "skype":
                    print("[PC]PC: Démarrage de Skype...")
                    time.sleep(2)
                    while entré != 5:
                        print("[PC]Skype: Fonction disponible sur Skype")
                        print("1: Modifier les paramètres")
                        print("2: Mode d'emploie des logiciels de votre PC")
                        print("3: Appelez John")
                        print("4: Connaitre mes informations")
                        #print("5: Afficher l'aide")
                        print("5: Éxécuter arrêt.dll")
                        try:
                            entré = int(input("[PC]Skype: Que faire?"))
                        except ValueError:
                            print("Skype à rencontré un problème: VALLUE_ERROR")
                            print("Eviter d'entrer des lettres dans Skype :)")
                            entré = 6
                        if entré == 1:
                            print("Paramètre du jeu")
                            print("1: Activer les fonctions keyboard (Etat:",clavier,")")
                            print("2: Modifier le code bancaire")
                            print("3: Mode immersion (état:",ciné,")")
                            try:
                                entré = int(input("[Paramètre] Que souhaitez-vous modifier"))
                            except ValueError:
                                print("Skype à rencontré un problème: VALLUE_ERROR")
                                print("Eviter d'entrer des lettres dans Skype")
                            if entré == 1:
                                if key == True:
                                    if clavier == True:
                                        clavier = False
                                        print("Keyboard est désactivé")
                                    else:
                                        clavier = True
                                        print("Keyboard est activée")
                                else:
                                    print("Impossible de modifier ce paramètre car le module KEYBOARD n'est pas installé ou Jours Frais l'a désactivé")
                                    time.sleep(5)
                            if entré == 2:
                                try:
                                    entré=input("Veuillez saisir votre nouveau code....")
                                except ValueError:
                                    print("Skype à rencontré un problème: VALLUE_ERROR")
                                    print("Eviter d'entrer des lettres dans Skype")
                                    entré = 6
                                if len(entré) == 4:
                                    code = entré
                                    print("Code modifié, le jeu doit être redémarré pour que les modifications soit corretements modifié")
                                    print("Sauvegarde de la partie", nbPartie,", veuillez patientez...")
                                    with open ("comm.emvv", 'r') as filin:
                                        comm = filin.read().splitlines()
                                    comm[0] = "1"
                                    energie = int(comm[1])
                                    faim = int(comm [2])
                                    humeur = int(comm[3])
                                    hygiène = int(comm[4])
                                    partie[0] = version
                                    partie[1] = pseudo
                                    partie[2] = état_partie
                                    partie[3] = lit
                                    partie[4] = code
                                    partie[5] = energie
                                    partie[6] = faim
                                    partie[7] = humeur
                                    partie[8] = hygiène
                                    with open ("comm.emvv", 'w') as fichier:
                                        for comm in comm:
                                            fichier.write(f'{comm}\n')
                                    try:
                                        if nbPartie == 1:
                                            with open("Sauvegarde 1.txt", 'w') as fichier:
                                                for partie in partie:
                                                    fichier.write(f'{partie}\n')
                                        if  nbPartie == 2:
                                            with open("Sauvegarde 2.txt", 'w') as fichier:
                                                for partie in partie:
                                                    fichier.write(f'{partie}\n')
                                        if nbPartie == 3:
                                            with open("Sauvegarde 3.txt", 'w') as fichier:
                                                for partie in partie:
                                                    fichier.write(f'{partie}\n')
                                        print("Partie Sauvegardé")
                                        print("Le jeu va s'arrêter")
                                        time.sleep(5)
                                        sys.exit()
                                    except PermissionError:
                                        print("Une erreur est survenue: PERMISSION_ERROR")
                                        print("Cet erreur est survenue car Python ne possède pas les permissions pour modifier le fichier! Vérifiez que le fichier sauvegarde.txt n'est pas protégé en écriture")
                                else:
                                    print("Votre code est invalide! Il doit comporter 4 chiffres!")
                            if entré == 3:
                                if ciné == True:
                                    ciné = False
                                    print("Le mode immersion est désactivé")
                                else:
                                    ciné = True
                                    print("Le mode immersion est activé")
                                entré = 0
                        if entré == 2:
                            print("1: Bouton.exe")
                            print("2: Calculatrice")
                            try:
                                entré =int(input("[Aide] Quels mode d'emploi voulez-vous avoir?"))
                            except ValueError:
                                    print("Skype à rencontré un problème: VALLUE_ERROR")
                                    print("Eviter d'entrer des lettres dans Skype")
                                    entré = 6
                            if entré == 1:
                                print("Guide de Bouton.exe")
                                print("Prérequis: Module KEYBOARD, Module MOUSE (Jours Frais l'installe si KEYBOARD est déjà installé).")
                                print("Bouton.exe est un logiciel où le but est de faire un maximum de click gauche de souris!")
                                print("Chaque click gauche vas augmenter la vitesse d'un moteur au seins de Johnservice!")
                                print("Après 100 click, le machine de Johnservice est en marche et vous donne 1$")
                                print("Si le logiciel s'arrête ou arrive à 100, la machine se remet à zéro et il faudra recommencer")
                                print("Pour quitter le logiciel, appuyer sur C")
                                input("Appuyer sur entrée pour continuer")
                            if entré == 2:
                                print("Guide de Calculatrice.exe")
                                print("Prérequis: Aucun")
                                print("Dans calculatrice.exe, des calculs vous sont donnés provenant directement de Johnservice (ne vous demandez pas pourquoi ces calculs)")
                                print("Il existe 3 modes; Facile/Modéré/Difficile")
                                print("Les modes évoluent au fur et à mesure de l'utilisation")
                                print("L'argent est distribué de cette façon:")
                                print("Facile: Correct; +1$ Faux;-1$/Modéré: Correct; +2$ Faux; +0$/Difficile: Correct; +3$ Faux; +0$")
                                print("Symboles des opérartions: + = Addition\ - = Soustractions\ * = Multiplication\ / = Division")
                                print("Pour quitter le logiciel, répondez C")
                                input("Appuyer sur entré pour continuer")
                        if entré == 3:
                            if ciné == True:
                                print("Appel en cours: John")
                                time.sleep(5)
                                print("[John]Allo",pseudo,"?")
                                time.sleep(1)
                                print("[John]Que souhaitez-vous?")
                                time.sleep(0.5)
                            print("[Vous (dans votre tête)]Je voulais lui dire quoi?")
                            print("1. Connaitre mon solde bancaire")
                            print("2. Lui demandez des nouvelles")
                            print("3: Je ne voulais pas l'appelé")
                            try:
                                entré = int(input())
                            except ValueError:
                                print("Skype à rencontré un problème: VALLUE_ERROR")
                                print("Eviter d'entrer des lettres dans Skype")
                                entré = 6
                            if entré == 1:
                                if ciné == True:
                                    print("[Vous] Quel est mon solde bancaire?")
                                    time.sleep(1.5)
                                    print("[John] Je vais vous le dire maintenant!")
                                    time.sleep(1.5)
                                    for loop in range(5):
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("|")
                                        time.sleep(0.1)
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("/")
                                        time.sleep(0.1)
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("-")
                                        time.sleep(0.1)
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("\\")
                                        time.sleep(0.1)
                                    print("[John] C'est bon je suis connecté à votre compte bancaire!")
                                    time.sleep(3)
                                print("Vous posséder",argent,"$ d'après votre banque!")
                                time.sleep(1.5)
                                if ciné == True:
                                    print("J'éspere que cela vous aura été utile!")
                                    time.sleep(2)
                                print("[PC] John à quitté la conversation")
                                time.sleep(1)
                            if entré == 2:
                                réponse = randint(0,5)
                                if réponse == 0:
                                    print("[John] Avez-vous réussi à retiré la disquette que j'ai sans le vouloir inséré dans votre ordinateur?")
                                if réponse == 1:
                                    print("[John] Ce serait cool d'avoir un lanceur qui démarre Jours Frais tout seul")
                                if réponse == 2:
                                    print("[John] J'aime bien le violet et vous?")
                                if réponse == 3:
                                    print("[John] J'espère qu'il ont retiré cet Assistant de mise à jour")
                                if réponse == 4:
                                    print("[John] Avez-vous entendue parler de la build du 29/07/1995 ?")
                                if réponse == 5:
                                    print("[John] Je travaille actuellement sur le projet: Vie-secondaire")
                                time.sleep(5)
                            if entré == 3:
                                if ciné == True:
                                    print("[John] Ah bon? Et bien c'est dommage...")
                                    time.sleep(2)
                                print("[PC] John à quitté la conversation")
                        if entré == 4:
                            print("Bonjour", pseudo)
                            print("Votre énergie est à",energie,"%")
                            print("Votre humeur est à",humeur,"%")
                            print("Votre faim est à",faim,"%")
                            print("Votre hygiène est à",hygiène,"%")
                            time.sleep(2)
                    exe = 1
                if entré == "Arrêt":
                    exe = 1
                if exe == 0:
                    print("Commande invalide! Vérifiez l'orthographe et les majuscules!")
                exe = 0
            salle = "Entrée"
            exe = 1
        if exe == 0:
            print("Commande invalide. Vérifiez que tout est en minuscule")
        exe = 0
        try:
            with open ("comm.emvv", 'r') as filin:
                comm = filin.read().splitlines()
            comm[1] = int(comm[1]) + energie_sav
            comm[2] = int(comm[2]) + faim_sav
            comm[3] = int(comm[3]) + humeur_sav
            comm[4] = int(comm [4]) + hygiène_sav
        except FileNotFoundError:
            print(":(")
            print("Le fichier comm.emvv à rencontrer un problème et Jours Frais doit redémarrer")
            time.sleep(10)
            sys.exit()
        with open ("comm.emvv", 'w') as fichier:
            for comm in comm:
                fichier.write(f'{comm}\n')
        energie_sav = 0
        faim_sav = 0
        humeur_sav = 0
        hygiène_sav = 0