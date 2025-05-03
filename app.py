import streamlit as st
from crew import build_crew

st.title("📈 Digital Marketing AI Agents")

topic = st.text_input("Enter marketing topic", "AI in E-commerce")

if st.button("Run Campaign Agents"):
    with st.spinner("Running agents..."):
        crew = build_crew(topic)
        result = crew.kickoff()
        st.success("Campaign complete!")
        st.markdown("### 📊 Final Result")
        st.markdown(f"```\n{result}\n```")
