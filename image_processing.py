import cv2
import numpy as np


def strip_alpha(bit_array: np.array):
    rgb_image = cv2.cvtColor(bit_array, cv2.COLOR_BGRA2RGB)
    return rgb_image[:, :, :3][:, :, ::-1]

def save_image(filename: str, image: np.array):
    return cv2.imwrite(filename, image)

def show_image(image: np.array):
    cv2.imshow("Window capture", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def crop_image(left, right, top, bottom, image):
    return image[top:bottom, left:right]

def colour_mask(lowerbound, upperbound, image):
    return cv2.inRange(image, np.array(lowerbound), np.array(upperbound))

def get_contours(image):
    ret, thresh = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    copy = image.copy()
    cv2.drawContours(image=copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)
    return copy

def denoise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
