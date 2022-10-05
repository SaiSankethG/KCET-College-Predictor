from medical.med_dataset import categories, seat_type, districts




def med_get_rank(r):

    return int(r)


def med_get_category(c):

    return categories[c]


def med_get_seat_type(b):

    n = []

    for br in b:
        br = br.strip()

        if br in seat_type:
            n.append(br)
        

    if len(n) == 1:

        return f"('{n[0]}')"


    elif len(n) != 0:

        return tuple(n)

       

def med_get_places(p):

    n = []

    for pl in p:

        if pl in districts:
            n.append(pl)


    if len(n) == 1:
        return f"('{n[0]}')"


    elif len(n) != 0:

        return tuple(n)


    