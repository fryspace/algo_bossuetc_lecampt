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

def fusion (J,L):
    for l in L:
        J.append(l)
    L=[]

def recherche(L,M):
    for l in L:
        for m in range (0,len(M)):
            if l==M[m]: 
                
                return True
    return False

def graphe(distance, points):
    convexe=[[pts] for pts in points]
    for i in range (1, len(points)):
        j=0
        while j <i:
            k,l=0,j+1
            while l<i : #si dans 2 convexes il y a le même point on les concatene
                if convexe[l]!=[] and convexe[j]!=[]:    
                    if recherche(convexe[j], convexe[l]):
                        fusion(convexe[j], convexe[l][:-1])
                        break
                l+=1
            while k < len(convexe[j]): #on regarde dans chaque convexe déjà fait si i est voisin a un point
                if Point.distance_to(points[i], convexe[j][k])<=distance:
                    convexe[j].append(points[i])
                    convexe[i]=[]
                    break
                k+=1
            j+=1
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
