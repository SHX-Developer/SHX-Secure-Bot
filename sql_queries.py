import sqlite3

db = sqlite3.connect("bot.db", check_same_thread=False)
sql = db.cursor()

#  SQL QUERIES

def queries():
    
    #  CREATE TABLE
    sql.execute('CREATE TABLE IF NOT EXISTS table (row_1 INTEGER, row_2 TEXT)')
    db.commit()

    #  DROP TABLE
    sql.execute('DROP TABLE IF EXISTS table')
    db.commit()

    #  INSERT
    sql.execute('INSERT INTO table (row_1, row_2) VALUES (?, ?)', ("value_1", "value_2"))
    db.commit()

    #  SELECT
    data = sql.execute('SELECT row FROM table WHERE row = ?', ("value",)).fetchone()[0]

    #  UPDATE
    sql.execute('UPDATE table SET row = ?', ("value"))
    db.commit()

    #  DELETE
    sql.execute('DELETE row FROM table WHERE row = ?', ("value"))
    db.commit()