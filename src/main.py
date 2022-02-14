import json
import random

videos = json.load(open('vids.json'))

url = random.sample(videos, 1)

print(url)