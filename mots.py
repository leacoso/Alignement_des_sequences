chemin_fichier = "./Instances_genome/"

def mots(fichier):
    f = open(chemin_fichier+fichier, "r")
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

    return (x,y)
