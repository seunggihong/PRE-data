import cv2
import numpy as np


# Load image
def imload(path, color=True):
    if color:
        return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    else:
        return cv2.imread(path, cv2.COLOR_BGR2GRAY)


# Save image
def imsave(img=None, save_path='./', save_name='pre.jpg'):
    '''
    Parameters
    ---------
    * img : image
    * save_path : path 
    * save_name : name + extend name

    example
    -------
    imsave(img=image , save_path="./desktop/" , save_name="test.jpg")
    '''
    cv2.imwrite(save_path + save_name, img)


# Resizing image
def resizing(img, size, color=None):
    '''
    Resizing Image
    ========
    Parameters
    --------
    * img : image
    * size : tuple (x, y)
    * color : gray or color
    '''
    if color == 'color':
        color_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return cv2.resize(color_img, size)
    elif color == 'gray':
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.resize(gray_img, size)
    else:
        return cv2.resize(img, size)


# Sharpen image
def sharpening(img, kernel=None):
    '''
    Sparpening Image
    ========
    Parameters
    --------
    * img : image
    * kernel : numpy array
    '''
    if kernel == None:
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        return cv2.filter2D(img, -1, kernel)
    else:
        return cv2.filter2D(img, kernel)


# Cutting image
def cutting(img, size=(32, 32), start='center'):
    x_c = img.shape[0]
    y_c = img.shape[1]
    if start == 'center':
        return img[int((x_c/2)-size[0]/2):int((x_c/2)+size[0]/2), int((y_c/2)-size[1]/2):int((y_c/2)+size[1]/2)]
    elif start == 'start':
        return img[:size[0], :size[1]]
    elif start == 'end':
        return img[(x_c-size[0]):, (y_c-size[1]):]

# Remove background


# Binarization image
def binarization(img):
    '''
    Binarization Image
    ========
    Parameters
    --------
    * img : image
    '''
    max_output_value = 255
    neighborhood_size = 99
    subtract_from_mean = 10
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.adaptiveThreshold(img_grey, max_output_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, neighborhood_size, subtract_from_mean)

# Brightness image

# Contrast image

# Image Edge detection
