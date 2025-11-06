# Day 30, 06.10.2025

---
##  __BASIC OVERVIEW__
 

*  scaling features
*  hyperparameter tuning
*  data loading workflow

---

##  __SCHEDULE__

|Time|Content|
|---|---|
|09:30 - 10:00|Daily review|
|10:00 - 12:35|Lecture with Anastasia Mikheeva, live coding|
|12:35 - 13:30|Lunch break|
|13:30 - open end|Group work/ practical exercises with notebooks 1 and 2, with optional session on SQL query at 14:30| 

---

##  __SCALING FEATURES__ 
problem: 
- some machine learning algorithms (e.g. KNN) do not perform well when features have very different scales/units
- housing data example: ranges for number of rooms or income
- without any scaling, most models will be biased

solution: getting all attributes to have the same scale, 2 methods:
- normalization (= min-max scaling)
- standardization

use on training data only:

```python
fit_transform()
```
once having a trained scaler, use on test set, validation set, and new data:

```python
transform()
```

steps:
- fit scaler using available training data
- apply scale to training data
- apply scale to data going forward
- scaling prior to modeling

---

### FEATURES IN FOCUS: DISTRIBUTION, OUTLIERS, TAILS ETC.
- if having outliers in new data: they may end up scaled outside the range - solution: set clip hyperparameter to True
- if having heavy tails (when values far from the mean not exponentially rare): first transform data to shrink the heavy tail, then scale the feature (bucketize)
- multimodal distribution of a feature: also transform data first (bucketize, Gaussian RBF)
- if target value has a heavy tail: replace target with its logarithm
- checking distribution and other relevant aspects of features first essential (e.g. histogram)
- encoded variables need no scaling

---

### NORMALIZATION

- simplest method
- values shifted & rescaled so that they end up ranging from 0 to 1
- subtracting min value and dividing by the difference between the min and max: y = (x-min)/(max-min)
- Scikit-Learn provides transformer

```python
from sklearn.preprocessing import MinMaxScaler
# perform a robust scaler transform of the dataset
minmax_scaler = MinMaxScaler()
data = minmax_scaler.fit_transform(data)
```

---

### STANDARDIZATION

- subtracting mean value, then dividing result by standard deviation: y = (x-mean)/standard_deviation
- does not restrict values to a specific range
- much less effected by outliers
- assumes that observations fit a Gaussian distribution
- requires to know / be able to estimate the mean and sd of observable values (estimating from training data ok)
- mean and sd estimates of dataset can be more robust to new data
- Scikit-Learn provides transfomer

```python
from sklearn.preprocessing import StandardScaler
# perform a robust scaler transform of the dataset
scaler = StandardScaler()
data = scaler.fit_transform(data)
```

---

### SOME INSIGHTS: NORMALIZE OR STANDARDIZE?

- depends on specifics of problem and each variable
- if distribution normal: standardize, otherwise normalize
- if values are small and distribution limited (e.g. sd near 1), no scaling may be necessary
- if in doubt: normalize
- if you have resources: explore modeling with raw data, standardized data, normalized data -> figure out beneficial difference in performance of resulting model

---

## __HYPERPARAMETER TUNING__ 
problem:
- choosing the right hyperparameters make a difference between an average model and a great one
- how do we select the best parameter values for our data?
- meticulously evaluating every possible combination of hyperparameters?
- is it even possible to check every possible hyperparameter combination?

solution: 
- hyperparameter tuning = systematically searching for the best combination of hyperparameter values to boost a model's performance
- tuning techniques: grid search, random search

---

### GRID SEARCH

- computes optimum values of hyperparameters
- exhaustive search
- picks every possible parameter combination from provided hyperparameter grid
- finds and returns best combination
- evaluates model on all possible hyperparameter combinations
- very time-consuming
- for each combination, grid search trains and evaluates a machine learning model using k-fold cross-validation - then it calculates the average performance across all folds to provide a final score for each combination of hyperparameters
- score based on an evaluation metric (accuracy, precision etc.)
- hyperparameter combination with the highest score is the winner

---

### RANDOM SEARCH

- does not try every possible combination for our search space
- samples from a distribution of hyperparameter values
- number of hyperparameter combinations to test is controlled explicitly
- instead of specific values, we define hyperparameter space specifying hyperparameter distributions
- we specify number of combinations to test
- studies: allowing random search to test 60 possible combinations, the technique finds optimal solutions for most machine learning models
- it trains a model using a hyperparameter combination with cross-validation and evaluates them using a specific performance metric 
- computationally efficient in large hyperparameter spaces  

---

### APPLICATION: GRID AND RANDOM

1. importing necessary libraries
2. loading dataset
3. splitting data
4. defining hyperparameter grid (here, diff codes)
5. training and evaluating model (here, diff codes)

---

## __DATA LOADING WORKFLOW__ 

example showing how SQL, .env and Python (SQLAlchemy + pandas) work together

SQL query - defines what data you want from the database
```python
SELECT *
FROM customers
WHERE country <> 'FakeLand' OR country IS NULL;
```

.env file - shows typical use cases (mainly DB config + examples for context)
```python
# Main variable used to connect to the database
# Includes username, password, host, port, and DB name
DB_STRING=postgresql+psycopg2://user:password@...:5432/...

# Other Examples:
# Enable debug mode (set to False in production)
DEBUG=True

# Example directories (just to show how .env can define paths)
DATA_DIR=./data
OUTPUT_DIR=./outputs

# Example login data for sth. else
USER=my_user
PASSWORD=my_password
```

SQLAlchemy + load_dotenv - connects Python to database
```python
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os, pandas as pd

load_dotenv()  # load .env variables
db_string = os.getenv("DB_STRING")  # load DB_STRING from .env
engine = create_engine(db_string)  # connect to DB

# Run SQL query and load result into pandas DataFrame (ready to use)
df = pd.read_sql_query("SELECT * FROM customers;", engine)
```

to_csv() - saves data for later use
```python
output_dir = os.getenv("OUTPUT_DIR")  # load OUTPUT_DIR from .env
df.to_csv(os.path.join(output_dir, "customers.csv"), index=False)  # flexible path defined in .env
```

---
##  __Helpful References__
* [Jason Brownlee on StandardScaler & MinMaxScaler](https://machinelearningmastery.com/standardscaler-and-minmaxscaler-transforms-in-python/)
* [Scikit Reference: MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html) 
* [Scikit Reference: StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
* [Scikit Reference: GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
* [Scikit Reference: Random Search](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html)
* [Blog on Grid Search vs Random Search](https://www.blog.trainindata.com/grid-search-vs-random-search-which-one-should-you-use/)