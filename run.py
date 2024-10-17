from get_vision import Image2Array, ImageCleaner, Array2Image
from model import MNISTClassifier
from solver import SudokuSolver
from utils import predict
import argparse

def recognize_digits(boxes, classifier):
    predictions = []
    n = 8
    L=[]
    for box in boxes:
        if n == 8 :
            if len(L)>0:
                predictions.append(L)
            L = [predict(box, classifier, 0.75)]
            n = 0
        else :
            L.append(predict(box, classifier, 0.75))
            n+=1
    predictions.append(L)
    return predictions

def main(input_image_path, output_image_path):
    print("Input Image Path:", input_image_path)

    ### IMAGE CLEANER ###
    img_cln = ImageCleaner(input_image_path)
    sudoku_img = img_cln.run()

    ### DIGITS RECOGNITION ###
    img2array = Image2Array(sudoku_img)
    boxes = img2array.splitBoxes()
    classifier = MNISTClassifier("model_mnist")
    predictions = recognize_digits(boxes, classifier)
    
    ### SUDOKU SOLVER ###
    solver = SudokuSolver([row.copy() for row in predictions])
    result = solver.resolve()
    
    ### RESULTS WRITING ###
    array2image= Array2Image(result, sudoku_img, predictions)
    array2image.run()
    array2image.save(output_image_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sudoku Solver Training")
    parser.add_argument('--input_image_path', type=str, required=True,
                        help='Path to the input image for Sudoku')
    parser.add_argument('--output_image_path', type=str, required=True,
                        help='Path to save the resolved Sudoku')
    args = parser.parse_args()
    main(args.input_image_path, args.output_image_path)

