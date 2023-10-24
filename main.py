from pytube import YouTube

def ytd(yt):
    stream = yt.streams.get_audio_only('mp4')
    stream.download(output_path='audio vids')
def vid(mp4):
    stream = mp4.streams.filter(only_video=False).get_highest_resolution()
    stream.download(output_path='vids')

print("Welcome to pmp3 | By XA72")

while True:
    user_i = input("| 1 | For Video only Audio | 2 | For Video: ")
    
    if user_i == "1":
        url = input("The link of the YouTube video: ")
        yt = YouTube(url)
        ytd(yt)
        break  # Exit the loop after successful input
    elif user_i == "2":
        url = input("The link of the YouTube video: ")
        mp4 = YouTube(url)
        vid(mp4)
        break  # Exit the loop after successful input
    else:
        print("Invalid input. Please enter 1 or 2.")