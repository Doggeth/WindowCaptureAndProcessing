import cv2
import numpy as np

def strip_alpha(bit_array: np.array):
    return cv2.cvtColor(bit_array, cv2.COLOR_BGRA2BGR)

def save_image(filename: str, image: np.array):
    return cv2.imwrite(filename, image)

def show_image(image: np.array):
    cv2.imshow("Window capture", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
