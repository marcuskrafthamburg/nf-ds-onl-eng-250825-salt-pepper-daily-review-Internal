# Day 24, 26.09.2025

##  __Basic Overview__ 
*  Today it was all about "Gradient Descent"
---
##  __Schedule__

|09:00 - 10:00|Daily Review|
|10:00 - 11:30|theoretical input: Gradient Descent|
|11:30 - 13:30|Lunch Break| 
|13:30 - 17:00|Practical exercises: [gradient-descent](https://github.com/neuefische/ds-gradient-descent “gradient-descent”)

##  __The core essentials of Gradient Descent:__ 
**Idea:** 
An iterative optimization method to minimize a cost function by updating parameters step by step in the opposite direction of the gradient.

**When to use:**
* The function is too complex to solve analytically (no closed-form solution).
* The function is high-dimensional, with many parameters (e.g., weights in a neural network).
* The loss/error function can only be evaluated on data samples, not solved directly.

**How it works:** Start with a random θ and update it step by step using Gradient Descent until the cost J(θ) becomes small. The final θ is (approximately) the optimal one. 

**Typical use cases:** Training machine learning models such as linear regression, logistic regression, and neural networks.


# 5 Steps of using Gradient Descent:
* Step 1: Define model
* Step 2: Define the cost function --> what do you want to minimize
* Step 3: Initialize Gradient Descent --> Deliberately set some starting values
* Step 4: Start descent:
  * Take derivatives with respect to parameters
  * Set your learning rate (step-size)
  * Adjust your parameters (step)
* Step 5: Repeat 4. till there is no further improvement 

### Learning rate: α
* if too large → may overshoot and diverge.
* if too small → very slow convergence.
* 𝛼 is a hyperparameter → you choose it manually.
* In practice, you test several values (e.g., 0.1, 0.01, 0.001).
* The goal is to find an 𝛼 where:
  * the cost decreases quickly,
  * but does not oscillate or diverge.  (In De: aber nicht chaotisch hin- und herspringt.)
* Usually, you pick 𝛼 by **experimentation** or **validation** data.

### Parameter vs. Hyperparameter: 
**Parameters** → values the model learns from data (z. B. θ0,θ1 in linear regression).

**Hyperparameters** → values we must set before training. They are not learned by the algorithm itself.

### Update rule:  θ:=θ−α⋅∇J(θ)
θ = parameters
α = learning rate (step size)
∇J(θ) = gradient (derivative of the cost function)

## Main challenges of Gradient Descent or Convex vs. non-convex.

* A convex function is like a smooth bowl. There’s only one lowest point (global minimum).
* If you pick any two points on the curve and connect them with a straight line, that line lies above or on the curve. That’s why convex functions just have one big global minimum.
* In linear regression with MSE (Mean Squared Error), the cost function is convex → Gradient Descent will always find that single minimum
  
**The problem in general ML models:** Not every cost function is convex. For example, in neural networks the cost surface can be very messy:
* Local minima → points that are lower than their neighbors, but not the absolute lowest. Gradient Descent can get stuck here.
* Plateaus → flat regions where the gradient is almost zero. Then Gradient Descent makes little or no progress and training becomes very slow.

* The data must be scaled. Because unscaled data causes slow convergence (like a zig-zag). Scaled data has fast convergence (straight path)).

### Different versions/types of Gradient Descent:
* #### Batch GD:
 * Uses the whole dataset → stable, but slow.
* #### Stochastic GD (SGD):
* Uses one data point randomly → fast, but noisy.
* #### Mini-Batch GD:
* Uses small batches → standard in practice.


### Example: 
#### A step by step example with linear regression:
**Step 1:** 
Suppose we want to predict house price (y) from size (x):
$$
\hat{y} = \theta_0 + \theta_1 x
$$

Here:  
- $\theta_0$ = intercept  
- $\theta_1$ = slope


**Step 2:** 
Take one house with size: 𝑥 to the power of 𝑖 and true price: 𝑦 to the power of 𝑖.
$$
\text{Error}^{(i)} = \hat{y}^{(i)} - y^{(i)}
$$

with Prediction:

$$
\hat{y}^{(i)} = \theta_0 + \theta_1 x^{(i)}
$$

**step 3:** Cost for one data point: We don’t want errors to cancel out, so we square it:
$$
\text{Cost}^{(i)} = \left( \hat{y}^{(i)} - y^{(i)} \right)^2
$$

**Step 4:** Cost for the whole dataset: If we have m houses (data points), we take the average squared error:
$$
J(\theta_0 , \theta_1) = \frac{1}{m} \sum_{i=1}^{m} \left( \hat{y}^{(i)} - y^{(i)} \right)^2
$$

**Step 5:** Optimization (Gradient Descent): Now we want to minimize this cost function. 
That means: Compute the gradient of J(θ) with respect to the parameters θ zero and one . 
Update the parameters step by step: 
   * θ:=θ−α⋅∇ θ ​ where α = learning rate.

**Step 6:** Iteration: Start with random values for 𝜃
* Repeat: Compute predictions  y hat
* Compute cost J(θ).
* Compute gradient ∇ θ ​ J(θ).
* Update 𝜃 θ.
* Stop when cost doesn’t decrease much anymore (convergence).

**Step 7:** Result:The final parameters 𝜃0 and 𝜃1 approximate the “best fit” line.
This line minimizes the average squared error between predictions and true values.
	​




