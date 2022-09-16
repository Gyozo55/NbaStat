import sklearn
from sklearn import linear_model
import numpy as np


def calculate_wins(data):
    predict = "HOME_TEAM_WINS"

    x = np.array(data.drop([predict, "GAME_ID"], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)

    predictions = linear.predict(x_test)

    successful_pred = 0

    for x in range(len(predictions)):
        print(round(predictions[x]), x_test[x], y_test[x])
        if round(predictions[x]) == y_test[x]:
            successful_pred += 1

    # Right prediction %
    result = round((successful_pred / len(predictions)) * 100, 2)

    return result
