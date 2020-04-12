from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, Email
from loan.models import *


class LoanForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=5, max=30)])
    id_number = StringField('Id_Number', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(min=3, max=20)])
    loan_amount = IntegerField('Loan Amount', validators=[DataRequired()])
    period = IntegerField('Period', validators=[DataRequired()])
    interest_rate = IntegerField('Interest Rate ', validators=[DataRequired()])
    submit = SubmitField('Save')

    def validate_id_number(self, id_number):
        loan = Loan.query.filter_by(id_number=id_number.data).first()
        if loan:
            raise ValidationError('The Id Number is taken')
