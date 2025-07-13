from pytubefix import YouTube

def download(url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if stream:
        print(f"Downloading: {yt.title}")
        stream.download()
        print("Download complete.")
    else:
        print("No suitable stream found.")

    print(f'Downloaded: {yt.title}')

url = input("Enter YouTube video URL: ")

download(url)