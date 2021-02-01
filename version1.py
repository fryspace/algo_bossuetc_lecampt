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

def construction_tableau_classe(graphe):
    



def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
