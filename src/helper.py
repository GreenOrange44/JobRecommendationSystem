from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
import os
import pypdf


load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    print("⚠️ WARNING: GOOGLE_API_KEY is missing!")

def read_pdf(file_stream) -> str:
    """
    Reads PDF text directly from a Streamlit file object (BytesIO) 
    or a standard file path.
    """
    try:
        # pypdf.PdfReader can handle both file paths and file-like objects (streams)
        pdf = pypdf.PdfReader(file_stream)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.1)

template = """
You are an expert technical recruiter and job search assistant.
Below is the text content of a candidate's resume.

Your goal is to extract the most effective search keywords to find job openings for this candidate. It should includejob titles (at max 4), core skills (at max 6), and relevant technologies or frameworks (at max 10). The keywords should be concise and relevant to the candidate's experience and skills.
Focus on:
1. Job Titles (e.g., "Senior Backend Engineer") (max 4)
2. Core Skills (e.g., "Python", "AWS", "React") (max 6)
3. Specific frameworks or domains mentioned in the resume. (e.g., "Django", "Numpy", "Machine Learning", "Data Science") (max 10)

RESUME CONTENT:
{resume_text}

OUTPUT INSTRUCTIONS:
- Return ONLY a single string of keywords separated by commas.
- Do not add explanations or labels like "Keywords:".
- Example output: "Software Developer,Django,Senior,Backend"
"""

prompt = PromptTemplate.from_template(template)

pdf_reader_runnable = RunnableLambda(read_pdf)

resume_keyword_chain = (
    pdf_reader_runnable | 
    (lambda text: {"resume_text": text}) |
    prompt | 
    llm | 
    StrOutputParser()
)