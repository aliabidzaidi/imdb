import pandas as pd
import numpy as np
import sqlite3
from sqlite3 import Error as dbError


conn = sqlite3.connect('IMdb.db')


def import_titles():
    chunksize = 10 ** 3
    columns = ["tconst", "titleType", "originalTitle", "startYear", "genres"]
    colNames = ["tconst", "titleType", "primaryTitle", "originalTitle", "isAdult",
                "startYear", "endYear", "runtimeMinutes", "genres"]
    print('started')
    skipRows = 0
    # skiprows = 4000000
    for chunk in pd.read_csv("TSVs/title_basics.tsv", skipinitialspace=True, delimiter="\t",
                             chunksize=chunksize, skiprows=skipRows, usecols=columns,
                             names=colNames, nrows=2000000
                             ):
        # print(type(chunk))
        # print(chunk)
        print(chunk.axes, end='\n\n')
        for row in chunk.values:
            print(row)

            # For basic titles
            # insert_title(row[0], row[1], None, row[2], None, row[3], None, None, row[4])

    conn.commit()
    conn.close()
    print('ended')


def import_ratings():
    conn = sqlite3.connect('IMdb.db')
    cursor = conn.cursor()
    chunksize = 10 ** 3
    columns = ["tconst", "averageRating", "numVotes"]
    colNames = ["tconst", "averageRating", "numVotes"]
    print('started')
    skipRows = 0
    # skiprows = 4000000
    nRows = 1000
    for chunk in pd.read_csv("TSVs/title_ratings.tsv", skipinitialspace=False, delimiter="\t",
                             chunksize=chunksize, skiprows=skipRows
                             # , names=colNames
                             #   , nrows= nRows
                             ):
        # print(type(chunk))
        # print(chunk)
        print(chunk.axes, end='\n\n')
        for row in chunk.values:
            # print(row)

            fieldNames = "(id, averageRating, numVotes)"
            query = "INSERT into Rating" + fieldNames + \
                " VALUES (?,?,?)"

            cursor.execute(query, (row[0], row[1], row[2]))

    conn.commit()
    conn.close()
    print('ended')


def import_names():
    print('started import_names')
    conn = sqlite3.connect('IMdb.db')
    cursor = conn.cursor()
    chunksize = 10 ** 4

    columns = ["nconst", "primaryName", "birthYear",
               "deathYear", "primaryProfession", "knownForTitles"]
    colNames = ["nconst", "primaryName", "birthYear",
                "deathYear", "primaryProfession", "knownForTitles"]
    skipRows = 0
    # skiprows = 4000000
    nRows = 1000
    for chunk in pd.read_csv("TSVs/name_basics.tsv", skipinitialspace=False, delimiter="\t",
                             chunksize=chunksize, skiprows=skipRows
                             # , names=colNames
                             #   , nrows= nRows
                             ):
        # print(type(chunk))
        # print(chunk)
        print(chunk.axes, end='\n\n')
        for row in chunk.values:
            # print(row)

            fieldNames = "(id, primaryName, birthYear, deathYear, primaryProfession, knownForTitles)"
            query = "INSERT into Name" + fieldNames + \
                " VALUES (?,?,?,?,?,?)"

            cursor.execute(
                query, (row[0], row[1], row[2], row[3], row[4], row[5]))

    conn.commit()
    conn.close()
    print('ended')


def import_crew():
    print('started insert_crew')
    conn = sqlite3.connect('IMdb.db')
    cursor = conn.cursor()
    chunksize = 10 ** 4

    # tconst
    # directors
    # writers
    columns = ["tconst", "directors", "writers"]
    colNames = ["tconst", "directors", "writers"]
    skipRows = 0
    # skiprows = 4000000
    nRows = 1000
    for chunk in pd.read_csv("TSVs/title_crew.tsv", skipinitialspace=False, delimiter="\t",
                             chunksize=chunksize, skiprows=skipRows
                             # , names=colNames
                             #   , nrows= nRows
                             ):
        # print(type(chunk))
        # print(chunk)
        print(chunk.axes, end='\n\n')
        for row in chunk.values:
            # print(row)

            fieldNames = "(id, directors, writers)"
            query = "INSERT into Crew" + fieldNames + \
                " VALUES (?,?,?)"

            cursor.execute(
                query, (row[0], row[1], row[2]))

    conn.commit()
    conn.close()
    print('ended')


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
    # import_titles()

    # import_ratings()

    # import_names()

    import_crew()
