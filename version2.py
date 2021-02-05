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
    liste_voisins=[]
    taille=len(points)
    for i in range(taille):
        voisins=[]
        for j in range(i+1,taille):
            if Point.distance_to(points[i], points[j]) < distance:
                voisins.append(j)
        liste_voisins.append(voisins)
    return liste_voisins


def construction_tableau_classe_iter(graphe):
    """
    construit le tableau des classes de manière itératives
    """
    tableau=[sommet for sommet in range(len(graphe))]
    for sommet in tableau:
        if tableau[sommet] == sommet:
            stack=[sommet]
            while len(stack)!= 0:
                sommet_traité=stack.pop()
                if tableau[sommet_traité] > sommet:
                    tableau[sommet_traité] = sommet
                else:
                    tableau[sommet]=tableau[sommet_traité]
                stack += graphe[sommet_traité]
    return tableau


def construction_tableaubis(tableau):
    tab_class=[0 for i in range(len(tableau))]
    for elem in tableau:
        tab_class[elem]+=1
    return tab_class

def construction_composante(tableau):
    tab_composante=[]
    for taille in tableau:
        if taille != 0:
            tab_composante.append(taille)
    return tab_composante


def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    graphe=construction_graphe(distance, points)
    classe=construction_tableau_classe_iter(graphe)
    tableau = construction_composante(construction_tableaubis(classe))
    print(sorted(tableau, reverse=True))



def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
