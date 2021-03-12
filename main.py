#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from time import time
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


def graphe(distance, points):
    """ fonction qui construit mes sous graphes au fur et à mesure
    """
    convexe=[[points[0]]]
    for i in range (1, len(points)):
        boucle=True
        j=0
        l=[]
        while j <len(convexe):
            k=0
            while k < len(convexe[j]):
                if Point.distance_to(points[i], convexe[j][k])<=distance:
                    l.append(j)
                    boucle=False
                    break
                k+=1
            j+=1
        if not boucle:
            convexe[l[0]].append(points[i])
        while len(l)>1:
            convexe[l[0]]+= convexe[l[-1]]
            convexe[-1], convexe[l[-1]] = convexe[l[-1]], convexe[-1]
            l.pop()
            convexe.pop()
        if boucle:
            convexe.append([points[i]])
    return convexe


def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    graph=graphe(distance,points)
    L=[]
    for g in graph:
        if len(g)!=0:
            L.append(len(g))
    print(sorted(L, reverse=True))


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)

main()
