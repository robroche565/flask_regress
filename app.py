from flask import Flask
from flask import render_template
import pickle
from forms import PredictForm
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY']='bscs3a2021'
test_model = pickle.load(open('CreditRegressionModel.pkl','rb'))

if __name__=="__main__":
    # app.run(debug=True, host="0.0.0.0") #to test on LAN
    app.run(debug=True)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/',methods=["GET","POST"])
def predict():
    form=PredictForm()
    newdata=dict()
    prediction=0
    if form.validate_on_submit():
        newdata['Customer_Age']=form.Customer_Age.data
        newdata['Gender']=form.Gender.data
        newdata['Dependent_count']=form.Dependent_count.data
        newdata['Education_Level']=form.Education_Level.data
        newdata['Marital_Status']=form.Marital_Status.data
        newdata['Income_Category']=form.Income_Category.data
        newdata['Card_Category']=form.Card_Category.data
        newdata['Total_Relationship_Count']=form.Total_Relationship_Count.data
        newdata['Months_Inactive_12_mon']=form.Months_Inactive_12_mon.data
        newdata['Credit_Limit']=form.Credit_Limit.data
        newdata['Total_Revolving_Bal']=form.Total_Revolving_Bal.data
        df=pd.DataFrame([newdata.values()],columns=list(newdata.keys()))
        prediction = test_model.predict(df)
        print('\n\nPrediction: ',prediction,'\n\n')
    return render_template('predict.html',form=form,pred=int(prediction))

