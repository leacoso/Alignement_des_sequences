import time
from tache_D import *
from tache_B import *
from lire_fichier import *
import matplotlib.pyplot as plt
import numpy as np
from memory_profiler import *
from mots import *
import os


def temps_sol2() :
    fichiers = [filename for filename in os.listdir("Instances_genome")]
    fichiers.sort()
    fichiers = fichiers[1:]
    lenf = len(fichiers)
    i=0
    ftmp=open("temps_cpu_D.txt","w")
    while i<44: #Après 43, le calcul prend plus de 10 minutes
        f = open("Instances_genome/"+fichiers[i], "r")
        (x,y) = mots(fichiers[i])
        le = len(x)
        start = time.time()
        b = sol_2(x,y)
        end = time.time()
        tmp = end-start
        ftmp.write(f"{le} {tmp} \n")
        f.close()
        print(f"{i}\n")
        i=i+1
    ftmp.close()


def courbe_sol_2() :
    #temps() : on l'utilse pour générer le fichier et les valeurs
    (l1,l2) = lire("temps_cpu_D.txt")
    plt.plot(l1, l2)
    plt.title("Courbe du temps CPU en fonction de la taille |x|")
    plt.xlabel("Taille |x|")
    plt.ylabel("Temps CPU en secondes")
    plt.show()

def courbe_comparaison_sol() :
    (l1,l2) = lire("temps_cpu_D.txt")
    (l3,l4) = lire("temps_cpu_B.txt")
    plt.plot(l1, l2,label="SOL_2")
    plt.legend()
    plt.plot(l3,l4,label="PROG_DYN")
    plt.legend()
    plt.title("Courbe du temps CPU en fonction de la taille |x|")
    plt.xlabel("Taille |x|")
    plt.ylabel("Temps CPU en secondes")
    plt.show()

def mem_sol2() :
    fichiers = [filename for filename in os.listdir("Instances_genome")]
    fichiers.sort()
    fichiers = fichiers[1:]
    lenf = len(fichiers)
    i=43 # grande instance
    tracemalloc.start()
    f = open("Instances_genome/"+fichiers[i], "r")
    (x,y) = mots(fichiers[i])
    a= sol_2(x,y)
    (mem_used, peak) = tracemalloc.get_traced_memory()
    print("Consommation memoire pour "+"Instances_genome/"+fichiers[i]+" : "+str(peak))

courbe_comparaison_sol()
