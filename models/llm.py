from langchain_openai import ChatOpenAI

def initialize_llm(api_key):
    return ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=api_key)
