def assess_risk(predicted_class):
    risk_map = {
        "Melanoma": {
            "risk_level": "High",
            "recommendation": "Melanoma is potentially life-threatening. Immediate consultation with a dermatologist is highly recommended."
        },
        "Nevus": {
            "risk_level": "Low",
            "recommendation": "Most nevi are benign. Monitor regularly for any changes in size, shape, or color."
        },
        "Seborrheic Keratosis": {
            "risk_level": "Low",
            "recommendation": "This condition is non-cancerous. Treatment is typically not necessary unless the lesion becomes irritated."
        },
        "Unknown": {
            "risk_level": "Unknown",
            "recommendation": "Unable to assess risk. Further expert evaluation is suggested."
        }
    }

    return risk_map.get(predicted_class, risk_map["Unknown"])
