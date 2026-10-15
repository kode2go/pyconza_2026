# indabax_page.py
import streamlit as st

st.set_page_config(
    page_title="Python, AI Agents, and the Future of Infrastructure Automation",
    page_icon="☁️",
    layout="centered"
)

st.title("PyconZA 2026")
st.subheader("Python, AI Agents, and the Future of Infrastructure Automation")

st.markdown(
    """
Thank you for attending the talk.

This page brings together the key links mentioned during the session.

### Contact

📧 **Email:** [bbarsch@csir.co.za](mailto:bbarsch@csir.co.za)  
🔗 **LinkedIn:** [Binjamin Barsch](https://www.linkedin.com/in/binjamin-barsch-43036216a/)
"""
)

st.divider()

st.header("Talk Slides")
st.markdown(
    """
Download or view the slides:
"""
)

st.link_button(
    "📄 Download Talk Slides (PDF)",
    "https://raw.githubusercontent.com/kode2go/pyconza_2026/main/Python, AI Agents, and the Future of Infrastructure Automation_v2.pdf.pdf"
    
)


st.divider()
st.header("Local Cloud - Sebowa")
st.markdown(
    """
To gain local cloud access - get VM access!
"""
)
st.link_button("Link", "https://sebowausers.chpc.ac.za")
st.divider()

st.header("Try VuthaStack")
st.markdown(
    """
**VuthaStack — VMs in Minutes**

Interested in trying local virtual machines hosted in South Africa?

Fill in the expression of interest form below.
"""
)
st.link_button(
    "Fill in VuthaStack Form",
    "https://forms.cloud.microsoft/r/QbHnRehVYy"
)

st.divider()

st.header("CHPC Access")
st.markdown(
    """
To know more about CHPC and gain access to local compute and cloud resources:
"""
)
st.link_button("Visit CHPC", "https://chpc.ac.za")

st.caption("CHPC | Local compute, cloud access, and responsible AI infrastructure")
