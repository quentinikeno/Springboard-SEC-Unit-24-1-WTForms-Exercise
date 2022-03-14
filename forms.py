from unicodedata import name
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class PetForm(FlaskForm):
    """Form for adding pets for adoption."""
    
    name = StringField("Name", validators=[InputRequired(message="Pet name can't be blank.")])
    
    choices = [('Cat', 'Cat'), ('Dog', 'Dog'), ('Hedgehog', 'Hedgehog')]
    species = SelectField("Species", choices=choices)
    
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])
    
class EditPetForm(FlaskForm):
    """Form for editing pets on detail page."""
    
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    available = BooleanField("Available for Adoption")