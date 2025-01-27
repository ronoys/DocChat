import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

load_dotenv()
st.title("Chat with Your Document")
uploaded_file = st.file_uploader("Upload your PDF document", type=["pdf"])

if uploaded_file is not None:
    
    temp_file_path = os.path.join("/tmp", uploaded_file.name)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    local_file_path = temp_file_path

    loader = PyPDFLoader(local_file_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    split_docs = text_splitter.split_documents(docs)


    difficulty_level = st.select_slider("Select Response Difficulty", options=["Simple", "Standard", "Advanced"], value="Standard", label_visibility="visible")
    response_restriction = st.select_slider("Select Response Type", options=["Bullet Points", "Short Answer", "Paragraph"], value="Short Answer", label_visibility="visible")

    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    index_name = "doc-chat"  # Hardcoded index name
    vector_store = PineconeVectorStore.from_documents(split_docs, embeddings, index_name=index_name)

    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )

    question = st.text_input("Ask a question about the document:")
    if question:
        full_query = f"{question} (Answer this question in the format of {response_restriction} and at difficulty level {difficulty_level}.)"
        answer = qa.invoke(full_query)['result']
        st.write("**Answer:**", answer)