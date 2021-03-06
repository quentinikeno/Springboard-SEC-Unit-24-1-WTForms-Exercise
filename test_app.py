from unittest import TestCase

from app import app
from models import db, Pet

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_test_db'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# Don't req CSRF for testing
app.config['WTF_CSRF_ENABLED'] = False

db.drop_all()
db.create_all()


class PetViewsTestCase(TestCase):
    """Tests for views for Pet."""
    
    def setUp(self):
        """Add a test pet."""
        
        Pet.query.delete()
        
        #Add test pet to db
        pet_url = 'https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fGNhdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60'
        pet = Pet(name="Test Cat", species = 'Cat', photo_url = pet_url, age = 1, notes = 'Test cat.', available = True)
        db.session.add(pet)
        db.session.commit()
        
        self.pet = pet
    
    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()
    
    def test_route_route(self):
        """Testing the route route listing all pets."""
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="text-center display-1">Pets</h1>', html)
            self.assertIn(f"{self.pet.name}", html)

    def test_pet_add_form(self):
        """Testing the form to add pets."""
        with app.test_client() as client:
            resp = client.get("/add")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form id="pet-form" method="POST">', html)

    def test_pet_add(self):
        """Testing the adding of new pet to db."""
        with app.test_client() as client:
            d = {"name": "Test Pet 2", "species": "dog"}
            resp = client.post("/add", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="text-center display-1">Pets</h1>', html)
            self.assertIn("Test Pet 2", html)
            
    def test_pet_detail(self):
        """Test pet detail page with form to edit pet."""
        with app.test_client() as client:
            resp = client.get(f"/{self.pet.id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f"What You Should Know About {self.pet.name}", html)
            
    def test_pet_update(self):
        """Testing of updating pet in db."""
        with app.test_client() as client:
            d = {"age": 2, "available": False}
            resp = client.post(f"/{self.pet.id}", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'Successfully updated {self.pet.name}!', html)