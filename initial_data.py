from main import app
from application.sec import datastore
from application.models import db, Role, Service, User
from flask_security import hash_password
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()
    datastore.find_or_create_role(name="admin",description="This  is an admin")
    datastore.find_or_create_role(name="service_professional",description="This  is a service professional")
    datastore.find_or_create_role(name="customer",description="This  is a customer")
    db.session.commit()
    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(email="admin@email.com",password=generate_password_hash("admin"),roles=["admin"])
    if not datastore.find_user(email="service_professional@email.com"):
        datastore.create_user(email="service_professional@email.com",password=generate_password_hash("service_professional"),roles=["service_professional"], active=False)
    if not datastore.find_user(email="customer1@email.com"):
        datastore.create_user(email="customer1@email.com",password=generate_password_hash("customer1"),roles=["customer"])
    
    db.session.commit()
