from application import db
from application.models import Fortunes

db.drop_all()
db.create_all()
