from youtube.youtube_secrets import *
from googleapiclient.discovery import build

class YoutubeClient:

    def __init__(self):
        super().__init__()

    def getCredentials(self):
        print("[*] Youtube: Getting credentials")

        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_DEVELOPER_KEY)

    def getPlaylistId(self, title):
        print("[*] Youtube: Getting the playlist Id")
        
        request = self.youtube.playlists().list(
            part="snippet",
            channelId=YOUTUBE_CHANNEL_ID,
            maxResults=15
        )

        response = request.execute()

        for playlist in response['items']:
            if playlist['snippet']['title'] == title:
                return playlist['id']

        return None

    def getVideosInPlaylist(self, playlistId):
        print("[*] Youtube: Getting the videos in the playlist")

        titles = []
        response = None
        nextPageToken = None

        while response is None or nextPageToken:

            request = self.youtube.playlistItems().list(
                part="snippet",
                maxResults=5,
                playlistId=playlistId,
                pageToken=nextPageToken
            )

            response = request.execute()

            for video in response['items']:
                titles.append(video['snippet']['title'])

            try:
                nextPageToken = response['nextPageToken']
            except KeyError:
                nextPageToken = None
            except TypeError:
                nextPageToken = None

        return titles