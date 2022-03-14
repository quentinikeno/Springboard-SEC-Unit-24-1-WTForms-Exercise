from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import PetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def show_homepage():
    """Show homepage."""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def show_new_pet_form():
    """Show form to add a pet.  Create the pet in db when POST request."""
    form = PetForm()
    
    if form.validate_on_submit():
        #Form data without csrf token
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        #Unpack data into Pet instance
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        
        flash("Successfully created a new pet!", "success")
        return redirect("/")
    else:
        if form.errors:
            flash("Something went wrong.  Please see the problems below.", "danger") 
        return render_template("add_pet_form.html", form=form)
    
@app.route("/<int:pet_id_number>", methods=["GET", "POST"])
def show_pet_detail(pet_id_number):
    """Show pet detail and form to edit pet.  Update pet in db when POST request."""
    pet = Pet.query.get_or_404(pet_id_number)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        
        flash(f"Successfully updated {pet.name}!", "success")
        return redirect("/")
    else:
        if form.errors:
            flash("Something went wrong.  Please see the problems below.", "danger") 
        return render_template("pet_detail.html", pet=pet, form=form)