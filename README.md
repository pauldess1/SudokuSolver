# Sudoku Solver

A Python project that automatically solves Sudoku grids from images. This project uses image processing techniques to extract Sudoku digits and solves the grid using a Sudoku solving algorithm.

## Table of Contents
- [Examples](#examples)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)

## Examples
<div style="display: flex; justify-content: space-between;"> <img src="visual\Sudoku_Solver.png" alt="Illustration" width="100%" /> </div>

## Features

- Digit extraction from a Sudoku image (png, jpg and other picture formats)
- Automatic solving of the Sudoku grid.

## Technologies Used

- Python
- OpenCV, PIL (for image processing)
- NumPy (for array manipulation)
- Transformers, PyTorch

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/sudoku-solver.git
   cd sudoku-solver

2. Install the required packages:

    ```bash
    pip install -r requirements.txt

3. Download the pre-trained weights and place them in the project directory. You can find them on HuggingFace :
https://huggingface.co/farleyknight/mnist-digit-classification-2022-09-04


4. Solve the Sudoku !
    ```bash
    python run.py --input_image_path visual/example.png --output_image_path visual/result.png

## Project Structure
- solver.py
contains the sudoku solver module, takes a numpy array as input and returns another completed numpy array.

- get_vision.py
contains the vision module, allowing you to switch from an image to a sudoku as a numpy table and complete the image using the completed sudoku table. 

- utils.py
contains functions with a variety of uses

- model.py
builds the digit detection model based on work of farleyknight on Huggingface

- run.py
processes all the steps to solve sudoku

## Future Improvements

- Train my own model for digit recognition on MNIST
- Optimize code for better performance in term of running time
- Add the option to run the project on real-time with camera

