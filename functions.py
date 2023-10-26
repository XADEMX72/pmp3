# Function to download audio from a YouTube video using the pytube library.
# It takes a pytube YouTube object as input.
def download_audio(yt):
    # Get the best available audio-only stream in mp4 format.
    stream = yt.streams.get_audio_only('mp4')

    file_name = input("What would you like to name the file: ")

    file_name_prefix = file_name + ".mp4"

    # Download the audio stream to the 'audio vids' directory.
    stream.download(output_path='audio files', filename=file_name_prefix)

# Function to download the highest resolution video from a YouTube video using the pytube library.
# It takes a pytube YouTube object as input.
def download_video(mp4):
    # Get the highest resolution video stream that is not audio-only.
    stream = mp4.streams.filter(only_video=False).get_highest_resolution()

    file_name = input("What would you like to name the file: ")

    file_name_prefix = file_name + ".mp4"

    # Download the video stream to the 'vids' directory.
    stream.download(output_path='videos files', filename=file_name_prefix)
