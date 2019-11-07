import app.lastfm

def test_artist_list_size():
    """
    Check that getting the artist list from Last.fm returns the correct size
    :return:
    """

    artist_list = app.lastfm.get_artist_list(10)

    assert len(artist_list) == 10
