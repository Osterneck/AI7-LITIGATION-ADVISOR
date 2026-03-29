def get_guidance(p_win, s_press):
    notes = []
    if p_win < 0.20:
        notes.append("🔴 **ADJUDICATION RISK**: Court ruling statistically unlikely.")
    if s_press > 0.60:
        notes.append("💰 **SETTLEMENT LEVERAGE**: High probability of bank-led resolution.")
    return notes