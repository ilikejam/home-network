from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class DisplayForm(FlaskForm):
    message = StringField("Message", [Length(min=1, max=25)])
    submit = SubmitField("Display")
