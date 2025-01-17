import openai
import PyPDF2
from typing import List, Dict, Tuple
import re
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdfs(pdf_files: List[str]) -> List[str]:
    pdf_texts = []
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            pdf_texts.append(text)
    return pdf_texts

def analyze_texts(texts: List[str]) -> List[Dict[str, str]]:
    analysis_results = []
    for text in texts:
        key_points, nuances = extract_key_points_and_nuances(text)
        statistical_data = extract_statistical_data(text)
        conclusions = extract_conclusions(text)
        references = extract_references(text)
        analysis_results.append({
            'key_points': key_points,
            'nuances': nuances,
            'statistical_data': statistical_data,
            'conclusions': conclusions,
            'references': references
        })
    return analysis_results

def extract_key_points_and_nuances(text: str) -> Tuple[str, str]:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Extract key points and nuances from the following text:\n\n{text}",
        max_tokens=150
    )
    key_points_and_nuances = response.choices[0].text.strip()
    return key_points_and_nuances, key_points_and_nuances

def extract_statistical_data(text: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Extract statistical data from the following text:\n\n{text}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def extract_conclusions(text: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Extract conclusions from the following text:\n\n{text}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def extract_references(text: str) -> List[str]:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Extract references from the following text:\n\n{text}",
        max_tokens=100
    )
    references = response.choices[0].text.strip().split('\n')
    return references if references else ["No references found."]