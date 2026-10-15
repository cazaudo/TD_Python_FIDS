def lecture_csv(fichier: str, sep: str=",") -> list[dict]:

    data = []
    with open(fichier, "r") as f:
        lines = f.read().splitlines()
        keys = lines[0].split(sep)
        for line in lines[1:]:
            values = line.split(sep)
            data.append(dict(zip(keys, values)))
    return data

def discretisation(x, seuils):
    for i in range(len(seuils)-1):
        if x >= seuils[i] and x < seuils[i+1]:
            return i

def compte(y: list[int | str]) -> dict[int | str, int]:
    label = []
    for i in range(len(y)):
        if y[i] not in label:
            label.append(y[i])
    nombre = dict()
    for k in range(len(label)):
        nombre[label[k]] = 0
    for i in range(len(y)):
        nombre[y[i]] += 1
    return nombre
    
def est_identique(d1, d2, attributs):
    for a in attributs:
        if d1[a] != d2[a]:
            return False
    return True

def groupe(data, attributs):
    n = len(data)
    G = [0] * n
    idx = 1
    for i in range(n):
        if G[i] == 0: # Nouveau groupe
            G[i] = idx
            for j in range(i+1, n):
                if est_identique(data[i], data[j], attributs):
                    G[j] = idx
            idx += 1
    return G

def k_anonymite(data, attributs):
    G = groupe(data, attributs)
    return min(compte(G).values())
    
