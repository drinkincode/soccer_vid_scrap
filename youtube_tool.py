
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_youtube_video(url):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        ys = yt.streams.get_highest_resolution()
        ys.download('./tmp/')
        return yt.title
    
    except Exception as e:
        return e
