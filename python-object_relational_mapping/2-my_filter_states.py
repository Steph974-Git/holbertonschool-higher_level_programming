#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",      # Adresse du serveur MySQL
        port=3306,             # Port par défaut
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    #!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",      # Adresse du serveur MySQL
        port=3306,             # Port par défaut
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(search_name)
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)



    cursor.close()
    db.close()
