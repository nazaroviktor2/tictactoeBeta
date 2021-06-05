import logging

import psycopg2 as psycopg2

from exception import NotFoundGame

DATABASE = "tictac"
USER = "postgres"
PASSWORD = "nazaroff"
HOST = "127.0.0.1"
PORT = "5432"


def create_user(user_id, user_name):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if cur.fetchone() is None:

            cur.execute(f"INSERT INTO users (id, name) VALUES (%s, %s)", (user_id, user_name))
            logging.info(f"User with id = {user_id} successfully registered")
        else:
            logging.info(f"User with id = {user_id} already registered")


def create_game(user_id, open_game: bool):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()

        cur.execute(f"INSERT INTO games(first_id, open_game) VALUES ({user_id}, {open_game}) RETURNING id;")
        game_id = cur.fetchone()[0]
        logging.info(f"game id = {game_id}")
    insert_user_and_game(user_id, game_id)
    return game_id


def delete_game(id):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT id FROM games WHERE id = '{id}'")
        if cur.fetchone() is None:
            logging.error(f"Game with id =  {id} not found ")
            raise NotFoundGame(f"Game with id =  {id} not found ")
        else:
            cur.execute(f"DELETE FROM games WHERE id = '{id}'")
            logging.info(f"Game with id =  {id} deleted")


def insert_user_and_game(user_id, game_id):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO user_and_game(user_id, game_id) VALUES (%s, %s)", (user_id, game_id))


def get_game_code_by_id(id):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT secret_code FROM games WHERE id = {id}")
        if cur.fetchone() is None:
            logging.error(f"Game with id =  {id} not found ")
            raise NotFoundGame(f"Game with id =  {id} not found ")
        else:
            cur.execute(f"SELECT secret_code FROM games WHERE id = {id}")
            return cur.fetchone()[0]


def get_game_id_by_code(code:str):
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(f"SELECT id FROM games WHERE secret_code = '{code}' ")
        if cur.fetchone() is None:
            logging.error(f"Game with code =  {code} not found ")
            raise NotFoundGame(f"Game with code =  {code} not found ")
        else:
            cur.execute(f"SELECT id FROM games WHERE secret_code = '{code}'")
            return cur.fetchone()[0]


def init_database():
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT) as con:
        cur = con.cursor()
        cur.execute(open("init.sql", "r").read())
