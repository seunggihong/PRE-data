from tools.imgPRE import ImgPRE
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("./data/test.jpg")
img = ImgPRE(img)

# PRE resizing
resize_img = img.resizing(256, 256, color='gray')
plt.imshow(resize_img, cmap='gray')

# PRE sharpening
sharpening_img = img.sharpening()
plt.imshow(sharpening_img)

# PRE binarization
binarization_img = img.binarization()
plt.imshow(binarization_img, cmap='gray')

plt.show()
# PRE save
# img.imsave(img=, save_path="./data/", save_name="test_gray.jpg")
