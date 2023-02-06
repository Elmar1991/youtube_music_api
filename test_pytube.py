from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=fkNjMuvtpLU')
audio_streams = yt.streams.filter(only_audio=True)
best_audio_stream = sorted(
    audio_streams, key=lambda stream: stream.abr, reverse=True)[0]
best_audio_stream_url = best_audio_stream.url
print(best_audio_stream_url)
