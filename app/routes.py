from app import app
from flask import render_template, flash, send_file
from app.forms import NDAForm
from flask_mail import Message
from app import mail
from app.doc import create_nda

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',title = "Home")

@app.route('/nda', methods = ['GET','POST'])
def nda():
	form = NDAForm()
	if form.validate_on_submit():
		flash ('NDA template created for {}'.format(form.partyname.data))
		create_nda(form.partyname.data, "test1")
		
	return render_template('NDA.html',title="NDA", form=form)

@app.route('/menu')
def menu():
	return render_template('menu.html')

@app.route('/download')
def download():
	path = 'C:\\Users\\james\\OneDrive\\Desktop\\Coding\\LegalDocGenerator\\LegalDocGenerator\\test1.docx'
	return send_file(path,as_attachment=True)
