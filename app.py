from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import PetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def homepage():
    """Show homepage."""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def new_pet_form():
    
    form = PetForm()
    
    if form.validate_on_submit():
        #Form data without csrf token
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        #Unpack data into Pet instance
        new_pet = Pet(**data)
        flask(f"Create new pet named {new_pet.name}!", "success")
        return redirect("/")
    else:
        if form.errors:
            flash("Something went wrong.  Please see the problems below.", "danger") 
        return render_template("add_pet_form.html", form=form)