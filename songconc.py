import os

n=1
directory = '.'
commandMergeAux = ""
for filename in os.listdir(directory):
    if(filename != "songconc.py"):
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
