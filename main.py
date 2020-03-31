from app_bridge import Bridge

import schedule
import time

print("[*] Running script every day at midnight")

bridge = Bridge()
bridge.initCredentials()

def fetch():
    bridge.fetchYoutubePlaylist()

try:
    fetch()
    schedule.every().day.at("00:00").do(fetch)

    while True:
        schedule.run_pending()
        time.sleep(1)
except Exception as e:
    print(e)