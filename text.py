import os, sys
import cv2
from PIL import Image


print("---Preparing your files---")
def files():

    i=0
    image_path_output = './outputted pictures/'
    name_path = "G:/washing machine/washing_machine_pics/namess/"
    mach_path = 'G:/washing machine/washing_machine_pics/imagess/'
    dir_mach = os.listdir(mach_path)

    print("Fetched all info.")

    for file in dir_mach:
        naming = name_path + "/some"+str(i)+".jpg"
        nameImage = Image.open(naming)
        print("naming:" + naming)


        machPath = mach_path + file
        print("opening "+ machPath )
        machineImg = Image.open(machPath)
        image = machineImg.resize((1080, 1080))
        image_copy = image.copy()

        print("Fetching names.....")
        position = ((image_copy.width - nameImage.width), (image_copy.height - nameImage.height))
        nam = "finished" + str(i) + ".jpg"
        save = image_path_output + nam
        image_copy.paste(nameImage, position, nameImage)
        image_copy.save(save)
        i += 1
        print("Saving........")




files()
