import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from flask_migrate import Migrate
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key-change-in-prod")

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Model definition using UUID
class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(
        db.String(120), nullable=False
    )  # Plaintext for demo; use hashing for prod


# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


# Routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session["user_id"] = str(user.id)  # Store UUID as string in session
            session["username"] = user.username
            flash("Login Successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid credentials.", "danger")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register() -> str:
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists.", "danger")
            return redirect(url_for("register"))

        # Create new user (ID is auto-generated as UUID)
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/profile/<uuid:user_id>")
@login_required
def profile(user_id):
    # In a real app, you'd do: user = User.query.get_or_404(user_id)
    # For this demo, we'll simulate a user object
    user_data = {
        "id": user_id,
        "username": session.get("username", "DevUser_01"),
        "email": "dev@example.com",
        "joined": "April 2026",
    }
    return render_template("profile.html", user=user_data)


@app.route("/logout")
def logout():
    # Clear the session
    session.clear()
    flash("You have been successfully logged out.", "success")
    return redirect(url_for("login"))


@app.route("/test-flash")
def test_flash():
    # A quick route to test different Bootstrap alert colors
    flash("This is a success message!", "success")
    flash("This is an error message!", "danger")
    flash("This is a warning message!", "warning")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
