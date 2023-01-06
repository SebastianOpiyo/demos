import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    cv2.imshow('frame', frame)

    # 'q' button is used as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the captured object
vid.release()
# Destroy all windows
cv2.destroyAllWindows()
