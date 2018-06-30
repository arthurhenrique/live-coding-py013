#curl https://api.meetup.com/BxPy013/events/250848897/rsvps?photo-host=public | jq

from requests import get
from random import choice
import os

pessoas_ativas = []

pessoas_evento = get('https://api.meetup.com/BxPy013/events/250848897/rsvps?photo-host=public&sig_id=254352040&sig=6082fb4e288d62030d1a7430764a08430adb4e4b').json()

for pessoa in pessoas_evento:
    if pessoa['response'] in ('yes', 'waitlist'):
        pessoas_ativas.append((pessoa['member']))

sortudo = choice(pessoas_ativas)

ascii_art_url = "http://artii.herokuapp.com/make?text={}".format(sortudo['name'].replace(' ', '+'))

os.system("firefox {} {}".format(ascii_art_url, sortudo['photo']['photo_link']))

print('log: ', sortudo)