from spotify.spotify_secrets import *

import spotipy
import spotipy.util as util

class SpotifyClient:

    def __init__(self):
        super().__init__()

    def getToken(self):
        print('[*] Spotify : Getting the access token')

        self.token = util.prompt_for_user_token(SPOTIFY_CLIENT_USERNAME,
            'user-read-private user-read-email playlist-read-private playlist-modify-public playlist-modify-private playlist-read-collaborative',
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri='https://www.google.fr/')

        self.sp = spotipy.Spotify(auth=self.token)

    def createPlaylist(self, title, description = ''):
        if self.token:
            print('[*] Spotify : Creating the playlist : {}'.format(title))

            response = self.sp.user_playlist_create(SPOTIFY_CLIENT_USERNAME, title, description)

            return response['id']
        
        return None
    
    def getPlaylist(self, title):
        if self.token:
            print('[*] Spotify : Trying to get the playlist with the title : {}'.format(title))

            playlists = self.sp.user_playlists(SPOTIFY_CLIENT_USERNAME)

            for playlist in playlists['items']:
                if playlist['owner']['id'] == SPOTIFY_CLIENT_USERNAME and playlist['name'] == title:
                    return playlist['id']
            
            return self.createPlaylist(title)
        
        return None

    def searchTrackId(self, title):
        if self.token:
            print('[*] Spotify : Getting the track with the title : {}'.format(title))

            result = self.sp.search(title)

            if len(result['tracks']['items']) > 0:
                print("[*] Spotify : Got the track named '{}'".format(result['tracks']['items'][0]['name']))

                return result['tracks']['items'][0]['id']

    def addTracksToPlaylist(self, playlist_id, track_ids):
        print('[*] Spotify : Adding {} tracks to the playlist'.format(str(len(track_ids))))

        results = self.sp.user_playlist_add_tracks(SPOTIFY_CLIENT_USERNAME, playlist_id, track_ids)
