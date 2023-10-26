# Import the necessary module 'YouTube' from the 'pytube' library and 'functions' module
from pytube import YouTube
from functions import *

# Display a welcome message
print("Welcome to pmp3 | By XA72")

# Create an infinite loop that keeps running until the user chooses to exit
while True:
    # Prompt the user to choose an option
    user_i = input("| 1 | For Audio Only | 2 | For Video | 3 | To Exit: ")
    # Check if the user wants to exit
    if user_i == "3":
        break  # Exit the loop if the user chooses option 3

    # Check if the user wants to download audio
    elif user_i == "1":
        # Create an infinite loop to get a valid YouTube video link
        while True:
            url = input("The link of the YouTube video: ")
            if url:
                break  # Exit the loop if a non-empty URL is provided
            else:
                print("Invalid Input")

        # Check if the provided URL is a valid YouTube URL
        if "https://www.youtube.com/" in url:
            # Initialize a YouTube object with the provided URL
            youtube_audio = YouTube(url)
            # Call the 'download_audio' function to download the audio
            download_audio(youtube_audio)
        else:
            print("The input does not contain 'https://www.youtube.com/'.")

        break  # Exit the loop after successful input

    # Check if the user wants to download video
    elif user_i == "2":
        # Create an infinite loop to get a valid YouTube video link
        while True:
            url = input("The link of the YouTube video: ")
            if url:
                break  # Exit the loop if a non-empty URL is provided
            else:
                print("Invalid Input")

        # Check if the provided URL is a valid YouTube URL
        if "https://www.youtube.com/" in url:
            # Initialize a YouTube object with the provided URL
            youtube_video = YouTube(url)
            # Call the 'download_video' function to download the video
            download_video(youtube_video)
        else:
            print("The input does not contain 'https://www.youtube.com/'.")

        break  # Exit the loop after successful input

    # Handle invalid user input
    else:
        print("Invalid input. Please enter 1 or 2.")