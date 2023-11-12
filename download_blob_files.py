"""
Download blob files:
https://stackoverflow.com/questions/48034696/python-how-to-download-a-blob-url-video
Script download blob file. use master url.
"""

import requests
import m3u8
import subprocess

master_url = ""
r = requests.get(master_url)
m3u8_master = m3u8.loads(r.text)
print(m3u8_master.data)

m3_datas = m3u8_master.data['segments']
with open('video.ts', 'wb') as fs:
    for segments in m3_datas:
        uri = segments['uri']
        r = requests.get(uri)
        fs.write(r.content)

# subprocess.run(['ffmpeg','-i','video.ts','video.mp4'])
