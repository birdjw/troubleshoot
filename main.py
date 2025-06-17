import streamlit as st

# List of steps
steps = [
    "Check that the power cable is connected.",
    "Restart the machine.",
    "Ensure the network cable or Wi-Fi is connected.",
    "Try logging out and back in.",
]

# Initialize session state to track progress
if "step_index" not in st.session_state:
    st.session_state.step_index = 0

st.title("🔧 Pre-Call Troubleshooting Guide")

# Show current step
current_step = st.session_state.step_index
st.write(f"**Step {current_step + 1}:** {steps[current_step]}")

# Add a "Next" button
if st.button("✅ Done - Next Step"):
    if st.session_state.step_index < len(steps) - 1:
        st.session_state.step_index += 1

# Final message when all steps are complete
if st.session_state.step_index == len(steps) - 1:
    if st.button("🎉 All steps completed"):
        st.success("Troubleshooting complete! You can now contact the helpdesk with this information.")