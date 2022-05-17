import requests
import os




# ------------------DOWNLOAD GIF AND CREATE MP4 -------------------------------
url = 'https://media.giphy.com/media/cgW5iwX0e37qg/giphy.gif'
r = requests.get(url, allow_redirects=True)

gifString = 'down/a.gif'
open(gifString, 'wb').write(r.content)


ffmpegStringLoop = 'ffmpeg -stream_loop 100 -i down/a.gif down/aLoop.gif'
os.system(ffmpegStringLoop)

ffmpegString = 'ffmpeg -f gif -i down/aLoop.gif down/a.mp4'
os.system(ffmpegString)



#-------------------DOWNLOAD SONGS--------------------------------










#---------------------------PUT AUDIO AND VIDEO TOGETHER--------------------











#-----------------------------UPLOAD TO YOUTUBE-------------------------
