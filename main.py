import tools.imgPRE as pre
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("./data/test.jpg", cv2.COLOR_BAYER_BG2BGR)
# PRE resizing
resize_img = pre.resizing(img, 256, 256, color='gray')
plt.imshow(resize_img, cmap='gray')

# PRE sharpening
sharpening_img = pre.sharpening(img)
plt.imshow(sharpening_img)

# PRE binarization
binarization_img = pre.binarization(img)
plt.imshow(binarization_img, cmap='gray')

plt.show()
# PRE save
# img.imsave(img=, save_path="./data/", save_name="test_gray.jpg")
