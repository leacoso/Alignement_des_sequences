import numpy as np

c_del=2
c_ins = 2

def c_sub(x,y) :
    if x==y :
        return 0
    if (x,y)==('A','T') or (x,y)==('G','C') or (x,y)==('T','A') or (x,y)==('C','G') :
        return 3
    return 4


def DIST_2 (x,y):
    n = len(x)
    m = len(y)
    T = np.zeros((2,m+1),int)

    for i in range(0,2) :
        T[i][0] = c_del*i

    for j in range(0,m+1) :
        T[0][j] = c_ins * j

    for i in range(1,n+1) :
        for j in range(0,m+1) :
            if j==0 :
                T[1,j] = T[0][j] + c_del
            else :
                T[1][j]  = min(T[0][j] + c_del , T[1][j-1] + c_ins, T[0][j-1] + c_sub(x[i-1],y[j-1]))
        for k in range(0,m+1) :
            T[0][k] = T[1][k]

    return T[1][m]



