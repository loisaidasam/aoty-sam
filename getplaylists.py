#!/usr/bin/env python

# https://developer.spotify.com/web-api/playlist-endpoints/
# https://developer.spotify.com/web-api/get-list-users-playlists/
# https://developer.spotify.com/web-api/get-playlist/

import argparse
import os
import sys

import spotipy


def playlist_generator(token, user):
    client = spotipy.Spotify(token)
    offset = 0
    while True:
        playlists = client.user_playlists(user, offset=offset, limit=50)
        if not playlists.get('items'):
            break
        for item in playlists['items']:
            yield item['name']
        offset += len(playlists['items'])


def main(token, user, number=False, limit=None):
    print >> sys.stderr, "Looking up playlists for user %s ..." % user
    generator = playlist_generator(token, user)
    for playlist_num, playlist in enumerate(generator, start=1):
        try:
            result = playlist.encode('utf-8')
            if number:
                result = "%s. %s" % (playlist_num, result)
            print result
        except Exception as exception:
            print "Error w/ playlist #%s - %s" % (playlist_num, exception)
        if limit and playlist_num >= limit:
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token',
                        default=os.environ.get('spotify_access_token'),
                        help="Spotify access token")
    parser.add_argument('--user',
                        default=os.environ.get('spotify_user'),
                        help="Spotify user")
    parser.add_argument('-n', '--number',
                        action='store_true',
                        default=False,
                        help="Number the results (1 through whatever)")
    parser.add_argument('--limit', type=int, default=None)
    args = parser.parse_args()
    main(args.token, args.user, args.number, args.limit)
