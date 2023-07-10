# Fashion MNIST Image Classification

A machine learning project for classifying images of clothing items from the [Fashion-MNIST dataset](https://github.com/zalandoresearch/fashion-mnist) using Convolutional Neural Networks (CNN), Random Forest, and Logistic Regression .

## Table of Contents

- [Installation](#installation)
- [Dataset Description](#dataset-description)
- [Implemented Models](#implemented-models)
- [Results](#results)


## Installation
1. Install Python 3.x from the [official website](https://www.python.org/downloads/).
2. Clone this repository or download the code as a ZIP file.
3. Install the required packages using pip:
   ```
   pip install numpy matplotlib seaborn scikit-learn keras tensorflow
   ```

## Dataset Description
The Fashion-MNIST dataset contains 70,000 grayscale images of clothing items, divided into 60,000 training images and 10,000 test images. Each image is 28x28 pixels, and each pixel has a value between 0 and 255. There are 10 classes of clothing items, as follows:
1. T-shirt/top
2. Trouser
3. Pullover
4. Dress
5. Coat
6. Sandal
7. Shirt
8. Sneaker
9. Bag
10. Ankle boot

## Implemented Models
This project implements three [machine learning models]

   -Convolutional Neural Network (CNN): A type of deep learning model specifically designed for image processing and recognition. CNNs consist of convolutional layers that can automatically learn to detect features in images, such as edges or patterns, by scanning small regions of the image. They often include pooling layers to reduce spatial dimensions, and fully connected layers to make predictions based on the detected features.
    
   -Random Forest Classifier: An ensemble learning method that builds multiple decision trees during the training process. Each tree is constructed using a random subset of features and samples from the dataset. When making a prediction, the input is passed through all the trees, and the final output is determined by the majority vote from all the trees. This approach helps improve the model's accuracy and prevents overfitting.
    
   -Logistic Regression: A supervised learning model that uses a logistic function to model the probability of a binary dependent variable. It can be extended to handle multi-class classification problems using techniques such as one-vs-rest or multinomial logistic regression. Logistic regression works by estimating the probabilities of each class and then selecting the class with the highest probability as the predicted output.    

## Results
The following table presents the accuracy scores for each model after training and testing on the Fashion-MNIST dataset:
-------------------------------------------------
| Model                              | Accuracy |
|------------------------------------|----------|
| Convolutional Neural Network (CNN) |  92.9%   |
| Random Forest Classifier           |  87.8%   |
| Logistic Regression                |  84.6%   |
-------------------------------------------------
These results show that the Convolutional Neural Network (CNN) achieved the highest accuracy among the three models, followed by the Random Forest Classifier and the Logistic Regression . Note that these values are examples and may vary depending on the specific configurations and training conditions.

You can also visualize the performance of each model by generating confusion matrices, which will help you understand how well each model is classifying each class and identify any misclassifications.

