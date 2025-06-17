import streamlit as st

st.set_page_config(page_title="Helpdesk Troubleshooting", layout="centered")

st.title("🛠️ Helpdesk Pre-Troubleshooting Assistant")
st.write("Please go through the steps below before contacting the helpdesk.")

# Step 0: Select machine type
machine_type = st.selectbox(
    "What type of machine are you working on?",
    ["Select an option", "Seaga Coil", "Seaga Locker", "Cribmaster Coil", "Cribmaster Locker", "Other"]
)

if machine_type == "Select an option":
    st.warning("Please select the type of machine you're working on.")
    st.stop()

st.info(f"You selected: **{machine_type}**")

# Step 1: Power check
power_on = st.radio("Is your device powered on?", ["Yes", "No"], index=1)
if power_on == "No":
    st.warning("Please power on your device and try again.")
    st.stop()

# Step 2: Restart check
restarted = st.radio("Have you tried restarting the device?", ["Yes", "No"], index=1)
if restarted == "No":
    st.info("Please restart your device and see if the problem persists.")
    st.stop()

# Step 3: Network check
network_issue = st.radio("Are you connected to the internet?", ["Yes", "No", "Not sure"], index=2)
if network_issue == "No":
    st.warning("Please check your Wi-Fi or Ethernet connection.")
    st.stop()

# Step 4: Error messages
error_msg = st.text_input("Are there any error messages? If so, enter them here.")

# Step 5: Final prompt (only shows when user is ready to proceed)
if st.button("Contact Helpdesk"):
    st.success("✅ You've completed the pre-troubleshooting steps.")
    st.write("📞 You can now call the helpdesk at **877-877-6408**")
    if error_msg:
        st.write(f"🔍 Error notes: _{error_msg}_")