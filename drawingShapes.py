import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('BLANK',blank)

# paint image with color space
blank[:]=0,255,0
cv.imshow('GREEN',blank)

# custom paint
blank[200:300,300:400]=0,0,255
cv.imshow('RED',blank)

# draw a hollow rectangle 
cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=2)
# for a solid in rectangle 
# cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=cv.FILLED)
# cv.imshow('RECTANGLE',blank)

# draw a circle
cv.circle(blank,(250,250),40,(255,0,0),thickness=-1)
cv.imshow('CIRCLE',blank)

# draw a line between
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
cv.imshow('LINE',blank)

# write text on an image
cv.putText(blank,"HELLO WORLD!",(0,255),cv.FONT_HERSHEY_TRIPLEX,1.4,(0,255,0),thickness=2)
cv.imshow('TEXT',blank)
cv.waitKey(0)