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

def calc_ndvi(imageNir,imageVis):
    b, g, Red = cv2.split(imageVis)
    #Red = contrast_stretch(Red)
    b, g, NIR = cv2.split(imageNir)
    #NIR = contrast_stretch(NIR)
    zeros = np.zeros(imageNir.shape[:2], dtype="uint8")
    ndvi = ((NIR.astype(float) - Red.astype(float))/(NIR.astype(float) + Red.astype(float)))*120
    #bottom = (r.astype(float) + b.astype(float))
    #bottom[bottom==0] = 0.01
    #ndvi = (b.astype(float) - r) / bottom
    #cv2.imwrite('videos/nir/img%03d.png' % i, NIR)
    #cv2.imwrite('videos/red/img%03d.png' % i, Red)
    return ndvi

for i in range(1,331):
    Nir = cv2.imread('videos/B-photos/out' + str(i) + '.png')
    Vis = cv2.imread('videos/A-photos/out' + str(i) + '.png')
    ndvi = calc_ndvi(Nir,Vis)
    #ndvi_contrasted = contrast_stretch(ndvi)
    ndvi_contrasted = contrast_stretch(ndvi)
    color_mapped_prep = (ndvi_contrasted).astype(np.uint8)
    #color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, cv2.COLORMAP_JET)
    cv2.imwrite('videos/ndvi/img%03d.png' % i, color_mapped_image)
    print(i)