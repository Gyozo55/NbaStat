from database import database_connection
import pandas as pd


def get_predictable_datas():
    conn = database_connection.connect_to_db()
    return pd.read_sql_query('Select GAME_ID, home_team_ranking.TEAM, home_team_ranking.W_PCT, home_team_ranking.W, '
                             'home_team_ranking.L, visitor_team_ranking.TEAM, visitor_team_ranking.W_PCT, '
                             'visitor_team_ranking.W, visitor_team_ranking.L, HOME_TEAM_WINS from games '
                             'left join ranking home_team_ranking on games.HOME_TEAM_ID=home_team_ranking.TEAM_ID '
                             'left join ranking visitor_team_ranking on games.VISITOR_TEAM_ID=visitor_team_ranking.TEAM_ID '
                             'where GAME_DATE_EST = home_team_ranking.STANDINGSDATE and '
                             'GAME_DATE_EST = visitor_team_ranking.STANDINGSDATE;',
                             con=conn)