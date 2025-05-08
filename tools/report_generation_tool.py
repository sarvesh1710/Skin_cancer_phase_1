import os
import datetime

def generate_diagnosis_report(prediction, explanation, risk_info, output_dir="output/diagnosis_reports"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(output_dir, f"diagnosis_report_{timestamp}.md")

    report_content = f"""# 🧾 Skin Lesion Diagnosis Report

**🗓️ Date:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

### 🔍 Predicted Diagnosis:
**{prediction}**

---

### 🧠 Medical Explanation:
{explanation}

---

### ⚠️ Risk Assessment:
- **Risk Level:** {risk_info['risk_level']}
- **Recommendation:** {risk_info['recommendation']}

---

*This report is AI-generated and should not replace professional medical advice.*

"""

    with open(report_path, "w") as f:
        f.write(report_content)

    return f"Diagnosis report saved at: `{report_path}`"
