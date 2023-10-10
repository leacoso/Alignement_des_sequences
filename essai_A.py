from mots import *
from tache_A import *
import ctypes
import time,os
import numpy as np
import matplotlib.pyplot as plt

def point_1() :

    (x,y) = mots("Inst_0000010_44.adn" )
    print("Pour Inst_0000010_44.adn " + " Dist = "+   str(dist_naif(x,y))+" \n")

    (x,y) = mots("Inst_0000010_7.adn" )
    print("Pour Inst_0000010_7.adn " + " Dist = "+   str(dist_naif(x,y))+" \n")

    (x,y) = mots("Inst_0000010_8.adn" )
    print("Pour Inst_0000010_8.adn " + " Dist = "+   str(dist_naif(x,y))+" \n")
    

def point_2() :

    fichiers = [filename for filename in os.listdir("Instances_genome")]
    fichiers.sort()
    fichiers = fichiers[1:]
    lenf = len(fichiers)
    i = 0 
    tracemalloc.start()
    while i<6: #Après 6, on depasse la minute
        f = open("Instances_genome/"+fichiers[i], "r")
        (x,y) = mots(fichiers[i])
        start = time.time()
        a = dist_naif(x,y)
        end = time.time()
        tmp = end-start
        mem_used, peak = tracemalloc.get_traced_memory()
        tracemalloc.clear_traces
        print(fichiers[i] + " Temps = "+ str(tmp) + " consommation mémoire "+  str(peak) +" \n")
        i = i+1

