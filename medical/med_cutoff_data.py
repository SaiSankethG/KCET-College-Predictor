import sqlite3


def med_read_db(rank: int, cat: str, place: str, seat_type: str):
    rank = rank * 0.9
    connection = sqlite3.connect('medical/med_r2_2021.sqlite')
    with connection:
        cursor = connection.cursor()

        if 'ALL DISTRICTs' in place and 'ALL seat_type' in seat_type:
            query = f"Select code,college,place,seat_type,{cat} FROM med_r2_2021 WHERE {cat} >= {rank} ORDER BY {cat}"

        elif 'ALL DISTRICTs' in place:
            query = f"Select code,college,place,seat_type,{cat} FROM med_r2_2021 WHERE {cat} >= {rank} AND seat_type in {seat_type} ORDER BY {cat}"

        elif 'ALL seat_type' in seat_type:
            query = f"Select code,college,place,seat_type,{cat} FROM med_r2_2021 WHERE {cat} >= {rank} AND place in {place} ORDER BY {cat}"

        else:
            query = f"Select code,college,place,seat_type,{cat} FROM med_r2_2021 WHERE {cat} >= {rank} AND place in {place} AND seat_type in {seat_type} ORDER BY {cat}"

        cursor.execute(query)
        data = cursor.fetchall()

        return data

