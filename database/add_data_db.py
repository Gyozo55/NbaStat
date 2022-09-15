from database import database_connection
import pandas as pd


def add_teams_data():
    conn = database_connection.connect_to_db()
    teams_data = pd.read_csv('input_datas\Teams.csv')

    try:
        teams_data.to_sql('teams',
                          con=conn)
    except Exception as e:
        return "Cause: %s" % e
    finally:
        conn.close()


def add_games_data():
    conn = database_connection.connect_to_db()
    games_data = pd.read_csv('input_datas\games.csv')

    try:
        games_data.to_sql('games',
                          con=conn)
    except Exception as e:
        return "Cause: %s" % e
    finally:
        conn.close()


def add_rankings_data():
    conn = database_connection.connect_to_db()
    ranking_data = pd.read_csv('input_datas\Ranking.csv')

    try:
        ranking_data.to_sql('ranking',
                            con=conn)
    except Exception as e:
        return "Cause: %s" % e
    finally:
        conn.close()
