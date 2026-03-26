import streamlit as st 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import tempfile

load_dotenv()

st.title(" Resume  chatbot (RAG)")

uploaded_file = st.file_uploader("upload your resume (PDF)" , type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size = 500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceBgeEmbeddings()
    vectorstore = FAISS.from_documents(docs , embeddings)
    retriever = vectorstore.as_retriever()

    llm = ChatGroq(model="llama-3.3-70b-versatile")

    query = st.text_input("ASK SOMETHING ABOUT YOUR RESUME")   

    if query:
        retrieved_docs = retriever.invoke(query)
        context = "\n".joint ([doc.page_content for doc in retrieved_docs]) 

       prompt = f"""
        You are a helpful AI assistant.
        Answer only from context.
        If not found, say you don't know.

        Context:
        {context}

        Question:
        {query}
        """

        response = llm.invoke(prompt)

        st.write("### Answer:")
        st.write(response.content)