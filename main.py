import json
from flask import Flask, request, jsonify, Response

from database import database_creation

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
    database_creation.create_db_table('teams')
    database_creation.create_db_table('games')
    database_creation.create_db_table('ranking')
    # app.run(debug=True)
