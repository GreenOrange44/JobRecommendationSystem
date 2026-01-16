import streamlit as st
from src.helper import resume_keyword_chain
from src.job_api import fetch_naukri_jobs


st.set_page_config(page_title="Job Recommender", layout="wide")
st.title("🤖 Job Recommender System")
st.markdown("""
This application helps you find job openings based on your resume. Upload your resume in PDF format, and the system will extract relevant keywords to search for job listings on platforms like LinkedIn and Naukri.
""")    

st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .job-card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

if uploaded_file:
    if "keywords" not in st.session_state:
        with st.spinner("Processing your resume..."):
            extracted = resume_keyword_chain.invoke(uploaded_file)
            st.session_state.keywords = extracted.replace("\n", "").strip()
            st.session_state.search_keywords_clean = st.session_state.keywords
            st.success("✅ Resume processed!")
            
    if st.button("Get Job Recommendations"):
        st.subheader("Extracted Keywords")
        st.write(st.session_state.search_keywords_clean)
        
        st.subheader("Job Recommendations")
        if "naukri_jobs" not in st.session_state:
            with st.spinner("Fetching job recommendations..."):
            
                # linkedin_jobs = fetch_linkedin_jobs(keywords)
                st.session_state.naukri_jobs = fetch_naukri_jobs(st.session_state.search_keywords_clean)
        st.markdown("---")
        st.header("💼 Top Naukri Jobs (India)")

        if st.session_state.naukri_jobs:
            for index, job in enumerate(st.session_state.naukri_jobs):
                # Create a clean card container
                with st.container(border=True):
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.markdown(f"### {job['title']}")
                        st.markdown(f"**🏢 {job['companyName']}**")
                        
                        # Details Row
                        c1, c2, c3 = st.columns(3)
                        with c1: st.markdown(f"📍 {job['location']}")
                        with c2: st.markdown(f"💰 {job['salary']}")
                        with c3: st.markdown(f"⏳ {job['experience']}")

                    with col2:
                        # "Apply" Button Logic
                        url = job['jdURL']
                        if url and url != "#":
                            st.link_button("👉 Apply Now", url, use_container_width=True)
                        else:
                            st.button("Link Expired", disabled=True, key=f"btn_{index}_{job['title']}")
        else:
            st.warning("No Naukri jobs found.")