import numpy as np
from tache_A import *


c_del= 2
c_ins = 2


def c_sub (a,b):
    if (a==b):
        return 0
    elif (a in {'A', 'T'} and b in {'A', 'T'}) or (a in {'C', 'G'} and b in {'C', 'G'}) :
        return 3
    return 4

def c_sub3(x,y) :
    if x==y :
        return 0
    elif (x=='A' or x=='E' or x=='I' or x=='O' or x=='U' or x=='Y') and (y=='A' or y=='E' or y=='I' or y=='O' or y=='U' or y=='Y') :
        return 5
    elif (x=='A' or x=='E' or x=='I' or x=='O' or x=='U' or x=='Y') :
        return 7
    elif (y=='A' or y=='E' or y=='I' or y=='O' or y=='U' or y=='Y') :
        return 7
    return 5


def sol_1 (x,y,T) :
    i=len(x)
    j=len(y)
    s=""
    t=""

    while i>0 and j>0 :
        if T[i,j] == T[i-1,j-1] + c_sub(x[i-1],y[j-1]) :
            s=x[i-1]+s
            t=y[j-1]+t
            i=i-1
            j=j-1
        elif T[i,j] == T[i,j-1] + c_ins :
            s="_"+s
            t=y[j-1]+t
            j=j-1
        elif T[i,j] == T[i-1,j] + c_del :
            s=x[i-1]+s
            t="_"+t
            i=i-1

    while i>0 :
        if T[i,j] == T[i-1,j] + c_del :
            s=x[i-1]+s
            t="_"+t
        i=i-1

    while j>0 :
        if T[i,j] == T[i,j-1] + c_ins :
            s="_"+s
            t=y[j-1]+t
        j=j-1
    return (s,t)

def dist_1(x,y,T) :
    n = len(x)
    m = len(y)

    for i in range(n+1) :
        T[i,0] = c_del *i

    for j in range(m+1) :
        T[0,j] = c_ins * j

    for i in range(1,n+1) :
        for j in range(1,m+1) :
            T[i,j] = min(T[i-1,j] + c_del , T[i,j-1] + c_ins, T[i-1,j-1] + c_sub(x[i-1],y[j-1]))

    return T[n][m]


def prog_dyn(x,y) :
    n=len(x)
    m=len(y)
    T = np.zeros((n+1,m+1),int)
    a=dist_1(x,y,T)
    c=sol_1(x,y,T)
    return (a,c)

