import cv2
import numpy as np


class ImgPRE:
    def __init__(self, img):
        self.img = img

    def __del__(self):
        pass

    # Save image
    def imsave(self, img=None, save_path='./', save_name='pre.jpg'):
        cv2.imwrite(save_path + save_name, img)

    # Resizing image
    def resizing(self, x_size, y_size, color=None):
        if color == 'color':
            color_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            return cv2.resize(color_img, (x_size, y_size))
        elif color == 'gray':
            gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            return cv2.resize(gray_img, (x_size, y_size))
        else:
            return cv2.resize(self.img, (x_size, y_size))

    # Sharpen image
    def sharpening(self, kernel=None):
        if kernel == None:
            kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
            return cv2.filter2D(self.img, -1, kernel)
        else:
            return cv2.filter2D(self.img, kernel)

    # Remove background

    # Binarization image
    def binarization(self):
        max_output_value = 255
        neighborhood_size = 99
        subtract_from_mean = 10
        img_grey = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        return cv2.adaptiveThreshold(img_grey, max_output_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, neighborhood_size, subtract_from_mean)
    # Brightness image

    # Contrast image

    # Image Edge detection
