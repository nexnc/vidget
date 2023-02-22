from pytube import Playlist

def url_extract(url):
    if 'shorts' or 'watch' in url:
        return url
    elif 'playlist' in url:
        for playlist_url in Playlist(url):
            return playlist_url