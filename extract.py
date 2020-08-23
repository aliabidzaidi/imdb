import csv
from db import Database
import sqlite3
from sqlite3 import Error as dbError


conn = sqlite3.connect('IMdb.db')

def main():
    with open("TSVs/test.tsv", encoding='utf-8') as tsv:
        tsvReader = csv.reader(tsv, delimiter='\t')

        # count = sum(1 for line in tsvReader)
        # print('Count of records: ', count)
        # db = Database()

        for line in tsvReader:

            for index, val in enumerate(line):
                if val == '\\N':
                    line[index] = None

            print(line[0])
            # Insert row in Table SQLite database
            # tconst, titleType, originalTitle, startYear, genres
            insert_title(line[0], line[1], None, line[3], None, line[5], None, None, line[8])
            # print()
        print('DONE !')

def insert_title(id, titleType, primaryTitle, originalTitle, isAdult,
                    startYear, endYear, runtimeMinutes, genres):
    try:
        # print('Inserting into DB')
        cursor = conn.cursor()

        fieldNames = "(id, titleType, primaryTitle,originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)"
        query = "INSERT into Title" + fieldNames + \
            " VALUES (?,?,?,?,?,?,?,?,?)"

        cursor.execute(query, (id, titleType, primaryTitle, originalTitle, isAdult,
                                startYear, endYear, runtimeMinutes, genres))
        

        # print(id, ' inserted successfully')

    except dbError as ex:
        print(id, ex)

if __name__ == "__main__":
    main()
    conn.commit()
    conn.close()
