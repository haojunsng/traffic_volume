from sklearn.preprocessing import PolynomialFeatures

class PolyTransform:
    def __init__(self, degree):
        self.degree = degree
        self.polyX = PolynomialFeatures(self.degree)

    def polyTransform(self, X):
        return self.polyX.fit_transform(X)
        