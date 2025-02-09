import streamlit as st
# from chains.credit_risk_chain import run_credit_risk_chain

# Optional: Make use of the wide screen layout
st.set_page_config(layout="wide", page_title="Credit Risk Chatbot")

# Set up session state for chat messages, logs, final results, etc.
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of {"role": "user"/"assistant", "content": str}
if "status_logs" not in st.session_state:
    st.session_state.status_logs = []
if "final_results" not in st.session_state:
    st.session_state.final_results = {}

# Define a callback for status messages
def status_callback(msg: str):
    st.session_state.status_logs.append(msg)
    # Optionally force a re-run to update the UI in real-time
    st.experimental_rerun()

# Create two columns: left for chat, right for status
col_chat, col_status = st.columns([2, 1])

# -------------
# LEFT COLUMN
# -------------
with col_chat:
    st.title("Credit Risk Chatbot")

    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.write(message["content"])
        else:
            with st.chat_message("assistant"):
                st.write(message["content"])

    # Chat input (Streamlit 1.23+). 
    # If older Streamlit, just use st.text_input + st.button.
    user_input = st.chat_input("Type your message...")
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # In this example, we do a single-step approach: 
        # If the user types something, we pass it to the chain.
        # You could break this into multiple steps or require a "Submit" button.
        
        # Add a placeholder assistant message for "Thinking..."
        thinking_index = len(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": "Thinking..."})

        # Run the workflow
        # results = run_credit_risk_chain(user_input, status_callback=status_callback)

        # Store final results
        # st.session_state.final_results = results

        # Update the assistant placeholder
        st.session_state.messages[thinking_index]["content"] = (
            "Workflow completed.\n\n"
            # f"**Problem Type**: {results['problem_type']}\n\n"
            f"See the **Status & Summaries** in the right column for details."
        )

        # Re-run so updates display
        st.experimental_rerun()

# -------------
# RIGHT COLUMN
# -------------
with col_status:
    st.header("Status & Summaries")

    # Show current status logs
    if st.session_state.status_logs:
        with st.expander("Progress Logs", expanded=True):
            for log in st.session_state.status_logs:
                st.write("- " + log)

    # If we have final results, show them
    if st.session_state.final_results:
        results = st.session_state.final_results
        st.subheader("Modeling Results")
        st.write("**Problem Type:**", results.get("problem_type"))
        st.write("**Performance Metrics:**", results.get("performance"))
        st.write("**Compliance:**", results.get("compliance"))
        st.write("**Benchmark:**", results.get("benchmark"))
        st.write("**Documentation Path:**", results.get("documentation_path"))
