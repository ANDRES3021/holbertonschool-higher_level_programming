#!/usr/bin/python3
"""script that takes in the name of a state
as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
        )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name\
            FROM cities INNER JOIN states ON cities.state_id=states.id\
                WHERE states.name=%s ORDER BY cities.state_id ASC",
        (argv[4],)
    )
    print(", ".join([cities[0] for cities in cur.fetchall()]))
    cur.close()
    db.close()
