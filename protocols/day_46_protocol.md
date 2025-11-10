# Day 46 - Unsupervised Learning: Dimensionality Reduction 07.11.25
Disclaimer: This protocol was created with the help of ChatGPT and Claude.ai

---

## __Basic Overview__

* Introduction to Dimensionality Reduction techniques
* Principal Component Analysis (PCA) for feature reduction
* t-SNE for data visualization
* PCA integration in ML pipelines with real-world applications

---

## __Schedule__

|Time|Content|
|---|---|
|09:30 - 10:00|Daily Review (Day 45 - Time Series - Continuation)|
|10:00 - 12:00|Lecture|
|12:00 - 13:30|Lunch|
|13:30 - 16:00|Notebooks|
|16:00 - 16:30|Stand-Up|
|16:30 - end|Notebooks|

---

## __Table of Contents__

1. [What is Dimensionality Reduction?](#1-what-is-dimensionality-reduction)
2. [Principal Component Analysis (PCA)](#2-principal-component-analysis-pca)
   - [Wine Quality Classification Example](#practical-example-wine-quality-classification)
3. [t-SNE (t-Distributed Stochastic Neighbor Embedding)](#3-t-sne-t-distributed-stochastic-neighbor-embedding)
4. [PCA in ML Pipelines](#4-pca-in-ml-pipelines)
   - [Face Recognition Application](#real-world-application-face-recognition)
5. [Comparison Summary](#5-comparison-summary)
6. [Key Takeaways](#6-key-takeaways)
7. [Practical Tips & Workflow](#8-practical-tips--workflow)
8. [Advanced Topics & Extensions](#9-advanced-topics--extensions)
9. [Helpful References](#11-helpful-references)

---

## __1. What is Dimensionality Reduction?__

Dimensionality Reduction is the process of reducing the number of features (dimensions) in a dataset while preserving as much information as possible.

### Why do we need it?

* **Curse of Dimensionality**: Too many features can lead to overfitting and poor model performance
* **Visualization**: Humans can only visualize 2-3 dimensions effectively
* **Computational Efficiency**: Fewer features = faster training and prediction
* **Noise Reduction**: Removes irrelevant or redundant features
* **Storage**: Reduces memory requirements for large datasets

### Two Main Approaches:

1. **Feature Selection**: Select a subset of existing features (e.g., filter methods, wrapper methods)
2. **Feature Extraction**: Create new features by combining existing ones (PCA, t-SNE, autoencoders)

---

## __2. Principal Component Analysis (PCA)__

### What is PCA?

PCA was invented in 1901 by Karl Pearson and later developed by Harold Hotelling in the 1930s.

PCA is a **linear** dimensionality reduction technique that:
* Transforms correlated features into **uncorrelated principal components**
* Each component captures maximum variance in the data
* Components are **orthogonal** to each other
* Uses an orthogonal transformation to convert observations into linearly uncorrelated variables

**Important**: PCA is sensitive to the relative scaling of the original variables!

### Key Concepts

| Concept | Description |
|---|---|
| **Principal Components (PCs)** | New features created as linear combinations of original features |
| **Explained Variance** | How much information (variance) each PC captures |
| **Explained Variance Ratio** | Proportion of total variance explained by each component |
| **Loadings/Weights** | Contribution of each original feature to a PC |
| **Eigenvalues** | Measure of variance explained by each component |
| **Eigenvectors** | Directions of maximum variance (principal components) |

### How PCA Works

1. **Standardize the data** (mean=0, std=1) - PCA is sensitive to scale!
2. **Compute covariance matrix** to understand feature relationships
3. **Calculate eigenvectors and eigenvalues** from the covariance matrix
4. **Sort components** by explained variance (descending order)
5. **Select top k components** that explain desired amount of variance
6. **Transform data** to new coordinate system

The transformation ensures:
* First PC has the largest possible variance
* Each succeeding component has the highest variance possible under the constraint that it is orthogonal to preceding components
* Resulting vectors form an uncorrelated orthogonal basis set

### PCA in Python (sklearn)

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Step 1: ALWAYS scale data first!
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)

# Optional: Convert to DataFrame to preserve feature names
X_scaled_df = pd.DataFrame(X_scaled, columns=X_train.columns)

# Step 2: Create and fit PCA
pca = PCA(n_components=None)  # None = keep all components
pca.fit(X_scaled_df)

# Step 3: Transform data
X_transformed = pca.transform(X_scaled_df)

# Convert to DataFrame for easier handling
X_pca_df = pd.DataFrame(X_transformed)

# Useful attributes to explore
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Explained variance:", pca.explained_variance_)
print("Number of components:", pca.n_components_)
print("Number of features:", pca.n_features_)
print("Shape of components:", pca.components_.shape)
```

### Choosing Number of Components

**Option 1: Set percentage of variance to retain**
```python
pca = PCA(n_components=0.95)  # Keep 95% of variance
pca.fit(X_scaled)
print(f"Number of components selected: {pca.n_components_}")
```

**Option 2: Scree plot - visualize explained variance**
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.scatter(x=[i+1 for i in range(len(pca.explained_variance_ratio_))],
            y=pca.explained_variance_ratio_,
            s=200, alpha=0.75, c='orange', edgecolor='k')
plt.grid(True)
plt.title("Explained variance ratio of principal components", fontsize=20)
plt.xlabel("Principal components", fontsize=15)
plt.ylabel("Explained variance ratio", fontsize=15)
plt.show()
```

Look for the "elbow" where adding more components doesn't add much variance.

**Option 3: Cumulative variance plot**
```python
cumsum = np.cumsum(pca.explained_variance_ratio_)
plt.plot(cumsum)
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.axhline(y=0.95, color='r', linestyle='--', label='95% variance')
plt.legend()
```

### When to Use PCA

✅ **Good for:**
* High-dimensional data with correlated features
* Speeding up training time
* Visualizing high-dimensional data
* Removing multicollinearity before regression
* Preprocessing step before classification
* Data compression

⚠️ **Not ideal for:**
* Data with non-linear relationships (consider t-SNE or kernel PCA)
* When interpretability of original features is critical
* Small datasets with few samples
* Features are already uncorrelated

---

## __Practical Example: Wine Quality Classification__

### Dataset
* **Wine data**: 178 samples, 13 features, 3 wine classes
* Features: Alcohol, Malic acid, Ash, Alcalinity, Magnesium, Total phenols, Flavanoids, etc.
* Problem: Features are correlated (not independent)

### Feature Correlation Analysis

```python
# Visualize correlation matrix
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure(figsize=(16,12))
ax1 = fig.add_subplot(111)
cmap = cm.get_cmap('jet', 30)
cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
plt.title('Wine data set features correlation', fontsize=15)
fig.colorbar(cax)
plt.show()
```

**Observation**: Many features show high correlation → PCA can help!

### Box Plot Analysis

```python
for c in df.columns[1:]:
    df.boxplot(c, by='Class', figsize=(7,4), fontsize=14)
    plt.title(f"{c}\n", fontsize=16)
    plt.xlabel("Wine Class", fontsize=16)
```

Some features (Alcalinity, Total Phenols, Flavanoids) show good class separation.

### Applying PCA

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Split data
X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Apply PCA
pca = PCA(n_components=None)
pca.fit(X_train_scaled)

# Transform data
X_train_pca = pca.transform(X_train_scaled)
```

### Results

**Key Finding**:
* First principal component explains ~36% of variance
* Second component explains ~20% of variance
* Together: First 2 components explain **56%** of total variance

### Classification Comparison

**Model 1: Naive Bayes on all 13 features**
```python
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
accuracy_score(y_test, y_pred)  # ~98-99%
```

**Model 2: Naive Bayes on first 2 PCA components**
```python
gnb_pca = GaussianNB()
gnb_pca.fit(X_train_pca[:, [0,1]], y_train)

# Transform test data
X_test_scaled = scaler.transform(X_test)
X_test_pca = pca.transform(X_test_scaled)

y_pred_pca = gnb_pca.predict(X_test_pca[:, [0,1]])
accuracy_score(y_test, y_pred_pca)  # ~95-97%
```

**Conclusion**:
* PCA reduces dimensions from 13 → 2 (85% reduction!)
* Accuracy drops only slightly (~2-4%)
* Much better visualization and faster training
* Great trade-off between dimensionality and performance

---

## __3. t-SNE (t-Distributed Stochastic Neighbor Embedding)__

### What is t-SNE?

t-SNE is a **non-linear** dimensionality reduction technique primarily used for **visualization** (2D or 3D).

**Key principle**: Converts distances between data points in the original space to probabilities, then tries to preserve these probability distributions in lower dimensions using a heavy-tailed (Student's t) distribution.

### PCA vs t-SNE Comparison

| Feature | PCA | t-SNE |
|---|---|---|
| **Type** | Linear transformation | Non-linear transformation |
| **Purpose** | Dimensionality reduction + visualization | **Visualization only** |
| **Speed** | Fast O(n×d²) | Slow O(n²) |
| **Use in pipeline** | ✅ Yes | ❌ No |
| **Methods** | `fit()` + `transform()` | **Only `fit_transform()`** |
| **Deterministic** | ✅ Yes (same input = same output) | ❌ No (stochastic/random) |
| **Preserves** | Global structure, maximum variance | Local structure, neighborhoods |
| **New data** | ✅ Can transform test data | ❌ Must rerun on all data |
| **Interpretability** | Components have meaning | No direct interpretability |
| **Best for** | Feature reduction, preprocessing | Exploratory visualization, finding clusters |

### How t-SNE Works (Mathematical Background)

1. **Compute conditional probabilities** in original space:
   $$p_{j|i} = \frac{\exp(-d(\mathbf{x}_i, \mathbf{x}_j) / (2\sigma_i^2))}{\sum_{i \neq k} \exp(-d(\mathbf{x}_i, \mathbf{x}_k) / (2\sigma_i^2))}, \quad p_{i|i} = 0$$

2. **Generate joint probabilities**:
   $$p_{ij} = \frac{p_{j|i} + p_{i|j}}{2N}$$

3. **Use heavy-tailed distribution** for embedded space:
   $$q_{ij} = \frac{(1 + ||\mathbf{y}_i - \mathbf{y}_j||^2)^{-1}}{\sum_{k \neq l} (1 + ||\mathbf{y}_k - \mathbf{y}_l||^2)^{-1}}$$

4. **Minimize Kullback-Leibler divergence**:
   $$KL(P|Q) = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$$

Using gradient descent with various optimization tricks.

### t-SNE in Python

```python
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# For high-dimensional data: ALWAYS reduce with PCA/TruncatedSVD first!
from sklearn.decomposition import TruncatedSVD

# Step 1: Pre-reduce to ~50 dimensions (recommended for large datasets)
X_reduced = TruncatedSVD(n_components=50, random_state=0).fit_transform(X)

# Step 2: Apply t-SNE
tsne = TSNE(n_components=2,        # 2D output
            perplexity=40,         # Balance local vs global (5-50)
            learning_rate=100,     # Step size for optimization
            n_iter=1000,           # Number of iterations
            verbose=2,             # Show progress
            random_state=42)       # For reproducibility (somewhat)

X_embedded = tsne.fit_transform(X_reduced)

# Step 3: Visualize
plt.figure(figsize=(10,6))
plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=y,
            cmap='viridis', edgecolors='k', alpha=0.75, s=150)
plt.title('t-SNE Visualization')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.colorbar()
plt.show()
```

### Important t-SNE Parameters

**`perplexity`** (default=30):
* Balances attention between local and global aspects
* Roughly: "how many neighbors each point has"
* **Low (5-10)**: Focus on very local patterns, may fragment clusters
* **High (30-50)**: Consider broader structure
* **Rule of thumb**: Try values between 5 and 50
* Should be smaller than number of data points

**`learning_rate`** (default=200):
* Step size during gradient descent optimization
* **Too low**: Slow convergence, may get stuck in local minima
* **Too high**: Unstable optimization, poor results
* **Typical range**: 10 to 1000
* Try 100-200 first, then experiment

**`n_iter`** (default=1000):
* Number of optimization iterations
* **Minimum**: 250
* **Recommended**: 1000+ for good results
* Watch the KL divergence in verbose output - should stabilize

**`random_state`**:
* Sets random seed for reproducibility
* Note: Results can still vary slightly due to floating point operations

### t-SNE Best Practices

⚠️ **Critical Warnings:**

1. **Different runs produce different results** - t-SNE is stochastic!
2. **Cannot transform new data** - no `.transform()` method, must rerun on entire dataset
3. **Don't interpret distances between clusters** - only cluster separation matters
4. **Don't interpret cluster sizes** - can be misleading
5. **Cost function is not convex** - multiple local minima possible

✅ **Best Practices:**

1. **Pre-reduce dimensions first**:
   ```python
   # For high-dimensional data (>50 features)
   X_reduced = PCA(n_components=50).fit_transform(X)
   X_tsne = TSNE().fit_transform(X_reduced)
   ```

2. **Run multiple times** with different random states:
   ```python
   for seed in [0, 42, 123]:
       tsne = TSNE(random_state=seed)
       X_embedded = tsne.fit_transform(X)
       # Plot and compare
   ```

3. **Experiment with perplexity**:
   ```python
   for perp in [5, 30, 50]:
       tsne = TSNE(perplexity=perp)
       # Visualize and compare
   ```

4. **Check convergence** with `verbose=2`:
   * KL divergence should decrease and stabilize
   * If not converging, increase `n_iter` or adjust `learning_rate`

### t-SNE Examples from Notebooks

**Example 1: Iris Dataset**
```python
from sklearn.datasets import load_iris

iris = load_iris()
X_tsne = TSNE(learning_rate=100).fit_transform(iris.data)
X_pca = PCA().fit_transform(iris.data)

# Compare visualizations
plt.subplot(121)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=iris.target)
plt.title('t-SNE')
plt.subplot(122)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target)
plt.title('PCA')
```

**Result**: Both show good class separation; PCA sufficient for linear separation.

**Example 2: 20 Newsgroups (High-dimensional sparse text data)**
```python
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

categories = ['alt.atheism', 'talk.religion.misc', 'comp.graphics', 'sci.space']
newsgroups = fetch_20newsgroups(subset="train", categories=categories)
vectors = TfidfVectorizer().fit_transform(newsgroups.data)

# Sparse matrix: 2,034 samples × 34,118 features!

# Step 1: Reduce with TruncatedSVD
X_reduced = TruncatedSVD(n_components=50, random_state=0).fit_transform(vectors)

# Step 2: Apply t-SNE
X_embedded = TSNE(n_components=2, perplexity=40, verbose=2).fit_transform(X_reduced)

# Visualize
plt.figure(figsize=(10,10))
colors = ['purple', 'blue', 'green', 'yellow']
for i in range(4):
    indices = np.argwhere(newsgroups.target == i)
    plt.scatter(X_embedded[indices, 0], X_embedded[indices, 1],
                c=colors[i], marker="x", label=newsgroups.target_names[i])
plt.legend()
plt.show()
```

**Result**: Clear cluster separation between document categories!

**Example 3: MNIST Handwritten Digits**
```python
from sklearn.datasets import load_digits

digits = load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1)) / 255.0

# Reduce with PCA first
X_pca = PCA(n_components=50).fit_transform(data)

# Apply t-SNE
X_embedded = TSNE(n_components=2, perplexity=40, verbose=2).fit_transform(X_pca)

# Visualize
plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=digits.target, cmap='tab10')
plt.colorbar()
```

**Result**: Visualization showing distinct clusters for each digit (0-9)!

---

## __4. PCA in ML Pipelines__

### What is a Pipeline?

A **Pipeline** chains multiple preprocessing steps and a model into a single object.

**Benefits:**
* ✅ **Prevents data leakage** - ensures transforms only fit on training data
* ✅ **Cleaner code** - one object instead of multiple steps
* ✅ **Reproducibility** - same preprocessing for train/test/production
* ✅ **Hyperparameter tuning** - tune all steps together with GridSearchCV
* ✅ **Easier deployment** - single object to save and load

### Creating a Pipeline with PCA

**Method 1: `make_pipeline()` - Automatic naming**
```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC

# Steps are automatically named
model = make_pipeline(
    StandardScaler(),
    PCA(n_components=150),
    SVC(kernel='rbf', class_weight='balanced')
)

# Fit entire pipeline
model.fit(X_train, y_train)

# Predict (automatically applies all steps!)
y_pred = model.predict(X_test)

# Access steps
print(model.named_steps['standardscaler'])
print(model.named_steps['pca'])
```

**Method 2: `Pipeline()` - Manual naming (better for GridSearch)**
```python
from sklearn.pipeline import Pipeline

model = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=100)),
    ('classifier', SVC(kernel='rbf'))
])

model.fit(X_train, y_train)

# Access steps with custom names
print(model.named_steps['pca'].explained_variance_ratio_)
```

### Hyperparameter Tuning with GridSearchCV

```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
# Syntax: 'stepname__parametername'
param_grid = {
    'pca__n_components': [50, 100, 150],
    'classifier__C': [5, 10, 50],
    'classifier__gamma': [0.0005, 0.001, 0.005]
}

# Grid search with cross-validation
grid = GridSearchCV(model,
                    param_grid,
                    cv=5,              # 5-fold cross-validation
                    verbose=2,         # Show progress
                    n_jobs=-1)         # Use all CPU cores

grid.fit(X_train, y_train)

# Best parameters and score
print("Best parameters:", grid.best_params_)
print("Best CV score:", grid.best_score_)

# Use best model
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)
```

---

## __Real-World Application: Face Recognition__

### Problem Setup
* **Dataset**: Labeled Faces in the Wild (LFW)
* **Task**: Classify faces of public figures
* **Challenge**: Each image has 62×47 = 2,914 pixels (features!)
* **Goal**: Reduce dimensions while maintaining classification accuracy

### Complete Pipeline Implementation

```python
from sklearn.datasets import fetch_lfw_people
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# 1. Load data
faces = fetch_lfw_people(min_faces_per_person=60)
print(faces.target_names)
print(faces.images.shape)

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    faces.data, faces.target, random_state=42
)

# 3. Create pipeline
# PCA reduces 2,914 → 150 features (95% reduction!)
model = make_pipeline(
    PCA(n_components=150, whiten=True, random_state=42),
    SVC(kernel='rbf', class_weight='balanced')
)

# 4. Hyperparameter tuning
param_grid = {
    'svc__C': [5, 10, 50],
    'svc__gamma': [0.0005, 0.001, 0.005]
}

grid = GridSearchCV(model, param_grid, cv=5, verbose=5)
grid.fit(X_train, y_train)

print("Best parameters:", grid.best_params_)

# 5. Evaluate
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)

# Classification report
print(classification_report(y_test, y_pred, target_names=faces.target_names))

# Confusion matrix
mat = confusion_matrix(y_test, y_pred)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=faces.target_names,
            yticklabels=faces.target_names)
plt.xlabel('True label')
plt.ylabel('Predicted label')
plt.show()

# 6. Visualize predictions
fig, ax = plt.subplots(4, 6)
for i, axi in enumerate(ax.flat):
    axi.imshow(X_test[i].reshape(62, 47), cmap='bone')
    axi.set(xticks=[], yticks=[])
    axi.set_ylabel(faces.target_names[y_pred[i]].split()[-1],
                   color='black' if y_pred[i] == y_test[i] else 'red')
fig.suptitle('Predicted Names; Incorrect Labels in Red', size=14)
```

### Results & Insights

**Performance:**
* Dimensionality: 2,914 → 150 features (95% reduction!)
* Training time: Significantly faster with PCA
* Accuracy: High accuracy on face recognition task
* Most errors: Confusion between similar-looking faces

**Why This Works:**
* SVM computational cost scales with number of samples and features
* PCA extracts most informative components (facial features)
* 150 components capture essential facial characteristics
* Combines dimensionality reduction + powerful classifier

**Note on SVM:**
* Support Vector Machine (SVM) - powerful but computationally expensive
* Used to be very popular in ML
* Legal licensing issues + computational cost → less common now
* Still excellent for small-to-medium datasets with PCA preprocessing
* Great demonstration of Pipeline + dimensionality reduction

---

## __5. Comparison Summary__

### When to Use What

| Scenario | Recommended Technique |
|---|---|
| Preprocessing for ML model | **PCA** (in Pipeline) |
| Visualizing clusters/patterns | **t-SNE** |
| Very high dimensions (>1000) | **PCA first**, then t-SNE |
| Need to transform new data | **PCA** (has transform method) |
| Linear relationships | **PCA** |
| Non-linear relationships | **t-SNE** or kernel PCA |
| Speed is critical | **PCA** |
| Interpretability matters | **PCA** (or feature selection) |
| Exploratory data analysis | **t-SNE** |

### Workflow Recommendation

```python
# Step 1: Explore with t-SNE
X_reduced = PCA(n_components=50).fit_transform(X_scaled)
X_tsne = TSNE(perplexity=30).fit_transform(X_reduced)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y)
# Understand: Are classes separable? Any patterns?

# Step 2: Build model with PCA in pipeline
model = make_pipeline(
    StandardScaler(),
    PCA(n_components=0.95),  # Keep 95% variance
    RandomForestClassifier()
)
model.fit(X_train, y_train)

# Step 3: Tune hyperparameters
param_grid = {
    'pca__n_components': [0.90, 0.95, 0.99],
    'randomforestclassifier__n_estimators': [100, 200]
}
grid = GridSearchCV(model, param_grid, cv=5)
grid.fit(X_train, y_train)
```

---

## __6. Key Takeaways__

1. **Always scale data before PCA** - it's sensitive to feature scales
   ```python
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)
   ```

2. **PCA is for modeling, t-SNE is for visualization**
   * PCA: Can use in pipelines, transform new data
   * t-SNE: Only `fit_transform()`, no prediction possible

3. **Choose n_components wisely**
   * Based on explained variance (e.g., 95%)
   * Using scree plot (look for elbow)
   * Through cross-validation in GridSearchCV

4. **Pre-reduce before t-SNE**
   * For data with >50 features, use PCA/TruncatedSVD first
   * Reduces to ~50 dimensions, then apply t-SNE
   * Much faster and often better results

5. **Pipelines prevent data leakage**
   * NEVER fit preprocessing on entire dataset
   * Pipeline ensures: fit on train, transform on test
   * Critical for valid model evaluation

6. **GridSearchCV works with pipelines**
   * Tune preprocessing AND model parameters
   * Syntax: `'stepname__parametername'`
   * Example: `'pca__n_components'`, `'svc__C'`

7. **t-SNE is stochastic**
   * Different runs → different results
   * Always set `random_state` for reproducibility
   * Run multiple times to verify patterns

8. **PCA preserves global structure, t-SNE preserves local structure**
   * PCA: Good for overall variance, linear relationships
   * t-SNE: Good for finding clusters, non-linear patterns

9. **Dimensionality reduction helps with curse of dimensionality**
   * Reduces overfitting
   * Speeds up training
   * Improves visualization
   * Removes noise and redundancy

10. **Practical rule of thumb**
    * <20 features: Maybe don't need dimensionality reduction
    * 20-100 features: PCA can help
    * >100 features: PCA almost always beneficial
    * >1000 features: PCA essential for most algorithms


---

## __7. Practical Tips & Workflow__

### Dimensionality Reduction Decision Tree

```
Do you have high-dimensional data?
├─ No (<20 features) → Probably don't need dimensionality reduction
└─ Yes (>20 features)
   ├─ Goal: Visualization?
   │  ├─ Linear patterns → Use PCA (2-3 components)
   │  └─ Non-linear patterns → Use t-SNE
   │     └─ If >50 features → PCA(50) first, then t-SNE
   │
   └─ Goal: Preprocessing for ML?
      ├─ Use PCA in Pipeline
      ├─ Choose n_components via:
      │  ├─ Variance threshold (0.95)
      │  ├─ Scree plot (elbow method)
      │  └─ GridSearchCV (best for production)
      └─ Always scale first!
```

### Recommended Analysis Workflow

```python
# 1. EXPLORE: Visualize with t-SNE
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Pre-reduce if needed
if X_scaled.shape[1] > 50:
    X_reduced = PCA(n_components=50).fit_transform(X_scaled)
else:
    X_reduced = X_scaled

# Apply t-SNE
X_tsne = TSNE(n_components=2, perplexity=30, random_state=42).fit_transform(X_reduced)

# Visualize
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='viridis', alpha=0.6)
plt.colorbar(scatter)
plt.title('t-SNE Visualization')
plt.show()

# 2. ANALYZE: Check PCA variance
pca = PCA()
pca.fit(X_scaled)

# Scree plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(pca.explained_variance_ratio_)+1),
         pca.explained_variance_ratio_, 'bo-')
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Scree Plot')
plt.show()

# Cumulative variance
cumsum = np.cumsum(pca.explained_variance_ratio_)
plt.plot(cumsum)
plt.axhline(y=0.95, color='r', linestyle='--')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.show()

# 3. MODEL: Build pipeline with PCA
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Define parameter grid
param_grid = {
    'pca__n_components': [0.90, 0.95, 0.99],
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [10, 20, None]
}

# Grid search
grid = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1, verbose=1)
grid.fit(X_train, y_train)

# Results
print("Best parameters:", grid.best_params_)
print("Best cross-validation score:", grid.best_score_)

# Evaluate on test set
y_pred = grid.predict(X_test)
print("\nTest set accuracy:", accuracy_score(y_test, y_pred))

# 4. INTERPRET: Analyze PCA components
best_pca = grid.best_estimator_.named_steps['pca']
print(f"Number of components: {best_pca.n_components_}")
print(f"Total variance explained: {sum(best_pca.explained_variance_ratio_):.3f}")

# Feature importance in first PC
if hasattr(X, 'columns'):
    loadings = pd.DataFrame(
        best_pca.components_[:3].T,
        columns=['PC1', 'PC2', 'PC3'],
        index=X.columns
    )
    print("\nTop features in first 3 components:")
    print(loadings.abs().sort_values('PC1', ascending=False).head(10))
```

---

## __8. Advanced Topics & Extensions__

### Other Dimensionality Reduction Techniques

**Linear methods:**
* **Truncated SVD**: Like PCA but works with sparse matrices (e.g., TF-IDF)
* **Linear Discriminant Analysis (LDA)**: Supervised, maximizes class separation
* **Factor Analysis**: Similar to PCA but models latent variables

**Non-linear methods:**
* **Kernel PCA**: Non-linear version of PCA using kernel trick
* **Isomap**: Preserves geodesic distances (manifold learning)
* **Locally Linear Embedding (LLE)**: Preserves local neighborhoods
* **UMAP**: Similar to t-SNE but faster and preserves more global structure
* **Autoencoders**: Neural network-based dimensionality reduction

### When to Try Advanced Methods

* **UMAP** instead of t-SNE: Faster, better global structure, can embed new data
* **Kernel PCA** instead of PCA: Non-linear relationships
* **LDA** instead of PCA: Supervised task, want class separation
* **Autoencoders**: Very high dimensions, need to embed new data, non-linear

### Further Resources for Deep Dive

**PCA Math:**
* [StatQuest: PCA Main Ideas](https://www.youtube.com/watch?v=HMOI_lkzW08)
* [Visual Explanation of PCA](https://setosa.io/ev/principal-component-analysis/)

**t-SNE Best Practices:**
* [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/)
* [Common t-SNE Mistakes](https://www.oreilly.com/content/an-illustrated-introduction-to-the-t-sne-algorithm/)

**UMAP (Modern Alternative):**
* [UMAP Documentation](https://umap-learn.readthedocs.io/)
* [Comparison: t-SNE vs UMAP](https://pair-code.github.io/understanding-umap/)

---
## __9. Helpful References__

### Documentation
* [Scikit-learn PCA Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
* [Scikit-learn t-SNE Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)
* [Scikit-learn Pipeline Documentation](https://scikit-learn.org/stable/modules/compose.html)
* [Scikit-learn Dimensionality Reduction Guide](https://scikit-learn.org/stable/modules/decomposition.html)

### Interactive Visualizations
* [PCA Explained Visually](https://setosa.io/ev/principal-component-analysis/)
* [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/)
* [Seeing Theory: PCA](https://seeing-theory.brown.edu/regression-analysis/index.html)

### Video Tutorials
* [StatQuest: PCA Step-by-Step](https://www.youtube.com/watch?v=FgakZw6K1QQ)
* [StatQuest: t-SNE Clearly Explained](https://www.youtube.com/watch?v=NEaUSP4YerM)

### Course Materials
* [Session Slides (PDF)](https://ideal-adventure-6vymekm.pages.github.io/sessions/22_Dimensionality_Reduction.html)
* Repository: `ds-dimensionality-reduction/`
  * [1_Principal_Component_Analysis.ipynb](../ds-dimensionality-reduction/1_Principal_Component_Analysis.ipynb)
  * [2_t_SNE.ipynb](../ds-dimensionality-reduction/2_t_SNE.ipynb)
  * [3_PCA_in_Pipeline.ipynb](../ds-dimensionality-reduction/3_PCA_in_Pipeline.ipynb)

### Additional Reading
* [Original PCA Paper (Karl Pearson, 1901)](https://www.tandfonline.com/doi/abs/10.1080/14786440109462720)
* [Original t-SNE Paper (van der Maaten & Hinton, 2008)](http://jmlr.org/papers/v9/vandermaaten08a.html)
* [Singular Value Decomposition (SVD)](https://en.wikipedia.org/wiki/Singular_value_decomposition)

### Cheat Sheets
* [Python Data Science Handbook: PCA](https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html)
* [Scikit-learn Cheat Sheet](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)
