import os
import time
import sys
from datetime import datetime
if os.path.exists("comm.emvv"):
    print("Bonjour")
    print("Il s'agit de l'extension qui gère différents paramètre au seins de Jours Frais")
    print("Vous pouvez la réduire mais ne l'arrêter pas!")
    print("Elle s'arrêteras automatiquement à l'arrêt de Jours Frais")
else:
    print("Une erreur est survenue, veuillez redémarrez Jours Frais")
    time.sleep(10)
    sys.exit()
j = 0
while True:
    with open ("j.emvv", 'w') as fichier:
        fichier.write(f'{j}')
    time.sleep(30)
    état_partie = 0
    energie = 0
    faim = 0
    humeur = 0
    hygiène = 0
    charge = [0, 0, 0, 0, 0]
    try:
        with open("comm.emvv", 'r') as filin:
            charge = filin.read().splitlines()
    except IndexError:
        os.remove('comm.emvv')
        os.remove('j.emvv')
        sys.exit()
    état_partie = int(charge[0])
    energie = int(charge[1])
    faim = int(charge[2])
    humeur = int(charge[3])
    hygiène = int(charge [4])   
    if état_partie == 1 or état_partie == "1":
        os.remove('comm.emvv')
        os.remove('j.emvv')
        sys.exit()
    print(charge)
    j = j + 1
    if energie > 0:
        energie = energie - 1 
    else:
        energie = 0
    if faim > 0:
        faim = faim - 1
    else:
        faim = 0
    if humeur > 0:
        humeur = humeur - 1
    else:
        humeur = 0
    if hygiène > 0:
        hygiène = hygiène -1
    else:
        hygiène = 0
    charge[0] = état_partie
    charge[1] = energie
    charge[2] = faim
    charge[3] = humeur
    charge[4] = hygiène
    with open ("comm.emvv", 'w') as fichier:
        for charge in charge:
            fichier.write(f'{charge}\n')