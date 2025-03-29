import sys
import cv2 as cv
import numpy as np
 
DELAY_CAPTION = 1500
DELAY_BLUR = 100
MAX_KERNEL_LENGTH = 31
WINDOW_NAME = "Smoothing Demo"
 
Image = np.ndarray

def main(image_file: str) -> int:
    cv.namedWindow(WINDOW_NAME, cv.WINDOW_AUTOSIZE)
    src: Image = cv.imread(cv.samples.findFile(image_file))
    if src is None:
        print("Failed to open the image")
        return 1

    img = image_with_caption(src, "Original Image")
    ok = display_image(img, DELAY_CAPTION)
    if not ok:
        return 0
    
    img = np.copy(src)
    ok = display_image(img, DELAY_CAPTION)
    if not ok:
        return 0

    img = image_with_caption(src, "Homogeneous Blur")
    ok = display_image(img, DELAY_CAPTION)
    if not ok:
        return 0

    for i in range(1, MAX_KERNEL_LENGTH, 2):
        img = cv.blur(src, (i, i))
        ok = display_image(img, DELAY_BLUR)
        if not ok:
            return 0
        
    img = image_with_caption(src, "Gaussian Blur")
    ok = display_image(img, DELAY_CAPTION)
    if not ok:
        return 0

    for i in range(1, MAX_KERNEL_LENGTH, 2):
        img = cv.GaussianBlur(src, (i, i), 0)
        ok = display_image(img, DELAY_BLUR)
        if not ok:
            return 0

    img = image_with_caption(src, "Median Blur")
    ok = display_image(img, DELAY_CAPTION)
    if not ok:
        return 0

    for i in range(1, MAX_KERNEL_LENGTH, 2):
        img = cv.bilateralFilter(src, i, i * 2, i / 2)
        ok = display_image(img, DELAY_BLUR)
        if not ok:
            return 0
        
 
    img = image_with_caption(src, "Done")
    ok = display_image(img, DELAY_CAPTION)
    return 0
 
def image_with_caption(src: Image, caption: str) -> Image:
    dest = np.zeros(src.shape, src.dtype)
    rows, cols, _ = src.shape
    cv.putText(
        dest,
        caption,
        (cols // 4, rows // 2),
        cv.FONT_HERSHEY_COMPLEX,
        1,
        (255, 255, 255)
    )
    return dest

def display_image(img: Image, delay: int) -> bool:
    cv.imshow(WINDOW_NAME, img)
    c = cv.waitKey(delay)
    if c >= 0:
        return False
    return True
 
 
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("USAGE: smoothing.py <image-name>")
        exit(1)
    exit(main(sys.argv[1]))