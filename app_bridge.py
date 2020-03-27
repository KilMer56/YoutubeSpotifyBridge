from spotify.spotify_client import SpotifyClient
from youtube.youtube_client import YoutubeClient

import json

class Bridge:

    def __init__(self):
        super().__init__()

        self.youtube = YoutubeClient()
        self.spotify = SpotifyClient()

        self.youtubePlaylistTitle = 'Colloc / Mix House Funky'
        self.spotifyPlaylistTitle = 'Youtube'

        with open('fetched_songs.json') as json_file:
            data = json.load(json_file)
            self.songs = data['songs']
    
    def initCredentials(self):
        self.youtube.getCredentials()
        self.spotify.getToken()

        self.areCredentialsSet = True

    def fetchYoutubePlaylist(self):
        if self.areCredentialsSet:
            playlistId = self.youtube.getPlaylistId(self.youtubePlaylistTitle)

            if playlistId:
                videos = self.youtube.getVideosInPlaylist(playlistId)
                videosToFetch = [i for i in videos if i not in self.songs]

                spotifyPlaylistId = self.spotify.getPlaylist(self.spotifyPlaylistTitle)
                trackIds = []

                if len(videosToFetch) > 0:
                    for videoTitle in videosToFetch:
                        trackId = self.getSpotifyTrackId(videoTitle)

                        if trackId:
                            trackIds.append(trackId)

                    if len(trackIds) > 0:
                        self.spotify.addTracksToPlaylist(spotifyPlaylistId, trackIds)

                    data = {}
                    data['songs'] = videos

                    with open('fetched_songs.json', 'w') as outfile:
                        json.dump(data, outfile)

    def getSpotifyTrackId(self, title):
        trackId = self.spotify.searchTrackId(title)

        if not trackId and title.find("-") != -1:
            titleParts = title.split("-")
            trackId = self.spotify.searchTrackId(titleParts[1].strip(), titleParts[0].strip().lower())

            if not trackId and titleParts[1].find("(") != -1:
                title = titleParts[1].split("(")[0]
                trackId = self.spotify.searchTrackId(title, titleParts[0].strip().lower())

        return trackId
