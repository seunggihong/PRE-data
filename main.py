from tools.imgPRE import ImgPRE
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("./data/test.jpg")
img = ImgPRE(img)

# PRE resizing
resize_img = img.resizing(256, 256, color='gray')

# PRE sharpening
sharpening_img = img.sharpening()
plt.imshow(sharpening_img)
plt.show()


# PRE save
# img.imsave(img=, save_path="./data/", save_name="test_gray.jpg")
