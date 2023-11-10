import tools.imgPRE as pre
import matplotlib.pyplot as plt

img = pre.imload("./data/test.jpg")

resize_img = pre.resizing(img, (45, 45))
plt.imshow(resize_img)
plt.show()
