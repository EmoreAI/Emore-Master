import openai
from typing import List, Dict
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_insights(analysis_results: List[Dict[str, str]]) -> List[str]:
    insights = []
    for result in analysis_results:
        key_points = result['key_points']
        nuances = result['nuances']
        statistical_data = result['statistical_data']
        conclusions = result['conclusions']
        references = result['references']
        
        insight = create_insight(key_points, nuances, statistical_data, conclusions, references)
        insights.append(insight)
    return insights

def create_insight(key_points: str, nuances: str, statistical_data: str, conclusions: str, references: List[str]) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(
            f"Create an insight based on the following information:\n"
            f"Key Points: {key_points}\n"
            f"Nuances: {nuances}\n"
            f"Statistical Data: {statistical_data}\n"
            f"Conclusions: {conclusions}\n"
            f"References: {', '.join(references)}"
        ),
        max_tokens=150
    )
    return response.choices[0].text.strip()

def summarize_insights(insights: List[str]) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following insights into a coherent report:\n\n{insights}",
        max_tokens=200
    )
    return response.choices[0].text.strip()

def compare_insights(insights: List[str]) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Compare the following insights:\n\n{insights}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def highlight_novel_findings(insights: List[str]) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Highlight novel findings from the following insights:\n\n{insights}",
        max_tokens=150
    )
    return response.choices[0].text.strip()