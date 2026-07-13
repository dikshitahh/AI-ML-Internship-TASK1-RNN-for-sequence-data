# AI-ML-Internship-TASK1-RNN-for-sequence-data

# Sentiment Analysis using LSTM

# Overview
This project demonstrates the use of Recurrent Neural Network (RNN), specially a Long Short Term Memory(LSTM) Network, for sentiment analysis on the IMDB Movie Reviews dataset. The model is trained to classify movie reviews as either positive or negative based on the next content.

# Objective
- Understand the working of Recurrent Neural Network(RNNs)
- Learn why Lstm networks perform better than standard RNNs for sequential data.
- Build and Train an LSTM model for sentiment classification.
- Evaluate the model using classification metrics and visualization.

# Dataset
- Dataset: IMDB Movie Reviews
- Training Samples: 25000
- Testing Samples: 25000
- Classes:
    - Positive(1)
    - Negative(0)

# Data Preprocessing
The following preprocessing steps were performed:
- Loaded the IMDB dataset from TensorFlow/Keras.
- Limited the vocabulary to the top 10000 most frequent words.
- Padded all review sequences to a fixed length of 200 words.

# Model Architecture
The model consists of:
- Embedding Layer
- LSTM layer(64 units)
- Dense Output Layer with Sigmoid Activation

# Training Configuration
- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Batch Size: 64
- Epochs: 5
- Validation Split: 20%

# Evaluation
The model was evaluated using:
- Test Accuracy
- Confusion Matrix
- Classification Report
- Training vs Validation Accuracy Graph
- Training vs Validation Loss Graph

# Results
The LSTM model successfully learned to classify movie reviews with high accuracy while maintaining a low validation loss. The confusion matrix and classification report demonstrate effective sentiment classification performance.

# Conclusion 
This project demonstrates how LSTM networks effectively process sequential text data by remembering long term dependencies between words. compared to standard RNN, The LSTM model provides improved performance for sentiment analysis because it reduces the vanishing gradient problem and retains important contextual information over longer sequences.
