from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField,StringField,IntegerField,SelectField
from wtforms.validators import  DataRequired

class PredictForm(FlaskForm):
    Customer_Age=IntegerField(label='Customer Age', validators=[DataRequired()])
    Gender =SelectField (choices=[('M', 'Male'), ('F', 'Female')],label='Gender', validators=[DataRequired()])
    Dependent_count=IntegerField(label='Dependent Count', validators=[DataRequired()])
    Education_Level=SelectField (choices=[('Uneducated', 'Uneducated'), ('High School', 'High School'), ('College', 'College'), ('Graduate', 'Graduate'), ('Post-Graduate', 'Post-Graduate'), ('Doctorate', 'Doctorate')],label='Education Level', validators=[DataRequired()])
    Marital_Status=SelectField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')],label='Marital Status', validators=[DataRequired()])
    Income_Category=SelectField(choices=[('Less than $40K', 'Less than $40K'), ('$40K - $60K', '$40K - $60K'), ('$60K - $80K', '$60K - $80K'), ('$80K - $120K', '$80K - $120K'), ('$120K +', '$120K +')],label='Income Category', validators=[DataRequired()])
    Card_Category=SelectField(choices=[('Blue', 'Blue'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')],label='Card Category', validators=[DataRequired()])
    Total_Relationship_Count=IntegerField(label='Total Relationship Count', validators=[DataRequired()])
    Months_Inactive_12_mon=IntegerField(label='Months Inactive', validators=[DataRequired()])
    Credit_Limit=FloatField(label='Credit Limit', validators=[DataRequired()])
    Total_Revolving_Bal=FloatField(label='Total Revolving Balance', validators=[DataRequired()])
    Prediction_of_months=StringField()
    submit= SubmitField(label='Predict')
