#!/usr/bin/env python

"""
https://github.com/plamere/spotipy/blob/master/spotipy/util.py
"""

import os

import spotipy.util as util


SCOPE = 'user-library-read'
REDIRECT_URI = 'http://localhost'
USERNAME = os.environ.get('spotify_user')
CLIENT_ID = os.environ.get('spotify_client_id')
CLIENT_SECRET = os.environ.get('spotify_client_secret')

print util.prompt_for_user_token(USERNAME,
                                 scope=SCOPE,
                                 client_id=CLIENT_ID,
                                 client_secret=CLIENT_SECRET,
                                 redirect_uri=REDIRECT_URI)
