# Day 25, 25.09.2025

##  📋 __Basic Overview__ (Table of Contents)

1. [Schedule](#schedule)
2. [Quick Review: Overfitting & Underfitting](#quick-review-overfitting--underfitting)
3. [Regularization Techniques](#regularization-techniques)
4. [Key Takeaways](#key-takeaways)
5. [Resources & References](#resources--references)

---

##  __Schedule__

|Time|Content|
|---|---|
|09:00 - 10:00|Daily Review 📝|
|10:00 - 12:00|Lecture: Regularization Techniques 👨‍🏫| 
|12:00 - 13:00|Lunch Break 🍽️|
|13:00 - end|Hands-on Exercises & Implementation 💪|

---

## Quick Review: Overfitting & Underfitting

### Polynomial Regression Term Structure

**From Simple to Complex Models:**

1) **Simple Linear Regression:** y = β0 + β1·x1

2) **Multiple Linear Regression:** y = β0 + β1·x1 + β2·x2 + β3·x3

3) **Add Interaction Terms (degree=2):** 
   - Original features: x1, x2, x3
   - Interaction terms: x1·x2, x1·x3, x2·x3
   - **Result:** y = β0 + β1·x1 + β2·x2 + β3·x3 + β4·(x1·x2) + β5·(x1·x3) + β6·(x2·x3)
   - Feature Count: 3 original + 3 combinations = 6 features total
   - **Beta mapping:** β0(intercept), β1(x1), β2(x2), β3(x3), β4(x1·x2), β5(x1·x3), β6(x2·x3)

4) **Exercise Example with 11 Features:**
   - Original features: 11 (x1, x2, ..., x11)
   - Interaction combinations: C(11,2) = 11!/(2!(11-2)!) = (11×10)/2 = 55
   - **Total features:** 11 + 55 = 66 features
   - **Final equation:** y = β0 + β1·x1 + β2·x2 + ... + β11·x11 + β12·(x1·x2) + β13·(x1·x3) + ... + β66·(x10·x11)
   - **Beta mapping:** β0(intercept), β1-β11(original features), β12-β66(interaction terms)

**With PolynomialFeatures:**
```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(interaction_only=True, include_bias=False, degree=2)
X_poly = poly.fit_transform(X)
# 11 original features → 66 features (11 + 55 combinations)
```

**The Problem:** More features = higher risk of overfitting
**The Solution:** Regularization controls these interaction coefficients

### Definition 📖
* **Overfitting** ❤️: Model captures noise → good training performance, poor test performance
* **Underfitting** 😂: Model too simple → poor performance on both training and test data

### Visual Indicators 📊
* **Overfitting**: Training accuracy >> Test accuracy
* **Underfitting**: Both training and test accuracy low
* **Good Fit**: Similar training and test accuracy, both high

---

## Regularization Techniques

### Why Regularization? 🤔

**The Problem:**
- Complex models often overfit to training data
- High variance leads to poor generalization
- Need to balance model complexity with performance

**The Solution:**
Regularization modifies the standard least squares objective function by adding penalty terms that constrain coefficient magnitudes. This addresses overfitting by limiting model complexity through coefficient shrinkage or elimination.

**Benefits:**
- ✅ Reduces overfitting
- ✅ Improves generalization
- ✅ Handles multicollinearity
- ✅ Prevents extreme coefficient values
- ✅ Works well with high-dimensional data

### Ridge Regression (L2) 🔵

**Mathematical Foundation:** 
```
Objective Function: MSE + α × Σ(βᵢ²)
```
The L2 penalty term Σ(βᵢ²) sums the squared coefficients, creating a smooth, differentiable constraint that proportionally shrinks all coefficients based on their magnitude.

**Characteristics:**
- Penalizes squared magnitude of coefficients
- Shrinks coefficients towards zero but never exactly zero
- Keeps all features in the model
- Handles multicollinearity effectively

**Ridge Function Attributes:**
```python
# Ridge Regression
ridge = Ridge(
    alpha=1.0,              # Regularization strength; higher = stronger shrinkage
    fit_intercept=True,     # Whether to calculate the intercept (otherwise assumed 0)
    normalize='deprecated', # Old option for normalizing X, now use preprocessing.StandardScaler
    max_iter=None,          # Max iterations for the solver (only for some solvers)
    tol=1e-3,               # Stopping tolerance for optimization
    solver='auto',          # Algorithm: 'auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga'
    random_state=None       # Random seed (used only by some solvers)
)
```

### Lasso Regression (L1) 🔶

**Mathematical Foundation:** 
```
Objective Function: MSE + α × Σ|βᵢ|
```
The L1 penalty term Σ|βᵢ| sums the absolute values of coefficients, creating a non-smooth constraint that can drive coefficients to exactly zero, effectively performing feature selection.

**Characteristics:**
- Penalizes absolute value of coefficients
- Can eliminate features completely (coefficients become 0)
- Creates sparse models through automatic feature selection
- Non-differentiable penalty function

**Lasso Function Attributes:**
```python
# Lasso Regression
lasso = Lasso(
    alpha=1.0,              # Regularization strength; higher = more coefficients driven to 0
    fit_intercept=True,     # Whether to fit the intercept
    max_iter=1000,          # Max iterations for coordinate descent solver
    tol=1e-4,               # Optimization tolerance (smaller = stricter convergence)
    precompute=False,       # Use precomputed Gram matrix for speed (can be 'auto')
    warm_start=False,       # Reuse solution of previous fit as initialization
    positive=False,         # If True, forces coefficients to be >= 0
    random_state=None,      # For coordinate descent shuffle
    selection='cyclic'      # How to update coefficients: 'cyclic' or 'random'
)
```

### Elastic Net 🔷

**Mathematical Foundation:** 
```
Objective Function: MSE + α × (l1_ratio × Σ|βᵢ| + (1-l1_ratio) × Σ(βᵢ²))
```
Combines both L1 and L2 penalties in a weighted sum. The l1_ratio parameter (0 ≤ l1_ratio ≤ 1) controls the balance: when l1_ratio=0 it becomes Ridge, when l1_ratio=1 it becomes Lasso.

**Characteristics:**
- Combines L1 and L2 penalties in single model
- l1_ratio parameter controls balance (0=Ridge, 1=Lasso)
- Provides both feature selection and coefficient shrinkage
- More stable than Lasso for correlated features

**Elastic Net Function Attributes:**
```python

# Elastic Net Regression
elastic = ElasticNet(
    alpha=1.0,              # Regularization strength (same meaning as Ridge/Lasso)
    l1_ratio=0.5,           # Mixing: 0 = Ridge (L2 only), 1 = Lasso (L1 only), in-between = both
    fit_intercept=True,     # Whether to fit the intercept
    max_iter=1000,          # Max iterations for solver
    tol=1e-4,               # Convergence tolerance
    warm_start=False,       # Reuse previous fit for initialization
    positive=False,         # If True, forces coefficients to be >= 0
    random_state=None,      # Seed for randomness in coefficient updates
    selection='cyclic'      # Update strategy: 'cyclic' or 'random'
)
```
---

## Visualization/Validation Tools

### Correlation heatmap
```python
ax = sns.heatmap(df.corr(), 
                 annot=True,     # Display correlation values in the cells
                 cmap="RdBu_r",  # Red-blue colormap (reversed)
                 center=0)       # Center the colormap at 0
```
Function description:
This function creates a heatmap that visualizes the pairwise correlation coefficients between all numerical features in the dataframe df.

The heatmap shows values ranging from -1 to +1, where:
+1 indicates a perfect positive correlation,
-1 indicates a perfect negative correlation,
0 indicates no linear correlation.
The color scale highlights the strength and direction of correlations, making it easy to detect strongly related or independent features.



### coeff_info() Analysis Function:

Coefficient Analysis Function: `coeff_info()`

**Purpose:**  
The `coeff_info()` function is a simple analysis tool to summarize the importance of features in a linear model.

**Function Definition:**
```python
def coeff_info(model):
    coeff_used = np.sum(model.coef_ != 0)  # count how many coefficients are non-zero
    print('The model is using', coeff_used, 'out of 66 features.')
    print("The highest coefficient has a value of:", max(model.coef_.round(3)))
```

- ✅ Gives a quick sense of which feature has the strongest impact on the model predictions.
- ✅ Helps identify feature importance at a glance.
- ✅ Useful to check if the model is sparse (few non-zero coefficients) or uses most features.
- ✅ Works best with linear models that expose coef_.
---

## Key Takeaways

### 🎯 **Regularization Method Selection**
- **Ridge (L2)**: Coefficient shrinkage, retains all features
- **Lasso (L1)**: Automatic feature selection, sparse solutions  
- **Elastic Net**: Combined approach, handles correlated features

### 🔧 **Implementation Guidelines**
- Scale features before applying regularization
- Higher α = stronger regularization = simpler model

---

## Resources & References

* [Link to exercise](https://github.com/neuefische/ds-predictive-regression/blob/main/2_Regularization.ipynb)

### Video Resources
* [Ridge Regression Explained](https://www.youtube.com/watch?v=Q81RR3yKn30&t=633s)
* [Lasso Regression Tutorial](https://www.youtube.com/watch?v=NGf0voTMlcs&t=37s)
* [Elastic Net Overview](https://www.youtube.com/watch?v=1dKRdX9bfIo&t=1s)
* [Regularization Comparison](https://www.youtube.com/watch?v=Xm2C_gTAl8c&t=118s)
* [Overfitting and Regularization](https://www.youtube.com/watch?v=EuBBz3bI-aA&t=2s)

### Documentation
* [Scikit-Learn Ridge Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
* [Scikit-Learn Lasso Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html)
* [Scikit-Learn ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html)
* [Cross-Validation Guide](https://scikit-learn.org/stable/modules/cross_validation.html)
* [Regularization Theory](https://scikit-learn.org/stable/modules/linear_model.html#regularization)