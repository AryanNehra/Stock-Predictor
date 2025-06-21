# 📈 Google Stock Price Predictor

A web-based application to predict the closing stock price of Google using machine learning models. Designed to demonstrate regression techniques on time series stock data.

🔗 Live Demo: [stock-predictor-nhbl.onrender.com](https://stock-predictor-nhbl.onrender.com/)

## 🧰 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Flask
- **Machine Learning Model:** XGBRegressor (best performing)
- **Deployment:** Render

## 🔍 Features

- Enter stock data and get predicted closing prices.
- Visual insights into historical data and model predictions.
- Clean and intuitive UI.

## 📁 Project Structure

```
stock-price-predictor/
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── stock_predictor.model
├── app.py
└── README.md
```

## 🧠 Model Details

- Dataset: Google stock price historical data
- Algorithms Tried: Linear Regression, Random Forest, XGBRegressor
- Best Result: XGBRegressor

## 💻 Local Setup

```bash
git clone https://github.com/AryanNehra/stock-price-predictor.git
cd stock-price-predictor
pip install -r requirements.txt
python app.py
```

## 🧑‍💻 Author

Aryan Nehra  
📧 f20220918@hyderabad.bits-pilani.ac.in  
🌐 [GitHub](https://github.com/AryanNehra)
