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

        return imgWarpColored
        
    def run(self):
        self.image = cv2.resize(self.image, (450, 450))
        sudoku_img = self.wrap()
        return sudoku_img

class Image2Array():
    def __init__(self, sudoku_img):
        self.sudoku_img = sudoku_img
    
    def splitBoxes(self):
        rows = np.vsplit(self.sudoku_img, 9)
        boxes=[]
        for row in rows :
            cols = np.hsplit(row, 9)
            for box in cols:
                boxes.append(box)
        return boxes
  
class Array2Image():
    def __init__(self, array, img_sudoku, predictions):
        self.array = array
        self.img_sudoku = img_sudoku
        self.predictions = predictions
        self.positions = self.calculate_cell_centers()

    
    def calculate_cell_centers(self):
        rows, cols = 9, 9
        height, width = self.img_sudoku.shape[:2]

        cell_height = height // rows
        cell_width = width // cols

        centers = [[] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                center_x = j * cell_width + cell_width // 2
                center_y = i * cell_height + cell_height // 2
                centers[i].append((center_x, center_y))

        return centers
    
    def write(self, i, j):
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 0, 0)  # Red color
        thickness = 1
        text = str(self.array[i][j])

        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]

        center_x, center_y = self.positions[i][j]

        text_x = center_x - text_size[0] // 2
        text_y = center_y + text_size[1] // 2
        cv2.putText(self.img_sudoku, text, (text_x, text_y), font, font_scale, font_color, thickness)
    
    def run(self):
        for i in range(9):
            for j in range(9):
                if self.predictions[i][j]==0:
                    self.write(i, j)

    def show(self):
        show(self.img_sudoku)

    def save(self, output_path):
        cv2.imwrite(output_path, self.img_sudoku)