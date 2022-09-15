from flask import Flask

from database import add_data_db

app = Flask(__name__)


# @app.route('/get-prediction', methods=['GET'])
# def add_new_aircraft():
#     try:
#         pass
#
#         return jsonify(created_row_id), 200
#
#     except Exception as e:
#         return Response("Cause: %s" % e, status=400)


if __name__ == '__main__':
    # Initial functions:
    add_data_db.add_teams_data()
    add_data_db.add_games_data()
    add_data_db.add_rankings_data()

    # app.run(debug=True)
