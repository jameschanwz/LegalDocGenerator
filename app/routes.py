from app import app
from flask import render_template, flash
from app.forms import NDAForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',title = "Home")

@app.route('/nda', methods = ['GET','POST'])
def nda():
	form = NDAForm()
	if form.validate_on_submit():
		flash ('NDA template created for {}'.format(form.partyname.data))
	return render_template('NDA.html',title="NDA", form=form)