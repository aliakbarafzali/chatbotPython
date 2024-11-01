import json

with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy =  []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intents['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = []