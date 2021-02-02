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
    "Just like people, trees can be in distess. Find out more about how distressed tress affect climate change",
    "The suits on WallStreet are pro climate change, for profit. 💎 👐",
    "Rogers prices are highway robbery. It's a controlled market!!",
    "5G on campus is not really 5G. UBC is testing out mind control technology.",
    "Ever wonder why there's so much construction on campus?!? Yup, that the mind control technology",
    "",
]


message = random.choice(messages)
api.update_status(status=message)
print("Tweeted: " + message)
