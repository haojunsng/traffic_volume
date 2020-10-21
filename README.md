# traffic_volume
 My first (and simple) End to end machine learning pipeline done by SNG HAO JUN - e0310591@u.nus.edu
 
This folder includes a data folder which contains the respective csv files:
1. traffic.csv - output of Task 1's Data Extraction using python's sqlite3
2. prepared_df.csv - output of Task 2's EDA

## Pipeline Execution
1. Install all dependencies (refer to requirements.txt)
2. Download the traffic.db file (https://aisgaice.blob.core.windows.net/aice-associate-sep2020-assessment-data/traffic.db)
3. Save traffic.db file into data folder
4. Run de.py (data extraction)
- Feel free to modify the WHERE clause in de.py to extract data desired. Provided code extracts the traffic data dated after and including 2013.
5. Refer to eda.ipynb (exploratory data analysis) for full report on analysis
- We first run a df.head(5) and df.tail(5) to have a quick visual on the data features and values.
- We use histograms to illustrate the distribution of the numerical variables.
- We chart out a correlation matrix to understand the relationships between numerical variables.
- Dive into each numerical variable by plotting a boxplot to check for presence of outliers in the data - This is highly important as outliers will skew linear regression models very extensively.
- We converted the date_time variable into Year, Month and Time as it is within reason to believe that traffic volume depends on the 3 variables.
- Conversion of categorical variables to dummy variables using one hot encoding
- Data is now ready for Machine Learning.
6. Run main.py
- Feel free to modify the ratio of the training data to test data in splitTrainTest.py (test_size = 0.2 implies 20% of data being used as test set)
- Degree used in polynomial transformation can also be changed, (MemoryError might surface due to a model of large degree being deployed)

### Key Findings from EDA (Quick Summary)
There is a low extent of correlation between numerical variables as well as with dependent variable traffic_volume. Categorical variables when converted to dummy variables also show little correlation with traffic_volume. Outliers are present in rain_1h and temp.

## Choice of Machine Learning Model
- Linear Regression: Despite low correlation levels, I have still decided to employ the use of a good old classic linear regression model first to establish statistically how bad the linear relationship between the independent variables and dependent variables is. From there, I can take advantage of the flexibility of linear regression models to tweak and fit a model of higher complexity if required.
- Polynomial Linear Regression: As expected, the R2 values and RMSE are far from ideal. I then choose to take on a model of higher complexity (degree = 2) to attempt to fit the data again, which yields a huge improvement in R2 values and RMSE (while still not ideal).
- A time series model using ARIMA or HoltWinters can be explored as they could possibly yield much better results.
