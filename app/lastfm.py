from lastfm_config import network


def get_artist_list(limit):
    top = network.get_top_artists(limit)

    for x in top:
        print(x[0].name)

    names = [x[0].name for x in top]

    return names

