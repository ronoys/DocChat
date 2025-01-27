from langchain.chains import RetrievalQA

def get_response(llm, retriever, question, response_type, difficulty):
    full_query = f"{question} (Answer in {response_type} at {difficulty} level.)"
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    return qa.invoke(full_query)['result']
