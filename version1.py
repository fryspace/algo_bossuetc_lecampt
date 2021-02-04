#!/usr/bin/env python3
"""
Première version de la résolution du problème d'algo, les entrées du programme sont
s la disctance minimale entre deux voisins et la liste des points et leurs coordonnées
"""
#from timeit import timeit
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

def traitement_sommet(graphe, tableau, valeur, sommet):
    """
    Fonction récursive permettant de traiter récursivement les sommets d'un graphe suivant la
    méthode de notre algorithme
    """
    for elem in graphe[sommet]:
        if tableau[elem] > valeur:
            tableau[elem]=valeur
            traitement_sommet(graphe,tableau, valeur, elem)
        else:
            tableau[valeur]=tableau[elem]
    return tableau



def construction_tableau_classe(graphe):
    """
    On construit le tableau des classes à partir de notre graphe et on le renvoie
    """
    tableau=[sommet for sommet in range(len(graphe))]
    for sommet in range(len(graphe)):
        if tableau[sommet] == sommet:
            tableau = traitement_sommet(graphe, tableau, sommet, sommet)
    return tableau


def construction_dico(tableau):
    """
    Construction d'un dictionnaire pour agréger les composantes entre elles
    """
    dictionnaire={}
    for counter, value in enumerate(tableau):
        if counter == value:
            dictionnaire[value]= 1
        else:
            dictionnaire[value]=dictionnaire[value] + 1
    return dictionnaire

def construction_liste(dictionnaire):
    """
    A partir du dictionnaire, on peut créer une liste avec les tailles des composantes connexes
    """
    liste=[]
    for clé in dictionnaire:
        liste.append(dictionnaire[clé])
    return liste

def sort(tableau1,tableau2):
    """
    Permet de faire la fusion de deux tableaux pour le tri fusion
    """
    if len(tableau1)==0:
        return tableau2
    if len(tableau2)==0:
        return tableau1
    if tableau1[0]>tableau2[0]:
        return [tableau1[0]] + sort(tableau1[1:],tableau2)
    else:
        return [tableau2[0]] + sort(tableau1,tableau2[1:])


def mergesort(tableau):
    """
    Réalise un tri fusion sur un tableau
    """
    if len(tableau) == 1:
        return tableau
    else:
        center = len(tableau) // 2
        left   = mergesort(tableau[:center])
        right  = mergesort(tableau[center:])
        return sort(left,right)





def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    graphe=construction_graphe(distance, points)
    tableau = construction_liste(construction_dico(construction_tableau_classe(graphe)))
    print(mergesort(tableau))



def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
