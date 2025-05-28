# script_generator.py

import os
from secret_key import openapi_key
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = openapi_key

# Initialize the LLM
llm = OpenAI(temperature=0.7, max_tokens=1024)


def get_topic_ideas(subject):
    prompt_text = """
    You're a data science educator and content strategist.
    Based on the broad subject "{subject}", generate:

    1. 10 conceptual but useful topics (avoid trivial definitions).
    2. 10 nuanced, industry-relevant, or thought-provoking subtopics.
    
    The advanced topics shouldn't be straight forward topics like what is P value or what is confidence interval,
    But rather questions Why a low p-value doesn't always mean practical significance OR Frequentist vs Bayesian interpretation of evidence — how p-values differ.
    Here are few more example of what I want my "Advanced Reels" to be about. Instead of a basic topic like "Understanding P-value in a begineer friendly way", advanced topics should be like below:
        Why a low p-value doesn't always mean practical significance

        The risk of p-hacking and how to detect it in real-world analysis
        
        Why p = 0.049 and p = 0.051 aren't meaningfully different — but are treated as such
        
        Misinterpretations of p-values in A/B testing
        
        The relationship between p-values and sample size: bigger sample ≠ better results
        
        Frequentist vs Bayesian interpretation of evidence — how p-values differ
        
        How p-values change with multiple hypothesis testing — and how to correct for it
        
        Why over-reliance on p < 0.05 can lead to misleading conclusions in business analytics
        
        What does a high p-value really mean — and what it doesn’t

        Should you use p-values at all? A growing debate in data science and research

    Format like this:

    BASIC_TOPICS:
    - ...
    - ...

    ADVANCED_TOPICS:
    - ...
    - ...
    """

    prompt = PromptTemplate(input_variables=["subject"], template=prompt_text)
    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.invoke({"subject": subject})
    return output["text"]


def generate_script(topic, hook_style):
    prompt_text = """
    Write a short voiceover script for an instagram reel on: "{topic}".

    Requirements:
    - Script must be engaging, under 2 minutes
    - The reel hook should be {hook_style} and the reel script should evidently start with that template
    - Use an informal tone suitable for Instagram or YouTube
    - Include insights or tips that provide value beyond the regular textbook information
    - End with a light hearted fun note
    - The tone of the entire script should be beginner friendly but also has enough and more technical information.
    - The entire script should be written in a beginner friendly tone and format. Similar to how statquest by Josh starmer script is
    """

    prompt = PromptTemplate(
        input_variables=["topic", "hook_style"],
        template=prompt_text
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.invoke({"topic": topic, "hook_style": hook_style})
    return output["text"]
