from app import app
from flask import render_template, flash
from app.forms import NDAForm
from flask_mail import Message
from app import mail

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',title = "Home")

@app.route('/nda', methods = ['GET','POST'])
def nda():
	form = NDAForm()
	if form.validate_on_submit():
		flash ('NDA template created for {}'.format(form.partyname.data))
		send_email('Automatic NDA', sender=app.config['ADMINS'][0], recipients = 'ilithrais@gmail.com', text_body='Test', html_body='test')

return render_template('NDA.html',title="NDA", form=form)