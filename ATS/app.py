import base64
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import PyPDF2
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input,pdf_cotent,prompt):
    # model=genai.GenerativeModel('gemini-1.5-pro')
    # response=model.generate_content([input,pdf_content[0],prompt])
    # return response.text
    pass

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_setup(uploaded_file):
    # this code uses pdf2image module which will get error if we dont have poppler in path
    # if uploaded_file is not None:
    #     ## Convert the PDF to image
    #     images=pdf2image.convert_from_bytes(uploaded_file.read())

    #     first_page=images[0]

    #     # Convert to bytes
    #     img_byte_arr = io.BytesIO()
    #     first_page.save(img_byte_arr, format='JPEG')
    #     img_byte_arr = img_byte_arr.getvalue()

    #     pdf_parts = [
    #         {
    #             "mime_type": "image/jpeg",
    #             "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
    #         }
    #     ]
    #     return pdf_parts
    # else:
    #     raise FileNotFoundError("No file uploaded")
    pass

def input_pdf_response(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for i,page in enumerate(reader.pages):
        text += str(page.extract_text())
    return text

def ForPdf2ImageModule():
    # st.set_page_config(page_title="ATS Resume EXpert")
    # st.header("ATS Tracking System")
    # input_text=st.text_area("Job Description: ",key="input")
    # uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


    # if uploaded_file is not None:
    #     st.write("PDF Uploaded Successfully")


    # submit1 = st.button("Tell Me About the Resume")

    # #submit2 = st.button("How Can I Improvise my Skills")

    # submit3 = st.button("Percentage match")

    # input_prompt1 = """
    # You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
    # Please share your professional evaluation on whether the candidate's profile aligns with the role. 
    # Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
    # """

    # input_prompt3 = """
    # You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
    # your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
    # the job description. First the output should come as percentage and then keywords missing and last final thoughts.
    # """

    # if submit1:
    #     if uploaded_file is not None:
    #         pdf_content=input_pdf_response(uploaded_file)
    #         response=get_gemini_response(input_prompt1,pdf_content,input_text)
    #         st.subheader("The Repsonse is")
    #         st.write(response)
    #     else:
    #         st.write("Please uplaod the resume")

    # elif submit3:
    #     if uploaded_file is not None:
    #         pdf_content=input_pdf_response(uploaded_file)
    #         response=get_gemini_response(input_prompt3,pdf_content,input_text)
    #         st.subheader("The Repsonse is")
    #         st.write(response)
    #     else:
    #         st.write("Please uplaod the resume")
    pass


input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_response(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)