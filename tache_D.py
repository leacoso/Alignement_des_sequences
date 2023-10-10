import numpy as np
from math import *

c_del=2
c_ins = 2

def c_sub2(x,y) :
    if x!=y :
        return 1
    return 0

def c_sub(x,y) :
    if x==y :
        return 0
    if (x,y)==('A','T') or (x,y)==('G','C') or (x,y)==('T','A') or (x,y)==('C','G') :
        return 3
    return 4

def mot_gaps (k):
    return '_'*k

def teste_lettre (x,l):
    for i in range (0,len(x)) :
        if x[i] ==l :
            return i
    return -1

def teste_complementaire(x,l):
    for i in range (0,len(x)) :
        if (x[i] in {'A','T'} and l in {'A','T'}) or (x[i] in {'C','G'} and l in {'C','G'}) :
            return i
    return -1

def align_lettre_mot (x, y):
    lettre = teste_lettre(y,x[0])
    complementaire = teste_complementaire(y,x[0])
    l = len(y)
    res = list(mot_gaps(l))

    if lettre >= 0 :
        res[lettre] = x[0]
        a = "".join(res)
        return (a,y)

    if complementaire >= 0 :
        res[complementaire] = x[0]
        a = "".join(res)
        return (a,y)

    res[0] = x[0]
    a = "".join(res)
    return (a,y)


def coupure(x,y) :
    n=len(x)
    m=len(y)
    i=floor(n/2)
    T=np.zeros((2,m+1),int)
    I=np.zeros((2,m+1),int)
    for i2 in range(0,2) :
        T[i2][0] = c_del*i2
        I[i2][0] = 0
    for j2 in range(0,m+1) :
        T[0][j2] = c_ins * j2
        I[0][j2] = j2

    for k in range(1,n+1) :
        for j in range(0,m+1) :
            if j==0 :
                T[1][j] = T[0][j] + c_del
            else:
                T[1][j]  = min(T[0][j] + c_del , T[1][j-1] + c_ins, T[0][j-1] + c_sub(x[k-1],y[j-1]))

            if k>i :
                if j==0 :
                    I[1][j] = I[0][j]
                else :
                    if T[1][j] == T[0][j] + c_del :
                        I[1][j] = I[0][j]
                    elif T[1][j] == T[1][j-1] + c_ins :
                        I[1][j] = I[1][j-1]
                    elif T[1][j] == T[0][j-1] + c_sub(x[k-1],y[j-1]) :
                        I[1][j] = I[0][j-1]

        for k2 in range(0,m+1) :
            if k> i :
                I[0][k2] = I[1][k2]
            T[0][k2] = T[1][k2]
    return I[1][m]




def sol_2(x,y) :
	n=len(x)
	m=len(y)
	if m==0 :
		s=mot_gaps(n)
		return(x,s)
	if n==1 and m>0 :
	    s= align_lettre_mot(x,y)
	    return s

	i = floor(n/2)
	j = coupure(x,y)

	(x1,y1)= sol_2(x[0:i],y[0:j])
	(x2,y2) = sol_2(x[i:n+1],y[j:m+1])

	return tuple( map( lambda i,j : i+j, (x1,y1) , (x2,y2) ))




