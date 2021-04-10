import numpy as np
import pandas as pd
import keras
from flask import Flask,render_template,request
from keras.models import model_from_json
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method =='POST':
        print(request.form.get('age'))
        print(request.form.get('sex'))
        print(request.form.get('trtbps'))
        print(request.form.get('thalachh'))
        print(request.form.get('exng'))
        print(request.form.get('oldpeak'))
        print(request.form.get('slp'))
        print(request.form.get('caa'))
        print(request.form.get('thall'))
        print(request.form.get('typical_angina'))
        print(request.form.get('atypical_angina'))
        print(request.form.get('non_anginal_pain'))
        print(request.form.get('asymptomatic'))
        print(request.form.get('normal'))
        print(request.form.get('having_abnormality'))
    try:    
        age=int(request.form['age'])
        sex=int(request.form['sex'])
        trtbps=int(request.form['trtbps'])
        thalachh=int(request.form['thalachh'])
        exng=int(request.form['exng'])
        oldpeak=float(request.form['oldpeak'])
        slp=int(request.form['slp'])
        caa=int(request.form['caa'])
        thall=int(request.form['thall'])
        typical_angina=int(request.form['typical_angina'])
        atypical_angina=int(request.form['atypical_angina'])
        non_anginal_pain=int(request.form['non_anginal_pain'])
        asymptomatic=int(request.form['asymptomatic'])
        normal=int(request.form['normal'])
        having_abnormality=int(request.form['having_abnormality'])
        pred_args=[age,sex,trtbps,thalachh,exng,oldpeak,slp,caa,thall,
                   typical_angina,non_anginal_pain,asymptomatic,normal,having_abnormality]
        pred_arr=np.array(pred_args)
        preds=pred_arr.reshape(1,-1)
        json_file = open('model.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        keras_model = model_from_json(loaded_model_json)
        keras_model.load_weights("model.h5")
        pred =keras_model.predict_classes(preds)
        if pred==0:
            model_prediction="less chance of heart attack"
        else:
            model_prediction="more chance of heart attack"
    except ValueError:
        return "Please Enter valid values"
    return render_template('predict.html',prediction=model_prediction)

if __name__=='__main__':
    app.run(debug=True)

