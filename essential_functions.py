import cv2 as cv

img=cv.imread('Photos/cat.jpg')

cv.imshow('Cat',img)

# converting to grey scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GREY',gray)

# blur an image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('BLUR',blur)

# Edge cascade
canny=cv.Canny(img,125,175)
cv.imshow('Canny',canny)

# dilating the image
dilate=cv.dilate(canny,(7,7),iterations=1)
cv.imshow('Dilate',dilate)

# eroding
eroded=cv.erode(dilate,(7,7),iterations=1)
cv.imshow('eroded',eroded)

# resizing 
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

# cropping
cropped=img[50:200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)