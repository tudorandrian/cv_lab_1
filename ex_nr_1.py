import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('city_hall.jpg',3)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# To save the image we will use the next function cv2.imwrite()
# cv2.imwrite('img_gray.jpg',img)

img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()

img2 = np.zeros((512, 512, 3), np.uint8)
height, width, channels = img.shape
img2[:, 0:int(0.5 * width)] = (255, 0, 0)  # (B, G, R)
img2[:, int(0.5 * width):width] = (0, 255, 0)

plt.imshow(img2)
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()

# img = cv2.imread('city_hall.jpg',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.hist(img.ravel(),256,[0,256])
plt.show()