from client_secret import *
from base64 import b64encode

import requests
import json

class SpotifyClient:

    def __init__(self):
        super().__init__()

        self.token = CLIENT_TOKEN

    def getToken(self):
        print('[*] Getting the access token')

        ids = '{}:{}'.format(CLIENT_ID, CLIENT_SECRET).encode()
        headers = {'Authorization': 'Basic {}'.format((b64encode(ids)).decode("utf-8"))}
        payload = {'grant_type': 'client_credentials'}

        response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=payload)
        json_response = response.json()

        self.token = json_response['access_token']

    def getMyId(self):
        if self.token is not None:
            print('[*] Getting the account Id')

            headers = {'Authorization': 'Bearer {}'.format(self.token)}

            response = requests.get("https://api.spotify.com/v1/me", headers=headers)
            json_response = response.json()

            self.id = json_response['id']

    def getListPlaylistTitle(self):
        names = []

        if self.token is not None:
            headers = {'Authorization': 'Bearer {}'.format(self.token)}

            response = requests.get("https://api.spotify.com/v1/me/playlists", headers=headers)
            json_response = response.json()
            
            for playlist in json_response['items']:
                names.append(playlist['name'])

        return names

    def isPlaylistExists(self, title):
        print('[*] Checking if the playlist exists')

        names = self.getListPlaylistTitle()

        return title in names

    def createPlaylist(self, title):
        if self.token is not None and self.id is not None and not self.isPlaylistExists(title):
            print('[*] Creating the playlist : {}'.format(title))

            headers = {'Authorization': 'Bearer {}'.format(self.token)}
            data = json.dumps({
                "name": title,
                "description": "Test Desc",
                "public": "false"
            })

            response = requests.post("https://api.spotify.com/v1/users/{}/playlists".format(self.id), headers=headers, data=data)
            json_response = response.json()

            print(json_response)

