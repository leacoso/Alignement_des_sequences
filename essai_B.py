from tache_B import *
from mots import *
from lire_fichier import *
import matplotlib.pyplot as plt
import numpy as np
import os,time
from memory_profiler import *


def temps() :
    fichiers = [filename for filename in os.listdir("Instances_genome")]
    fichiers.sort()
    fichiers = fichiers[1:]
    lenf = len(fichiers)
    i=0
    ftmp=open("temps_cpu_B.txt","w")
    
    while i<52: #Après 51, le calcul prend plus de 10 minutes
        f = open("Instances_genome/"+fichiers[i], "r")
        (x,y) = mots(fichiers[i])
        le= len(x)
        start = time.time()
        a= prog_dyn(x,y)
        end = time.time()
        tmp = end-start
        ftmp.write(f"{le} {tmp} \n")
        print(f"{i}\n")
        i=i+1
        f.close()
    ftmp.close()



def courbe() :
    #temps() : on l'utilse pour générer le fichier et les valeurs
    (l1,l2) = lire("temps_cpu_B.txt")
    plt.plot(l1, l2)
    plt.title("Courbe du temps CPU en fonction de la taille |x|")
    plt.xlabel("Taille |x|")
    plt.ylabel("Temps CPU en secondes")
    plt.show()

def mem() :
    fichiers = [filename for filename in os.listdir("Instances_genome")]
    fichiers.sort()
    fichiers = fichiers[1:]
    lenf = len(fichiers)
    i=50 # grande insatnce
    tracemalloc.start()
    f = open("Instances_genome/"+fichiers[i], "r")
    (x,y) = mots(fichiers[i])
    a= prog_dyn(x,y)
    (mem_used, peak) = tracemalloc.get_traced_memory()
    print("Consommation memoire pour "+"Instances_genome/"+fichiers[i]+" : "+str(peak))



    
