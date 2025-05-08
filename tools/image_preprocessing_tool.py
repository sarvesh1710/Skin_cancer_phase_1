from PIL import Image
import torchvision.transforms as transforms
from transformers import AutoImageProcessor

def preprocess_skin_image(image_path, model_type="cnn"):
    try:
        image = Image.open(image_path).convert("RGB")
        
        if model_type == "huggingface":
            # HuggingFace vision models (e.g., ResNet, ViT)
            processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
            inputs = processor(images=image, return_tensors="pt")
            return inputs["pixel_values"]  # shape: [1, 3, 224, 224]
        
        else:
            # Standard CNN (PyTorch)
            transform = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406],
                                     [0.229, 0.224, 0.225])
            ])
            tensor_image = transform(image).unsqueeze(0)  # Add batch dimension
            return tensor_image
    
    except Exception as e:
        print(f"[Preprocessing Error]: {e}")
        return None
