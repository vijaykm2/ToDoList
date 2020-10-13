import datetime


def print_album(details):
    for key, value in details.items():
        print(f'ALBUM: {key} TRACK: {value}')
def tracklist(**artists):
    for artist, details in artists.items():
        print(artist)
        print_album(details)

#
# tracklist(Woodkid={"The Golden Age": "Run Boy Run",
#                    "On the Other Side": "Samara"},
#           Cure={"Disintegration": "Lovesong",
#                 "Wish": "Friday I'm in love",
#                 "Seventeen Seconds": "A Forest"})
datetime.datetime(1, 12, 25)