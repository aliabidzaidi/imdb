# SQLite3 Docs

### Database

```sql
-- Create Database as a new file
sqlite3 D:\source\sql\moviesDB\IMdb.db  -- Access Database
.database   -- View all Databases

```

### Create Tables using 👇

```sql
-- Active fields: id, titleType, originalTitle, startYear, genres
CREATE TABLE Title(id TEXT PRIMARY KEY, titleType TEXT, primaryTitle TEXT,
                    originalTitle TEXT, isAdult INTEGER, startYear TEXT,
                    endYear TEXT, runtimeMinutes TEXT, genres TEXT);
CREATE UNIQUE INDEX idx_title_id ON Title(id);

CREATE TABLE RATING(id TEXT PRIMARY KEY, averageRating INTEGER, numVotes INTEGER);
CREATE UNIQUE INDEX idx_rating_id ON Rating(id);
```
