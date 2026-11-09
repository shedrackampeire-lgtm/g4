import streamlit as st
import joblib  # or pickle / your model framework

# 1. Load your existing model once when the app starts
@st.cache_resource
def load_my_model():
    # Replace with the actual filename of your saved model
    return joblib.load("fake_job_model.joblib")

model = load_my_model()

st.title("Fake Job Posting Checker")
st.write("Enter the details of a job posting to estimate whether it may be fraudulent. This is a screening aid, not a definitive judgment.")

# 2. Collect inputs exactly matching your UI layout
st.header("Job posting details")

title = st.text_input("Title")
location = st.text_input("Location")
department = st.text_input("Department")
salary_range = st.text_input("Salary Range")

company_profile = st.text_area("Company Profile")
description = st.text_area("Description")
requirements = st.text_area("Requirements")
benefits = st.text_area("Benefits")

employment_type = st.selectbox(
    "Employment Type",
    ["Full-time", "Part-time", "Contract", "Temporary"]
)

required_experience = st.selectbox(
    "Required Experience",
    ["Entry-level", "Mid-level", "Senior"]
)

required_education = st.selectbox(
    "Required Education",
    ["High School", "Bachelor's", "Master's", "PhD"])

employment_type = st.text_input("Employment Type")
required_experience = st.text_input("Required Experience")
required_education = st.text_input("Required Education")
industry = st.text_input("Industry")
function = st.text_input("Function")

st.header("Additional signals")
telecommuting=st.checkbox("Offer telecommuting")
has_company_logo = st.checkbox("Has company logo")
has_questions = st.checkbox("Includes screening questions")

# 3. Predict when the button is clicked
if st.button("Check posting"):
    # Combine your inputs into the exact format your model expects (e.g., a list or dataframe)
    features = [
        title, location, department, salary_range, 
        company_profile, description, requirements, benefits,
        employment_type, required_experience, required_education, 
        industry, function, int(has_company_logo), int(has_questions)
    ]
    
    # Run prediction using your loaded model
    prediction = model.predict([features])[0]
    
    # Show the result clearly
    if prediction == 1:
        st.error("⚠️ Warning: This job posting looks highly suspicious / fraudulent.")
    else:
        st.success("✅ Clean: This job posting appears legitimate.")
