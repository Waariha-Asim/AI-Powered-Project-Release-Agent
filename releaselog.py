import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Release Log",
    layout="wide"
)

st.title("Release History")
st.caption("All projects published through the AI Release Pipeline")

st.divider()

releases = [
    {
        "project": "AI Project Release Agent",
        "framework": "Streamlit",
        "github": "https://github.com/Waariha-Asim",
        "linkedin": "Published",
        "secrets": 0,
        "time": "3 min",
        "status": "Success"
    },
    {
        "project": "CarePilot AI",
        "framework": "FastAPI + RAG",
        "github": "https://github.com/Waariha-Asim",
        "linkedin": "Published",
        "secrets": 2,
        "time": "3 min",
        "status": "Success"
    },
    {
        "project": "Social Media Automation",
        "framework": "n8n + Gemini",
        "github": "https://github.com/Waariha-Asim",
        "linkedin": "Rejected",
        "secrets": 1,
        "time": "3 min",
        "status": "Success"
    },
]

for r in releases:
    with st.expander(f"{r['project']} — {r['framework']}"):
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Framework", r["framework"])
        c2.metric("GitHub", "Published")
        c3.metric("LinkedIn", r["linkedin"])
        c4.metric("Secrets Caught", r["secrets"])
        c5.metric("Time Taken", r["time"])

        if r["status"] == "Success":
            st.success("Pipeline completed successfully")

st.divider()

st.subheader("Pipeline Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Projects Released", "3")
    st.metric("Total Secrets Caught", "3")

with col2:
    st.metric("Average Release Time", "3 min")
    st.metric("Manual Time Saved", "2+ hours")

with col3:
    st.metric("GitHub Success Rate", "100%")
    st.metric("LinkedIn Post Rate", "67%")

st.divider()
