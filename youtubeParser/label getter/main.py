# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#from resemblyzer import preprocess_wav, VoiceEncoder
from pathlib import Path
import os
import sys
from pytube import YouTube
import string

def downloadMp4(vidUrl: str) -> tuple:

    youtube = YouTube(vidUrl)
    video = youtube.streams.get_highest_resolution()
    name = video.title.replace(" ", "_")
    printable = set(string.printable)
    ''.join(filter(lambda x: x in printable, name))
    video.download()
    os.rename(video.default_filename, name+'.mp4')
    res = tuple([name, vidUrl])

    return res

def transformMp4ToWAV(filenameMP4:str) -> str:


    return FilenameWAV



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    a = downloadMp4('https://www.youtube.com/watch?v=hJzNWVkW83I')

    print(a)


for filename in os.listdir(path):
    if (filename.endswith(".mp4")): #or .avi, .mpeg, whatever.
        os.system("ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.png".format(filename))
    else:
        continue


def main(args):

    #  download vids and form a dict

    videos = {}
    for video in args:
        keyValTuple = downloadMp4(video)
        videos[keyValTuple[0]] = keyValTuple

     #   transformToWav()
      #  getLabels(args)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'youtube urls')
    main(sys.argv[:])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
