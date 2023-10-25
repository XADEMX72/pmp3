def ytd(yt):
    stream = yt.streams.get_audio_only('mp4')
    stream.download(output_path='audio vids')
def vid(mp4):
    stream = mp4.streams.filter(only_video=False).get_highest_resolution()
    stream.download(output_path='vids')