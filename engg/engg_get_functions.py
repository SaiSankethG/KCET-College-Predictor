from engg.engg_dataset import categories, branches, districts




def engg_get_rank(r):

    return int(r)


def engg_get_category(c):

    return categories[c]


def engg_get_branches(b):

    n = []

    for br in b:
        br = br.strip()

        if br in branches.keys():
            n.append(br)
        

    if len(n) == 1:

        return f"('{n[0]}')"


    elif len(n) != 0:

        return tuple(n)

       

def engg_get_places(p):

    n = []

    for pl in p:

        if pl in districts:
            n.append(pl)


    if len(n) == 1:
        return f"('{n[0]}')"


    elif len(n) != 0:

        return tuple(n)


    