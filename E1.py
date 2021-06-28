import os
import time
import sys
if os.path.exists("comm.emvv"):
    print("Bonjour")
    print("Il s'agit de l'extension qui gère différents paramètre au seins de ma vie virtuelle")
    print("Vous pouvez la réduire mais ne l'arrêter pas!")
    print("Elle s'arrêteras automatiquement à l'arrêt de Ma vie virtuelle")
else:
    print("Une erreur est survenue, veuillez redémarrez ma vie virtuelle")
    time.sleep(10)
    sys.exit()
while True:
    time.sleep(30)
    état_partie = 0
    energie = 0
    faim = 0
    humeur = 0
    hygiène = 0
    charge = [0, 0, 0, 0, 0]
    with open("comm.emvv", 'r') as filin:
        charge = filin.read().splitlines()
    état_partie = int(charge[0])
    energie = int(charge[1])
    faim = int(charge[2])
    humeur = int(charge[3])
    hygiène = int(charge [4])    
    if état_partie == 1 or état_partie == "1":
        os.remove('comm.emvv')
        sys.exit()
    if energie > 0:
        energie = energie - 1 
    else:
        energie = 0
    if faim > 0:
        faim = faim - 1
    else:
        energie = 0
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