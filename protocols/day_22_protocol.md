# Day 22, 22.09.2025


##  __Basic Overview__
 

*  [Linear Regression: Theory](#linear-regression)
*  [Implementation with scikit-learn](#implementation-in-sklearn)
* Implementation with Statsmodels


---
##  __Schedule__

|Time|Content|
|---|---|
|10:00 - 11:15|Lecture on Linear Regression|
|11:15 - 11:30|Reflection on lecture|
|11:30 - 13:00|Lunch Break| 
|13:00 - 18:30 <br> (or whenever finished) |Self-study/Pair-Programming: <br>Practical exercises|

---
## __Linear Regression__ 
Goals <span style="color:grey"> (Why do we need this?)</span>:

* explanation <span style="color:grey"> (Why is my house worth xyz?)</span> &rarr; descriptive statistics
* prediction <span style="color:grey"> (How much is my house worth?)</span> &rarr; inferential statistics

### Regression: 

* *regredi* (Latin) = to go back
* "going back" from a cloud of data points to find the underlying relationship

### Linear Regression:

* assuming two (or more) variables have a certain kind of relationship - **linear**
* using this assumption to find the equation that best describes this relationship

<img src="../images/lin_reg.png" alt="A simple regression plot" width="500">

<p style="font-size: 0.8em; margin-top: 4px;">
  <a href="https://ideal-adventure-6vymekm.pages.github.io/_images/6ebd10e7ee7ec8605f50720098e185e572eeb40bfceff8adeea66193e5ec2073.png" target="_blank">Source: Salt&Pepper Cookbook</a>
</p>

    
| General Equation     | Key Terms |
|----------------------|-----------|
| y = b₀ + b₁x + e <br> <br> &rarr; find b₀ and b₁! | Intercept (b₀, value of y when x = 0) <br> Slope (b₁, weights/coefficients) <br> Residuals (e, difference in true vs. estimated value: eᵢ = yᵢ - ŷᵢ) |



<img src="../images/reg_front2.svg" alt="A simple regression plot" width="500">

<p style="font-size: 0.8em; margin-top: 4px;">
  <a href="https://www.reneshbedre.com/blog/learn-to-calculate-residuals-regression.html" target="_blank">Source: RS Blog</a>
</p>

💡idea: finding the "line" (aka fit) that best describes the data

❗how: looking at the sum of the residuals ("errors")<br>
less errors &rarr; better fit

### Least squares criterion

<img src="../images/lin_squ.gif" alt="A simple regression plot" width="500">

<p style="font-size: 0.8em; margin-top: 4px;">
  <a href="https://medium.datadriveninvestor.com/asap-guide-to-linear-regression-fda841656fbd" target="_blank">Source: ASAP Guide to Linear Regression</a>
</p>

* residuals are squared and summed, so that negative and positive values don't negate each other

* Ordinary Least Squares Regression: analytically finds least squares estimate which give $b_0$ and $b_1$<br>
 $\min J(b_0, b_1) = \sum (y_i - b_0 - b_1 x_i)^2 $


## Multiple Linear Regression
* same idea but with more explanatory variables (& coefficients)
* $y = b_0 + b_1 x_1 + b_2 x_2 + \dots + b_k x_k + e$
* each variable adds another dimension
* visualisation difficult
<img src="../images/lin_reg_mult.gif" alt="A simple regression plot" width="500">

<p style="font-size: 0.8em; margin-top: 4px;">
  <a href="https://medium.com/@MerelyAI/visualizing-ordinary-least-squares-regression-in-3d-0ce4b7372fb8" target="_blank">Source: MerelyAI</a>, original plane = green, estimated plane = red
</p>


### What counts as linear regression/equation?
"linear" = linear in the coefficients ($b$)

✅ Linear regression ($b$ enters linearly):<br>
$y = b_0 + b_1·x$<br>
$y = b_0 + b_1·x + b_2·x²$<br>
$y = b_0 + b_1·log(x)$

❌ Not linear regression ($b$ enters nonlinearly):<br>
$y = b_0 + x^{b_1}$ ($b$ in exponent)<br>
$y = b_0 + (b_1)²·x$ ($b$ squared → nonlinear in $b$)l

## Assumptions
1. **Linearity**: The target variable and the coefficients of the explanatory variables are linearly related.
2. **Zero-Mean Error**: The mean of all residuals is zero.
3. **Strict Exogeneity**: All the explanatory variables are uncorrelated with the residual.
4. **Homoscedasticity**: The variance of the residuals across a single observation remains the same.
5. **No Multicollinearity**: All the explanatory variables are linearly independent.

## Model Evaluation
Simple Linear Regression
*  $R^2 = 1 - \frac{SSR}{SST}$<br>
with $SSR =\sum_{i=1}^n e_i^2$ (sum of squared residuals)<br>
and $SST =\sum_{i=1}^n (y_i - \bar{y})^2$ (total sum of squares)


---
## __Exercises__ 
## Implementation in sklearn

```python
# Packages needed 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import PredictionErrorDisplay
```

### Simple Linear Regression

0. *Recommended:* get an idea of relationship(s) between variables by creating scatter plots first
```python
sns.pairplot(df) 
# automatically plot pairwise scatter plots and histograms of all variables in a df
```

1. Prepare data for modeling by defining target and feature
```python
X = df[['feature_variable']]  # X needs to be 2-dimensional so we need double brackets here
y = df['target_variable']

```
2. Instantiate the model and train it
```python
lin_reg = LinearRegression() # instantiate
lin_reg.fit(X, y) # train
```
* Show intercept and slope/coefficient: 
```python
print(lin_reg.intercept_) # intercept
print(lin_reg.coef_[0]) # first coefficient
```
* Plot data points with fitted regression line
```python
# Plotting our data points
plt.scatter(X, y)
# Adding the fitted regression line of our model
plt.plot(X, X*slope +intercept, '-')

# plt.title()
# plt.ylabel()
# plt.xlabel()
```
* Estimate model fit with $R^2$
```python
# Calculate the estimated value for each data point
y_pred = lin_reg.predict(X)
# Note: the input for predict() needs to be a dataframe
# single values can be passed in this form: pd.DataFrame({'col_name': [value]})

# Calculate the R-squared for our model
print(r2_score(y, y_pred))
```
#### Limitations of Linear Regression
* estimating the quality of the model in only one value (e.g. $R^2$) can lead to biased interpretation
* if the errors follow certain patterns: indicates poor fit i.e. not all variance is captured in the model

```python
# plot residual plot with integrated sklearn function
display = PredictionErrorDisplay(y_true=y, y_pred=y_hat)
display.plot()
```
### Multiple Linear Regression
0. *Recommended:* get an idea of relationships between variables by creating scatter plots first
```python
sns.pairplot(df) 
# automatically plot pairwise scatter plots and histograms of all variables in a df
```
1. Prepare data for modeling by defining target and features
```python
X = df[['feature_variable1, feature_variable2']]  
y = df['target_variable']

```
2. Instantiate the model and train it
```python
lin_reg = LinearRegression() # instantiate
lin_reg.fit(X, y) # train
```
* Show intercept and slope/coefficient: *see above*
* Predict new values:
```python
new_y = pd.DataFrame({'col1': [num], 'col2': [num]})
y_prediction = lin_reg.predict(new_y)
```
* Estimate model fit with Adjusted $R^2$
```python
# Define function for calculating adjusted r-squared
def adjusted_r_squared(r_squared, X):
    adjusted_r2 = 1 - ((1 - r_squared) * (len(X) - 1) / (len(X) - X.shape[1] - 1))
    return adjusted_r2 

# Calculate adjusted r-squared to compare different models
adj_r_sq = {}
adj_r_sq['M1'] = adjusted_r_squared(r2_score(y, y_hat), X)
adj_r_sq['M2'] = adjusted_r_squared(r2_score(y, y_hat2), X2)
adj_r_sq['M3'] = adjusted_r_squared(r2_score(y, y_hat3), X3)
print(adj_r_sq)
```
### Dealing with Categorical Variables
* need to be transformed if used in regression models
* how to find them in a df: visual identification via scatter plot or histogram:
```python
# e.g. using seaborns pairplot function
sns.pairplot(df) 
```
* declare strings as categories:
```python
# string column to category
cat_df = df['cat_col'].astype('category'

```
* label encoding:
```python
# converts strings into numerical labels
cat_df.cat.codes
# alternative:
from sklearn.preprocessing import OrdinalEncoder
ord_make = OrdinalEncoder()
ord_make.fit_transform(df[['cat_col']])

```

* creating dummy variables:
```python
# using pandas .get_dummies()
pd.get_dummies(df['cat_col'])
# alternative
from sklearn.preprocessing import LabelBinarizer
lb = LabelBinarizer()
dummies = lb.fit_transform(df['cat_col'])
# needs to be converted back to a dataframe
dum_df = pd.DataFrame(dummies,columns=lb.classes_)
```
* Dummy Variable Trap: avoid multicollinearity by dropping the first of the newly created dummy variable columns
```python
# set drop_first=True when creating dummies
pd.get_dummies(df['cat_col'], drop_first=True)
```

---
##  __Helpful References__
* [Pre-Preppers](https://docs.google.com/presentation/d/1a7cdrUL_-Reg-myKLcfaBgx_ReR2efUf/edit?slide=id.p1#slide=id.p1)
* [Slides](https://ideal-adventure-6vymekm.pages.github.io/sessions/08_Linear_Regression.html#)
