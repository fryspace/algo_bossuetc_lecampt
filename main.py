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
    """
    permet de definir le maillage
    """
    return distance/1.4142135623730951


def construction_matrice(maille, points):
    """
    permet de definir la grille en fonction de la maille. 
    ajoute a chaque case les points qui lui appartiennent
    """
    nb = int(1/maille) + 1
    matrice_point = [[[]for _ in range(nb)] for _ in range(nb)]
    for point in points:
        c = point.coordinates
        i = int(c[0] // maille)
        j= int(c[1] // maille)
        matrice_point[i][j].append(point)
    return matrice_point

def est_connexe(case1, case2, distance):
    """
    permet de verifier si 2 cases sont connexes en parcourant les points dans les 2 cases
    """
    for point1 in case1:
        for point2 in case2:
            if point1.distance_to(point2) <= distance:
                return True
    return False


def trouver_borne( i, j, nb):
    """
    donne les bornes inferieurs et supperieurs des cases potentiellement connexes pour une case donnee en 
    fonction du nombre de cases dans la grille
    """
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


def construit_table_√©quivalence(matrice_point, maille, distance):
    """
    construit la liste des tailles des composantes connexes
    """
    nb = int(1/maille) + 1
    tableau_√©quiv = [ [None for _ in range(nb)] for _ in range(nb)]
    nouveau = 0
    composantes = {}
    for i in range(nb):
        for j in range(nb):
            if matrice_point[i][j] != []:
                i_min, i_max, j_min, j_max = trouver_borne(i, j, nb)
                attente={}
                for k in range(i_min, i_max + 1):
                    for l in range(j_min, j_max + 1):
                        if matrice_point[k][l] != []:
                            if est_connexe(matrice_point[i][j], matrice_point[k][l], distance):
                                attente[(k,l)]= tableau_√©quiv[k][l]
                classe = nouveau
                for cl√©, values in attente.items():
                    if values is not None:
                        classe=min(classe, values)
                tableau_√©quiv[i][j]=classe
                if classe not in composantes:
                    composantes[classe]= [(i,j)]
                    del attente[(i,j)]
                for cl√© , values in attente.items():
                    if values is None:
                        tableau_√©quiv[cl√©[0]][cl√©[1]] = classe
                        composantes[classe] += [cl√©]
                    elif values != classe:
                        liste = composantes[values]
                        composantes[classe] += liste
                        composantes[values] = []
                        for z in range(len(liste)):
                            z1, z2 = liste[z][0], liste[z][1]
                            tableau_√©quiv[z1][z2] = classe
                if nouveau == classe:
                    nouveau += 1
    liste= []
    for cl√©, values in composantes.items():
        compteur = 0
        for doublet in values:
            i = doublet[0]
            j = doublet[1]
            compteur += len(matrice_point[i][j])
        if compteur != 0:
            liste.append(compteur)
    return liste


def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    maille = maillage(distance)
    matrice_point= construction_matrice(maille, points)
    print(sorted(construit_table_√©quivalence(matrice_point, maille, distance), reverse=True))



def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
