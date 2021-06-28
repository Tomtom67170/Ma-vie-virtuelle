print("Démarrage")
import time
import os
import sys
version_jeu = "0.1.2"   #Doit être modifié à CHAQUE maj
partie = []
entré = 0
version = 0
NbVar = 9   #Doit être modifié à CHAQUE maj
NbPartie = 0
fichier = 0
test = []
copie = 0
print("Bienvenue dans l'assistant de sauvegarde!")
print("Ce programme est conçu pour gérer les sauvegardes de Ma vie virtuel.py version", version_jeu)
if os.path.exists("Ma vie virtuelle.py"):
    print("Ma vie virtuelle à été trouvé dans ce dossier")
else:
    print("Impossible de trouver Ma vie virtuelle.py! Veuillez extraire le fichier de l'archive .rar dans le même dossier que cet assistant!")
    print("Le programme va s'arrêter")
    time.sleep(15)
    sys.exit()
time.sleep(2)
print("Action possible:")
print("1. Créer une sauvegarde")
print("2. Mettre à jour une sauvegarde")
print("3. Copiez une sauvegarde")
print("4. Recommencer une sauvegarde")
print("5. Supprimer une sauvegarde")
print("6. Préparez une sauvegarde pour une mise à jour")
print("7. Connaitre nom des sauvegardes (en cas de renommation des fichiers .txt)")
print("Autre chiffre. Quitter")
print(version_jeu)
def VALLUE_ERROR (question):
    global entré
    try:
        entré = int(input(question))
    except ValueError:
        print("Une erreur est survenue: VALUE_ERROR")
        print("Cela signifie qu'une valeur non entière à été entré")
        print("Le programme va s'arrêter")
        time.sleep(15)
        sys.exit()
VALLUE_ERROR("Que souhaitez-vous faire?")
if entré == 1:
    VALLUE_ERROR("Quelle numéro de sauvegarde voulez-vous créer?")
    if entré == 1:
        try :
            with open ("Sauvegarde 1.txt", 'r') as filin:
                partie = filin.read().splitlines()
            print("Une sauvegarde existe déjà! Veuillez la supprimer!")
            print("Le jeu va s'arrêter")
            time.sleep(5)
            sys.exit()
        except FileNotFoundError:
            print("Une partie va être créer dans la sauvegarde 1")
        with open ("Sauvegarde 1.txt", 'w') as fichier:
            fichier.write(f'{version_jeu}\n')
            for loop in range(NbVar):
                fichier.write('0\n')
    if entré == 2:
        try:
            with open ("Sauvegarde 2.txt", 'r') as filin:
                partie = filin.read().splitlines()
            print("Une sauvegarde existe déjà! Veuillez la supprimer!")
            print("Le jeu va s'arrêter")
            time.sleep(5)
            sys.exit()
        except FileNotFoundError:
            print("Une partie va être crée  dans la sauvegarde 2")
        with open ("Sauvegarde 2.txt", 'w') as fichier:
            fichier.write(f'{version_jeu}\n')
            for loop in range(NbVar):
                fichier.write('0\n')
    if entré == 3:
        try:
            with open ("Sauvegarde 3.txt", 'r') as filin:
                partie = filin.read().splitlines()
            print("Une sauvegarde existe déjà! Veuillez la supprimer!")
            time.sleep(6)
            sys.exit()
        except FileNotFoundError:
            print("Une partie va être créer dans la sauvegarde 3")
        with open ("Sauvegarde 3.txt", 'w') as fichier:
            fichier.write(f'{version_jeu}\n')
            for loop in range(NbVar):
                fichier.write('0\n')
    print("Partie créé avec succés!")
    time.sleep(10)
    sys.exit()
if entré == 2:
    print("Bienvenue dans l'assitant pour mettre à jour vos sauvegardes au cas où vous tombez sur l'erreur: INDEX_ERROR")
    entré = input("L'assistant va démarrer, une fois démarrer vous ne pourrez plus quitter! Continuer? [o/n]")
    if entré == "o":
        VALLUE_ERROR("Quel sauvegarde voulez-vous mettre à jour?")
        NbPartie = entré
        if (NbPartie == 1) or (NbPartie == 2) or (NbPartie == 3):
            print("Étape 1/5: Vérification de la disponibilité du fichier...")
        else:
            print("Les parties inférieur à 0 ou supérieur 3 ne sont pas disponible dans cette version")
            print("Le jeu va s'arrêter")
            time.sleep(10)
            sys.exit()
        try:
            if NbPartie == 1:
                with open ("Sauvegarde 1.txt", 'r') as filin:
                    partie = filin.read().splitlines()
            if NbPartie == 2:
                with open ("Sauvegarde 2.txt", 'r') as filin:
                    partie = filin.read().splitlines()
            if NbPartie == 3:
                with open ("Sauvegarde 3.txt", 'r') as filin:
                    partie = filin.read().splitlines()
            print("Étape 1/5: Une erreur est survenue")
            print("Une sauvegarde existe déjà! Veuillez la supprimer")
            time.sleep(10)
            sys.exit()
        except FileNotFoundError:
            input("Étape 2/5: Placer l'ancien fichier de sauvegarde (la sauvegarde doit être préparée au mise à jour) dans le dossier de ma vie virtuel, appuyer sur entrée une fois cela fait")
        print("3/5: Lecture du fichier...")
        try:
            if NbPartie == 1:
                with open ("Sauvegarde 1.old.txt", 'r') as filin:
                    partie = filin.read().splitlines()
            if NbPartie == 2:
                with open ("Sauvegarde 2.old.txt", 'r') as filin:
                    partie = filin.read().splitlines()
            if NbPartie == 3:
                with open ("Sauvegarde 3.old.txt", 'r') as filin:
                    partie = filin.read().splitlines()
            version = partie [0]
            partie [0] = version_jeu
            print(partie)
        except FileNotFoundError:
            print("Étape 3/5: Une erreur est survenue")
            print("Le fichier de l'ancienne sauvegarde est introuvable! Vérifiez qu'il est préparée au mise à jour")
            time.sleep(10)
            sys.exit()
        print("Une sauvegarde préparée à la mise à jour à été trouvée!")
        print("Conversion de la sauvegarde provenenant de la version:", version)
        print("Étape 4/5: Création d'un fichier de sauvegarde compatible à la version", version_jeu,"...")
        partie[0] = version_jeu
        if NbPartie == 1:
            with open("Sauvegarde 1.txt", 'w') as fichier:
                for partie in partie:
                    fichier.write(f'{partie}\n')
                    copie = copie + 1
                for loop in range(NbVar - copie):
                    fichier.write('0\n')
        if NbPartie == 2:
            with open("Sauvegarde 2.txt", 'w') as fichier:
                for partie in partie:
                    fichier.write(f'{partie}\n')
                    copie = copie + 1
                for loop in range(NbVar - copie):
                    fichier.write('0\n')
        if NbPartie == 3:
            with open("Sauvegarde 3.txt", 'w') as fichier:
                for partie in partie:
                    fichier.write(f'{partie}\n')
                    copie = copie + 1
                for loop in range(NbVar - copie):
                    fichier.write('0\n')
        print("Étape 5/5: Votre sauvegarde est prête! Vous pouvez supprimez l'ancienne sauvegarde et utiliser la nouvelle dans ma vie virtuelle")
        print("Le programme va s'arrêter")
        time.sleep(15)
    sys.exit()
if entré == 3:
    print("Bienvenue danns l'assistant de copie de sauvegarde!")
    print("Cet opération est utilile si vous souhaiter avoir un chekpoint de vos sauvegarde")
    print("Nous avons besoin de connaitre la sauvegarde de départ puis la sauvegarde cible!")
    time.sleep(10)
    VALLUE_ERROR("Quel est la sauvegarde de départ?")
    NbPartie = entré
    if (NbPartie == 1) or (NbPartie == 2) or (NbPartie == 3):
        try:
            if NbPartie == 1:
                with open("Sauvegarde 1.txt", 'r') as filin:
                    partie = filin.read().splitlines()
            if NbPartie == 2:
                with open("Sauvegarde 2.txt", 'r') as filin:
                    partie = filin.read().splitlines()
            if NbPartie == 3:
                with open("Sauvegarde 3.txt", 'r') as filin:
                    partie = filin.read().splitlines()
        except FileNotFoundError:
            print("Une erreur est survenue: FILE_NOT_FOUND_ERROR")
            print("Cet erreur est survenue car votre sauvegarde est introuvable")
            print("Il a peut-être été déplacé, renommé ou supprimer")
    else:
        print("Cet assistant ne prend pas en charge les sauvegardes inferieur à 0 et supérieur à 3")
        print("Le programme va s'arrêter")
        time.sleep(10)
        sys.exit()
    VALLUE_ERROR("Où voulez-vous copiez votre sauvegarde?")
    NbPartie = entré
    if (NbPartie == 1) or (NbPartie == 2) or (NbPartie == 3):
        try:
            if NbPartie == 1:
                with open("Sauvegarde 1.txt", 'r') as filin:
                    test = filin.read().splitlines()
            if NbPartie == 2:
                with open("Sauvegarde 2.txt", 'r') as filin:
                    test = filin.read().splitlines()
            if NbPartie == 3:
                with open("Sauvegarde 3.txt", 'r') as filin:
                    test = filin.read().splitlines()
            print("Une sauvegarde existe déjà! Veuillez la supprimer!")
            print("Le programme va s'arrêter")
            time.sleep(10)
            sys.exit()
        except FileNotFoundError:
            print("Sauvegarde en cours de copie...")
        if NbPartie == 1:
            with open("Sauvegarde 1.txt", 'w') as fichier:
                for partie in partie:
                    fichier.write(f'{partie}\n')
        if NbPartie == 2:
            with open("Sauvegarde 2.txt", 'w') as fichier:
                for partie in partie:
                    fichier.write(f'{partie}\n')
        if NbPartie == 3:
            with open("Sauvegarde 3.txt", 'w') as fichier:
                for partie in partie:
                    fichier.write(f'{partie}\n')
        print("Partie copié avec succés")
        time.sleep(10)
        sys.exit()
    else:
        print("Cet assistant ne prend pas en charge les parties inférieur à 0 et supérieur à 3")
        print("Le programme va s'arrêter")
        time.sleep(10)
    sys.exit()
if entré == 4:
    print("Bienvenue dans cet assistant, vous allez pouvoir recommencer vos sauvegardes!")
    print("ATTENTION: Toutes actions réalisé dans cet assistant est irréversible, il est recommandé de copiez vos sauvegardes au cas-où!")
    entré = input("Voulez-vous continuer ? [o/n]")
    if entré == "o":
        VALLUE_ERROR("Quel sauvegarde voulez-vous recommencer?")
        if (entré == 1) or (entré == 2) or (entré == 3):
            try:
                if entré == 1:
                    with open ("Sauvegarde 1.txt", 'r') as filin:
                        partie = filin.read().splitlines()
                if entré == 2:
                    with open ("Sauvegarde 2.txt", 'r') as filin:
                        partie = filin.read().splitlines()
                if entré == 3:
                    with open ("Sauvegarde 3.txt", 'r') as filin:
                        partie = filin.read().splitlines()
            except FileNotFoundError:
                print("Une erreur est survenue: FILE_NOT_FOUND_ERROR")
                print("Cet erreur est survenue car votre sauvegarde est introuvable! Il est possible qu'elle est était supprimé, déplacé ou renommer")
                print("Le programme va s'arrêter")
                time.sleep(10)
                sys.exit()
            print("Remise à zéro de la sauvegarde...")
            if entré == 1:
                with open ("Sauvegarde 1.txt", 'w') as fichier:
                    fichier.write(f'{version_jeu}\n')
                    for loop in range(NbVar):
                        fichier.write('0\n')
            if entré == 2:
                with open ("Sauvegarde 2.txt", 'w') as fichier:
                    fichier.write(f'{version_jeu}\n')
                    for loop in range(NbVar):
                        fichier.write('0\n')
            if entré == 3:
                with open ("Sauvegarde 3.txt", 'w') as fichier:
                    fichier.write(f'{version_jeu}\n')
                    for loop in range(NbVar):
                        fichier.write('0\n')
            print("Remise à zéro de votre sauvegarde terminé!")
            print("Le programme va s'arrêter")
        else:
            print("Cet assistant ne prend pas en charge les sauvegardes inférieur à 0 et supérieur à 3")
            print("Le programme va s'arrêter")
        time.sleep(10)
    sys.exit()
if entré == 5:
    print("Bienvenue dans cette assistant qui vous permettra de supprimer vos sauvegardes")
    print("ATTENTION: Toute suppresion est DÉFINITIVE!")
    entré = input("Voulez-vous continuez ? [o/n]")
    if entré == "o":
        VALLUE_ERROR("Quel sauvegarde voulez-vous supprimer?")
        if (entré == 1) or (entré == 2) or (entré == 3):
            if entré == 1:
                if os.path.exists("Sauvegarde 1.txt"):
                    os.remove("Sauvegarde 1.txt")
                else:
                    print("Une erreur est survenue:FILE_NOT_FOUND_ERROR")
                    print("Votre fichier est introuvable. Vérifiez qu'il n'a pas été supprimé, déplacé ou renommer")
                    time.sleep(10)
                    sys.exit()
            if entré == 2:
                if os.path.exists("Sauvegarde 2.txt"):
                    os.remove("Sauvegarde 2.txt")
                else:
                    print("Une erreur est survenue:FILE_NOT_FOUND_ERROR")
                    print("Votre fichier est introuvable. Vérifiez qu'il n'a pas été supprimé, déplacé ou renommer")
                    time.sleep(10)
                    sys.exit()
            if entré == 3:
                if os.path.exists("Sauvegarde 3.txt"):
                    os.remove("Sauvegarde 3.txt")
                else:
                    print("Une erreur est survenue:FILE_NOT_FOUND_ERROR")
                    print("Votre fichier est introuvable. Vérifiez qu'il n'a pas été supprimé, déplacé ou renommer")
                    time.sleep(10)
                    sys.exit()
            print("Partie supprimée")
        else:
            print("Cet assistant ne prend pas en charge les sauvegardes inférieur à 0 et supérieur à 3")
            print("Le programme va s'arrêter")
        time.sleep(10)
    sys.exit()
if entré == 6:
    print("Bienvenue dans l'assistant de mise à jour! Cet assistant va préparez vos sauvegardes au mise à jour de Ma vie virtuelle.py")
    print("ATTENTION: Les sauvegardes préparées au mise à jour ne peuvent plus être utilisé autremant qu'avec l'assistant de mise à jour")
    entré = input("Voulez-vous continuer? [o/n]")
    if entré == "o":
        VALLUE_ERROR("Quel sauvegarde voulez-vous préparée au mise à jour?")
        if (entré == 1) or (entré == 2) or (entré == 3):
            if entré == 1:
                if os.path.exists("Sauvegarde 1.txt"):
                    os.rename("Sauvegarde 1.txt","Sauvegarde 1.old.txt")
            if entré == 2:
                if os.path.exists("Sauvegarde 2.txt"):
                    os.rename("Sauvegarde 2.txt","Sauvegarde 2.old.txt")
            if entré == 3:
                if os.path.exists("Sauvegarde 3.txt"):
                    os.rename("Sauvegarde 3.txt","Sauvegarde 3.old.txt")
            print("Partie préparée au mise à jour")
        else:
            print("Cet assistant ne prend pas en charge les sauvegardes inférieur à 0 et supérieur à 3")
            print("Le programme va s'arrêter")
    else:
        sys.exit()
    time.sleep(10)
    sys.exit()
if entré == 7:
    print("Cet assistant va vous permettre de connaitre le nom des sauvegardes au cas où vous les avait renommé")
    VALLUE_ERROR("Quel nom de sauvegarde voulez-vous connaitre?")
    if (entré == 1) or (entré == 2) or (entré == 3):
        if entré == 1:
            print("Votre sauvegarde se nomme: Sauvegarde 1.txt")
        if entré == 2:
            print("Votre sauvegarde se nomme: Sauvegarde 2.txt")
        if entré == 3:
            print("Votre sauvegarde se nomme: Sauvegarde 3.txt")
    else:
        print("Cet assistant ne prend pas en charge les sauvegardes inférieur à 0 et supérieur à 3")
        print("Le programme va s'arrêter")
    time.sleep(10)
    sys.exit()
