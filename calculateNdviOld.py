import cv2
import numpy as np
from fastiecm import fastiecm

def display(image, image_name):
    image = np.array(image, dtype=float)/float(255)
    shape = image.shape
    image = cv2.resize(image, (width, height))
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out

def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi

for i in range(1,331):
    original = cv2.imread('videos/B-photos/out' + str(i) + '.png')
    contrasted = contrast_stretch(original)
    #display(contrasted, 'Contrasted original')
    cv2.imwrite('contrasted.png', contrasted)
    ndvi = calc_ndvi(contrasted)
    #display(ndvi, 'NDVI')
    ndvi_contrasted = contrast_stretch(ndvi)
    #color_mapped_prep = ndvi_contrasted.astype(np.uint8)
    #color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    cv2.imwrite('videos/ndvi/img%03d.png' % i, ndvi_contrasted)
    print(i)