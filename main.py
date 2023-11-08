from tools.imgPRE import ImgPRE
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("./data/test.jpg")
img = ImgPRE(img)
resize_1 = img.resizing(256, 256, color='gray')

img.imsave(img=resize_1, save_path="./data/", save_name="test_gray.jpg")
