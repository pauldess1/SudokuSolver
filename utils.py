import cv2
import numpy as np

def show(img):
    cv2.imshow("image", img)
    cv2.waitKey(6000)

def find_biggest_contours(contours):
    biggest_contour = None
    max_area = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50:
            perimeter = cv2.arcLength(contour, True)
            shape = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            if area > max_area and len(shape) == 4:
                biggest_contour = shape
                max_area = area

    return biggest_contour

def reorder_points(points):
    points = points.reshape(4, 2)
    ordered_points = np.zeros((4, 2), dtype=np.float32)
    add = points.sum(1)
    
    ordered_points[0] = points[np.argmin(add)]
    ordered_points[3]= points[np.argmax(add)]
    diff = np.diff(points, axis=1)
    ordered_points[1] = points[np.argmin(diff)]
    ordered_points[2] = points[np.argmax(diff)]
    return ordered_points
    