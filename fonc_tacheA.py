positive_infinity = float('inf')
chemin_fichier = "./INSTANCES/"
import numpy as np
import time,os, psutil
c_del = 2
c_ins = 2

def c_sub1 (a,b):
    if (a==b):
        return 0
    elif (a in {'A', 'T'} and b in {'A', 'T'}) or (a in {'C', 'G'} and b in {'C', 'G'}) :
        return 3
    return 4

def dist_naif_rec (x,y,i,j,c,dist) :
    lenx = len(x)
    leny = (len(y))
    if (i == (lenx)) and (j == (leny)) :
        if (c<dist):
            dist = c
    else :
        if (i < (lenx)) and (j < (leny)) :
            dist = dist_naif_rec(x,y,i+1,j+1,c+c_sub1(x[i],y[j]),dist)
        if (i < (lenx)) :
            dist = dist_naif_rec(x,y,i+1,j,c+c_del,dist )
        if (j<(leny)):
            dist = dist_naif_rec(x,y,i,j+1,c+c_ins,dist)

    return dist


def dist_naif(x,y):
    process1 = psutil.Process(os.getpid())
    print(process1)
    process3 = process1.memory_info().rss
    print(process3)
    b=dist_naif_rec (x,y,0,0,0,positive_infinity )
    process2 = psutil.Process(os.getpid())
    process4 = process2.memory_info().rss
    print(process4)
    return process4-process3

chemin_fichier = "./Instances_genome/"

f = open(chemin_fichier+"Inst_0000012_32.adn", "r")
n = f.readline()
m = f.readline()
x1 = f.readline()
y1 = f.readline()
x=''
y=''
for c in x1[: len(x1)-1] :
    if c != ' ':
        x = x + c

for c in y1[: len(y1)-1] :
    if c != ' ':
        y = y + c

f.close()
print("Pour Inst_0000012_32.adn " + " Nombre octets = "+   str(dist_naif(x,y))+" \n")





