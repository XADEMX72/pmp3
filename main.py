from pytube import YouTube
from functions import *

print("Welcome to pmp3 | By XA72")

while True:
    user_i = input("| 1 | For Video only Audio | 2 | For Video: ")

    if user_i == "1":
        while True:
            url = input("The link of the YouTube video: ")
            if url:
                break
            else:
                print("Invalid Input")
        if "https://www.youtube.com/" in url:
            youtube_video_audio = YouTube(url)
            ytd(youtube_video_audio)
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
            youtube_audio = YouTube(url)
            vid(youtube_audio)
        else:
            print("The input does not contain 'https://www.youtube.com/'.")
        break  # Exit the loop after successful input
    else:
        print("Invalid input. Please enter 1 or 2.")