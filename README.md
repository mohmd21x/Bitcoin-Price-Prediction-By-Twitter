# Bitcoin Price prediction with Bitcoin Twitter's Sentiment
## 1. Predict Price without Twitter's
in this section we tried to predict Bitcoin price with Long-Short-Term-Memory models.
and the end of code we try to show predicted price with real by plotting.
![btc-lstm](https://github.com/mohmd21x/Bitcoin-Price-Prediction/assets/81675003/5c93e542-5685-4f0b-98d5-0647c67d3e81)
## Sentiment Twitter's Data
in this section with using NLP model we predict sentiment of each twitte and groupe them by date of them.
and we try to consider both of positive and negetive sentiments and use average of sentiment in every day twitte's.
![price-with-sentiment](https://github.com/mohmd21x/Bitcoin-Price-Prediction-By-Twitter/assets/81675003/d0de4b04-7231-46a8-afb9-f2e21761a33f)
in this plot we show price across the sum of sentiment in each day.(negetive numbers means more negetive sentiment)
## Predict price with sentiment's
in this part we compine both data's(price data and sentiment data) after it we implanted LSTM model on it.
the results of model was not better than first model because Twitter data was not available for all days.
but we figure out a process: we the price is in a directionless market sentiment of twitters plays an important role in the future of the market.
![price](https://github.com/mohmd21x/Bitcoin-Price-Prediction-By-Twitter/assets/81675003/4a2872ff-4641-4531-910d-a4ccce391ac1)


