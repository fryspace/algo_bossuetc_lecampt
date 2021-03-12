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

def update_clé_quad(quad1, quad2):
    """
    permet d'update la clé à partir de deux quad
    """
    return ( min(quad1[0], quad2[0]), max(quad1[1], quad2[1]),
             min(quad1[2], quad2[2]), max (quad1[3], quad2[3]))

def update_clé_quad_point(point, quad, distance):
    """
    permet d'update la clé à partir d'un quad et d'un point
    """
    c = point.coordinates
    return (min(max(c[0] - distance, 0), quad[0]), max(min(c[0] + distance, 1), quad[1]),
            min(max(c[1] - distance, 0), quad[2]), max(min(c[1] - distance, 1), quad[3]))


def est_dans_carré(point, quad):
    """
    vérifie si un point est dans un quad
    """
    c = point.coordinates
    if quad[0] <= c[0] <= quad[1] and quad[2] <= c[1]<= quad[3]:
        return True
    else:
        return False

def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    composantes = {}
    for point in points:
        print(composantes)
        l=[]
        for clé, value in composantes.items():
            if est_dans_carré(point, clé):
                for point_in in value:
                    if point.distance_to(point_in) <= distance:
                        l.append(clé)
                        break
        if l == []:
            c= point.coordinates
            composantes[(max(c[0]-distance, 0), min(c[0]+distance, 1),
                         max(c[1]- distance, 0), min(c[1]+distance, 1))] = [point]
        else:
            while len(l) > 1:
                quad = update_clé_quad(l[0], l[-1])
                composantes[l[0]] += composantes.pop(l[-1])
                composantes[quad]=composantes.pop(l[0])
                l[0]=quad
                l.pop()
            composantes[l[0]] += [point]
            quad = update_clé_quad_point(point, l[0], distance)
            composantes[quad] = composantes.pop(l[0])
    liste_composante=[]
    for clé, value in composantes.items():
        liste_composante.append(len(value))
    print(sorted(liste_composante, reverse=True))


                


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
