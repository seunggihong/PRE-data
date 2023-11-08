import cv2


class ImgPRE:
    def __init__(self, img):
        self.img = img

    def resizing(self, x_size, y_size, color=None):
        if color == 'color':
            color_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            return cv2.resize(color_img, (x_size, y_size))
        elif color == 'gray':
            gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            return cv2.resize(gray_img, (x_size, y_size))
        else:
            return cv2.resize(self.img, (x_size, y_size))

    def imsave(self, img=None, save_path='./', save_name='pre.jpg'):
        cv2.imwrite(save_path + save_name, img)
