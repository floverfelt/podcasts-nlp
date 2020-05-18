import feedparser
from pydub import AudioSegment
import os
import wget

BEN_SHAPIRO_RSS = 'https://feeds.megaphone.fm/WWO8086402096'
POD_SAVE_AMERICA_RSS = 'http://feeds.feedburner.com/pod-save-america'

feeds = [POD_SAVE_AMERICA_RSS]

for feed in feeds:
    i = 1  # Counter for file naming
    parsed_feed = feedparser.parse(feed)
    # First 50 episodes that appear
    for entry in parsed_feed['entries'][:50]:
        episode_url = entry['links'][0]['href']
        TEMP_FILE = "temp.mp3"
        wget.download(episode_url, TEMP_FILE)
        sound = AudioSegment.from_mp3(TEMP_FILE)
        out_file = ""
        if feed == BEN_SHAPIRO_RSS:
            out_file = ("ben_shapiro_wav/ben_shapiro_%s.wav" % i)
        if feed == POD_SAVE_AMERICA_RSS:
            out_file = ("psa_wav/psa_%s.wav" % i)
        sound.export(out_file, format="wav")
        # Cleanup
        os.remove(TEMP_FILE)
        i += 1
