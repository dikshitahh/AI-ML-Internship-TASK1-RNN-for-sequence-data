# Performance Evaluation

## Introduction

This project applies a Long Short-Term Memory (LSTM) network to perform sentiment analysis on the IMDB Movie Reviews dataset. The objective is to classify each movie review as either positive or negative by learning patterns from sequential text data.

## Model Performance

The model was trained using the Adam optimizer and Binary Crossentropy loss function for five epochs. During training, both the training and validation accuracy increased steadily, while the loss decreased, indicating effective learning.

## Evaluation Metrics

The model was evaluated using:

- Test Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-Score

The confusion matrix provides a visual summary of correct and incorrect predictions, while the classification report presents precision, recall, and F1-score for each class.

## Training Analysis

The training accuracy improved with each epoch, and the validation accuracy followed a similar trend, indicating good generalization. The loss curves showed a gradual decrease without significant overfitting.

## LSTM vs Standard RNN

| Standard RNN                      | LSTM                                           |
| --------------------------------- | ---------------------------------------------- |
| Struggles with long sequences     | Handles long sequences effectively             |
| Suffers from vanishing gradients  | Reduces the vanishing gradient problem         |
| Limited memory of previous inputs | Maintains long-term memory through gated cells |
| Lower performance on text data    | Higher performance on sentiment analysis tasks |

## Conclusion

The LSTM model successfully classified movie reviews by learning contextual relationships between words. Compared with a standard RNN, the LSTM architecture demonstrated better memory retention, improved learning capability, and higher overall performance for sequential text classification tasks.
