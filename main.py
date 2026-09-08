import re
import paddleocr
import time
from windows_toasts import Toast, WindowsToaster

import capture_window as cw
import image_processing as imgproc

if __name__ == '__main__':
    ocr = paddleocr.PaddleOCR(device='gpu', lang="en", use_textline_orientation=False)

    toaster = WindowsToaster('TERRARIA TOASTER')
    sandstorm_toast = Toast()
    sandstorm_toast.text_fields = ['SANDSTORM ALERT!']
    sandstorm_toast.on_activated = lambda _: print("SANDSTORM ALERT!")
    travelling_merchant_toast = Toast()
    travelling_merchant_toast.text_fields = ['TRAVELING MERCHANT']
    travelling_merchant_toast.on_activated = lambda _: print("TRAVELING MERCHANT!")

    title_pattern = re.compile("Terraria:*")
    current_windows = cw.get_window_names()
    matching_windows = cw.match_titles(current_windows, title_pattern)

    if len(matching_windows) == 1:
        terraria_window = matching_windows[0]

        while True:
            bitmap = cw.capture_window(terraria_window[0])
            image = imgproc.strip_alpha(bitmap)
            imgproc.save_image('latest_capture.png', image)
            info_img = imgproc.crop_image(1550,1880,425,775, image)
            chat_img = imgproc.crop_image(100, 600, 700, 1080, image)

            info_data = ocr.predict(info_img)
            for line in info_data[0]['rec_texts']:
                if "sandstorm" in line.lower():
                    toaster.show_toast(sandstorm_toast)

            chat_data = ocr.predict(chat_img)
            for line in chat_data[0]['rec_texts']:
                if "traveling" in line.lower():
                    toaster.show_toast(travelling_merchant_toast)

            time.sleep(3)
    else:
        print("Error: Found " + str(len(matching_windows)) + " windows matching title pattern")