import sys
import cv2 as cv

def main(argv: list[str]) -> None:
    window_name = 'Sobel Demo - Simple Edge Detector'

    if len(argv) < 1:
        print('Not enough parameters')
        print('Usage:')
        print('sobel.py <path_to_image>')
        return -1

    # Load the image
    src = cv.imread(argv[0], cv.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print('Error opening image: ' + argv[0])
        return -1

    src = cv.GaussianBlur(src, (3, 3), 0)

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    for ksize, scale, delta in [
        (3, 1, 0),
    ]:
        grad_x = cv.Sobel(gray, cv.CV_16S, 1, 0, ksize=ksize, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
        grad_y = cv.Sobel(gray, cv.CV_16S, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

        abs_grad_x = cv.convertScaleAbs(grad_x)
        abs_grad_y = cv.convertScaleAbs(grad_y)

        grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        cv.imshow(window_name, grad)
        cv.waitKey(1000)

    cv.waitKey(0)

    return 0

if __name__ == "__main__":
    exit(main(sys.argv[1:]))