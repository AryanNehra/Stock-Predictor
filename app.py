from flask import Flask, render_template, request
import xgboost as xbg
from xgboost import XGBRegressor
import numpy as np
from sklearn.preprocessing import MinMaxScaler

model=xbg.XGBRegressor()
model.load_model('stock_predictor.model')

app=Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')

scale=MinMaxScaler(feature_range=(0,1))

def preprocess_data(data):
    data=np.array(data).reshape(-1,1)
    scaled_data=scale.fit_transform(data)
    return scaled_data

def postprocess_data(pred):
    pred=np.array(pred).reshape(-1,1)
    pred=scale.inverse_transform(pred)
    return pred

@app.route('/predict', methods=['POST'])
def home():
    data1=request.form['open']
    data2=request.form['high']
    data3=request.form['low']
    data=[data1,data2,data3]
    scaled_data=preprocess_data(data).reshape(1,-1)
    pred=model.predict(scaled_data)
    final_pred=postprocess_data(pred)
    return render_template('result.html',data=final_pred[0][0])

# if __name__=="__main__":
#     app.run(debug=True)