from flask import render_template, flash, redirect, url_for, request
from loan import app
from loan.forms import *
from loan.models import *


@app.route('/')
def home():
    loans = Loan.query.all()
    return render_template('home.html', loans=loans)


@app.route('/loan', methods=['GET', 'POST'])
def loan():
    form = LoanForm()
    if form.validate_on_submit():
        try:
            total_loan = round(form.loan_amount.data * form.interest_rate.data / 100 * form.period.data)
            compiled = Loan(loan_amount=form.loan_amount.data, interest_rate=form.interest_rate.data,
                            period=form.period.data, total_loan=total_loan, id_number=form.id_number.data,
                            name=form.name.data, location=form.location.data)
            db.session.add(compiled)
            db.session.commit()
            flash('successful', 'success')
            return redirect(url_for('home'))
        except ValueError:
            return redirect(url_for('loan'))
    return render_template('loan.html', form=form, legend='New Loan')


@app.route('/loan_detail/<int:loan_id>')
def loan_detail(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    image_file = url_for('static', filename='img/' + loan.image_file)
    return render_template('loan_detail.html', title=loan.name, loan=loan, image_file=image_file)


@app.route('/loan_detail/<int:loan_id>/update', methods=['GET', 'POST'])
def update(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    form = LoanForm()
    if form.validate_on_submit():
        try:
            total_loan = round(form.loan_amount.data * form.interest_rate.data / 100 * form.period.data)
            new_compile = Loan(loan_amount=form.loan_amount.data, interest_rate=form.interest_rate.data,
                               period=form.period.data, total_loan=total_loan, name=form.name.data,
                               id_number=loan.id_number, location=form.location.data)
            db.session.add(new_compile)
            db.session.commit()
            return redirect(url_for('home'))
        except ValueError:
            return redirect(url_for('loan'))
    else:
        form.name.data = loan.name
        form.id_number.data = loan.id_number
        form.location.data = loan.location
        form.loan_amount.data = loan.loan_amount
        form.period.data = loan.period
        form.interest_rate.data = loan.interest_rate
    return render_template('loan.html', title='Update', loan=loan
                           , legend='Update Loan', form=form)
