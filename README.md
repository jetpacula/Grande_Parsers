# Grande_Parsers

### I. Instagram captions

As easiest source of data the instagram captions were chosen to get one-liners
after extraction with Osintgram following bash commands were used to clean emojis and empty captions
[Commands to clean data](https://github.com/jetpacula/Grande_Parsers/blob/main/instaScraper/commands).
Results stored [here](https://github.com/jetpacula/Grande_Parsers/blob/main/instaScraper/insta_captions.txt)

### II. Magazine interviews
Next source was interveiws from magazines, this could be a pretty valuable source of data due to task priorities (Q-A conversation data being most valuable)
The quickest approach was to use BS4

The written [code](https://github.com/jetpacula/Grande_Parsers/blob/main/magParser/MagParser.ipynb) and resulting [data](https://github.com/jetpacula/Grande_Parsers/blob/main/magParser/youtube_CDM.txt).

### III. Youtube interviews
Now for the fun part: as Q-A convos are at high priority and standard interviews with Arianna are scarce on the internet, the most amount of usefull data actually could be found at talk-show interviews. However the result dataset should be in a structured Q-A from, the content on youtube is in audioform, and at best you could find is subtitles without speaker label. 
Following steps were taken to structure the data:
  1. Audiotracks from videos were deserialized and categorized using [this article](https://medium.com/saarthi-ai/who-spoke-when-build-your-own-speaker-diarization-module-from-scratch-e7d725ee279). The example .ipynb file for second interview could be found [here](https://github.com/jetpacula/Grande_Parsers/blob/main/youtubeParser/label%20getter/Grande_Fallon2_Labels-2.ipynb). As a result we'got [csv's](https://github.com/jetpacula/Grande_Parsers/blob/main/youtubeParser/labels_Kelly.csv) with ranges in seconds marked with speaker labels.
  2. Official subs were downloaded with youtube_transcript_api library
  3. To get speaker lables these were matched and then processed according to each interview specifics. Basically, I calculated the intersection of each conversation window from VAD processing with the range of the official subtitles and chosen the maximum value speaker label. (something like 1-nearest neighbor algorythm).
A more detailed commentary with example could be found in [Kelly ipynb file](https://github.com/jetpacula/Grande_Parsers/blob/main/youtubeParser/Interview_Kelly.ipynb).
  4. Each interview is then saved as txt file in [this directory](https://github.com/jetpacula/Grande_Parsers/tree/main/youtubeParser/results).
As a bonus, Ariana's monologue can be found [here](https://github.com/jetpacula/Grande_Parsers/blob/main/youtubeParser/results/youtube_mono.txt). This data was not cleaned or transformed due to low value of one-liners.

Lessons learned and future work
Youtube NLP processing presents a significant potential as a data source when used with VAD method, however the accuaracy is pretty low due to simplicity of chosen algorytm. The accuaracy of this approach could be dramatically increased by adding more neighbors to calculation and implementing full-fledged K-Means or even deep learning NN. 
