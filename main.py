from pytube import YouTube

def Download(link):
    youtube = YouTube(link)
    video = youtube.streams.get_highest_resolution()
    try:
        video.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)