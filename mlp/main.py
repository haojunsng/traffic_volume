import pandas as pd
import numpy as np
import regression as r
from splitTrainTest import split
from featureScaling import scale
from modelEvaluation import modelEvaluation
import polytransformer as pt
import fileReader as fr

print("We first read in data to obtain X and y")
df = fr.FileReader("data/prepared_df.csv") # Read in data
X = df.features() # Predictor Variables
y = df.y() # Dependent Variable
print("Data successfully loaded.")

print("Next, we scale our features for ML.")
scaled_X = scale(X) # Scale our features for ML
print("Features have been scaled.")

print("Then, we prepare our training and test sets.")
X_train, X_test, y_train, y_test = split(scaled_X, y) # Prepare train and test sets
print("Training and test datasets have been prepared.")

# Conduct Linear Regression on our training X and y

print("Now, we conduct linear regression on our training data")
linear_r = r.Regressor(X_train, y_train)
print("Linear regression training is completed on our training data")

# Predict on X_test and compare with y_test

print("Predict using X_test, then observe the results with y_test")
predicted = linear_r.predict(X_test)
modelEvaluation(predicted, y_test)

print("A R2 value of 0.148 is very bad, and suggests the issue of underfiting. We then attempt to increase the complexity of the model using a polynomial regression.")
poly_r = pt.PolyTransform(2)
transformed_X = poly_r.polyTransform(X)
polyX_train, polyX_test, y_train, y_test = split(transformed_X, y)
transformed_r = r.Regressor(polyX_train, y_train)
print("Finally, we predict on polyX_test and observe if the metric scores are improved, specifically R2")
poly_predicted = transformed_r.predict(polyX_test)
modelEvaluation(poly_predicted, y_test)

print("A model with R2 = 0.584, and RMSE values in the thousands is definitely far from ideal, especially in the context of a traffic volume case study. A time series model deploying ARIMA or Holt Winters could possibly do better in terms of accuracy.")



