#!/usr/bin/python3
""" script that takes in an argument and
displays all values in the states"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
        )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE '{:s}'\
        ORDER BY id ASC".format(argv[4])
    )

    for states in cur.fetchall():
        if states[1] == argv[4]:
            print(states)
    cur.close()
    db.close()
