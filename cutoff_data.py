import sqlite3


def read_db(rank: int, cat: str, place: str, branch: str):
    rank = rank * 0.9
    connection = sqlite3.connect('data.sqlite')
    with connection:
        cursor = connection.cursor()

        if 'ALL DISTRICTs' in place and 'ALL BRANCHES' in branch:
            query = f"Select code,college,place,branch,{cat} FROM engg_2021_r3 WHERE {cat} >= {rank} ORDER BY {cat}"

        elif 'ALL DISTRICTs' in place:
            query = f"Select code,college,place,branch,{cat} FROM engg_2021_r3 WHERE {cat} >= {rank} AND BRANCH in {branch} ORDER BY {cat}"

        elif 'ALL BRANCHES' in branch:
            query = f"Select code,college,place,branch,{cat} FROM engg_2021_r3 WHERE {cat} >= {rank} AND place in {place} ORDER BY {cat}"

        else:
            query = f"Select code,college,place,branch,{cat} FROM engg_2021_r3 WHERE {cat} >= {rank} AND place in {place} AND BRANCH in {branch} ORDER BY {cat}"

        cursor.execute(query)
        data = cursor.fetchall()

        return data

