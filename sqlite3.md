# SQLite3 Docs

### Database

```sql
-- Create Database as a new file
sqlite3 D:\source\sql\moviesDB\IMdb.db  -- Access Database
.database   -- View all Databases

```

### Create Tables using 👇

```sql
CREATE TABLE Title(id TEXT, titleType TEXT, primaryTitle TEXT,
                    originalTitle TEXT, isAdult INTEGER, startYear TEXT,
                    endYear TEXT, runtimeMinutes TEXT, genres TEXT);
```
