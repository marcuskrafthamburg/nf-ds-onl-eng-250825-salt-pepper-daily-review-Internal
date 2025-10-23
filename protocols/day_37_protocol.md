# Day 37 — 21.10.2025
## Basic Overview
* [Neural Networks](#NN)
* [Training the Network](#Training)
* [Python Deep Learning Libraries](#NN)
* [References](#Training)
## Schedule
Time| Content
-- | -- 
10:00 - 10:15 |Good morning love + retroperspective of presenting at ML challenge
10:15 - 11:30 |Neural Networks
11:30 - 13:00 |Lunch Break
13:00 - 16:00 |Practical exercises
16:00 |End of day


## Retroperspective Recap
- Hacks for presenting: post-it on screen, structured slides with action titles etc.
- Developing presentation skills through exercising  
- Regulating nervous system down (i.e. positive self-talk, breathing technique, massage, power positions)
- How to explain it to a grandma/child/friend?



## Neural Networks

Note: Switching from Machine Learning into Deep Learning


### When do we want to use Deep Learning?
- non linear 
- many dimensions

Note: Needs lot of energy, therefore always try simpler models first


### What are Neural Networks?
Origin idea comes from neurons connected to logical computation: 
- INPUT --> SUM of INPUT -> ACTIVATION of function -> OUTPUT

Therefore,  a neural network is a set of connected math functions that learn pattern from data, and backpropagation (see below) is the process that helps it learn by adjuszing its mistakes step by step.

<img src="https://www2.cs.uregina.ca/~dbd/cs831/notes/neural-networks/neural-networks/mlp.png" width="600">
 

- layer 0 = input layer R
- layer 1 = hidden layer (can be more) R
- layer 2 = output layer R

I.e. Deep Learning network with D=4 hidden layers: 16 neurons required to solve problem (much more compact as size in linear)

Each layer transforms data a bit more until the last one gives a prediction. Together the neurons figure out complex relationships.

It’s basically lots of simple math equations stacked together that learn from examples.
-> Adaptive basis function model = sum of many functions (remember ensemble methods)

Note: You don't need to know the math if you don't want to become a Deep Learning Developer but it helps for backpropagation, CNNs, regularization for ANNs etc.


### Most common activation functions
These decide how much “signal” each neuron passes forward - they add nonlinearity, letting the network learn complex things (not just straight lines).

- Sigmoid 
- Tanh
- ReLU (Rectified Linear unit)


## Training the Network 

### Backpropagation 

Makes training of very deep networks possible 
<div style="background-color:white; padding:10px;">
  <img src="https://i.sstatic.net/1214s.png" width="600">
</div>

In simple terms: 
1. The network makes a prediction (feed forward)
2. It compares the prediction to the true answer (using a loss function, i.e. MSE, MAE etc.)
3. It calculates how wrong it was and sends the error backward through all the layers of network
4. Each neuron slightly adjusts its weights to reduce future errors

Repeat this over and over, and the network gets smarter! 
(feed foward -> loss calculation -> backpropagating and changing weights)

### Parameters 
These are internal values that change during training - the model “learns” them automatically to minimize the loss function (Think: memory)

- Weights 
- Biases 
- Layer outputs (activations)

### Hyperparameters
These define how the model learns - they aren’t learned, but tuned by you.

- Learning rate (very important - using it as indicator to update the weights)
- Number of layers (not so much)
- Number of neurons per layer (important)
- Number of features (important)
- Mini-batch size (important)
- Optimization algorithm (important)
- Learning rate decay (not so much)

How to tune them?
- Try random values - do not use a grid!

### Regularization in Neural Networks 
To prevent overfitting (they are considered hyperparameters, too)

- L2 (constraining/limiting the weights)
- L1 (constraining/limiting the weights)
- Dropout (randomly eliminates nodes in each optimization step)
- Early stopping 

## Python Deep Learning Libraries

- TensorFlow
- Keras
- PyTorch
- etc.

TensorFlow tool: https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=2,2&seed=0.48360&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false

Note: DAG - directed acyclic graph/flowchart

=)

##  References
* Lecture slides
https://ideal-adventure-6vymekm.pages.github.io/sessions/18_Neural_Networks.html
    
* Explainer video Neural Networks Part 1: 
https://www.youtube.com/watch?v=CqOfi41LfDw&list=PLKPJtUGFjr1v8JvbezsTl36GT3B9TvprL&index=3

* Explainer video Neural Networks Part 2: 
https://www.youtube.com/watch?v=IN2XmBhILt4&list=PLKPJtUGFjr1v8JvbezsTl36GT3B9TvprL&index=4


