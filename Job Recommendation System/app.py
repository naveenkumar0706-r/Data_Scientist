import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Job Recommendation System",
    page_icon="💼",
    layout="wide"
)

# Background Image
page_bg = """
<style>

.stApp {
    background-image: url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Center Container */
.main-box {
    background: rgba(0, 0, 0, 0.65);
    padding: 40px;
    border-radius: 15px;
    width: 60%;
    margin: auto;
    margin-top: 80px;
    text-align: center;
}

/* Text Color */
h1, h2, h3, p, label {
    color: white !important;
}

/* Text Area */
textarea {
    background-color: rgba(255,255,255,0.9) !important;
    color: black !important;
    font-size: 16px !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background-color: #00b4d8;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Centered Heading
st.markdown(
    """
    <div class="main-box">
        <h1>💼 Job Recommendation System</h1>
        <p>Enter your skills or resume summary to get a recommended job role.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Center Column Layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    skills = st.text_area(
        "Enter Skills / Resume Summary",
        height=180
    )

    if st.button("Recommend Job"):

        if skills.strip() == "":
            st.warning("Please enter your skills.")
        else:

            skills = skills.lower()

            if "python" in skills or "machine learning" in skills:
                job = "Data Scientist"

            elif "java" in skills:
                job = "Java Developer"

            elif "sql" in skills or "power bi" in skills:
                job = "Data Analyst"

            elif "html" in skills or "css" in skills:
                job = "Web Developer"

            elif "aws" in skills or "cloud" in skills:
                job = "Cloud Engineer"

            else:
                job = "Software Engineer"

            st.success(f"🎯 Recommended Job: {job}")