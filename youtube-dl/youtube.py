from __future__ import unicode_literals
import youtube_dl
import sys

def main():
    if len(sys.argv) == 1:
        print('Video id must be passed as parameter.')
        exit(0)
    url = 'http://www.youtube.com/watch?v={}'.format(sys.argv[1])
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    main()
