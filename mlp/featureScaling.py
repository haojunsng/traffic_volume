from sklearn.preprocessing import StandardScaler

def scale(x):
    sc_x = StandardScaler()
    X_new = sc_x.fit_transform(x)
    return X_new
