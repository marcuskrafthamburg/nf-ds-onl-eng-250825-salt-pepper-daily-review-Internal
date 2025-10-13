

---


---
#  Day 34, 09.10.2025

---

## **Basic Overview**

* CART (Classification and Regression Trees)
* Decision trees: greedy splits, cost functions (MSE for regression, Gini for classification)
* Pros/cons: interpretable, handles mixed data, robust to outliers vs unstable, high variance
* Ensemble methods: reduce variance, increase robustness

  * Bagging, Random Forest, Extra-Trees
  * Stacking/Blending
* Majority voting: hard vs soft voting
* Weak learners: slightly better than random, independence/diversity matters
* Bias-variance tradeoff: high variance in single trees vs reduced variance in forests
* Random Forest: bootstrapping + random feature subsets → averaging predictions

---

## Schedule

| Time | Content |
|------|----------|
| 09:30 - 10:00 | Daily review |
| 10:00 - 11:00 | Lecture on Ensemble Methods |
| 11:00 - 13:00 | Lunch Break |
| 13:00 -       | Self-study/Pair-Programming|

---
#  Ensemble Methods   
### Daily Review Summary

---

## CART (Classification and Regression Trees)

**Key idea:**  
CART builds decision trees using a *greedy* approach — finds the best feature and value to split data.

- **Regression cost:** MSE (Mean Squared Error) - Is a metric that calculates the average of the squared differences between predicted values and actual values, used to measure the performance of regression models. By squaring the errors, MSE penalizes larger errors more heavily, and a lower MSE indicates a more accurate model. 
- **Classification cost:** Gini impurity - Is a measure used in decision trees to quantify the likelihood of a randomly chosen data point being misclassified. A low Gini impurity value indicates a "pure" node where most data points belong to a single class, while a high value indicates a "mixed" or "impure" node with a more even distribution of different classes 
- **Regularisation:** It means adding limits to stop the tree from growing too complex and overfitting the training data.
These parameters control how deep or detailed the tree can grow. pruning with 

`max_depth` - What it does: Limits how deep the tree can go (number of levels). Why it helps: Prevents the tree from memorizing the data (overfitting);
```python
DecisionTreeClassifier(max_depth=5)
```
`max_leaves` - What it does: Sets the maximum number of leaf nodes (final decision points). Why it helps: Fewer leaves = simpler model = better generalisation.
```python
DecisionTreeClassifier(max_leaf_nodes=10)
```
`min_samples_split` - What it does: The minimum number of samples required to split a node. Why it helps: Ensures that nodes with very few samples don’t split (reduces noise and overfitting).
```python
DecisionTreeClassifier(min_samples_split=4)
```

- **Problem type:** NP-complete (hard to solve optimally)

**Pros:**
- Interpretable (“white box” model)
- Handles mixed data types
- Robust to outliers

**Cons:**
- Prone to overfitting (high variance)
- Unstable (small data changes → different trees)
- Greedy → local, not global, optimum



**Conclusion:**  
 Don’t rely on a single tree — combine many (ensemble).

---

##  Wisdom of Crowds

Ensemble = “asking multiple models for opinions.”

**Conditions for effective crowds:**
1. Diverse opinions  
2. Independence  
3. Decentralization  
4. Aggregation (e.g., voting)

---

##  Majority Voting

Combine predictions from several models:

- **Hard Voting:** choose the majority class  
- **Soft Voting:** average predicted probabilities (usually better)
Python Example:
```python
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier()
clf3 = SVC(probability=True)

voting_clf = VotingClassifier(
    estimators=[('lr', clf1), ('dt', clf2), ('svc', clf3)],
    voting='soft'
)
voting_clf.fit(X_train, y_train)
y_pred = voting_clf.predict(X_test)
```

**Calibration:**  
Calibrated probabilities ensure proper aggregation using `CalibratedClassifierCV` in sklearn.

**Why it works:**  
If models are:
- Better than random (weak learners)
- Sufficiently different (low correlation)
- Numerous enough  

→ Ensemble lowers overall error (reduces variance).

---

##  Ways to Build Ensembles

### 1️ Bagging (Bootstrap Aggregating)
- Train same model on random *subsets* of data (with replacement).  
- Reduces variance, but models can still be correlated.  
```python
from sklearn.ensemble import BaggingClassifier

bagging = BaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=100,
    random_state=42
)
bagging.fit(X_train, y_train)
```
### 2️ Random Forest
- Adds randomness to features at each split → decorrelates trees.  
- Improves performance and stability.  
- Out-of-bag (OOB) evaluation estimates error without extra validation data.
```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, max_features='sqrt', oob_score=True, random_state=42)
rf.fit(X_train, y_train)
print("OOB Accuracy:", rf.oob_score_)
```

### 3️ Extra Trees (Extremely Randomized Trees)
- Randomly choose both *features* and *split thresholds.*  
- Faster and less variance than Random Forest.
```python
from sklearn.ensemble import ExtraTreesClassifier

et = ExtraTreesClassifier(n_estimators=100, random_state=42)
et.fit(X_train, y_train)
```

---

##  Accuracy vs Variance

| Model Type      | Accuracy | Variance |
|------------------|-----------|-----------|
| Decision Tree    | Low       | High      |
| Random Forest    | High      | Medium    |
| Extra Trees      | High      | Low       |

---

##  Stacking / Blending

- Train multiple base models (can be different types: Tree, SVM, NN, etc.)
- Use a **meta-model** to combine predictions.
- Use **cross-validation** to avoid overfitting.
```python
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

estimators = [
    ('dt', DecisionTreeClassifier()),
    ('svc', SVC(probability=True))
]
stacking_clf = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression()
)
stacking_clf.fit(X_train, y_train)
y_pred = stacking_clf.predict(X_test)
```

---

##  References

  

- Sklearn documentation: `VotingClassifier`, `RandomForestClassifier`, `ExtraTreesClassifier`

- GitHubRepo: https://github.com/neuefische/ds-random-forest 

- Course Material: https://ideal-adventure-6vymekm.pages.github.io/sessions/16_Ensemble_Methods_part1.html

- Lecture slides: https://docs.google.com/presentation/d/1Wc3OWeEpJDr_6JhS31EZjsRtcZp8FYyD/edit?slide=id.p27#slide=id.p27

---

 **Main takeaway:**  
> Don’t trust one tree — trust the forest  
