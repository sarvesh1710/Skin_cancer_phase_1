def explain_diagnosis(predicted_class):
    explanations = {
        "Melanoma": (
            "Melanoma is a serious form of skin cancer that begins in melanocytes. It can spread rapidly if not detected early. "
            "It usually appears as an irregularly shaped mole or dark spot on the skin."
        ),
        "Nevus": (
            "A nevus, or mole, is a common benign skin growth composed of melanocytes. Most nevi are harmless and don't require treatment, "
            "but changes in shape or color should be monitored."
        ),
        "Seborrheic Keratosis": (
            "Seborrheic keratosis is a non-cancerous skin lesion that often appears as a brown, black, or light tan growth. It may look waxy or scaly, "
            "and is commonly found in older adults."
        ),
        "Unknown": (
            "The prediction could not be matched with a known diagnosis. Further expert review may be needed."
        )
    }
    return explanations.get(predicted_class, explanations["Unknown"])
