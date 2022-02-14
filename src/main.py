import json, random, webbrowser

links = json.load(open('urls.json'))

url = random.sample(links, 1)
webbrowser.open(url[0])