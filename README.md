## Twitter_Sentiment
In this project by using the NLP, sentiment analysis has been done on tweet.

For this a model has been built and rather than training the model again and again
**pickle** has been used to save the model. Later for training this **.pickle** model hase been
reopened. This code is in the **analysis.py** file.

Next in the **sentiment_mod.py** a custom **Voting class** has been created. This class takes different Classifier into account
and based on their prediction this class returned a modified **confidence level**.

And then in **sentiment.py** live twitter data has been used to analysis the sentiment on those models.

Here are two screenshots about **MESSI** and **RONALDO** based on twitter data.

## Ronaldo
![figure_1-1](https://user-images.githubusercontent.com/19304394/42262895-6a8da772-7f8e-11e8-8c06-76f63255f791.png)

## Messi
![figure_1-2](https://user-images.githubusercontent.com/19304394/42262910-72c450bc-7f8e-11e8-8842-d7e8aa010c65.png)
