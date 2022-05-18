import requests
import os


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
    r = requests.get(url, allow_redirects=True)
    imgString = 'down/a.jpg'
    open(imgString, 'wb').write(r.content)


    #Convert to mp4
    ffmpegString = 'ffmpeg -loop 1  -t 3600 -framerate 10 -i down/a.jpg down/a.mp4'
    os.system(ffmpegString)









#---------------------------PUT AUDIO AND VIDEO TOGETHER--------------------











#-----------------------------UPLOAD TO YOUTUBE-------------------------
