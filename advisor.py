def get_guidance(p_win, s_press):
    if p_win > 0.7:
        return ["Strong case position.", "Consider settlement leverage."]
    elif p_win > 0.4:
        return ["Moderate outlook.", "Review discovery documents."]
    else:
        return ["High risk detected.", "Consult senior counsel."]
