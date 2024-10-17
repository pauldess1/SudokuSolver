from get_vision import Image2Array, ImageCleaner
from values import sudoku1, sudoku2
from model import MNISTClassifier
from solver import SudokuSolver
from utils import predict, preprocess, accuracy

sudo_path = "sudoku_1.jpg"
img_cln = ImageCleaner(sudo_path)

SUDO = sudoku2 if sudo_path == "sudoku_2.png" else sudoku1
sudoku_img = img_cln.run()
img2array = Image2Array(sudoku_img)
boxes = img2array.splitBoxes()

classifier = MNISTClassifier("model_mnist")
predictions = []
n = 8
L=[]
for box in boxes:
    if n == 8 :
        if len(L)>0:
            predictions.append(L)
        L = [predict(box, classifier, 0.9)]
        n = 0
    else :
        L.append(predict(box, classifier, 0.9))
        n+=1
predictions.append(L)

sudoku = predictions
solver = SudokuSolver(sudoku)
solver.resolve()