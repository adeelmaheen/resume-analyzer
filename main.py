import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
from pdf2image import convert_from_path
import pytesseract
import pdfplumber

# Load environment variable
load_dotenv()

# Configure Google Gemini API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = " "
    try:
        #  try direct text extraction 
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        if text.strip():
            return text.strip()
    
    except Exception as e:
        print(f"Direct text extraction failed: {e}")

    
    # Fallback to OCR for image bsed  pdfs
    print("Falling back to OCR for image-based PDFs.")
    try:
        images = convert_from_path(pdf_path)
        for image in images:
           page_text = pytesseract.image_to_string(image)
           text += page_text + "\n"
        
    except Exception as e:
        print(f"OCR extraction failed: {e}")
        

    return text.strip()

# Function to generate a summary using Google Gemini
def analyze_resume(resume_text, job_description=None):
    if not resume_text:
        
        return {"error": "Resume text is required for analysis."}
    
    model = genai.GenerativeModel("gemini-1.5-flash")

    base_prompt = f"""
    You are an experienced HR with Technical Experience in the field of any one job role from data science, data analyst, devops, machine learning engineer, prompt engineer, AI engineer, full stack web development, big data engineering, marketing analyst, human resource manager,
    business analyst, product manager, project manager, software engineer, data engineer, cloud engineer, software developer and data architect.
    your task is to review the provided resume.Please share your professional evaluation on whether the candidate's profile aligns with the role. Also mention skills he already have and suggest some skills to improve his resume, also suggest some course he might take to improve the skills. Highlight the strengths and weakness. 
    Resume:
    {resume_text}

    """

    if job_description:
        base_prompt += f"""
        Additionally, compare this resume to the following job description:

        Job Description: 
        {job_description}
        Highlight the strengths and weaknesses of the resume in relation to the job description.
        """
    
    response = model.generate_content(base_prompt)

    analysis = response.text.strip()
    return analysis

# Streamlit app
st.set_page_config(page_title="Resume Analyzer", page_icon=":guardsman:", layout="wide")
# title
st.title("AI Resume Analyzer")
st.write("Analyze your resume and match it with a job description using Google Gemini.")

col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
with col2:
    job_description = st.text_area("Job Description", placeholder="Paste the job description here...")

if uploaded_file is not None:
    st.success("File uploaded successfully!")
else:
    st.warning("Please upload a PDF file to proceed.")

st.markdown("<div style= 'padding-top:10px; '></div>", unsafe_allow_html=True)
if uploaded_file:
    # save uploaded file locally for processing
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    # Extract text from the uploaded PDF
    resume_text = extract_text_from_pdf("uploaded_resume.pdf")
    
    if st.button("Analyze Resume"):
        
        with st.spinner("Analyzing resume..."):
                try:
                    # Analyze the resume using Google Gemini
                    analysis = analyze_resume(resume_text, job_description)
                    st.success("Analysis completed!")
                    st.write("### Analysis Result:")
                    st.write(analysis)
                except Exception as e:
                    st.error(f"Error during analysis: {e}")
                    st.write("Please check the resume format and try again.")

# Clean up the uploaded file
if os.path.exists("uploaded_resume.pdf"):
        os.remove("uploaded_resume.pdf")
        st.success("Temporary files cleaned up.")
else:
        st.warning("No temporary files to clean up.")
# Footer
st.markdown("-----")
st.markdown(
    """
    <p style= 'text-align: center; color: black; font-size: 14px;'> Powered by <b>Google Gemini API</b> and <b>Streamlit </b> | 
    Developed by ❤ <a href="https://www.linkedin.com/in/maheen-arif-a929412b6/" target="_blank" style='text-decoration:none; color:black'> <b>Maheen Arif </b></a> </p>
   
    """,
    unsafe_allow_html=True,
)
                