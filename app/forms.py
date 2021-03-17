from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NDAForm(FlaskForm):
	partyname = StringField('Partyname')
	submit = SubmitField('Submit')