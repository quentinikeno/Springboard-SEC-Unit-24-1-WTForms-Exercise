from app import db
from models import Pet

db.drop_all()
db.create_all()

woofly_url = 'https://images.unsplash.com/photo-1517849845537-4d257902454a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80'
woofly = Pet(name="Woofly", species = 'Dog', photo_url = woofly_url, age = 3, notes = 'Cool dog.', available = True)

pokey_url = 'https://images.unsplash.com/photo-1605369179590-014a88d4560a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8cG9yY3VwaW5lfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60'
pokey = Pet(name="Pokey", species = 'Hedgehog', photo_url = pokey_url, age = 1, notes = 'Cool hedghog.', available = True)

carl_url = 'https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fGNhdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60'
carl = Pet(name="Carl", species = 'Cat', photo_url = carl_url, age = 2, notes = 'Cool cat.', available = True)

db.session.add_all([woofly, pokey, carl])
db.session.commit()