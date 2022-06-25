import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
model = pickle.load(open('linear_regression_model.pkl', 'rb'))
scaling = pickle.load(open('std_scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

#standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = request.form['sex']
        if(sex == 'Male'):
            sex = 1
        else:
            sex = 0
        cp = request.form['cp']
        if(cp == 'Atypical angina'):
            cp_1 = 1
            cp_2 = 0
            cp_3 = 0
        elif(cp == 'Not angina'):
            cp_1 = 0
            cp_2 = 1
            cp_3 = 0
        elif(cp == 'Asymptomatic'):
            cp_1 = 0
            cp_2 = 0
            cp_3 = 1
        else:
            cp_1 = 0
            cp_2 = 0
            cp_3 = 0
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = request.form['fbs']
        if(fbs=='True'):
            fbs=1
        else:
            fbs=0
        restecg = request.form['restecg']
        if(restecg == 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)'):
            restecg_1 = 1
            restecg_2 = 0
        elif(restecg == 'Normal'):
            restecg_1 = 0
            restecg_2 = 0
        else:
            restecg_1 = 0
            restecg_2 = 1
        thalach = int(request.form['thalach'])
        exang = request.form['exang']
        if(exang=='Yes'):
            exang = 1
        else:
            exang = 0
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        if(slope == 'Flat'):
            slope_1 = 1
            slope_2 = 0
        elif(slope == 'Downsloping'):
            slope_1 = 0
            slope_2 = 1
        else:
            slope_1 = 0
            slope_2 = 0
        ca = request.form['ca']
        if(ca=='1'):
            ca_1 = 1
            ca_2 = 0
            ca_3 = 0
            ca_4 = 0
        elif(ca=='2'):
            ca_1 = 0
            ca_2 = 1
            ca_3 = 0
            ca_4 = 0
        elif(ca=='3'):
            ca_1 = 0
            ca_2 = 0
            ca_3 = 1
            ca_4 = 0
        elif(ca=='4'):
            ca_1 = 0
            ca_2 = 0
            ca_3 = 0
            ca_4 = 1
        else:
            ca_1 = 0
            ca_2 = 0
            ca_3 = 0
            ca_4 = 0
        thal = request.form['thal']
        if(thal=='1'):
            thal_1=1
            thal_2=0
            thal_3=0
        elif(thal=='2'):
            thal_1=0
            thal_2=1
            thal_3=0
        elif(thal=='3'):
            thal_1=0
            thal_2=0
            thal_3=1
        else:
            thal_1=0
            thal_2=0
            thal_3=0
        #Kms_Driven2=np.log(Kms_Driven)
        #Owner=int(request.form['Owner'])
        #Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        #if(Fuel_Type_Petrol=='Petrol'):
        #        Fuel_Type_Petrol=1
        #        Fuel_Type_Diesel=0
        #elif(Fuel_Type_Petrol=='Diesel'):
        #    Fuel_Type_Petrol=0
        #    Fuel_Type_Diesel=1
        #else:
        #    Fuel_Type_Petrol=0
        #    Fuel_Type_Diesel=0
        #Year=2022-Year
        #Seller_Type_Individual=request.form['Seller_Type_Individual']
        #if(Seller_Type_Individual=='Individual'):
        #    Seller_Type_Individual=1
        #else:
        #    Seller_Type_Individual=0	
        #Transmission_Mannual=request.form['Transmission_Mannual']
        #if(Transmission_Mannual=='Mannual'):
        #    Transmission_Mannual=1
        #else:
        #    Transmission_Mannual=0
        X = [[age, sex, trestbps, chol, fbs, thalach, exang, oldpeak, cp_1, cp_2, cp_3, restecg_1, restecg_2, slope_1, slope_2, ca_1, ca_2, ca_3, ca_4, thal_1, thal_2, thal_3]]
        X_scaled = scaling.transform(X)
        #prediction = model.predict([[age, sex, trestbps, chol, fbs, thalach, exang, oldpeak, cp_1, cp_2, cp_3, restecg_1, restecg_2, slope_1, slope_2, ca_1, ca_2, ca_3, ca_4, thal_1, thal_2, thal_3]])
        prediction = model.predict(X_scaled)
        
        #output = prediction
        #if (output == 0):
        #    return render_template('result.html',prediction="Less chance of Heart Attack")
        #else:
        #    return render_template('result.html',prediction="High chance of Heart Attack")
        if prediction == 1:
            prediction ="High chance of Heart Disease"
        else:
            prediction ="Less chance of Heart Disease"           
        return render_template("result.html", prediction1 = prediction)
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)