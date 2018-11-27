import csv
from PIL import Image, ImageEnhance
import os
import cv2
import random
import numpy as np
import glob


# MAIN FUNKCIJA

# PRIMJENA MASKE ZA SUNCANE SLIKE

Images_list=os.listdir("C:/Users/Vildan/Desktop/Opencountry/Sunce")

ifile=open('C:/Users/Vildan/Desktop/suncano.csv')
reader = csv.DictReader(ifile)

for i in Images_list:
    print("PETLJA 1 pocetak")
    print(i)
    for row in reader:
        print("PETLJA 2")
        if (str(row['filename'])==i):
            print(str(row['filename']))
            print(i)
            print('true')
            naziv=str(i)
            slika=Image.open("C:/Users/Vildan/Desktop/Opencountry/Sunce/"+naziv)
            baza=int(str(row['region_shape_attributes']).index('height'))
            donja=baza+8
            if (str(row['region_shape_attributes'][donja]).isnumeric()):
                t=1
                if(str(row['region_shape_attributes'][donja+1]).isnumeric()):
                    t=2
                    if (str(row['region_shape_attributes'][donja + 2]).isnumeric()):
                        t=3
            gornja=donja+t
            finalbroj=int(str(row['region_shape_attributes'][donja:gornja]))
            pixelMap = slika.load()
            pixelsNew = slika.load()
            for x in range(slika.size[0]):
                for y in range(slika.size[1]):
                    if y>finalbroj:
                        pixelMap[x,y] = (0,0,0)
            #slika.show()
            slika.save('C:/Users/Vildan/Desktop/MaskaSunce/slika'+i+'.jpg')
    ifile.seek(0)
    print("PETLJA 1 KRAJ")

#MASKA ZA OBLACNE SLIKE

Images_list = os.listdir("C:/Users/Vildan/Desktop/Opencountry/oblaci")

ifile = open('C:/Users/Vildan/Desktop/oblaci.csv')
reader = csv.DictReader(ifile)

for i in Images_list:
    print("PETLJA 1 pocetak")
    print(i)
    for row in reader:
        print("PETLJA 2")
        if (str(row['filename']) == i):
            print(str(row['filename']))
            print(i)
            print('true')
            naziv = str(i)
            slika = Image.open("C:/Users/Vildan/Desktop/Opencountry/oblaci/" + naziv)
            baza = int(str(row['region_shape_attributes']).index('height'))
            donja = baza + 8
            if (str(row['region_shape_attributes'][donja]).isnumeric()):
                t = 1
                if (str(row['region_shape_attributes'][donja + 1]).isnumeric()):
                    t = 2
                    if (str(row['region_shape_attributes'][donja + 2]).isnumeric()):
                        t = 3
            gornja = donja + t
            finalbroj = int(str(row['region_shape_attributes'][donja:gornja]))
            pixelMap = slika.load()
            pixelsNew = slika.load()
            for x in range(slika.size[0]):
                for y in range(slika.size[1]):
                    if y > finalbroj:
                        pixelMap[x, y] = (0, 0, 0)
            # slika.show()
            slika.save('C:/Users/Vildan/Desktop/MaskaOblaci/slika' + i + '.jpg')
    ifile.seek(0)
    print("PETLJA 1 KRAJ")

#FILTER SMOOTH ZA SUNCANJE SLIKE

Images_list=os.listdir("C:/Users/Vildan/Desktop/MaskaSunce")

for i in Images_list:
    print(i)
    # read the image
    image = cv2.imread('C:/Users/Vildan/Desktop/MaskaSunce/'+i)
    # apply the 3x3 median filter on the image
    processed_image = cv2.medianBlur(image, 3)
    # display image
    cv2.imshow('Median Filter Processing', processed_image)
    # save image to disk
    cv2.imwrite('C:/Users/Vildan/Desktop/SmoothSunce/'+i, processed_image)
    # pause the execution of the script until a key on the keyboard is pressed
    #cv2.waitKey(0)

#FILTER SMOOTH ZA OBLACNE SLIKE

Images_list=os.listdir("C:/Users/Vildan/Desktop/MaskaOblaci")

for i in Images_list:
    print(i)
    # read the image
    image = cv2.imread('C:/Users/Vildan/Desktop/MaskaOblaci/'+i)
    # apply the 3x3 median filter on the image
    processed_image = cv2.medianBlur(image, 3)
    # display image
    cv2.imshow('Median Filter Processing', processed_image)
    # save image to disk
    cv2.imwrite('C:/Users/Vildan/Desktop/SmoothOblaci/'+i, processed_image)
    # pause the execution of the script until a key on the keyboard is pressed
    #cv2.waitKey(0)

#POVECAVANJE KONTRASTA OBLACI

Images_list=os.listdir("C:/Users/Vildan/Desktop/SmoothOblaci")

for i in Images_list:
    print(i)
    # read the image
    image = Image.open('C:/Users/Vildan/Desktop/SmoothOblaci/'+i)

    #scale_value = scale.get()
    image = ImageEnhance.Contrast(image).enhance(1.5)
    #image.show()
    image.save('C:/Users/Vildan/Desktop/KontrastOblaci/'+i)

#POVECAVANJE KONTRASTA SUNCANE
Images_list=os.listdir("C:/Users/Vildan/Desktop/SmoothSunce")

for i in Images_list:
    print(i)
    # read the image
    image = Image.open('C:/Users/Vildan/Desktop/SmoothSunce/'+i)

    #scale_value = scale.get()
    image = ImageEnhance.Contrast(image).enhance(1.5)
    #image.show()
    image.save('C:/Users/Vildan/Desktop/KontrastSunce/'+i)

#POVECAVANJE BRIGNESSA OBLACI

Images_list=os.listdir("C:/Users/Vildan/Desktop/KontrastOblaci")

for i in Images_list:
    print(i)
    # read the image
    image = Image.open('C:/Users/Vildan/Desktop/KontrastOblaci/'+i)

    #scale_value = scale.get()
    image = ImageEnhance.Brightness(image).enhance(1.4)
    #image.show()
    image.save('C:/Users/Vildan/Desktop/BrightnessOblaci/'+i)

#POVECAVANJE BRIGNESSA SUNCE

Images_list=os.listdir("C:/Users/Vildan/Desktop/KontrastSunce")

for i in Images_list:
    print(i)
    # read the image
    image = Image.open('C:/Users/Vildan/Desktop/KontrastSunce/'+i)

    #scale_value = scale.get()
    image = ImageEnhance.Brightness(image).enhance(1.10)
    #image.show()
    image.save('C:/Users/Vildan/Desktop/BrightnessSunce/'+i)


#HISTOGRAM OBLACI

Images_list=os.listdir("C:/Users/Vildan/Desktop/BrightnessOblaci")

for i in Images_list:
    print(i)
    # read the image

    img = cv2.imread('C:/Users/Vildan/Desktop/BrightnessOblaci/'+i,0)
    equ = cv2.equalizeHist(img)
    #res = np.hstack((img, equ))  # stacking images side-by-side
    cv2.imwrite('C:/Users/Vildan/Desktop/HistogramOblaci/'+i, equ)


#HISTOGRAM SUNCE


Images_list=os.listdir("C:/Users/Vildan/Desktop/BrightnessSunce")

for i in Images_list:
    print(i)
    # read the image

    img = cv2.imread('C:/Users/Vildan/Desktop/BrightnessSunce/'+i,0)
    equ = cv2.equalizeHist(img)
    #res = np.hstack((img, equ))  # stacking images side-by-side
    cv2.imwrite('C:/Users/Vildan/Desktop/HistogramSunce/'+i, equ)

#rasporedjivanje slika

Images_list=os.listdir("C:/Users/Vildan/Desktop/SVE_SLIKE")

for i in Images_list:
    img = cv2.imread('C:/Users/Vildan/Desktop/SVE_SLIKE/' + i)
    if(random.randint(1, 101)%3==0):
        cv2.imwrite('C:/Users/Vildan/Desktop/TEST/'+i, img)
    else:
        cv2.imwrite('C:/Users/Vildan/Desktop/TRAIN/' +i, img)





