import streamlit as st
import os
from dotenv import load_dotenv
from util.file_handler import save_uploaded_file
from util.document_processing import process_document
from util.query_handler import get_response
from models.embeddings import get_embeddings
from models.llm import initialize_llm
from components.ui_components import render_ui
from langchain_pinecone import PineconeVectorStore

load_dotenv()

uploaded_file, difficulty_level, response_restriction = render_ui()

if uploaded_file is not None:
    local_file_path = save_uploaded_file(uploaded_file)
    split_docs = process_document(local_file_path)

    embeddings = get_embeddings(os.getenv("OPENAI_API_KEY"))
    index_name = os.getenv("INDEX_NAME")
    vector_store = PineconeVectorStore.from_documents(split_docs, embeddings, index_name=index_name)

    llm = initialize_llm(os.getenv("OPENAI_API_KEY"))

    question = st.text_input("Ask a question about the document:")
    if question:
        answer = get_response(llm, vector_store.as_retriever(), question, response_restriction, difficulty_level)
        st.write("**Answer:**", answer)
