# importing openCV library
import cv2
print(cv2.__version__)

# 1 for color, 0 for gray Scale, -1 color including alpha channel
# flag = [-1, 0, 1]
# loading color image
flag = 1
try:
    image = cv2.imread('arpit.jpg', flag)
    print("Image loaded ")
    print(image.shape)
except Exception as e:
    print("Error in loading image ",e)

# showing image
frameName = "myFrame"
cv2.imshow(frameName, image)
# wait for 5 second
cv2.waitKey(5000)
cv2.destroyAllWindows()

# Saving image in grayScale format
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayArpit.png", grayImage)

