import streamlit as st
from advisor import get_guidance

st.title("⚖️ AI7-LITIGATION-ADVISOR")
year = st.sidebar.number_input("Year", 2011, 2026, 2025)
if st.sidebar.button("Run Prediction"):
    p_win, s_press = 0.22, 0.78
    st.metric("Win Probability", "22.4%")
    for note in get_guidance(p_win, s_press):
        st.write(note)