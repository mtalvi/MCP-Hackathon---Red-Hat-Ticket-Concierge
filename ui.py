import streamlit as st
import requests
import webbrowser

st.title("🎫 Red Hat Ticket Concierge")

msg = st.text_input("What do you need help with?", placeholder="e.g. I need a locker")

if st.button("Ask Agent"):
    if not msg.strip():
        st.warning("Please enter a request.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post("http://127.0.0.1:8080/agent", json={"message": msg})
            if response.status_code == 200:
                data = response.json()
                if data["status"] == "ok":
                    st.success(f"Ticket type: {data['ticket_type']}")
                    st.write("**Form URL:**")
                    st.write(data["ticket_url"])
                    st.write("**Suggested Field Values:**")
                    for k, v in data["prefilled_fields"].items():
                        st.write(f"- **{k}**: {v}")
                    if st.button("Open Form"):
                        webbrowser.open(data["ticket_url"])
                else:
                    st.error("Could not classify request. Try rephrasing.")
            else:
                st.error("Agent is unavailable.")
