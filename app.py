from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('ada_classfier_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Education_Type=request.form['Education_Type']
        #Education_Type.astype(float)
        if(Education_Type =='Graduate'):
            Education_Type=1
            #Education_Type_Under_Graduate=0
        else:
            Education_Type=0
            #Education_Type_Under_Graduate=1
            
        Married_Type=request.form['Married_Type']
        if(Married_Type =='Yes'):
            Married_Type=1
        else:
           Married_Type=0
        
        Gender_Type=request.form['Gender_Type']
        if(Gender_Type =='Male'):
            Gender_Type=1
        else:
           Gender_Type=0
           
        Self_Employed_Type=request.form['Self_Employed_Type']
        if(Self_Employed_Type =='Yes'):
            Self_Employed_Type=1
        else:
           Self_Employed_Type=0
         
        dependents=int(request.form['dependents'])
        
        
        applicantincome = int(request.form['applicantincome'])
        coapplicantincome = int(request.form['coapplicantincome'])
        loanamount=int(request.form['loanamount'])  
        loanamountterm=int(request.form['loanamountterm'])  
        credithist=int(request.form['credithist'])
        
        propertyarea=request.form['property']
        if(propertyarea =='Urban'):
            propertyarea=2
        elif(propertyarea=='Rural'):
            propertyarea=0
        else:
            propertyarea=1
        
    
        prediction=model.predict([[Gender_Type,Married_Type,dependents,Education_Type,Self_Employed_Type,applicantincome,coapplicantincome,loanamount,loanamountterm,credithist,propertyarea]])
        output=round(prediction[0],2)
        if output<1:
            return render_template('index.html',prediction_text="Sorry you can't accept the loan")
        else:
            return render_template('index.html',prediction_text="You Can Santion the Loan {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
