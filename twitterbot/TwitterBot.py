#!/usr/bin/env python
import os
import random
import sys
from twython import Twython

from auth import consumer_key, consumer_secret, access_token, access_token_secret

# Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

# Using our newly created object, utilize the update_status to send in the text passed in through CMD

messages = [
    "Ahhhhhhhh, I'm a talking tree, wot!!! 🤔",
    "Stressed out? Have a chat with the Red Oak on MainMall and Stores!",
    "So much construction at UBC! I wish those construction workers would LEAF me alone.",
]


message = random.choice(messages)
api.update_status(status=message)
print("Tweeted: " + message)
