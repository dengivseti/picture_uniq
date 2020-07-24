from PIL import Image
from PIL import ImageDraw
import random
from PIL import ImageFilter
import os
from random import sample, choice, randrange
import time
from math import sin, cos, pi

def drawSun(draw, centre, radius, startAngle=0, finishAngle=360, rayAngle=10, rayGap=10, rayLength=1000, rayColour="Yellow", rayOutline="Orange"):
    x1,x2 = centre[0] - radius, centre[0] + radius
    y1,y2 = centre[1] - radius, centre[1] + radius
    for rayStart in range(startAngle, finishAngle, rayAngle+rayGap):
     rayEnd = (rayStart+rayAngle) * pi/180
     rayStart *= pi/180
     corner1 = centre[0] + rayLength*cos(rayStart), centre[1] + rayLength*sin(rayStart)
     corner2 = centre[0] + rayLength*cos(rayEnd), centre[1] + rayLength*sin(rayEnd)
     draw.polygon([centre, corner1, corner2], fill=(255,random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
     draw.ellipse((x1, y1, x2, y2), fill=(255,0,0,0))

def randomphoto():
    chars = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHKMNPQRSTUVWXYZ"
    imgname = ''.join(sample(chars, random.randint(9, 12))) + '.jpg'
    diravatar = 'origin/'
    dirmask = 'maskinst/'
    dirsave = 'result/' + imgname
    urlavatar = getavatar(diravatar)
    urlmask = getavatar(dirmask)
    im1 = Image.open(urlavatar)
    razim1 = im1.size

    if (razim1[0] != razim1[1]):
        if (razim1[0] > razim1[1]):
            udaluch = (razim1[0] - razim1[1])/2
            area = (udaluch, 0, razim1[1] + udaluch, razim1[1])
        else:
            area = (0, 0, razim1[0], razim1[0])
        im1 = im1.crop(area)
        razim1 = im1.size
    im2 = Image.open(urlmask)
    razim2 = im2.size
    im2 = im2.rotate(random.randint(0,360))

    if not (razim1[0] >= razim2[0]):
        im2.thumbnail((razim1[0], razim1[1]))
    if not (razim1[1] >= razim2[1]):
        im2.thumbnail((razim1[0], razim1[1]))
    im1.thumbnail((razim2[0], razim2[1]))
    im1.paste(im2, (0, 0), im2)
    width, height = 600, 600
    skyBlue = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    im = Image.new("RGBA", (width, height), skyBlue)
    draw = ImageDraw.Draw(im)
    drawSun(draw, (300, 300), 300, startAngle=0, finishAngle=360, rayAngle=3, rayGap=5)
    im1.paste(im, (0, 0), im)
    im1.save(dirsave)

def getavatar(diravatar):
    try:
        for top, dirs, files in os.walk(diravatar):
            file = random.choices(files)
            put = diravatar + file[0]
        return put
    finally:
        return put
start = time.time()
for x in range(30000):
    a = randomphoto()
time_itog = time.time() - start
print(time_itog)
