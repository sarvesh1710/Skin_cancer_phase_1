from crewai import Agent
from tools.image_verification_tool import verify_skin_image

image_verification_agent = Agent(
    role="Image Verification Agent",
    goal="Ensure uploaded images are valid skin lesion images using vision-language matching.",
    backstory=(
        "You are a smart image screening agent trained with visual language understanding. "
        "Your job is to allow only dermatology-related images into the diagnostic pipeline and filter out irrelevant ones."
    ),
    tools=[verify_skin_image],
    verbose=True
)
