# Day 27 — 30.09.2025
## Basic Overview
* [Logistic Regression](#logistic-regression)
    * [General](#general)
* [Resources](#resources)
## Schedule
Time| Content
-- | --
09:00 - 10:00 |daily review
10:00 - 12:00 |presentation
12:00 - 13:00 |lunch
14:00 - end of day |work on notebooks


# Logistic Regression

### What?
A classification algorithm that predicts the probability of a binary outcome. Used in **supervised Learning**, where model uses annotated data (eg foto with label) to learn classification

**difference to Linear Regression:**
- Linear regression predicts continuous values and can output any number
- Logistic regression predicts probabilities (bounded between 0 and 1) and classifies into discrete categories

**Use cases:**
- email spam detection, sentiment analysis (sad/not sad), medical diagnosis, survive-die, admitted-rejected...
- can be extended to **multi-class classification**
- useful for categorical variables?

---


### 1. Sigmoid Function
- Takes any real number ($z$) as input
- Outputs a probability between 0 and 1
- Creates an S-shaped curve
- -> Maps number to probability (0 to 1)
- Used for predictions
- $σ(z) = 1/(1 +  e⁻ᶻ)$
- $z = θ₀ + θ₁x₁ + θ₂x₂ + ...$ <- make it linear optimization problem

![sigmoid](../images/sigmoid.png)

### 2. Logit Function
- aka **log-odds**
- -> Maps probability (0 to 1) to number
- Used for training/optimization
- $logit(p) = log(p/(1-p)) = θ₀ + θ₁x₁ + θ₂x₂ + ...$

> the two functions above are needed, because transformation goes in **both directions**


### Cost Function: Log Loss
- aka **Binary Cross-Entropy**
- ⚠️ cost function must be **convex** → guaranteed to find the global minimum using gradient descent
pic!!

**Why not use MSE (Mean Squared Error)?**
- Linear regression uses: $J(θ) = Σ(y_i - ŷ_i)²$
- This creates a **non-convex** function for logistic regression (hard to optimize, multiple local minima)

**Solution: Log-Likelihood Loss (Binary Cross-Entropy)**

**Formula:**
$$ J(θ) = -1/m Σ [y_i log(h_θ(x_i)) + (1 - y_i) log(1 - h_θ(x_i))] $$

**How it works:**
- When y = 1: only the first part matters → penalizes if prediction is far from 1
- When y = 0: only the second part matters → penalizes if prediction is far from 0
- **Loss** = error for a single data point
- **Cost** = average loss across ALL data points

**Goal:** Minimize J(θ) to increase confidence and reduce misclassification


---


---

## Decision Boundary

The **decision boundary** is where the model switches predictions:

**Mathematical definition:**
$$ θ^T x = 0 $$

- Depends on the number of features (n_features)
- For 1 feature: a point on the line
- For 2 features: a line in 2D space
- For 3+ features: a hyperplane in n-dimensional space

**Example:** If θ = [-3, 1] and feature is x:
- Decision boundary: -3 + 1·x = 0 → x = 3
- x < 3 → predict class 0
- x > 3 → predict class 1

---

## Key Takeaways

✅ Logistic regression predicts **probabilities**, not raw values
✅ The **sigmoid function** squashes outputs to [0, 1] range
✅ **Log loss** creates a convex cost function (unlike MSE)
✅ **Gradient descent** iteratively finds optimal parameters
✅ The **decision boundary** splits the feature space into classes
✅ **Logit & sigmoid** are inverse functions that transform between probability and log-odds spaces

---

## Resources

- [StatQuest: Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8)
- [StatQuest: LogOdds / logit()](https://www.youtube.com/watch?v=ARfXDSkQf1Y&list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe&index=2&pp=iAQB)
- 📚 [Hands-On Machine Learning with Scikit-Learn](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646)
- [Andrew Ng's Machine Learning Course](https://www.coursera.org/learn/machine-learning)
- [SVM Decision Boundaries Visualization](https://www.researchgate.net/figure/Classification-results-of-SVC-with-the-nonlinear-decision-boundary_fig1_255572951)

---

## TODO: Add Visuals

- [ ] Sigmoid curve showing the S-shape
- [ ] Convex vs non-convex cost functions
- [ ] Decision boundary examples
- [ ] Code examples from today's session