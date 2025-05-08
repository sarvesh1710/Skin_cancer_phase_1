import torch
import torch.nn as nn

# 👇 Import your trained model class from your GitHub repo (adjust if needed)
from model import CNNModel  # Replace with actual class if it's different

# Load the model (update path to your .pth file)
MODEL_PATH = 'models/melanoma_cnn.pth'
CLASS_NAMES = ['Melanoma', 'Nevus', 'Seborrheic Keratosis']  # Example classes

def load_model():
    model = CNNModel(num_classes=len(CLASS_NAMES))
    model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
    model.eval()
    return model

cnn_model = load_model()

def classify_skin_lesion(image_tensor):
    try:
        with torch.no_grad():
            outputs = cnn_model(image_tensor)
            _, predicted = torch.max(outputs, 1)
            class_id = predicted.item()
            return CLASS_NAMES[class_id]
    except Exception as e:
        print(f"[CNN Inference Error]: {e}")
        return "Error in classification"
