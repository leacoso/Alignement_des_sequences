,import time
from mots import *
from tache_C import *
from tache_B import *
from lire_fichier import *
import matplotlib.pyplot as plt
import numpy as np
import os

def temps_dist1() :
    fichiers = [filename for filename in os.listdir("Instances_genome")]
    fichiers.sort()
    fichiers = fichiers[1:]
    lenf = len(fichiers)
    i=0
    ftmp=open("temps_cpu_C_dist_1.txt","w")

    while i<49 : #Après 48, le temps de calcul dépasse 10 minutes
        f = open("Instances_genome/"+fichiers[i], "r")
        (x,y) = mots(fichiers[i])
        le = len(x)
        m=len(y)
        T = np.zeros((le+1,m+1),int)
        start = time.time()
        b = dist_1(x,y,T)
        end = time.time()
        tmp = end-start
        ftmp.write(f"{le} {tmp} \n")
        f.close()
        print(f"{i}\n")
        i=i+1
    ftmp.close()


def temps_dist2() :
    fichiers = [filename for filename in os.listdir("Instances_genome")]
    fichiers.sort()
    fichiers = fichiers[1:]
    lenf = len(fichiers)
    i=0
    ftmp=open("temps_cpu_C_dist_2.txt","w")

    while i<49 : #Après 48, le temps de calcul dépasse 10 minutes
        f = open("Instances_genome/"+fichiers[i], "r")
        (x,y) = mots(fichiers[i])
        le = len(x)
        start = time.time()
        b = DIST_2(x,y)
        end = time.time()
        tmp = end-start
        ftmp.write(f"{le} {tmp} \n")
        f.close()
        print(f"{i}\n")
        i=i+1
    ftmp.close()



def comparaison_dist1_dist2() :
    (l1,l2) = lire("temps_cpu_C_dist_1.txt")
    plt.plot(l1, l2,label="DIST_1")
    plt.legend()
    (l3,l4 ) = lire("temps_cpu_C_dist_2.txt")
    plt.plot(l1,l4,label="DIST_2")
    plt.legend()
    plt.title("Courbe du temps CPU en fonction de la taille |x|")
    plt.xlabel("Taille |x|")
    plt.ylabel("Temps CPU en secondes")
    plt.show()

def mem_dist2():
    tracemalloc.start()
    (x,y) = mots("Inst_0015000_3.adn")
    dist = DIST_2(x,y)
    mem_used, peak = tracemalloc.get_traced_memory()
    tracemalloc.clear_traces()
    print("Consommation mémoire de " + "Inst_0015000_3.adn"+ str(peak))

