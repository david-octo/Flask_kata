import random
from typing import Optional

import pandas as pd


class TitanicModel:
    def __init__(self):
        self.woman_survival_probability_: Optional[float] = None
        self.men_survival_probability_: Optional[float] = None

    def predict(self, X: pd.DataFrame):
        return X.apply(self.predict_according_to_sex, axis=0)

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self.woman_survival_probability_ = self.compute_survival_probability_by_sex(X, y, 'female')
        self.men_survival_probability_ = self.compute_survival_probability_by_sex(X, y, 'male')

    def compute_survival_probability_by_sex(self, X, y, sex):
        count_survived = 0
        subset_passengers = X[X['Sex'] == sex]
        for index, _ in subset_passengers.iterrows():
            if y[index] == 1:
                count_survived += 1
        return count_survived / subset_passengers.shape[0]

    def predict_according_to_sex(self, row):
        print(row)
        if row[0] == 'male':
            return random.choices([0, 1], k=1,
                                  weights=[1 - self.men_survival_probability_, self.men_survival_probability_])
        else:
            return random.choices([0, 1], k=1,
                                  weights=[1 - self.woman_survival_probability_, self.woman_survival_probability_])
