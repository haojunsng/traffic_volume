from sklearn.linear_model import LinearRegression

class Regressor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.regr = LinearRegression()
        self.fit()

    def fit(self):
        self.regr.fit(self.x, self.y)

    def predict(self, X):
        preds = self.regr.predict(X)
        return preds