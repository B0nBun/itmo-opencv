import sys
import cv2 as cv
import math

def main(argv: list[str]) -> None:
    if len(argv) < 1:
        print('Not enough parameters')
        print('Usage:')
        print('hough.py <path_to_image>')
        return -1

    # Load the image
    src = cv.imread(argv[0], cv.IMREAD_GRAYSCALE)

    # Check if image is loaded fine
    if src is None:
        print('Error opening image: ' + argv[0])
        return -1

    canny = cv.Canny(src, 50, 200, None, 3)
    colored = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
    coloredP = colored.copy()
    lines = cv.HoughLines(canny, 1, math.pi / 180, 150, 0, 0)
    for [line] in lines:
        rho = line[0]
        theta = line[1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 - 1000 * b), int(y0 + 1000 * a))
        pt2 = (int(x0 + 1000 * b), int(y0 - 1000 * a))
        cv.line(colored, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

    linesP = cv.HoughLinesP(canny, 1, math.pi / 180, 50, None, 50, 10)

    if linesP is not None:
        for [l] in linesP:
            cv.line(coloredP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow("source", src)
    cv.imshow("standard hough", colored)
    cv.imshow("probobalistic hough", coloredP)

    cv.waitKey(0)
    return 0

if __name__ == "__main__":
    exit(main(sys.argv[1:]))