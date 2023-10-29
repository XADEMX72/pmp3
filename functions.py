# Function to download audio from a YouTube video using the pytube library.
# It takes a pytube YouTube object as input.
def download_audio(yt):
    # Get the best available audio-only stream in mp4 format.
    stream = yt.streams.get_audio_only('mp4')

    # Prompt the user for the desired file name.
    while True:
        file_name = input("What would you like to name the file: ")
        if file_name:
            file_name_prefix = file_name + ".mp3"
            # Download the audio stream to the 'audio files' directory.
            stream.download(output_path='audio files', filename=file_name_prefix)
            break  # Exit the loop after a valid file name is provided.
        else:
            print("Invalid Input")

# Function to download the highest resolution video from a YouTube video using the pytube library.
# It takes a pytube YouTube object as input.
def download_video(mp4):
    # Get the highest resolution video stream that is not audio-only.
    stream = mp4.streams.filter(only_video=False).get_highest_resolution()

    # Prompt the user for the desired file name.
    file_name = input("What would you like to name the file: ")

    # Create a file name prefix with the desired name and the ".mp4" extension.
    file_name_prefix = file_name + ".mp4"

    # Download the video stream to the 'videos files' directory.
    stream.download(output_path='videos files', filename=file_name_prefix)
