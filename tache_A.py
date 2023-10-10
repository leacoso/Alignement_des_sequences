positive_infinity = float('inf')
from memory_profiler import *
import numpy as np
c_del = 2
c_ins = 2

def c_sub1 (a,b):
    if (a==b): 
        return 0
    elif (a in {'A', 'T'} and b in {'A', 'T'}) or (a in {'C', 'G'} and b in {'C', 'G'}) : 
        return 3
    return 4

def complementaire(a,b): 
    return (a in {'A','T'} and b in {'A','T'}) or (a in {'C','G'} and b in {'C','G'})


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
    return dist_naif_rec (x,y,0,0,0,positive_infinity )

