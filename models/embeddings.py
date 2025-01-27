from langchain_openai import OpenAIEmbeddings

def get_embeddings(api_key):
    return OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=api_key)
