# Day 26, 22.09.2025 (Evaluation-metrics)


##  __Basic Overview__
 

*  [Goals and general Question for Evaluation Metrics](#https://ideal-adventure-6vymekm.pages.github.io/sessions/11_Evaluation_Metrics.html)
*  [Evaluation Metrics for Classification](https://ideal-adventure-6vymekm.pages.github.io/sessions/11_Evaluation_Metrics.html)
*  [Regression Metrics](https://ideal-adventure-6vymekm.pages.github.io/sessions/11_Evaluation_Metrics.html)
* [Quick Hint Table](https://ideal-adventure-6vymekm.pages.github.io/sessions/11_Evaluation_Metrics.html)


---
##  __Schedule__

|Time|Content|
|---|---|
|10:00 - 11:15|Lecture on Evaluation Metrics|
|11:15 - 11:30|Reflection on lecture|
|11:30 - 13:00|Lunch Break| 
|13:00 - 18:30 <br> (or whenever finished) |Self-study/Pair-Programming: <br>Practical exercises|

---
## __Evaluation Metrics__ 
Goals <span style="color:grey"> (Why do we need this?)</span>:

* quantitative evidence <span style="color:grey"> (how good or bad a model is?)
* objectively compare models <span style="color:grey"> (An accuracy of 95% sounds good, but it is not enough?)
* align with real-world goals
* tune models

### General Questions

* What is being evaluated? <span style="color:grey"> (e.g. classification model, regression model, clustering)
* What is the objective of the evaluation <span style="color:grey"> (e.g. maximise accuracy, minimise error costs?)
* What does this metric actually measure? <span style="color:grey"> (Is it about the accuracy of all predictions, or only the positive/negative ones?)
* What type of error does the metric take into account? <span style="color:grey"> (false positives or false negatives?)
* When is this metric useful, and when is it not?


## __Evaluation Metrics for Classification__ 

### Metrics used
    
| Metrics     | Definition | Relevant Points|
|-------------|--------------------------|-----------------|
| Accuracy | Proportion of correctly classified observations| It's beneficial when classes are balanced.|
Precision |Proportion of correctly recognised positives among all those predicted to be positive. |Relevant when false positives are costly (e.g. false alarms). | 
|Recall (Sensitivity, True Positive Rate)|Proportion of correctly recognised positives among all actual positives. | Relevant when false negatives are costly (e.g. overlooking an illness).| 
F1-Score| Harmonic mean of precision and recall|Good for unbalanced classes when balance between precision and recall is important. |
ROC-AUC|Area under the ROC curve.|Measures how well the model separates classes (regardless of the threshold value).|
Confusion Matrix |Matrix (TP, FP, TN, FN) that summarizes the classification results of a binary classifier |clearly shows error patterns. |




💡note : 

+ The choice of evaluation metric depends on the specific problem and the importance of false positives and false negatives.
+ It is essential to carefully select the appropriate metric(s) for evaluating the performance of a classification model.

### Let go a little bit deeper in each Metric


#### Confusion Matrix
It consists of four components:

- True positive: actual = 1, predicted = 1
- False positive: actual = 0, predicted = 1
- False negative: actual = 1, predicted = 0
- True negative: actual = 0, predicted = 0
![alt text](image-1.png)
![alt text](image-2.png)

-> How you can implement it as self define function
```python
def find_TP(y_true, y_pred):
    # counts the number of true positives (y_true = 1, y_pred = 1)
    return sum((y_true == 1) & (y_pred == 1))

def find_FN(y_true, y_pred):
    # counts the number of false negatives (y_true = 1, y_pred = 0)
    return sum((y_true == 1) & (y_pred == 0))

def find_FP(y_true, y_pred):
    # counts the number of false positives (y_true = 0, y_pred = 1)
    return sum((y_true == 0) & (y_pred == 1))

def find_TN(y_true, y_pred):
    # counts the number of true negatives (y_true = 0, y_pred = 0)
    return sum((y_true == 0) & (y_pred == 0))

def find_conf_matrix_values(y_true,y_pred):
    '''calculate TP, FN, FP, TN'''
    TP = find_TP(y_true,y_pred)
    FN = find_FN(y_true,y_pred)
    FP = find_FP(y_true,y_pred)
    TN = find_TN(y_true,y_pred)
    return TP,FN,FP,TN

def my_confusion_matrix(y_true, y_pred):
    '''display our own confusion matrix'''
    TP,FN,FP,TN = find_conf_matrix_values(y_true,y_pred)
    return np.array([[TN,FP],[FN,TP]])
```

### Accuracy
Accuracy is calculated using the following formula:

 $ \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} $

#### Implementation in Sklearn
```python
from sklearn.metrics import accuracy_score

y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 0, 1, 1]

accuracy = accuracy_score(y_true, y_pred)

print("Accuracy: ", accuracy)
```
#### self Implementation 
```python

def my_accuracy_score(y_true, y_pred):
    '''own function for the metric accuracy'''
    # calculates the fraction of samples predicted correctly
    TP,FN,FP,TN = find_conf_matrix_values(y_true,y_pred)  
    return (TP + TN)/(TP + TN + FP + FN)
```

### Precision
precision is calculated using the following formula:

  $ \text{Precision} = \frac{TP}{TP + FP} $

If the model says ‘positive’, how confident can I be in this statement?

+ High precision = The model produces few false alarms.

+ Low precision = Many normal cases are incorrectly classified as positive.

**Precision is therefore important when false positives are costly.**

#### Let's take a spam filter:

+ True positives (TP): Emails that are actually spam and have been identified as spam.

+ False positives (FP): Emails that are not spam but have nevertheless been marked as spam.

+ If the model marks 100 emails as spam and 80 of them are actually spam: precision = 80 / (80 + 20) = 80%

#### Implementation in Sklearn
```python
from sklearn.metrics import precision_score

y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 0, 1, 1]

precision = precision_score(y_true, y_pred)
print("Precision: ", precision)
```
#### self implimented
```python
def my_precision_score(y_true, y_pred):
    '''own function for the metric precision'''
    # calculates the fraction of predicted positives samples that are actually positive
    TP,FN,FP,TN = find_conf_matrix_values(y_true,y_pred)  
    return TP/(TP+FP)
```
### Recall
Recall is calculated using the following formula:

  $ \text{Recall} = \frac{TP}{TP + FN} $

Of all the real positives: how many did my model find?
+ High recall = The model hardly overlooks any true positives.
+ Low recall = Many positives slip through the model's net.

**Recall is therefore important when false negatives are very costly.**

#### Examples:

+ Cancer diagnosis: A sick person must not be overlooked.
+ Fraud detection: Cases of fraud must be found at all costs.

#### Implementation in Sklearn
```python
from sklearn.metrics import recall_score

y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 0, 1, 1]

recall = recall_score(y_true, y_pred)

print("Recall: ", recall)
```
#### self implimented
```python
def my_recall_score(y_true, y_pred):
    '''own function for the metric recall'''
    # calculates the fraction of positive samples predicted correctly
    TP,FN,FP,TN = find_conf_matrix_values(y_true,y_pred)  
    return TP/(TP + FN)
```

### 🔹 Precision vs. Recall

* Precision = ‘How many of the cases predicted to be positive are actually positive?’

* Recall = ‘How many of the cases that are actually positive did I find?’

* Often, a trade-off must be made: increasing recall (detecting more positives) often decreases precision (generating more false alarms).


### F1-score
F1-score is calculated using the following formula:

 $ \text{F1-Score} = \frac{2*(precision*recall)}{precision + recall} $
* A high F1-score indicates that the model is performing well in both precision and recall, 
* while a low F1-score indicates that the model is not performing well in either precision or recall.

#### Implementation in Sklearn
```python
from sklearn.metrics import f1_score

y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 0, 1, 1]

f1 = f1_score(y_true, y_pred)

print("F1-Score: ", f1)
```
#### self implimented
```python
def my_f1_score(y_true, y_pred):
    '''own function for the metric f1 score'''
    # calculates the F1 score
    recall = my_recall_score(y_true,y_pred)  
    precision = my_precision_score(y_true,y_pred)  
    return 2*(precision * recall)/(precision + recall)
```
### AUC-ROC curve
AUC stands for Area Under the Curve, 
and ROC stands for Receiver Operating Characteristic.
+ tradeoff between true positive rate (TPR) and false positive rate (FPR) at different thresholds

$ \text{TPR } = \frac{True Positive}{(True Positives + False Negatives)} $

$ \text{FPR } = \frac{False Positive}{(False Positives + True Negatives)} $

The TPR is also known as Sensitivity, Recall, or Hit Rate.

---

## __Regression Metrics__ 

### 1. Mean Absolute Error (MAE)

$$
MAE = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
$$

* How it works: 
   * Takes the absolute difference between predicted and actual values and averages them.

* **When to use:**

  * When you want an error metric that’s easy to interpret (e.g., “on average, my model is off by 5 units”).

  * When outliers are not critical (MAE treats all errors equally).

Example:

Predicting house prices → MAE = $5,000 means the model is off by about $5k per house.

### 2. Mean Squared Error (MSE)

$$
MSE = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

* How it works: 
  * Squares errors before averaging → larger errors are penalized more heavily.

* **When to use:**

  * When large errors are very costly (you care more about not making big mistakes).

  * Useful during training because it’s differentiable and smooth → common loss function in regression.

Example: 

Predicting energy demand → underestimating by 100 units is much worse than underestimating by 10 units.

### 3. Root Mean Squared Error (RMSE)

$$
RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}
$$

* How it works: 
   * Just the square root of MSE, so it has the same unit as the target variable.

* **When to use:**

  * When you want to penalize large errors (like MSE), but still want the metric in interpretable units.

  * Often the default metric for regression tasks in practice.

Example: 

Predicting temperature → RMSE = 2.5°C means predictions are typically within 2.5°C of the real value.

### 4. R² (Coefficient of Determination)

$$
R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}
$$

+ How it works: 
  + Compares the model’s error to simply predicting the mean. Measures how much variance is explained.

+ **When to use:**

   + To understand overall fit of the model.

   + Best when comparing models on the same dataset.

⚠️ Can be misleading in non-linear regression or when extrapolating.

Example: 

R² = 0.85 means the model explains 85% of the variance in housing prices.

### 5. Mean Absolute Percentage Error (MAPE)

$$
MAPE = \frac{100}{n} \sum_{i=1}^n \left|\frac{y_i - \hat{y}_i}{y_i}\right|
$$

+ How it works: 
  + Expresses errors as a percentage of the actual values.

+ **When to use:**

  + When you need relative error, not absolute error.

  + Popular in forecasting and business settings (e.g., demand, sales).

⚠️ Problem: If actual values are very close to zero, MAPE can blow up or be undefined.

Example: 

Forecasting sales → MAPE = 7% means the forecast is on average 7% off from reality.

### Summary Regression metrics

| Metric | Description | Relevant Points |
|--------|-------------|-----------------|
| **MAE** (Mean Absolute Error) | Average of absolute errors. Easy to interpret. | Robust to outliers, good for general interpretability. |
| **MSE** (Mean Squared Error) | Average of squared errors. | Penalizes large errors more heavily, useful when big mistakes are costly. |
| **RMSE** (Root Mean Squared Error) | Square root of MSE, same unit as target. | Popular in practice, balances error penalization with interpretability. |
| **R²** (Coefficient of Determination) | Proportion of variance explained by the model. | Good for model comparison, but can be misleading with non-linear data. |
| **MAPE** (Mean Absolute Percentage Error) | Average error in percentage terms. | Useful in forecasting, intuitive, but unstable when actual values are near zero. |
---
## __Quick Hint Tables__ 


| Problem Type | Metrics Commonly Used | Example Applications |
|--------------|------------------------|-----------------------|
| **Regression (continuous, numerical target)**  how can we reduce the distance between prediction and real world| - MAE (Mean Absolute Error)  <br> - MSE (Mean Squared Error)  <br> - RMSE (Root Mean Squared Error)  <br> - R² (Coefficient of Determination)  <br> - MAPE (Mean Absolute Percentage Error) | - House price prediction  <br> - Temperature forecasting  <br> - Sales forecasting |
| **Classification (categorical target : class / label)** is the case or is not the case | - Accuracy  <br> - Precision  <br> - Recall (Sensitivity)  <br> - F1-score  <br> - Confusion Matrix  <br> - ROC-AUC | - Spam vs. Not Spam email filter  <br> - Fraud detection  <br> - Disease diagnosis |
---
##  __Helpful References__
* [course-material](https://ideal-adventure-6vymekm.pages.github.io/sessions/11_Evaluation_Metrics.html)
* [GitHub exercises repo]( neuefische/ds-evaluation-metrics)
* [The confusion Matrix by Statquest](https://www.youtube.com/watch?v=Kdsp6soqA7o)
* [ROC and AUC by Statquest](https://www.youtube.com/watch?v=4jRBRDbJemM)
* [Evaluation Metrics for classification](https://medium.com/@mlmind/evaluation-metrics-for-classification-fc770511052d)
* [Insights into Performance Fitness and Error Metrics for Machine Learning](https://arxiv.org/pdf/2006.00887)