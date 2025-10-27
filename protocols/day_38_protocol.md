# Day 38, 24.10.2025
On this day we learned about **Convolutional Neural Networks (CNNs)**, which are one of the most important architectures in deep learning. They are designed to process data that has a grid-like structure, such as images, videos and audio spectrograms.

---
## <span style="color:black"> __Basic Overview__ </span>
- Convolutional Neural Network's definition
- Steps (Forward and backpropagation)
- Useful code for CNN in Tensorflow

---
##  __Schedule__

|Time|Content|
|---|---|
|09:30 - 10:00|Daily Review (Artificial Neural Networks)|
|10:00 - 11:30|Convolutional Neural Networks|
|11:30 - 13:00|Lunch Break| 
|13:00 - 17:00|Practical exercises|

---
## <span style="color:black"> __What are CNNs?__ </span>
A **Convolutional Neural Network (CNN)** is a type of deep learning model designed to process and analyze visual data such as images or videos.
It automatically learns to detect important features, like edges, colors, shapes, and textures, by applying a series of layers that transform the input step by step.

It’s called "convolutional" because it uses a mathematical operation called a convolution, where small filters slide across the image to detect features like edges or textures. Mathematically, this means performing element-wise multiplication between the filter and small patches of the input, followed by summing up the results.

---
## <span style="color:black"> __Advantages of using CNNs when making image classification__ </span>

* Reduce number of input nodes
* Tolerate small shifts of the pixels positions
* take advantage of the correlations with near pixels

## <span style="color:black"> __Steps Forward Pass__ </span>

<img src="https://cdn-media-1.freecodecamp.org/images/dobVrh3SGyqQraM2ogi-P3VK2K-LFsBm7RLO" width="700">

Input Image  
↓  
1️⃣ **Apply Filter (Kernel)**  
   - Detect edges, patterns, or textures  
   - Create feature maps  
   <details>
   <summary><span style="color: red;">Click here for more information</span></summary>

   - Filters are small random matrices used to detect patterns (edges, curves, etc) or apply effects on the image.  
   - They are usually of size 3×3.  
   - For each 3×3 block of pixels in the input image:
       - Multiply each pixel by the corresponding entry of the kernel.  
       - Sum all the results.  
       - This sum plus a bias term becomes a new pixel in the output feature map. 
       - Stride is the step size of the filter by which it moves along the image 
   - To handle edges, the image is often padded with extra pixels so that border pixels also have enough neighbors to apply the filter properly.

   </details>
   <br>

   ↓
2️⃣ **Activation Function (ReLU)**
   - Adds non-linearity   
   - Keep positive values  
   - Set negative values to zero  
  <details>
   <summary><span style="color: red;">Click here for more information</span></summary>

   - After applying a filter, the feature map may contain positive and negative values.  
   - An activation function (usually ReLU) is applied to:
        - Keep positive values the same.  
        - Set negative values to zero.  
   - This adds **non-linearity**, allowing the network to learn more complex patterns.

   Other activation functions: https://www.tensorflow.org/api_docs/python/tf/keras/activations

   </details>
   <br>

   ↓
3️⃣ **Pooling Layer (Max Pooling)**  
   - Reduce feature map size while keeping important information (downsample)   
   - Make network robust to shifts 
  <details>
   <summary><span style="color: red;">Click here for more information</span></summary>

   - The most common is **max pooling**, which: 
     - Looks at a small block (e.g., 2×2) in the feature map.   
     - Keeps only the largest value.   
   - Pooling makes the network **faster** and more **robust** to small shifts in the image.
   - Other options: Average Pooling, Global Pooling, L2-norm

   </details>
   <br>

   ↓
4️⃣ **Flatten Feature Maps**  
   - Takes the 3D output and flattens it into a 1D vector so it can be passed into a dense (fully connected) layer. 

  <details>
   <summary><span style="color: red;">Click here for more information</span></summary>

   - After several convolution and pooling layers, the feature maps are multi-dimensional.   
   - Flattening transforms them into a **1D vector** so they can be processed by a fully connected layer.

   </details>
   <br>

   ↓
5️⃣ **Fully Connected (Dense) Layers**  
   - Combine all features  
   - Learn complex patterns 

  <details>
   <summary><span style="color: red;">Click here for more information</span></summary>

   - Dense layers connect every neuron in one layer to every neuron in the next.    
   - They combine all the extracted features to make a final prediction.  
   - The last dense layer typically has:
        - **One neuron with sigmoid** for binary classification.  
        - **Several neurons with softmax** for multi-class classification.

   </details>
   <br>

   ↓
6️⃣ **Output Prediction**  
   - Binary: sigmoid → probability 0 or 1  
   - Multi-class: softmax → converts raw scores to probabilities that sum to 1 across classes.

  <details>
   <summary><span style="color: red;">Click here for more information</span></summary>

   - After the dense layers, the network outputs probabilities for each class.    
   - The highest probability determines the predicted class.  

   </details>
   <br>

7️⃣ **Compute Loss**  
   - Measures how far the prediction is from the true labels  
   <details>
  <summary><span style="color: red;">Click here for more information</span></summary>

   - **Binary Cross-Entropy:** For binary classification  
   - **Categorical Cross-Entropy:** For multi-class classification. Requires the target labels Y to be one-hot encoded.
  
   - **Mean Squared Error (MSE):** For regression problems  
   - The loss value guides how much the network needs to adjust

   </details>
   <br>

  
## <span style="color:black"> __Backpropagation__ </span>

* After the forward pass, the network knows how wrong it was (loss).
* The backward pass computes gradients of the loss with respect to each weight, which tell each weight how it should change to reduce the loss.

<details>
   <summary><span style="color: red;">Click here for more information</span></summary>

   - **Optimizer:** Algorithm that updates weights and biases using gradients  
   - Common optimizers:
       - **SGD:** Basic gradient descent  
       - **Momentum:** Accelerates learning using past gradients  
       - **RMSProp:** Scales learning rate adaptively  
       - **Adam:** Combines momentum + RMSProp (most popular)  
   - Weight update formula: `new_weight = old_weight - learning_rate * gradient` 
</details> 


## <span style="color:black"> __Overfitting__ </span>
When validation loss significantly increases as you train for more epochs when compared to training loss

## <span style="color:black"> __Useful code for CNN in Tensorflow__ </span>
```python
from tensorflow.keras.layers import Conv2D, Dense, MaxPooling2D, Activation, Flatten
```
## Model definition
```python
# Sequential means the model is built layer-by-layer, one after another

model = Sequential([
    # convolutional block
    Conv2D(filters=6,kernel_size=(3,3),strides=(1,1),padding='same',activation='relu',input_shape=(28,28,1)),

    MaxPooling2D(pool_size=(2,2),strides=2),

    Flatten(),
    Dense(units=10,activation='softmax')
])
```
* filters=6 → the layer learns 6 different feature detectors (e.g., edges, curves, etc.).
* kernel_size=(3,3) → each filter is a 3×3 sliding window.
* strides=(1,1) → move the filter 1 pixel at a time (standard stride).
* padding='same' → pads input with zeros so the output has the same spatial size (28×28).
* activation='relu' → replaces all negative values with 0, introducing nonlinearity.
* input_shape=(28,28,1) → input images are 28×28 pixels, 1 channel (grayscale).
* After this layer, you’ll have an output of shape (28, 28, 6).
* pool_size=(2,2) → take the maximum value in each 2×2 block.
* strides=2 → move the pooling window 2 pixels at a time (non-overlapping).

* Flatten() takes the 3D output of the last conv block and flattens it into a 1D vector so it can be passed into a dense (fully connected) layer.
* Dense(units=10, activation='softmax')
  * 10 units → one for each class (e.g., digits 0–9 in MNIST).
  * softmax → converts raw scores to probabilities that sum to 1 across classes.

## Model compilation
```python
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])
```
* Instead of using one fixed learning rate, RMSProp slows down updates for weights that frequently change and speeds up updates for those that rarely change.
* loss='categorical_crossentropy' defines what your model tries to minimize during training. Used for multi-class classification problems. Requires the target labels Y to be one-hot encoded.

## Fit the model
```python
epochs = 10
accuracy_metrics = model.fit(xtrain,ytrain,batch_size=128,epochs=epochs,validation_split=0.3)
```
- The number of epochs controls the number of complete passes through the training dataset.
- The batch size controls the number of training samples to work through before the model’s internal parameters are updated.

## Prediction
```python
pred = model.predict(data)
```
---
## <span style="color:black"> __Helpful References__
* Lecture slides:\
 https://ideal-adventure-6vymekm.pages.github.io/sessions/19_Image_Modelling.html#
* An intuitive guide to Convolutional Neural Networks:\
https://www.freecodecamp.org/news/an-intuitive-guide-to-convolutional-neural-networks-260c2de0a050/
* Understanding Kernels:\
https://setosa.io/ev/image-kernels/
