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
    
def crop_center(image):
    height, width = image.shape

    new_width = width - 12
    new_height = height - 12

    if new_width <= 0 or new_height <= 0:
        raise ValueError("L'image doit être suffisamment grande pour être recadrée.")

    center_x, center_y = width // 2, height // 2

    x1 = center_x - new_width // 2
    y1 = center_y - new_height // 2
    x2 = center_x + new_width // 2
    y2 = center_y + new_height // 2

    cropped_image = image[y1:y2, x1:x2]

    return cropped_image

def preprocess(image):
        imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, 1, 1, 11, 2)
        return imgThreshold

def predict(box, classifier, confidence):
    guess = 0
    n_box = cv2.resize(box, (28, 28))
    n_box = preprocess(box)
    n_box = crop_center(n_box)
 
    pred = classifier.predict(n_box)
    if pred[1] > confidence :
        guess = pred[0]
    return guess