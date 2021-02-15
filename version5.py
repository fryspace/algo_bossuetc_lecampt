#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""
from time import time
from timeit import timeit
from sys import argv

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



def construction_composante(distance, points):
    """
    à partir d'une liste trié de point par ordre lexicographique
    """
    visité=[i for i in range(len(points))]
    composante=[]
    for i in range(len(visité)):
        if visité[i]==i:
            compteur=1
            stack=[i]
            while stack != []:
                k=stack.pop()
                for j in range(1,len(points)):
                    if points[k].distance_to(points[j]) <= distance and visité[j]!=i:
                        visité[j]=i
                        compteur+=1
                        stack.append(j)
            composante.append(compteur)
    return composante


def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    print(sorted(construction_composante(distance, points), reverse=True))


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)

t0=time()
main()
t1=time()
print(t1-t0)
