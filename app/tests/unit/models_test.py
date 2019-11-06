from app.models import Artist

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.hashed_password != 'FlaskIsAwesome'
    assert not new_user.authenticated
    assert new_user.role == 'user'


def test_new_artist():
    """
    GIVEN an Artist model
    WHEN a new Artst is created
    THEN check the attributes
    """
    artist = Artist('2', 'Black Flag', 55, 'www.url')
    assert artist.name == 'Black Flag'
    assert artist.popularity == 55
