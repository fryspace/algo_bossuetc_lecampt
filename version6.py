#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
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


def est_connexe(composante1, composante2, distance):
    if composante1 is None or composante2 is None:
        return False
    for i in range(len(composante1)):
        for j in range(len(composante2)):
            if composante1[i].distance_to(composante2[j]) <= distance:
                return True
    return False 


def fusion_partition(partition1, partition2, distance):
    for composante2 in partition2:
        L=[]
        for i, composante1 in enumerate(partition1):
            if est_connexe(composante1, composante2, distance):
                L.append(i)
        if len(L)==0:
            partition1+=[composante2]
        elif len(L)==1:
            partition1[L[0]] += composante2
        else:
            partition1[L[0]] += composante2
            for i in range(1, len(L)):
                partition1[L[0]] += partition1[L[i]]
                partition1[L[i]]=None
            for i in range(len(partition1)-1, 0, 1):
                if partition1[i] is None:
                    partition1[i], partition1[-1] = partition1[-1], partition1[i]
                    partition1.pop()


def procédure_formation(points, distance):
    L=[]
    for i in range(len(points)):
        L.append([[points[i]]])
    n=len(L)
    while n!=1:
        if n%2==1:
            fusion_partition(L[n-2],L[n-1], distance)
            L[n-1]=None
            n-=1
        elif n==2:
            fusion_partition(L[0],L[1],distance)
            L[1]=None
            n=1
        else:
            for i in range(0,n,2):
                fusion_partition(L[i], L[i+1], distance)
            if (n/2)%2==1:
                for i in range(1, int(len(L)/2),2):
                    L[i],L[int(n/2)+i]=L[int(n/2)+i], None
                for i in range(int(n/2),n):
                    L[i]=None
            else:
                for i in range(1,int(n/2 +1),2):
                    L[i],L[int(n/2)+i-1]=L[int(n/2)+i-1], None
                for i in range(int(n/2),n):
                    L[i]=None
            n= int(n/2)
    liste_composante=[]
    for elem in L[0]:
        if elem is not None:
            liste_composante.append(len(elem))
    return liste_composante

def nombre_elem(L,n):
    compteur=0
    for i in range(int(n)):
        for composante in L[i]:
            compteur+=len(composante)
    return compteur
        



def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    liste_composante=procédure_formation(points, distance)
    print(sorted(liste_composante, reverse=True))


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
