import sys
import cv2 as cv

def main(argv: list[str]) -> None:
    window_name1 = "Edge map : Canny default (Sobel gradient)"
    window_name2 = "Edge map : Canny with custom gradient (Scharr)"

    if len(argv) < 1:
        print('Not enough parameters')
        print('Usage:')
        print('canny.py <path_to_image>')
        return -1

    # Load the image
    src = cv.imread(argv[0], cv.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print('Error opening image: ' + argv[0])
        return -1

    cv.namedWindow(window_name1, 1)
    cv.namedWindow(window_name2, 1)

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    def onTrackbar(edgeThresh: int, edgeThreshScharr: int):
        blur = cv.blur(gray, (3, 3))
        edge1 = cv.Canny(blur, edgeThresh, edgeThresh*3, 3)
        cv.imshow(window_name1, edge1)

        dx = cv.Scharr(blur, cv.CV_16S, 1, 0)
        dy = cv.Scharr(blur, cv.CV_16S, 0, 1)
        edge2 = cv.Canny(dx, dy, edgeThreshScharr, edgeThreshScharr*3)
        cv.imshow(window_name2, edge2)

    edgeThresh = 0
    edgeThreshScharr = 0

    def onThreshTrackbar(x: int):
        edgeThresh = x
        onTrackbar(edgeThresh, edgeThreshScharr)

    def onScharrThreshTrackbar(x: int):
        edgeThreshScharr = x
        onTrackbar(edgeThresh, edgeThreshScharr)

    cv.createTrackbar(
        "Canny threshold default",
        window_name1,
        0, 100,
        onThreshTrackbar
    )
    cv.createTrackbar(
        "Canny threshold Scharr",
        window_name2,
        0, 400,
        onScharrThreshTrackbar
    )

    onTrackbar(0, 0)

    cv.waitKey(0)
    return 0

if __name__ == "__main__":
    exit(main(sys.argv[1:]))