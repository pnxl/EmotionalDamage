import json
import random
import webbrowser

videos = json.load(open('vids.json'))

url = random.sample(videos, 1)
webbrowser.open(url[0])