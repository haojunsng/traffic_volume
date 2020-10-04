from sklearn import metrics
import numpy as np

def modelEvaluation(predictions, y_test_set):
    #Print model evaluation to predicted results
    print('R Squared : ',metrics.r2_score(y_test_set, predictions))
    print('Mean Squared Error: ', metrics.mean_squared_error(y_test_set, predictions))
    print('Mean Absolute Error: ', np.sqrt(metrics.mean_squared_error(y_test_set, predictions)))
    print('Root Mean Squared Error : ',np.sqrt(metrics.mean_squared_error(y_test_set, predictions)))