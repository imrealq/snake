import sqlite3
import os

db_filename = 'score_records.db'
player_table = 'players'
games_score_table = 'games_score'

def init_db():
    create_tables = f"""
        create table {player_table}( 
            id integer primary key autoincrement not null,
            name text unique
        );
        create table {games_score_table}( 
            id integer primary key autoincrement not null,
            score integer not null, 
            player_id integer not null references players(id)
        );
    """
    db_not_exist = not os.path.exists(db_filename)

    if db_not_exist:
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            cursor.executescript(create_tables)
    else:
        pass

def get_player_id(player_name):
    query_player = f"""
        select id from {player_table} where name = ?;
    """
    insert_player = f"""
        insert into {player_table} (name) values (?);
    """
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.execute(query_player, (player_name,))
        player = cursor.fetchone()
        if not player:
            cursor.execute(insert_player, (player_name,))
            conn.commit()
            player_id = cursor.lastrowid
        else:
            player_id = player[0]
        return player_id

def insert_game_score(score, player_id):
    insert_score = f"""
        insert into {games_score_table} (score, player_id) values (?, ?);
    """
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.execute(insert_score, (score, player_id,))
        conn.commit()


def main():
    init_db()
    player_name = input()
    print(get_player_id(player_name))


if __name__ == '__main__':
    main()