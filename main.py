from pytube import YouTube
from functions import *

print("Welcome to pmp3 | By XA72")

while True:
    user_i = input("| 1 | For Audio Only | 2 | For Video: ")

    if user_i == "1":
        while True:
            url = input("The link of the YouTube video: ")
            if url:
                break
            else:
                print("Invalid Input")
        if "https://www.youtube.com/" in url:
            # Initialize a YouTube object with the provided URL
            youtube_audio = YouTube(url)
            # Call the download_audio function to download the audio
            download_audio(youtube_audio)
        else:
            print("The input does not contain 'https://www.youtube.com/'.")
        break  # Exit the loop after successful input
    elif user_i == "2":
        while True:
            url = input("The link of the YouTube video: ")
            if url:
                break
            else:
                print("Invalid Input")
        if "https://www.youtube.com/" in url:
            # Initialize a YouTube object with the provided URL
            youtube_video = YouTube(url)
            # Call the download_video function to download the video
            download_video(youtube_video)
        else:
            print("The input does not contain 'https://www.youtube.com/'.")
        break  # Exit the loop after successful input
    else:
        print("Invalid input. Please enter 1 or 2.")