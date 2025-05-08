from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

# Load CLIP model and processor (from Hugging Face - FREE)
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def verify_skin_image(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        descriptions = ["A dermatoscopic image of a skin lesion", "An unrelated image"]

        inputs = clip_processor(text=descriptions, images=image, return_tensors="pt", padding=True)
        outputs = clip_model(**inputs)

        # Compute probabilities
        logits = outputs.logits_per_image
        probs = logits.softmax(dim=1).detach().numpy()[0]

        print(f"[Verification] Confidence: Skin: {probs[0]:.2f}, Non-skin: {probs[1]:.2f}")
        return probs[0] > 0.75  # returns True if skin lesion confidence > 75%
    
    except Exception as e:
        print(f"[Verification Error]: {e}")
        return False
