import yt_dlp
import re

class Downloader:
    def __init__(self, url):
        self.url = url

    def get_sub(self):
        ydl_opts = {
            "skip_download": True,
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitleslangs": ["en"],
            "outtmpl": "%(id)s"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
        pattern = r"v=([\w-]{11})&?"
        m = re.search(pattern, self.url)
        file_name = m.group(1) + ".en.vtt"
        return file_name

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, s):
        #url regex
        pattern2 = r"v=([\w-]{11})&?"
        if re.search(pattern2, s) is None:
            raise ValueError
        else:
            self._url = s