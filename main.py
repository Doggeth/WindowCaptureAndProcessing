import re
import paddleocr

import capture_window as cw
import image_processing as imgproc

if __name__ == '__main__':
    ocr = paddleocr.PaddleOCR(device='gpu', lang="en")
    title_pattern = re.compile("Terraria:*")
    current_windows = cw.get_window_names()
    matching_windows = cw.match_titles(current_windows, title_pattern)

    if len(matching_windows) == 1:
        terraria_window = matching_windows[0]

        while True:
            answer = input('y or n: ').lower()
            if answer in ['n']:
                break

            bitmap = cw.capture_window(terraria_window[0])
            image = imgproc.strip_alpha(bitmap)
            imgproc.save_image('latest_capture.png', image)
            imgproc.show_image(image)

            result = ocr.predict(image)
            for line in result[0]['rec_texts']:
                print(line)
    else:
        print("Error: Found " + str(len(matching_windows)) + " windows matching title pattern")