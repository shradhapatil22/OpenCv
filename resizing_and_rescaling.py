import cv2 as cv

img=cv.imread('Photos/cat.jpg')

cv.imshow('Cat',img)

# works only for live videos
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)

# works for image,videos and live videos
def rescaleFrame(frame,scale=0.2):
    # set width
    width=int(frame.shape[1]*scale)
    # set height
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)
# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized=rescaleFrame(frame)
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        cv.imshow('Video Resized', frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()