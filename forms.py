from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional

class PetForm(FlaskForm):
    """Form for adding/editing pets for adoption."""
    
    name = StringField("Name", validators=[InputRequired(message="Pet name can't be blank.")])
    species = StringField("Species", validators=[InputRequired(message="Species name can't be blank.")])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = StringField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])