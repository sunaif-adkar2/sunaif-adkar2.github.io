import youtube_dl

video = {}
url = "https://youtu.be/SckGR8XiJhQ"
with youtube_dl.YoutubeDL(video) as ydl:
	ydl.download([url])