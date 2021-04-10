#!/usr/bin/env python3
"""
générateur de fichiers de points
"""
import random

def generateur(nb, distance):
    print(distance)
    for _ in range (0, nb):
        x=random.random()
        y=random.random()
        print(x, ", ", y, sep="")
    return None

generateur(100000, 0.001)
