from ai.ai import calculate_wins
from database import add_data_db
from database.get_data import get_predictable_datas

if __name__ == '__main__':
    # Initial functions:
    add_data_db.add_teams_data()
    add_data_db.add_games_data()
    add_data_db.add_rankings_data()

    print(calculate_wins(get_predictable_datas()))