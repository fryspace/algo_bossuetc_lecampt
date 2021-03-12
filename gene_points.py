#!/usr/bin/env python3
"""
générateur de fichiers de points
"""
import random

def generateur(nb, distance):
    print(distance)
    for i in range (0, nb):
        x=random.random()
        y=random.random()
        print(x, ", ", y, sep="")
    return None

n=generateur(10000, 0.01)
