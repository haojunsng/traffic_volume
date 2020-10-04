from sklearn.model_selection import train_test_split

def split(x, y):
    return train_test_split(x, y, test_size = 0.2, random_state =0)