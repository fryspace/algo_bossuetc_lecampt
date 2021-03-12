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


def maillage(distance):
    départ = Point([0,0])
    opposée = Point([distance, distance])
    maille = départ.distance_to(opposée)
    return maille

def construction_matrice(maille, points):
    nb = int(1/maille) + 1
    matrice_point = [[[]for _ in range(nb)] for _ in range(nb)]
    for point in points:
        c = point.coordinates
        i = int(c[0] // maille)
        j= int(c[1] // maille)
        matrice_point[i][j].append(point)
    return matrice_point

def est_connexe(case1, case2, distance):
    for point1 in case1:
        for point2 in case2:
            if point1.distance_to(point2) <= distance:
                return True
    return False


def actualiser_classe( i, j, nb):
    min = None
    i_max = i + 2
    j_min = j - 2
    j_max = j + 2 
    if i_max > nb - 2:
        i_max = i
    if i_max > nb - 1: 
        i_max = i + 1 
    if 
    
    
    
        
            


def construit_table_équivalence(matrice_point, maille):
    nb = int(1/maille) + 1
    l=[]
    tableau_équiv = [ [None for _ in range(nb)] for _ in range(nb)]
    nouveau = 0 
    for i in range(nb):
        for j in range(nb):
            if matrice_point[i][j] != []:
                




def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    pass #TO DO


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
