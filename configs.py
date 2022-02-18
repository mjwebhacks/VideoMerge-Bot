# (c) @ManyaDon007

import os


class Config(object):
    API_ID = "3796974"
    API_HASH = "9511d0112631f9990337eb724d1a7d0d"
    BOT_TOKEN = "5288446787:AAGPvKJeD5gPzJfZ_fqx0tvO3-ruaVXxBzI"
    SESSION_NAME = "Video-Merge-Bot"
    UPDATES_CHANNEL = "-1001771465683"
    LOG_CHANNEL = "-1001771465683"
    DOWN_PATH = "./downloads"
    TIME_GAP = 5
    MAX_VIDEOS = 10
    STREAMTAPE_API_USERNAME = "c66b279ae191202bc510"
    STREAMTAPE_API_PASS = "golO1z3WjYc3O0"
    MONGODB_URI = "mongodb+srv://mjfreeflix:Manya007@cluster0.kinyk.mongodb.net/uploads?retryWrites=true&w=majority"
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = 1464063686
    START_TEXT = """
Hi Sir/Madam, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.

Made by @ManyaDon007
"""
    CAPTION = "Video Merged by @{}\n\nMade by @ManyaDon007"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
