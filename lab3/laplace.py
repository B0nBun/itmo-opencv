import sys
import cv2 as cv

def main(argv: list[str]) -> None:
    window_name = 'Laplace Demo - Simple Edge Detector'

    if len(argv) < 2:
        print('Not enough parameters')
        print('Usage:')
        print('laplace.py <path_to_image> <smooth_type:gaussian|blur|median>')
        return -1

    # Load the image
    src = cv.imread(argv[0], cv.IMREAD_GRAYSCALE)
    smooth_type = argv[1]

    # Check if image is loaded fine
    if src is None:
        print('Error opening image: ' + argv[0])
        return -1

    cv.namedWindow(window_name)

    smooth_type = smooth_type
    def show_result(sigma: float):
        ksize = int(sigma * 5) | 1
        if smooth_type == "gaussian":
            smoothed = cv.GaussianBlur(src, (ksize, ksize), sigma, sigma)
        elif smooth_type == "blur":
            smoothed = cv.blur(src, (ksize, ksize))
        elif smooth_type == "median":
            smoothed = cv.medianBlur(src, ksize)
        else:
            raise Exception("expected smooth type to be 'gaussian', 'blur' or 'median', but got '" + smooth_type + "'")
        laplace = cv.Laplacian(smoothed, cv.CV_16S, 5)
        result = cv.convertScaleAbs(laplace, (sigma + 1)*0.25)
        cv.imshow(window_name, result)
    
    cv.createTrackbar("Sigma", window_name, 0, 15, show_result)
    show_result(0)

    cv.waitKey(0)
    return 0

if __name__ == "__main__":
    exit(main(sys.argv[1:]))