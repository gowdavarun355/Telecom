import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__,template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        International_Plan = int(request.form['International_Plan'])
        Day_Mins = int(request.form['Day_Mins'])
        Day_Charge = int(request.form['Day_Charge'])
        CustServ_Calls= int(request.form['CustServ_Calls'])
   
        data =[np.array([International_Plan, Day_Mins, Day_Charge, CustServ_Calls])]
        my_prediction = model.predict(data)
        output = round(my_prediction[0], 2)
        
    if output>float(0.5):
        return render_template('index.html',prediction_text=' Customer will Churn {} '.format(output))
    else:
        return render_template('index.html',prediction_text=' Customer will not Churn {} '.format(output))



if __name__ == "__main__":
        app.run(debug=True)