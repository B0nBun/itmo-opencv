import cv2 as cv
import numpy as np
import random
from typing import Any

Image = np.ndarray[Any, np.dtype[np.uint8]]

def random_color() -> tuple[int, int, int]:
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

def draw_random_lines(image: Image, iters: int) -> Image:
    height, width, _ = image.shape
    x1 = -width / 2
    x2 = 3*width / 2
    y1 = -height / 2
    y2 = 3*height / 2
    for _ in range(iters):
        p1 = (random.randint(x1, x2), random.randint(y1, y2))
        p2 = (random.randint(x1, x2), random.randint(y1, y2))
        color = random_color()
        cv.line(image, p1, p2, color, random.randint(1, 10))
    return image

def draw_random_rectangles(image: Image, iters: int) -> Image:
    height, width, _ = image.shape
    x1 = -width / 2
    x2 = 3*width / 2
    y1 = -height / 2
    y2 = 3*height / 2
    for _ in range(iters):
        p1 = (random.randint(x1, x2), random.randint(y1, y2))
        p2 = (random.randint(x1, x2), random.randint(y1, y2))
        color = random_color()
        cv.rectangle(image, p1, p2, color, random.randint(1, 10))
    return image

def draw_random_ellipses(image: Image, iters: int) -> Image:
    height, width, _ = image.shape
    x1 = -width / 2
    x2 = 3*width / 2
    y1 = -height / 2
    y2 = 3*height / 2
    for _ in range(iters):
        center = (random.randint(x1, x2), random.randint(y1, y2))
        angle = random.randint(0, 180)
        axes = (random.randint(0, 200), random.randint(0, 200))
        color = random_color()
        cv.ellipse(image, center, axes, angle, angle - 100, angle + 200, color, random.randint(1, 10))
    return image


def draw_random_polylines(image: Image, iters: int) -> Image:
    height, width, _ = image.shape
    x1 = -width / 2
    x2 = 3*width / 2
    y1 = -height / 2
    y2 = 3*height / 2
    random_point = lambda: (random.randint(x1, x2), random.randint(y1, y2))
    for _ in range(iters):
        points = np.array([
            random_point(), random_point(), random_point(),
            random_point(), random_point(), random_point(),
        ], np.int32)
        points = points.reshape((-1, 1, 2))
        color = random_color()
        cv.polylines(image, [points], True, color, random.randint(1, 10))
    return image

def draw_random_text(image: Image, iters: int) -> Image:
    height, width, _ = image.shape
    x1 = -width / 2
    x2 = 3*width / 2
    y1 = -height / 2
    y2 = 3*height / 2
    for _ in range(iters):
        p = (random.randint(x1, x2), random.randint(y1, y2))
        cv.putText(image, "Testing text rendering", p, cv.FONT_HERSHEY_SIMPLEX, random.randint(0, 100) * 0.05 + 0.1, random_color(), random.randint(1, 10))
    return image

def draw_big_end(image: Image, iters: int) -> Image:
    height, width, _ = image.shape
    text_size = cv.getTextSize("OpenCV Forever!", cv.FONT_HERSHEY_SIMPLEX, 3, 5)
    origin = ((width - text_size[0][0]) // 2, (height - text_size[0][1]) // 2)
    image = np.zeros(image.shape, dtype=np.uint8)
    cv.putText(image, "OpenCV Forever!", origin, cv.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)
    return image

def main() -> None:
    win_height = 600
    win_width = 900
    win_name = "lab1"
    delay = 750
    iterations = 50

    image: Image = np.zeros((win_height, win_width, 3), dtype=np.uint8)

    for func in [
        draw_random_lines,
        draw_random_rectangles,
        draw_random_ellipses,
        draw_random_polylines,
        draw_random_text,
        draw_big_end,
    ]:
        image = func(image, iterations)
        cv.imshow(win_name, image)
        c = cv.waitKey(delay)
        if c >= 0:
            exit(0)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
