from spotify.spotify_client  import SpotifyClient
from youtube.youtube_client import YoutubeClient

spotify = SpotifyClient()
youtube = YoutubeClient()

youtube.getCredentials()
testId = youtube.getPlaylistId('House')
youtube.getVideosInPlaylist(testId)
# spotify.getToken()
# playlistId = spotify.getPlaylist('Test')
# trackId = spotify.searchTrackId('Life is a dancefloor')

# spotify.addTracksToPlaylist(playlistId, [trackId])