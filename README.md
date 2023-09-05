
![Stock_prediction__06](https://github.com/P4RASTOO/Sample/assets/132952512/ed9a645c-1916-4978-9c65-59724c3d9283)

# Project_2 Report
## Overview of the Analysis
The purpose of the analysis was to build a machine learning model to have comprehensive approach to forecasting stock prices, taking into account historical stock data and external economic indicators to improve prediction accuracy. The analysis assesses model performance using various evaluation metrics, ensuring that the model's predictions are reliable and useful for investment decision-making.
We aimed at forecasting market prices for three stock sectors: Energy (IYE), Financials (IYF), and Technology (IYW) over the upcoming 60 days. Let's break down the key aspects of the analysis:
1. **Financial Information and Prediction Target:**
   - The data used for analysis includes historical daily stock price information, including Open, High, Low, Close prices, and trading volume (i.e., financial market data).
   - The main variable being predicted is the "Close" price of each stock sector for the next 60 days.
2. **Variables to Predict:**
   - The key variable to predict is the "Close" price of each stock sector (Energy, Financials, and Technology) for the next 60 days.
3. **Stages of the Machine Learning Process:**
   - **Data Collection:** Historical daily stock price data is collected from the Alpha Vantage API, including Open, High, Low, Close prices, and trading volume. Additionally, data for financial indicators like MACD(Moving Average Convergence Divergence), Federal Funds Rate, Unemployment Rate, EMA 20, and CPI was obtained.
   - **Feature Engineering:** Several financial and economic indicators are collected, including the Federal Funds Rate, Unemployment Rate, EMA (Exponential Moving Average), and CPI (Consumer Price Index). These indicators are merged with stock price data.
   - **Data Preprocessing:** Data was cleaned, merged, and preprocessed. Features like Open, High, Low, Volume, MACD, Federal Funds Rate, and Unemployment Rate were selected for training the model. The data was normalized using Min-Max scaling. Other precoccing steps includs: sequence creation, and splitting into training, validation, and testing sets.
   - **Sequence Data Preparation:** The data was organized into sequences of a fixed length (e.g., 100 days) for training. These sequences were used to predict the stock prices for the next 60 days.
   - **Model Building:** A Sequential LSTM model was designed with 150 hidden neurons. It was followed by a Dense layer with 60 neurons to predict the next 60 days' stock prices.
   - **Model Compilation:** The model was compiled using the Adam optimizer and mean squared error (MSE) loss function. Additionally, a custom metric for root mean squared error (RMSE) was used for monitoring.
   - **Model Training:** The model is trained using historical data, including the created sequences and targets. An early stopping callback was used to prevent overfitting.
   - **Validation:** A validation set was used to monitor the model's performance during training.
   - **Model Evaluation:** Root Mean Square Error (RMSE), Mean Absolute Percentage Error (MAPE), and Pearson Correlation Coefficient (R) are used to evaluate the model's performance.
   - **Prediction on New Data:** The model is used to make predictions on new data, and future dates are generated for the forecasted prices.
4. **Methods Used:**
   - Data retrieval from the Alpha Vantage API.
   - Feature engineering to combine stock price data with additional financial and economic indicators.
   - Data preprocessing, including normalization, sequence creation, and train-validation-test splitting.
   - LSTM neural network for time series forecasting.
   - Evaluation of the model's performance using RMSE, MAPE, and Pearson Correlation Coefficient.
   - Saving and loading the trained model.
   - Making predictions on new data.

## Results:

- **RMSE Evaluation:** RMSE was calculated to measure the model's prediction accuracy. The RMSE for the model was found to be approximately 1.6624.

- **MAPE Evaluation:** The Mean Absolute Percentage Error (MAPE) was calculated to assess prediction accuracy. The average MAPE for all windows was approximately 11.3114.

- **Pearson Correlation:** The Pearson Correlation Coefficient (R) was used to evaluate the linear relationship between predicted and actual prices. The average R value was approximately 0.8839.

- **Visualization:** The model's predictions were visualized for different time horizons (e.g., first day, last day, 10th day, and 30th day) to assess its performance.

- **Future Predictions:** The model was used to generate future stock price predictions for the next 60 days.

## Conclusion
Federal Reserve's monetary policy plays a crucial role in managing economic stability, and it can have a significant impact on inflation and economic growth. The intricate relationship between monetary policy, economic news, and stock market trends in inflationary periods on Technology and Financial Stock Sector are as follows:

**Impact of Federal Reserve Money Tightening on Stock Market:**
- Rising interest rates and borrowing costs increase expenses for businesses, potentially reducing corporate profits.
- Anticipation of reduced profitability can lead to a decline in stock prices.
- Reduction in bond purchases by the central bank reduces liquidity in financial markets, making it harder for investors to find lucrative opportunities.

**Stockholder Response to Tightening Monetary Policy:**
- The prospect of declining stock values can prompt stockholders to sell their stocks to secure existing gains.
- This collective desire to sell adds to the downward pressure on stock prices.

**Role of Economic News and Events in Inflationary Markets:**
- Bad economic news, signaling economic challenges or slowdown, can be viewed as good news for the stock market.
- Such news can lead investors to expect a more accommodative monetary policy from the Federal Reserve, encouraging increased investments in stocks.
- Economic calendars categorize news and events based on their market impact, with three-star market news denoting high-impact events.
- Investors closely monitor these calendars for insights into market-moving events.
- Anything aligning with the Federal Reserve's goals and fostering economic optimism can drive buying activity in the stock market during times of inflation.

Energy stocks are uniquely positioned in the market, with their performance deeply intertwined with the fluctuations in oil, gas, and petroleum markets. Unlike their counterparts in the technology and financial sectors, energy stocks are highly sensitive to the dynamics of these resources. 

**Characteristics of Energy Stocks:**
- Depend heavily on the performance of oil, gas, and petroleum markets.
- Exhibit a distinct sensitivity to fluctuations in these resource markets.

**Impact of Crude Oil Inventory Levels:**
- High crude oil inventory levels often suggest weak previous oil sales.
- This can result in a decline in oil prices.
- Energy stocks typically follow suit, experiencing price drops.

**OPEC Decisions and Energy Stocks:**
- OPEC's decision to lower oil production rates can boost oil prices.
- Higher oil prices are favorable for energy companies.
- Such developments tend to increase stock prices within the energy sector.

**Dominance of Political Events on Oil Prices:**
- Political events and news concerning oil prices wield significant influence.
- They can override the impacts of inventory levels and OPEC decisions.
- Political factors signaling economic recession can lead to oil price decrements, affecting energy stocks negatively.

These dynamics highlight the intricate relationship between energy stocks, oil markets, and political developments, emphasizing the importance of monitoring both economic and political factors for investors in this sector.
