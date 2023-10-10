def lire(txt) :
    l1 = []
    l2 = []
    fichier = open(txt,"r")
    for ligne in fichier :
        n=len(ligne)
        c=''
        i=0
        while ligne[i]!=' ' :
            c=c+ligne[i]
            i=i+1
        l1.append(int(c))
        i=i+1
        b=''
        while i<n :
            b=b+ligne[i]
            i=i+1
        l2.append(float(b))
    fichier.close()
    return (l1,l2)


