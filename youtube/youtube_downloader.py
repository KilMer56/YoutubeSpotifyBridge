from pytube import YouTube

class YoutubeDownloader:

    def __init__(self):
        super().__init__()

    def download(self, videoId):
        print("[*] PyTube : Downloading the Youtube video with the id : {}".format(videoId))

        videoUrl = 'https://www.youtube.com/watch?v={}'.format(videoId)
        
        yt = YouTube(videoUrl)
        yt.streams.filter(only_audio=True).first().download('./downloads')