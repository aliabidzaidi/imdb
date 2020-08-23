import sqlite3
from sqlite3 import Error as dbError


class Database:

    conn = None

    def __init__(self):
        try:
            self.conn = sqlite3.connect('IMdb.db')
            print('DB connection created successfully, sqlite version: ',
                  sqlite3.version)

        except dbError as ex:
            print(ex)

    def __del__(self):
        print('destructor called')
        if self.conn:
            self.conn.close()

    def get_all_titles(self):
        try:
            rows = self.conn.execute('Select * from Title').fetchall()

            for row in rows:
                print(row)

        except dbError as ex:
            print(ex)

    def insert_title(self, id, titleType, primaryTitle, originalTitle, isAdult,
                     startYear, endYear, runtimeMinutes, genres):
        try:
            # print('Inserting into DB')
            cursor = self.conn.cursor()

            fieldNames = "(id, titleType, primaryTitle,originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)"
            query = "INSERT into Title" + fieldNames + \
                " VALUES (?,?,?,?,?,?,?,?,?)"

            cursor.execute(query, (id, titleType, primaryTitle, originalTitle, isAdult,
                                   startYear, endYear, runtimeMinutes, genres))
            self.conn.commit()

            # print(id, ' inserted successfully')

        except dbError as ex:
            print(id, ex)


if __name__ == "__main__":
    # print('trying to connect to DB')
    db = Database()
    db.insert_title("tt0000003", "short", "Pauvre Pierrot",
                    "Pauvre Pierrot", 0, 1892, None, 4, "Animation,Comedy,Romance")

    # create_connection()
    # tconst	titleType	primaryTitle	originalTitle	isAdult	startYear	endYear	runtimeMinutes	genres
    # Convert \N to None
    # Convert genres to Comma-seperated string
    # insert_title("tt0000002", "short", "Le clown et ses chiens",
    #              "Le clown et ses chiens", 0, 1892, None, 5, "Animation,Short")

    # insert_title("tt0000003", "short", "Pauvre Pierrot",
    #              "Pauvre Pierrot", 0, 1892, None, 4, "Animation,Comedy,Romance")
