from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image
import numpy as np
import cv2


class MNISTClassifier:
    def __init__(self, model_dir):
        self.processor = AutoImageProcessor.from_pretrained(model_dir)
        self.model = AutoModelForImageClassification.from_pretrained(model_dir)

    def predict(self, image):
        if isinstance(image, np.ndarray):
            if image.ndim == 2:
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            else:
                image = Image.fromarray(image)
        else:
            image = Image.open(image).convert('RGB')
        
        inputs = self.processor(images=image, return_tensors="pt")
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=-1)
        predicted_class_idx = logits.argmax(-1).item()
        confidence = probabilities[0, predicted_class_idx].item()
        
        return predicted_class_idx, confidence
