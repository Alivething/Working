import time
import cv2
import numpy as np
import matplotlib.pyplot as plt


class ConvolutionFilter():

    def __init__(self, image):

        self.image = image
        
        self.sharpen = np.array(([-1, -1, -1],
                                 [-1,  9, -1],
                                 [-1, -1, -1]))

        self.gaussian = (1 / 16.0) * np.array([[1., 2., 1.],
                                  [2., 4., 2.],
                                  [1., 2., 1.]])

    def __applyFilter(self, image, kernel):

        filtered_image = np.zeros(image.shape)

        for row in range(1, len(image)-1):
            for col in range(1, len(image[row])-1):
                    # Convolution calculation
                    pixels = image[row-1:row+2, col-1:col+2]
                    pixel_kernel = (pixels * kernel).sum()
                    if pixel_kernel > 0:
                        filtered_image[row, col] = pixel_kernel % 255
                    else:
                        filtered_image[row, col] = 0

        return filtered_image

    def applySharpen(self):

        kernel = self.sharpen
        filtered_image_red = self.__applyFilter(self.image[:, :, 0], kernel)
        filtered_image_green = self.__applyFilter(self.image[:, :, 1], kernel)
        filtered_image_blue = self.__applyFilter(self.image[:, :, 2], kernel)
        filtered_image = np.dstack((np.rint(abs(filtered_image_red)), 
                                np.rint(abs(filtered_image_green)), 
                                np.rint(abs(filtered_image_blue))))/255
        return filtered_image

    def applyGaussian(self):

        kernel = self.gaussian
        filtered_image_red = self.__applyFilter(self.image[:, :, 0], kernel)
        filtered_image_green = self.__applyFilter(self.image[:, :, 1], kernel)
        filtered_image_blue = self.__applyFilter(self.image[:, :, 2], kernel)
        filtered_image = np.dstack((np.rint(abs(filtered_image_red)), 
                                np.rint(abs(filtered_image_green)), 
                                np.rint(abs(filtered_image_blue))))/255
        return filtered_image


image_path="pics\puppy.jpg"
image = cv2.imread(image_path)
image = cv2.resize(image, (1024, 1024))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

high_filters = ConvolutionFilter(image)

fig, ax = plt.subplots(1,2, figsize=(17,17))
ax[0].set_title("Origin Image")
ax[0].imshow(high_filters.image, cmap="gray")
ax[1].set_title("Sharpened Image")

start = time.time()
ax[1].imshow(high_filters.applySharpen(), cmap="gray")
end = time.time()
plt.show()


print(f"Time taken for image size {image.size}: {end - start} s")