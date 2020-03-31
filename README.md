<h1 align="center">Welcome to YoutubeSpotifyBridge 👋</h1>
<p style="text-align:center">
<img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
<img src="https://img.shields.io/badge/python-%3E%3D3.6.9-blue.svg" />
<a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-Green.svg" />
  </a>
</p>

> Simple script that converts Youtube videos inside a specific playlist into Spotify music playlist

## Table of Content

-   [Prerequisites](#prerequisites)
-   [Configuration](#configuration)
-   [Usage](#usage)
-   [ToDo](#todo)
-   [Author](#author)

## Prerequisites

-   python >=3.6.9
-   pip >=3.0.0

## Configuration

### Youtube

Before setting up your Youtube Secrets, the playlist that you want to fetch must be in public and accessible

1. Create a developer key using [this link](https://developers.google.com/youtube/v3/quickstart/python)
2. Create a ``youtube_secrets.py`` file inside the youtube folder
3. Set the following vars :

```python
YOUTUBE_DEVELOPER_KEY = "YOUR DEVELOPER KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_CHANNEL_ID = "YOUR CHANNEL ID"
```

### Spotify

1. Register an App using [this link](https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app)
2. Create a ``spotify_secrets.py`` file inside the spotify folder
3. Set the following vars :

```python
SPOTIFY_CLIENT_ID = "YOUR APP CLIENT ID"
SPOTIFY_CLIENT_SECRET = "YOUR APP CLIENT SECRET"
SPOTIFY_CLIENT_USERNAME = "YOUR USERNAME"
```

### Global

After setting up your Youtube and Spotify secrets, just set the ``youtubePlaylistTitle`` and ``spotifyPlaylistTitle`` vars inside the ``app_bridge.py`` file that correspond to the name of your Youtube and Spotify playlist to link

## Usage

Just run the following commands to launch the script (it will run every hour, but you can modify this in the ``main.py`` file)

```sh
docker build -t youtube_spotify_bridge .
docker run youtube_spotify_bridge
```

## ToDo
- Improve configuration process (all vars within a single file)
- Improve matching process between Youtube and Spotify
- Documentation
- Add interface ??

## Author

👤 **KilMer56**

* LinkedIn: [@killianmer](https://linkedin.com/in/killianmer)

## Show your support

Give a ⭐️ if this project helped you!
