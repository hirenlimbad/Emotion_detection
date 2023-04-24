# Mood Detection from Tweets

This project aims to detect the mood or sentiment of a tweet using natural language processing techniques. The model used in this project has an accuracy score of 88% and was built as a beginner level project.

## Dataset

The dataset used in this project is the emotion_dataset_twitter dataset, which consists of 2000 tweets labeled as 0,1,2,3,4.

## Dependencies

The following Python libraries are required to run this project:

- pandas
- numpy
- scikit-learn
- nltk

## Running the Code

To run the code, first clone the repository:


Then, install the required dependencies:


Finally, run the `server.py` file:


This will run the model on the dataset and output the accuracy score.

## Model

The model used in this project is a simple Naive Bayes classifier. We used the NLTK library to preprocess the text data and extract features from the tweets. The features used in this model include word frequencies and presence of certain words and emoticons commonly associated with positive or negative sentiment.

## Conclusion

This project demonstrates how natural language processing techniques can be used to detect the sentiment of text data such as tweets. The accuracy score of the model is 88%, which is a good starting point for a beginner level project.
