import cv2
# specify path of the video which you want to open
# 0 is hardware address for web camera of your laptop
# Here we will be capturing video from our web camera
path = 0
cap = cv2.VideoCapture(path)
print("Frame count ",cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Width : ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height : ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# Saving video from web camera
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while cap.isOpened():
    ret, frame = cap.read()
    # ret will return true if we have more frame
    # print all frame or quit if 'q' is pressed
    # opening multiple video at a time
    if ret:
        output.write(frame)
        cv2.imshow("FrameName", frame)
        cv2.imshow("NewFrame GrayScale" , cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release hardware
cap.release()
output.release()
cv2.destroyAllWindows()