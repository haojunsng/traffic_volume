import pandas as pd

class FileReader:
    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(path)

    def features(self):
        return self.df.loc[:, self.df.columns!='traffic_volume']
    
    def y(self):
        return self.df['traffic_volume']
