from app_bridge import Bridge

import schedule
import time

print("[*] Running script every hour")

bridge = Bridge()
bridge.initCredentials()

def fetch():
    bridge.fetchYoutubePlaylist()

try:
    fetch()
    schedule.every().hour.do(fetch)

    while True:
        schedule.run_pending()
        time.sleep(1)
except Exception as e:
    print(e)