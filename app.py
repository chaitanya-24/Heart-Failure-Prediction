from flask import Flask, render_template, request
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

import warnings
warnings.filterwarnings('ignore')



application = Flask(__name__)

app = application

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict_data():
    if request.method=="GET":
        return render_template('index(1).html')


    else:
        data = CustomData(
            Age = request.form.get('age'),
            Sex = request.form.get('sex'),
            ChestPainType = request.form.get('chestpaintype'),
            RestingBP = request.form.get('resting_bp'),
            Cholesterol = request.form.get('cholesterol'),
            FastingBS = request.form.get('fasting_bs'),
            RestingECG = request.form.get('resting_ecg'),
            MaxHR = request.form.get('max_hr'),
            ExerciseAngina = request.form.get('exercise_angina'),
            Oldpeak = request.form.get('oldpeak'),
            ST_Slope = request.form.get('st_slope'),
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        
        result = predict_pipeline.predict(pred_df)
        results = int(result[0])
        print("After Prediction")

        if results == 1:
            predicted_text = "Heart Disease Predicted"
        else:
            predicted_text = "Heart Disease Not Predicted"

        print(predicted_text)

        return render_template('index(1).html', predicted_text=predicted_text)


if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True, port=5000)
    app.run(host="0.0.0.0",port=5000)