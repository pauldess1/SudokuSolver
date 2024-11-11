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

## Model Parameters

This project uses a **Vision Transformer (ViT)** model for digit recognition, based on the pre-trained model available on Hugging Face. Below are the important parameters of the model used in this project:

- **Model Type**: `ViTForImageClassification`  
  The model is based on the **Vision Transformer** architecture, specifically designed for image classification tasks, which in this case is used for recognizing digits from Sudoku images.

- **Image Size**: `224 x 224`  
  The model expects input images of size 224x224 pixels. Therefore, any input images (such as Sudoku grid images) must be resized accordingly.

- **Patch Size**: `16`  
  The model splits each image into patches of size 16x16 pixels, which are processed independently by the transformer layers.

- **Number of Channels**: `3`  
  The model expects color images with 3 channels (RGB). As the Sudoku images are grayscale (1 channel), they are converted to RGB by duplicating the single channel across all three color channels.

- **Hidden Size**: `768`  
  The hidden size refers to the number of units in the hidden layers of the transformer model. This value is set to 768 for this ViT model.

- **Intermediate Size**: `3072`  
  The intermediate size is the size of the hidden layers in the feed-forward network within each transformer block.

- **Number of Attention Heads**: `12`  
  The model uses 12 attention heads in the multi-head self-attention mechanism, allowing it to focus on different parts of the input image.

- **Number of Hidden Layers**: `12`  
  The model consists of 12 layers in its transformer encoder, each performing self-attention and feed-forward processing.

- **Dropout Rates**:  
  - **Attention Dropout**: `0.0`  
  - **Hidden Dropout**: `0.0`  
  The model does not use dropout in either the attention mechanism or the hidden layers, ensuring that all units are active during inference.

- **Fine-Tuning Task**: `image-classification`  
  The model is fine-tuned for image classification, specifically for recognizing digits from images of Sudoku grids.

- **Label Mapping**:  
  The model is configured to classify 10 digits (0-9), as required for the Sudoku digit recognition task.

## Future Improvements

- Train my own model for digit recognition on MNIST
- Optimize code for better performance in term of running time
- Add the option to run the project on real-time with camera

