#!/usr/bin/env python3
"""
Même raisonnement que la première version mais de manière itérative
"""
#from timeit import timeit
from sys import argv
from time import time
from geo.point import Point

def load_instance(filename):
    """
    loads .pts file.
    returns distance limit and points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]

    return distance, points


def construction_graphe(distance, points):
    """
    Fonction permettant de constuire un graphe à partir des données du problèmes.
    Ce graphe se construit en considérant voisin un point seulement ses voisins
    d'indices plus grand que lui-même.
    """
    liste_voisins=[[] for i in range(len(points))]
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            if Point.distance_to(points[i], points[j]) <= distance:
                liste_voisins[i].append(j)
                liste_voisins[j].append(i)
    return liste_voisins

def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    construction_graphe(distance, points)

def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)

t0=time()
main()
print(time()-t0)
