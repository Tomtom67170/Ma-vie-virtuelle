print("sys:Démarrage...")
import time
import os
import sys
entré = 0 #non
partie = [0, 0, 0] #non
état_partie = 0 #oui 3
nbPartie = 0 #non
save = 0 #?
pseudo = 0 #oui 2
version = "0.0.3" #oui 1
salle = "Entré"
lit = "0" #oui 4
code = 0 #oui 5
exe = 0 #non
def minuteur (minute, seconde):
    while minute > -1:
        while seconde > 0:
            time.sleep(0.9)
            seconde = seconde - 1
            print(minute,":", seconde)
        minute = minute - 1
        seconde = 60
def demande():
    global entré
    global salle
    entré = input("["+salle+"] Que voulez vous faire?")
print("Ma vie virtuelle made in Python (Version ALPHA 0.0.3)")
print("sys:Séléctionner une partie avec 1, 2 ou 3")
print("sys:Pour gérer les sauvegardes démarrer l'assistant de sauvegarde inclu avec l'archive .rar")
try:
    entré = int(input())
except ValueError:
    print("Une erreur est survenue: VALUE_ERROR")
    print("Cet erreur est survenue car vous avez entré autre chose qu'un chiffre! L'erreur n'est pas fatal et le jeu va reprendre!")
    time.sleep(10)
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
    if version != "0.1.1":
        print("Votre sauvegarde n'est pas conçu pour tourner sous cette version de Ma vie virtuelle.py veuillez supprimer cette sauvegarde puis en créer une dans l'assistant de sauvegarde")
        print("Le jeu va s'arrêter")
        time.sleep(10)
        sys.exit()
except FileNotFoundError:
    print(":(")
    print("Une erreur est survenue et le jeu ne peux plus fonctionner pour la raison suivante: FILE_NOT_FOUND")
    print("Sauv.txt")
    print("Le jeu va s'arrêter")
    time.sleep(20)
    sys.exit()
if entré == 4:
    print("???: Bienvenue dans l'assistant de mise à jour")
    time.sleep(5)
    print("sys: Vous avez découvert un easter-egg ATTENTION: Il va disparaître  pour la 0.2")
    print("Après cette version, seul l'assistant de sauvegarde pourra mettre à jour vos sauvegardes")
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
    input("étape 1: Aller dans le dossier de la version qui vous intéresse de ma vie virtuelle, appuyer sur entré pour continuer...")
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
    état_partie = partie[2]
    lit = partie[3]
    code = partie[4]
except IndexError:
    print(":(")
    print("Une erreur est survenue et le jeu ne peux plus continuer à fonctionner pour la raison suivante: INDEX_ERROR")
    print("Cette erreur est survenue car certaines informations n'ont pas été trouvé dans votre sauvegarde! N'oubliez pas de mettre à jour vos sauvegardes")
    print("Le jeu va s'arrêter")
    time.sleep(15)
    sys.exit()
print("sys:Partie chargé")
while True:
    if état_partie == "0":
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
        print("[Salon]John: S'il vous plait retournée à l'entré.")
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
        print("[Entrée]John: Contrairement à ce que vous pouvez probablement croire, il ne faut pas dire Télétravailler mais démarrer")
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
        print("[PC]John: Écoutez", pseudo,", Johnservice vous à trouvé un toit et les pièces qui vont avec, aviez-vous réellement cru que tout cela serais gratuit?")
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
        print("1: Connaitre les nouveauté de mise à jour")
        print("2: Connaitre le but des logiciels de votre PC")
        print("3: Appelez John")
        print("4: Connaitre mon solde bancaire")
        print("5: Éxécuter arrêt.dll")
        time.sleep(15)
        print("[PC]John: Chaque programme possède un fichier arrêt.dll. Sur skype, il faut entrer 5 pour l'éxécuter arrêt.dll")
        time.sleep(10)
        print("[PC]John: Les fichiers arrêt.dll vous permettent de quitter un programme ou alors d'éteindre votre PC si vous êtes sur l'invite de commande")
        time.sleep(15)
        try:
            while entré != 5:
                entré = int(input("Skype: Que voulez-vous faire? Action limité par tutoriel.exe"))
                if entré != 5:
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
        print("[PC]John: ATTENTION: Il s'agit du tutoriel de la version ALPHA 0.1.1, IL EST INCOMPLET")
        time.sleep(7)
        print("[PC]John: Après chaque maj, liser MAJ.txt pour connaitre les ajouts, il est recommandé de réaliser un tutoriel après chaque mise à jour")
        time.sleep(10)
        print("sys: John à quitté la conversation")
        print("sys: Le tutoriel est terminé! Vous vous trouvé à l'entré de chez vous.")
        time.sleep(10)
        salle = "entrée"
        exe = 1
    else:
        demande()
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
                partie[0] = version
                partie[1] = pseudo
                partie[2] = état_partie
                partie[3] = lit
                partie[4] = code
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
                                fichier.write('f{partie}\n')
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
                print("Une autre réponse que {o} ou {n} à été répondu! Arrêt annulé par Ma vie virtuelle.py")
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
            print("démarrer (indisponible): Démarre le PC de travail")
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
                    if lit == "0":
                        print("Votre lit n'est pas fait, vous dormez plus longtemps car vous n'êtes pas à l'aise")
                        minuteur(5,0)
                    else:
                        print("Votre lit est fait, vous êtes à l'aise")
                        minuteur(2,0)
                    lit = "1"
                    exe = 1
                    print("Vous avez dormi")
                if entré == "faire le lit":
                    if lit == "0":
                        print("Vous allez faire votre lit")
                        minuteur(1,0)
                        lit = "1"
                    else:
                        print("Votre lit à déjà été fait, inutile de le refaire mais je connais une personne qui sera content de dormir")
                    exe = 1
                if exe == 0:
                    print("Commande invalide. Vérifiez que tout est en minuscule.")
                exe = 0
            salle = "Entrée"
            exe = 1
        if exe == 0:
            print("Commande invalide. Vérifiez que tout est en minuscule")
        exe = 0
