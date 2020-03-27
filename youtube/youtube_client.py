from youtube.youtube_secrets import *
from googleapiclient.discovery import build

class YoutubeClient:

    def __init__(self):
        super().__init__()

    def getCredentials(self):
        print("[*] Youtube: Getting credentials")
        
        # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        
        # api_service_name = "youtube"
        # api_version = "v3"
        # client_secrets_file = "youtube/youtube_secrets.json"
        # scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        #  # Get credentials and create an API client
        # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        # credentials = flow.run_console()

        # self.youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

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
        titles = []

        request = self.youtube.playlistItems().list(
            part="snippet",
            maxResults=50,
            playlistId=playlistId
        )

        response = request.execute()

        for video in response['items']:
            titles.append(video['snippet']['title'])

        print(titles)
        return titles