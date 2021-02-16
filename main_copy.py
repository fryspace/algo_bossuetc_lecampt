#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

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


def graphe(distance, points):
    convexe=[[points[0]]]
    for i in range (1, len(points)):
        boucle=True
        bcl=True
        j=0
        while j <len(convexe) and boucle:
            k=0
            while k < len(convexe[j])  and bcl:
                if Point.distance_to(points[i], convexe[j][k])<=distance:
                    convexe[j].append(points[i])
                    bcl,boucle=False, False
                k+=1
            j+=1
        if boucle:
            convexe.append([points[i]])
    return convexe



def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    graph=graphe(distance,points)
    print(sorted([len(g) for g in graph], reverse=True))


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
