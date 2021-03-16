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


def maillage(distance):
    return distance/1.4142135623730951


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


def trouver_borne( i, j, nb):
    i_max = i + 2
    j_min = j - 2
    j_max = j + 2
    i_min = i - 2
    if i_min < -1:
        i_min=0
    elif i_min < 0:
        i_min = i-1
    if i_max > nb - 2:
        i_max = i
    elif i_max > nb - 1:
        i_max = i + 1
    if j_min < -1:
        j_min= j
    elif j_min < 0:
        j_min= j-1
    if j_max > nb-2:
        j_max = j
    elif j_max > nb-1:
        j_max = j+1
    return i_min, i_max, j_min, j_max


def construit_table_équivalence(matrice_point, maille, distance):
    nb = int(1/maille) + 1
    liste_classe={}
    tableau_équiv = [ [None for _ in range(nb)] for _ in range(nb)]
    nouveau = 0
    for i in range(nb):
        for j in range(nb):
            if matrice_point[i][j] != []:
                i_min, i_max, j_min, j_max = trouver_borne(i, j, nb)
                attente={}
                for k in range(i_min, i_max + 1):
                    for l in range(j_min, j_max + 1):
                        if matrice_point[k][l] != []:
                            if est_connexe(matrice_point[i][j], matrice_point[k][l], distance):
                                attente[(k,l)]= tableau_équiv[k][l]
                classe = nouveau
                for clé, values in attente.items():
                    if values is not None:
                        classe=min(classe, values)
                tableau_équiv[i][j]=classe
                for clé , values in attente.items():
                    tableau_équiv[clé[0]][clé[1]]= classe
                if classe == nouveau:
                    nouveau+=1
    for i in range(nb-1, -1, -1):
        for j in range(nb-1, -1, -1):
            i_min, i_max, j_min, j_max = trouver_borne(i, j, nb)
            attente={}
            for k in range(i_min, i_max + 1):
                for l in range(j_min, j_max + 1):
                    if tableau_équiv[k][l] is not None and est_connexe(matrice_point[i][j], matrice_point[k][l], distance):
                        attente[(k,l)]=tableau_équiv[k][l]
            classe = tableau_équiv[i][j]
            for clé, values in attente.items():
                classe=min(classe, values)
            for clé , values in attente.items():
                tableau_équiv[clé[0]][clé[1]]= classe
    for i in range(nb):
        for j in range(nb):
            if tableau_équiv[i][j] is None:
                pass
            elif tableau_équiv[i][j] not in liste_classe:
                liste_classe[tableau_équiv[i][j]]= len(matrice_point[i][j])
            else:
                liste_classe[tableau_équiv[i][j]] += len(matrice_point[i][j])
    liste= []
    for clé, values in liste_classe.items():
        liste.append(values)
    return liste




def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    maille = maillage(distance)
    matrice_point= construction_matrice(maille, points)
    print(sorted(construit_table_équivalence(matrice_point, maille, distance), reverse=True))


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
