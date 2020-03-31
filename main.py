from app_bridge import Bridge

import schedule
import time

print("[*] Running script every hour")

bridge = Bridge()

def fetch():
    bridge.initCredentials()
    bridge.fetchYoutubePlaylist()

try:
    fetch()
    schedule.every().hour.do(fetch)

    while True:
        schedule.run_pending()
        time.sleep(1)
except Exception as e:
    print(e)