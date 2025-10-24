from app import db

# Create all tables in the database
db.create_all()

print("✅ Database created successfully!")
