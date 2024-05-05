import cv2
import os
from os import makedirs
from PIL import Image
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (thresh, im_blw) = cv2.threshold(grayImg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        im_blw_color = cv2.cvtColor(im_blw, cv2.COLOR_GRAY2BGR)
        combined_Image = cv2.add(im_blw_color, img)
        #im = Image.open(combined_Image)
        #im.save(r"C:\Users\Tommy\Desktop\ven", 'TIFF')
        cv2.imshow('', combined_Image)
        cv2.waitKey(0)
        if img is not None:
            images.append(img)
    return images
load_images_from_folder(r"C:\Users\Tommy\Desktop\School Files\477GFP;S6kSTDETE x G477GFP jpegs")