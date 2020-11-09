import joblib
import requests
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/hasil',methods=['POST'])
def hasil():
    if request.method == 'POST':
        input = request.form
        sl = (input['sl'])
        sw = (input['Kelamin'])
        pl = (input['CP'])
        pw = (input['pw'])
        ch = (input['chol'])
        fbs = input(['fbs'])
        rest = input['rest']

        pred = model.predict([[sl,sw,pl,pw,ch,fbs,rest]])[0]
        
    return render_template('hasil.html',data = input,prediksi = pred)



if __name__ =='__main__':
    model = joblib.load("ModelHeartDisease")
    app.run(debug=True)