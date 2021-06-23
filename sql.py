import sqlite3
import os

db_filename = 'score_records.db'
user_table = 'users'
games_score_table = 'games_score'

def init_db():
    create_tables = f"""
        create table {user_table}( 
            id integer primary key autoincrement not null,
            name text unique
        );
        create table {games_score_table}( 
            id integer primary key autoincrement not null,
            score integer not null, 
            user_id integer not null references users(id)
        );
    """
    db_not_exist = not os.path.exists(db_filename)

    if db_not_exist:
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.executescript(create_tables)
    else:
        pass

def query_user_id(user_name):
    query_user = f"""
        select id from {user_table} where name = ?;
    """
    insert_user = f"""
        insert into {user_table} (name) values (?);
    """
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.execute(query_user, (user_name,))
        user = cursor.fetchone()
        if not user:
            cursor.execute(insert_user, (user_name,))
            user_id = cursor.lastrowid
        else:
            user_id = user[0]
        return user_id

def insert_game_score(score, user_id):
    insert_score = """
        insert into {games_score_table} (score, user_id) values (?, ?);
    """
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.execute(insert_score, (score, user_id,))


def main():
    init_db()
    user_name = input()
    print(query_user_id(user_name))


if __name__ == '__main__':
    main()