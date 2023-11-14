import tools.imgPRE as pre
import matplotlib.pyplot as plt

img = pre.imload("./data/test.jpg")
# img_shap = pre.sharpening(img)
# img_b = pre.binarization(img_shap)
# img_reshape = pre.resizing(img_b, (245, 245))
# plt.imshow(img_reshape, cmap='gray')
# plt.show()

cut = pre.cutting(img, size=(1500, 1500), start='center')
plt.imshow(cut)
plt.show()
