import cv2
import numpy as np
from utils import show, find_biggest_contours, reorder_points

class ImageCleaner():
    def __init__(self, image_path, height = 450, width= 450):
        self.image_path = image_path

        self.img_height = height
        self.img_width = width
        self.image = cv2.imread(image_path)

    def preprocess(self):
        imgGray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, 1, 1, 11, 2)
        return imgThreshold

    def find_contours(self):
        prepro_img = self.preprocess()
        contours, _ = cv2.findContours(prepro_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour = find_biggest_contours(contours)
        return contour
    
    def wrap(self):
        pts1 = reorder_points(self.find_contours())     
        pts2 = np.float32([[0,0], [self.img_width, 0], [0, self.img_height], [self.img_width, self.img_height]])

        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgWarpColored = cv2.warpPerspective(self.image, matrix, (self.img_width, self.img_height))
        show(imgWarpColored)
        
    def run(self):
        self.image = cv2.resize(self.image, (450, 450))
        self.wrap()


img_cln = ImageCleaner("sudoku_1.jpg")
img_cln.run()