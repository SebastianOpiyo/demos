import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not vid.isOpened():
    raise IOError("Cannot open webcam")

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # c = cv2.waitKey(1)
    # if c == 27:
    #     break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()