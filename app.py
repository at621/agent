import streamlit as st
from chains.credit_risk_chain import run_credit_risk_chain

st.title("Credit Risk AI Agent (Chatbot Interface)")

# Keep conversation or status logs in session state
if "status_logs" not in st.session_state:
    st.session_state["status_logs"] = []

# Chat-like text input
user_request = st.text_input("Enter your modeling request (e.g., 'Build a PD model')")

if st.button("Run Workflow"):
    # Clear old logs
    st.session_state["status_logs"] = []
    
    # Define a simple callback for progress updates
    def status_callback(message: str):
        st.session_state["status_logs"].append(message)
        # Rerun immediately to show the update (optional)
        st.experimental_rerun()
    
    # Run the chain with the callback
    results = run_credit_risk_chain(user_request, status_callback=status_callback)
    
    # Display final results
    st.subheader("Workflow Completed")
    st.write(results)

# Display the status logs as they accumulate
st.subheader("Status Updates")
for log in st.session_state["status_logs"]:
    st.write(log)
