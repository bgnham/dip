import cv2
import numpy as np

class operation:

    def blend(self, image, logo, x=None, y=None, alpha=None):
        '''
        Use logo and blend it on the image at location (x, y)
        image: the original image
        logo: the logo to blend on to the image
        x: topleft coordinate x
        y: topleft coordinate y
        alpha: blend ratio to the logo

        returns the image blended with logo at loction (x, y)
        '''
		#code
        ### add your code here
        ### Please do not change the structure
        (h, w) = image.shape
        (logoH, logoW) = logo.shape
        output = image
        for i in range(x, x + logoW):
            for j in range(y, y + logoH):
                if i >= 0 and i < w and j >= 0 and j < h:
                    output[i, j] = (alpha * image[i, j]) + ((1 - alpha) * logo[i - x,j - y])
                
        return output #Currently the original image is returned, please replace this with the blended image

