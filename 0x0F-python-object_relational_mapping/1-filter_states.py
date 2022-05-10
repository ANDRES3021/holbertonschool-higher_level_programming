#!/usr/bin/python3
"""lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for states in cur.fetchall():
        if states[1][0] == "N":
            print(states)
    cur.close()
    db.close()
