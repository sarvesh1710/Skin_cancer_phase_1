from crewai import Agent
from tools.report_generation_tool import generate_diagnosis_report

report_generation_agent = Agent(
    role="Report Generation Agent",
    goal="Create a clear and comprehensive diagnostic report based on model output and clinical reasoning.",
    backstory=(
        "You're responsible for synthesizing the output from the CNN, medical explanation, and risk assessment into a clean, "
        "user-friendly report for patients or doctors to review."
    ),
    tools=[generate_diagnosis_report],
    verbose=True
)
