import scrapetube
from pytube import YouTube
from youtube_tool import download_youtube_video

videos = scrapetube.get_search("soccer match")
print(videos)
for video in videos:
    print(video['videoId'])
    url = 'https://www.youtube.com/watch?v=X0we8220k74'
    res = download_youtube_video(url)
    print(res)