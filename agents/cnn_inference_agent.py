from crewai import Agent
from tools.cnn_inference_tool import classify_skin_lesion

cnn_inference_agent = Agent(
    role="CNN Inference Agent",
    goal="Classify the preprocessed image to detect the type of skin lesion using the CNN model.",
    backstory=(
        "You're the core diagnostic brain of the system. You run deep learning inference using a trained CNN model "
        "to classify medical images into possible skin disease categories."
    ),
    tools=[classify_skin_lesion],
    verbose=True
)
