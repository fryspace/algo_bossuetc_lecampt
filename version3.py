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
            if Point.distance_to(points[i], points[j]) <= distance:
                voisins.append(j)
        liste_voisins.append(voisins)
    return liste_voisins


def construction_tableau_classe_iter(graphe):
    """
    construit le tableau des classes de manière itératives
    """
    tableau=[ sommet for sommet in range(len(graphe))]
    tableau_indice=[0 for i in range(len(graphe))]
    L=[]
    indice_ajout=0
    for i in range(len(graphe)):
        if tableau[i]== i:
            stack=[i]
            compteur=1
            while len(stack)!= 0:
                sommet_traité=stack.pop()
                if tableau[sommet_traité] > tableau[i]:
                    tableau[sommet_traité] = tableau[i]
                    compteur+=1
                elif tableau[sommet_traité] < tableau[i]:
                    tableau[i]=tableau[sommet_traité]
                stack += graphe[sommet_traité]
            if tableau[i]==i:
                tableau_indice[i]=indice_ajout
                indice_ajout+=1
                L.append(compteur)
            else:
                L[tableau_indice[tableau[i]]]+=compteur
    return L



def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    graphe=construction_graphe(distance, points)
    classe=construction_tableau_classe_iter(graphe)
    print(sorted(classe,reverse=True))



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
