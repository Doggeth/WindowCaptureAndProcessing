import re

import capture_window as cw
import image_processing as imgproc

if __name__ == '__main__':
    title_pattern = re.compile("Terraria:*")
    current_windows = cw.get_window_names()
    matching_windows = cw.match_titles(current_windows, title_pattern)

    if len(matching_windows) == 1:
        terraria_window = matching_windows[0]
        bitmap = cw.capture_window(terraria_window[0])
        image = imgproc.strip_alpha(bitmap)
        imgproc.save_image('latest_capture.png', image)
        cellphone_info_img = imgproc.crop_image(1560, 1860, 440, 780, image)
        # masked_image = imgproc.colour_mask([65,65,65],[255,255,255], cellphone_info_img)
        # contour_image = imgproc.get_contours(masked_image)
        denoised_image = imgproc.denoise(cellphone_info_img)
        imgproc.show_image(cellphone_info_img)
        imgproc.show_image(denoised_image)
    else:
        print("Error: Found " + str(len(matching_windows)) + " windows matching title pattern")