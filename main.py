import cv2

# read the image file
import matplotlib.pyplot as plt

# read the image file in a grayscale mode

img = cv2.imread('r11.png',0)
sum = 0
count = 0
# logic :- taking average of the value of array of the image so that we can get the threshold value
for i in img:
    for j in i:
        sum = sum+j
        count+=1
avg = int(sum/count)

ret, bw_img = cv2.threshold(img, avg, 1, cv2.THRESH_BINARY_INV)
plt.imshow(bw_img)
plt.show()
print(bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
