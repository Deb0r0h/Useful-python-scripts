from pytube import YouTube
def downloadVideo(url):
    yt = YouTube(url)
    audio = yt.streams.all()
    traccia = list(enumerate(audio))
    for i in traccia:
        print(i)
    print("Inserire itag: ")
    itag = int(input())
    audio[itag].download()
    print("Download Completato 100%")


if __name__=="__main__":
    print("Inserire link video: ")
    url = input()
    downloadVideo(url)

