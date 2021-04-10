#!/usr/bin/env python3
"""
générateur de fichiers de points
"""
import random



def generateur(nb, distance):
    
    fichier = open(f'tests_{nb}_{distance}.pts', "w")
    print(distance, file=fichier)
    for i in range (0, nb):
        x=random.random()
        y=random.random()
        print(x, ", ", y, sep="", file=fichier)
    return None

#n=generateur(10000, 0.01)

for i in range (1000, 100000, 500):
    for dist in  [0.01, 0.05, 0.1]:
        generateur(i, dist)
