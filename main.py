# main.py

from crewai import Crew
from agents.image_verification_agent import image_verification_agent
from agents.image_preprocessing_agent import image_preprocessing_agent
from agents.cnn_inference_agent import cnn_inference_agent
from agents.diagnosis_explanation_agent import diagnosis_explanation_agent
from agents.risk_assessment_agent import risk_assessment_agent
from agents.report_generation_agent import report_generation_agent

# Step 1: Load input image path (from user or test folder)
image_path = "data/input_images/sample_skin_lesion.jpg"  # Replace with your own image

# Step 2: Crew setup with all agents
crew = Crew(
    agents=[
        image_verification_agent,
        image_preprocessing_agent,
        cnn_inference_agent,
        diagnosis_explanation_agent,
        risk_assessment_agent,
        report_generation_agent
    ],
    verbose=True
)

# Step 3: Define the task flow
# You can optionally modularize these as subtasks
def run_diagnosis_pipeline(image_path):
    # Agent 1: Verify if it's a valid skin image
    is_skin = image_verification_agent.tools[0](image_path)
    if not is_skin:
        return "🚫 The uploaded image does not appear to be a skin lesion. Please upload a valid skin image."

    # Agent 2: Preprocess image
    preprocessed_tensor = image_preprocessing_agent.tools[0](image_path)

    # Agent 3: Run inference
    predicted_class = cnn_inference_agent.tools[0](preprocessed_tensor)

    # Agent 4: Explain diagnosis
    explanation = diagnosis_explanation_agent.tools[0](predicted_class)

    # Agent 5: Assess risk
    risk_info = risk_assessment_agent.tools[0](predicted_class)

    # Agent 6: Generate report
    report_path = report_generation_agent.tools[0](
        prediction=predicted_class,
        explanation=explanation,
        risk_info=risk_info
    )

    return f"✅ Diagnosis complete.\nPrediction: {predicted_class}\nReport: {report_path}"

# Run the workflow
if __name__ == "__main__":
    print(run_diagnosis_pipeline(image_path))
