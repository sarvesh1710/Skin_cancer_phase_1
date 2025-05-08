from crewai import Agent
from tools.image_preprocessing_tool import preprocess_skin_image

image_preprocessing_agent = Agent(
    role="Image Preprocessing Agent",
    goal="Transform verified skin lesion images into model-ready tensors.",
    backstory=(
        "You're an expert in image preprocessing. Your job is to resize, normalize, and "
        "prepare skin lesion images for deep learning inference using either CNNs or HuggingFace vision models."
    ),
    tools=[preprocess_skin_image],
    verbose=True
)
