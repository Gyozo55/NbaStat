import sqlite3

from database import database_connection


def create_db_table(table_type):
    conn = database_connection.connect_to_db()
    try:
        conn.execute(insert_table(table_type))
        conn.commit()
        print(f"{table_type} Table created successfully")
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if conn:
            conn.close()


def insert_table(table_type):
    if table_type == 'teams':
        return ''' CREATE TABLE teams (
                        TEAM_ID INTEGER PRIMARY KEY NOT NULL,
                        MIN_YEAR DATETIME2 NOT NULL, 
                        MAX_YEAR DATETIME2 NOT NULL, 
                        ABBREVIATION VARCHAR(5) NOT NULL,
                        NICKNAME VARCHAR(20) NOT NULL,
                        YEARFOUNDED DATETIME2 NOT NULL,
                        CITY VARCHAR(20) NOT NULL,
                        ARENA VARCHAR(40) NOT NULL,
                        ARENACAPACITY INTEGER NOT NULL,
                        OWNER VARCHAR(20) NOT NULL,
                        GENERALMANAGER VARCHAR(20) NOT NULL,
                        HEADCOACH VARCHAR(20) NOT NULL
                    );'''

    if table_type == 'games':
        return ''' CREATE TABLE games (
                        GAME_ID INTEGER PRIMARY KEY NOT NULL,
                        GAME_DATE_EST DATETIME2 NOT NULL, 
                        HOME_TEAM_ID INTEGER,
                        VISITOR_TEAM_ID INTEGER,  
                        SEASON INTEGER,
                        PTS_home INTEGER,
                        FG_PCT_home FLOAT,
                        FT_PCT_home FLOAT,
                        FG3_PCT_home FLOAT,
                        AST_home INTEGER,
                        REB_home INTEGER,
                        PTS_away INTEGER,
                        FG_PCT_away FLOAT,
                        FT_PCT_away FLOAT,
                        FG3_PCT_away FLOAT,
                        AST_away INTEGER,
                        REB_away INTEGER,
                        HOME_TEAM_WINS INTEGER,
                        FOREIGN KEY(HOME_TEAM_ID) REFERENCES teams(TEAM_ID),    
                        FOREIGN KEY(VISITOR_TEAM_ID) REFERENCES teams(TEAM_ID)
                    );'''

    if table_type == 'ranking':
        return ''' CREATE TABLE ranking (
                        TEAM_ID INTEGER PRIMARY KEY NOT NULL,
                        SEASON_ID INTEGER,
                        STANDINGSDATE DATETIME2 NOT NULL,
                        CONFERENCE VARCHAR(5) NOT NULL,
                        TEAM_NAME VARCHAR(15) NOT NULL,
                        GAMES_PLAYED INTEGER,
                        WINS INTEGER,
                        LOSE INTEGER,
                        WINS_PCT FLOAT,
                        HOME_RECORD VARCHAR(5) NOT NULL,
                        ROAD_RECORD VARCHAR(5) NOT NULL
                    );'''