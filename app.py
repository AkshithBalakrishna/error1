# import streamlit as st
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# import PyPDF2 as pdf
# from PIL import Image
# import io
# import json  # For checking JSON validity

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to get response from the Gemini model
# def get_gemini_response(input_text, input_image=None):
#     model = genai.GenerativeModel('gemini-pro' if input_image is None else 'gemini-1.5-flash')
#     if input_image:
#         response = model.generate_content([input_text, input_image])
#     else:
#         response = model.generate_content(input_text)
#     return response.text

# # Function to extract text from PDF
# def input_pdf_text(uploaded_file):
#     reader = pdf.PdfReader(uploaded_file)
#     text = ""
#     for page in reader.pages:
#         text += str(page.extract_text())
#     return text

# # Function to extract text from a .txt file
# def input_txt_text(uploaded_file):
#     stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
#     return stringio.read()

# # Function to check if the response is valid JSON
# def is_json(response):
#     try:
#         json.loads(response)
#         return True
#     except ValueError:
#         return False

# # Streamlit UI components
# st.title("Error Analyzer")
# st.text("Upload your error message, screenshot, or log for analysis")

# # Input type selection
# input_type = st.radio("Select input type:", ("Text", "Image", "PDF", "Text File (.txt)"))

# # Text input or file upload based on input type selection
# if input_type == "Text":
#     user_input = st.text_area("Paste your error message or code snippet here:")
#     file_input = None
# elif input_type == "Image":
#     file_input = st.file_uploader("Upload an image of your error", type=["png", "jpg", "jpeg"])
#     user_input = None
# elif input_type == "PDF":
#     file_input = st.file_uploader("Upload your error log or code file (PDF)", type="pdf")
#     user_input = None
# else:
#     file_input = st.file_uploader("Upload your error log or code file (.txt)", type="txt")
#     user_input = None

# # Input prompt template for error analysis
# input_prompt = """
# As an expert in API troubleshooting and code debugging, your role is to analyze errors, diagnose their root causes, and provide clear explanations and solutions. When presented with an error:

# 1. Carefully examine the error message, status code (if applicable), and any additional context provided.
# 2. Identify the type of error (e.g., API-related, syntax error, runtime error, logical error).
# 3. Explain the error in simple terms, avoiding overly technical jargon.
# 4. Suggest potential causes for the error, considering common pitfalls and best practices.
# 5. Provide step-by-step troubleshooting instructions, including how to:
#    - Verify API credentials and authentication (if applicable)
#    - Check request formatting and parameters (for API errors)
#    - Validate data being sent or processed
#    - Test API endpoints or specific code sections
#    - Review logs or error messages
# 6. Recommend tools or techniques for debugging (e.g., API testing tools, logging, debuggers, print statements).
# 7. Offer potential solutions or workarounds for the error.
# 8. If relevant, suggest preventive measures to avoid similar errors in the future.
# 9. Be prepared to explain API concepts, HTTP methods, status codes, and common programming concepts as needed.
# 10. If the error seems unique or complex, provide resources for further research or suggest escalation paths.

# Error details:
# {input_text}

# Please provide a comprehensive analysis and solution in this format:
#   "Error Type": "",
#   "Explanation": "",
#   "Potential Causes": [],
#   "Troubleshooting Steps": [],
#   "Recommended Tools": [],
#   "Potential Solutions": [],
#   "Preventive Measures": [],
#   "Additional Resources": []
# """

# # Analyze button to trigger error analysis
# submit = st.button("Analyze")

# # Error analysis logic
# if submit:
#     if input_type == "Text" and user_input:
#         # Text input analysis
#         response = get_gemini_response(input_prompt.format(input_text=user_input))
        
#         # Check if response is valid JSON
#         if is_json(response):
#             st.json(json.loads(response))
#         else:
#             st.text_area("Response (Text)", response)
    
#     elif input_type == "Image" and file_input:
#         # Image input analysis
#         image = Image.open(file_input)
#         response = get_gemini_response(input_prompt.format(input_text="Analyze the error in this image:"), image)
        
#         # Check if response is valid JSON
#         if is_json(response):
#             st.json(json.loads(response))
#         else:
#             st.text_area("Response (Text)", response)
    
#     elif input_type == "PDF" and file_input:
#         # PDF input analysis
#         text = input_pdf_text(file_input)
#         response = get_gemini_response(input_prompt.format(input_text=text))
        
#         # Check if response is valid JSON
#         if is_json(response):
#             st.json(json.loads(response))
#         else:
#             st.text_area("Response (Text)", response)

#     elif input_type == "Text File (.txt)" and file_input:
#         # Text file (.txt) input analysis
#         text = input_txt_text(file_input)
#         response = get_gemini_response(input_prompt.format(input_text=text))
        
#         # Check if response is valid JSON
#         if is_json(response):
#             st.json(json.loads(response))
#         else:
#             st.text_area("Response (Text)", response)
    
#     else:
#         st.error("Please provide input based on your selected input type.")




# ----------------------


# import streamlit as st
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# import json
# from flask import Flask, request

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Flask app to handle incoming requests
# app = Flask(__name__)

# # Store responses in a dictionary for later retrieval
# responses = {}

# # Function to get response from the Gemini model
# def get_gemini_response(input_text):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(input_text)
#     return response.text

# # Function to check if the response is valid JSON
# def is_json(response):
#     try:
#         json.loads(response)
#         return True
#     except ValueError:
#         return False

# # Input prompt template for error analysis
# input_prompt = """
# As an expert in API troubleshooting and code debugging, your role is to analyze errors, diagnose their root causes, and provide clear explanations and solutions. When presented with an error:

# Error details:
# {input_text}

# Please provide a comprehensive analysis and solution in this format:
#   "Error Type": "",
#   "Explanation": "",
#   "Potential Causes": [],
#   "Troubleshooting Steps": [],
#   "Recommended Tools": [],
#   "Potential Solutions": [],
#   "Preventive Measures": [],
#   "Additional Resources": []
# """

# # Streamlit UI components
# st.title("Error Analyzer")
# st.text("Paste your error message or code snippet for analysis:")

# # Text input for error message
# user_input = st.text_area("Error Message:", "")

# # Analyze button to trigger error analysis
# submit = st.button("Analyze")

# # Error analysis logic
# if submit and user_input:
#     # Text input analysis
#     response = get_gemini_response(input_prompt.format(input_text=user_input))
    
#     # Generate a unique ID for the response
#     response_id = f"response_{len(responses) + 1}"
#     responses[response_id] = response
    
#     # Check if response is valid JSON
#     if is_json(response):
#         st.json(json.loads(response))
#     else:
#         st.text_area("Response (Text)", response)
# else:
#     if submit:
#         st.error("Please provide an error message.")

# # Flask API endpoint to handle incoming requests from SAP CPI
# @app.route('/api/error', methods=['POST'])
# def receive_error():
#     data = request.json
#     error_message = data.get('error_message', '')
#     if error_message:
#         # Process the error message
#         response = get_gemini_response(input_prompt.format(input_text=error_message))
#         # Generate a unique ID for the response
#         response_id = f"response_{len(responses) + 1}"
#         responses[response_id] = response
#         return {"response_id": response_id}, 200
#     else:
#         return {"error": "No error message provided"}, 400

# # Flask API endpoint to retrieve the response
# @app.route('/api/response/<response_id>', methods=['GET'])
# def get_response(response_id):
#     response = responses.get(response_id, None)
#     if response:
#         return {"response": response}, 200
#     else:
#         return {"error": "Response not found"}, 404

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8501)

# ------------------

import streamlit as st
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Dict
import threading
import uvicorn
import logging

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FastAPI app initialization
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your allowed origins for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store for responses
responses: Dict[str, str] = {}

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Define the request body for error message submission
class ErrorMessage(BaseModel):
    error_message: str

# Function to get response from the Gemini model
def get_gemini_response(input_text: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input_text)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Input prompt template for error analysis
input_prompt = """
As an expert in API troubleshooting and code debugging, your role is to analyze errors, diagnose their root causes, and provide clear explanations and solutions. When presented with an error:

1. Carefully examine the error message, status code (if applicable), and any additional context provided.
2. Identify the type of error (e.g., API-related, syntax error, runtime error, logical error).
3. Explain the error in simple terms, avoiding overly technical jargon.
4. Suggest potential causes for the error, considering common pitfalls and best practices.
5. Provide step-by-step troubleshooting instructions, including how to:
   - Verify API credentials and authentication (if applicable)
   - Check request formatting and parameters (for API errors)
   - Validate data being sent or processed
   - Test API endpoints or specific code sections
   - Review logs or error messages
6. Recommend tools or techniques for debugging (e.g., API testing tools, logging, debuggers, print statements).
7. Offer potential solutions or workarounds for the error.
8. If relevant, suggest preventive measures to avoid similar errors in the future.
9. Be prepared to explain API concepts, HTTP methods, status codes, and common programming concepts as needed.
10. If the error seems unique or complex, provide resources for further research or suggest escalation paths.

Error details:
{input_text}

Please provide a comprehensive analysis and solution in this format:
  "Error Type": "",
  "Explanation": "",
  "Potential Causes": [],
  "Troubleshooting Steps": [],
  "Recommended Tools": [],
  "Potential Solutions": [],
  "Preventive Measures": [],
  "Additional Resources": []
"""

# API to handle POST requests from SAP CPI
@app.post("/api/error")
def receive_error(error_message: ErrorMessage):
    logging.info(f"Received error message: {error_message.error_message}")
    response_text = get_gemini_response(input_prompt.format(input_text=error_message.error_message))
    response_id = f"response_{len(responses) + 1}"
    responses[response_id] = response_text
    logging.info(f"Response generated for ID: {response_id}")
    return {"response_id": response_id}

# API to retrieve responses based on ID
@app.get("/api/response/{response_id}")
def get_response(response_id: str):
    if response_id in responses:
        return {"response": responses[response_id]}
    else:
        raise HTTPException(status_code=404, detail="Response not found")

# Function to start FastAPI server in a background thread
def run_fastapi():
    port = int(os.getenv("PORT", 8000))  # Use Render's PORT variable
    uvicorn.run(app, host="0.0.0.0", port=port)

# Start FastAPI server in a separate thread
fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
fastapi_thread.start()

# Streamlit UI components
st.title("Error Analyzer")
st.text("Paste your error message or code snippet for analysis:")

# Text input for error message
user_input = st.text_area("Error Message:", "")

# Analyze button to trigger error analysis
submit = st.button("Analyze")

# Error analysis logic
if submit and user_input:
    # Update to your deployed FastAPI URL
    url = "https://your-fastapi-url.onrender.com/api/error"  # Replace with actual URL
    try:
        response = requests.post(url, json={"error_message": user_input})
        if response.status_code == 200:
            response_id = response.json().get("response_id")
            st.success(f"Response saved! Use ID: {response_id} to retrieve it.")
        else:
            st.error("Error occurred while sending the request.")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to FastAPI: {e}")
else:
    if submit:
        st.error("Please provide an error message.")
