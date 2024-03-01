import cv2 as cv

cap=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter('output.mp4',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame=cap.read()

    if ret==True:
        # to get the dimensions of cap
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        # save the video captured
        out.write(frame)

        # display
        cv.imshow('FRAME',frame)

        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()