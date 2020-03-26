from spotify_client import SpotifyClient

spotify = SpotifyClient()
spotify.getToken()
playlistId = spotify.getPlaylist('Test')
trackId = spotify.searchTrackId('Life is a dancefloor')

spotify.addTracksToPlaylist(playlistId, [trackId])