def lecture_csv(fichier: str, sep: str=",") -> list[dict]:

    data = []
    with open(fichier, "r") as f:
        lines = f.read().splitlines()
        keys = lines[0].split(sep)
        for line in lines[1:]:
            values = line.split(sep)
            data.append(dict(zip(keys, values)))
    return data