from app_bridge import Bridge

import schedule
import time

print("[*] Running script every hour")

bridge = Bridge()
bridge.initCredentials()
bridge.downloadYoutubePlaylist()

# def fetch():
#     bridge.fetchYoutubePlaylist()

# try:
#     fetch()
#     schedule.every(1).hour.do(fetch)

#     while True:
#         schedule.run_pending()
#         time.sleep(1)
# except Exception as e:
#     print(e)