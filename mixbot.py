import requests
import os
import time
#------------------------------------------------------------------------------
                        #    IMAGESCRAP
                    #Reads URLS from images.txt and
                    #makes a 1hr mp4 video (/down/a.mp4)
#------------------------------------------------------------------------------

# ------------------DOWNLOAD GIF AND CREATE MP4 -------------------------------
#Get urls from file
imgsFile = open("images.txt", "r")
imgUrls = imgsFile.readlines()
print(imgUrls)


#for each url
for url in imgUrls:
    #Download img from internet
    os.system("wget -c "+ url + " -O a.jpg")
    os.system("mv *.jpg a.jpg")
    #r = requests.get(url, allow_redirects=True)
    #imgString = './a.jpg'
    #open(imgString, 'wb').write(r.content)
    print("Waiting for images...")
    time.sleep(5)
    #Convert to mp4
    ffmpegString = 'ffmpeg -loop 1  -t 60 -framerate 10 -i a.jpg a.mp4'
    os.system(ffmpegString)



#------------------------------------------------------------------------------
                        #    songconcatenate
                    #decodes and concatenates
                    #all mp3 i directory
#------------------------------------------------------------------------------

n=1
directory = '.'
commandMergeAux = ""
for filename in os.listdir(directory):
    fname, extension = os.path.splitext(filename)
    print(extension)
    if(extension == ".mp3"):
        #f = os.path.join(directory, filename)
        #convert to wav
        #mpg321 -w testing2.wav 0002.mp3
        commandConvert = "mpg321 -w " + str(n) + ".wav " + filename
        os.system(commandConvert)
        #Set Sample rate of 16 kHz (-r 16000), one channel (mono) (-c 1), 16 bits bit depth (-b 16).
        #sox in.wav -r 16000 -c 1 -b 16 out_16000_mono_16bit.wav
        commandProc = "sox " + str(n) + ".wav " +  "-r 16000 -c 1 -b 16 " + str(n) + "_proc.wav"
        os.system(commandProc)
        commandMergeAux = commandMergeAux + str(n) + "_proc.wav "
        n=n+1

#merge wavs
#sox testing_16000_mono_16bit.wav testing2_16000_mono_16bit.wav long.wav
commandMerge = "sox " + commandMergeAux + "long.wav"
os.system(commandMerge)
#convert to mp3?
#ffmpeg -i long.wav -acodec mp3 long.mp3
commandString = "ffmpeg -i long.wav -acodec mp3 long_out.mp3"
os.system(commandString)


#------------------------------------------------------------------------------
                        #    FINAL MERGE
                    #
#------------------------------------------------------------------------------

#----Merge mp3 and MP4
commandFinalMerge = 'ffmpeg -i "a.mp4" -i "long_out.mp3" -shortest outPutFile.mp4'
os.system(commandFinalMerge)
