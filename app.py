from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# -----------------------------------------
# Initialize Flask app
# -----------------------------------------
app = Flask(__name__)

# Database configuration (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# -----------------------------------------
# Database Model
# -----------------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


# -----------------------------------------
# Marshmallow Schema (✅ FIXED)
# -----------------------------------------
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True  # optional, allows direct model loading

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# -----------------------------------------
# Routes
# -----------------------------------------

@app.route("/")
def home():
    return "✅ Flask User CRUD API is running successfully!"

# ✅ Create User
@app.route("/user", methods=["POST"])
def add_user():
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]

    new_user = User(name, email, password)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# ✅ Get All Users
@app.route("/users", methods=["GET"])
def get_users():
    all_users = User.query.all()
    return jsonify(users_schema.dump(all_users))

# ✅ Get Single User by ID
@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)

# ✅ Update User
@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    user.name = request.json.get("name", user.name)
    user.email = request.json.get("email", user.email)
    user.password = request.json.get("password", user.password)

    db.session.commit()
    return user_schema.jsonify(user)

# ✅ Delete User
@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully!"})


# -----------------------------------------
# Run App
# -----------------------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
