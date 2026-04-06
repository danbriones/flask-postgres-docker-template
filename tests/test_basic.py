import pytest
from app import app, db, User


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///:memory:"  # Use fast in-memory DB for tests
    )

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()


def test_index_page(client):
    """Test that the home page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Ready to Build" in response.data


def test_registration(client):
    """Test that a user can register."""
    response = client.post(
        "/register",
        data={"username": "testuser", "password": "password123"},
        follow_redirects=True,
    )
    assert b"Registration successful" in response.data

    # Verify user exists in DB
    user = User.query.filter_by(username="testuser").first()
    assert user is not None


def test_login_protected_route(client):
    """Test that the profile page is protected."""
    response = client.get(
        "/profile/550e8400-e29b-41d4-a716-446655440000", follow_redirects=True
    )
    assert b"Please log in to access this page" in response.data
