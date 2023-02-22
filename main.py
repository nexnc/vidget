import re
from pytube import Playlist



def url_sorter(url):
    if 'shorts' in url or 'watch' in url:
        return url
    elif 'playlist' in url:
        playlist_urls = []
        for playlist_url in Playlist(url):
            playlist_urls.append(playlist_url)
        return playlist_urls
    else:
        return None




while True:
    input_url = input("Enter a URL or type 'quit' to exit: ")
    urls = [url for url in url_sorter(input_url)]
    if input_url.lower() == 'quit':
        break
    if re.match(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+$', input_url):
        print("Valid URL entered:", input_url)
        # Do further processing here
        break
    else:
        print("Invalid URL entered. Please try again.")


