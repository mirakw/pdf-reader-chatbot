import streamlit as st
from pdf_reader import extract_text_from_pdf
from text_chunker import chunk_text_by_newlines
from rag_search import retrieve_relevant_chunks
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("📄 PDF Q&A App with RAG Search")

st.title("📄 PDF Q&A App with RAG Search")

# Upload a PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    # Step 1: Extract text from PDF
    with st.spinner("Extracting text from PDF..."):
        document_text = extract_text_from_pdf(uploaded_file)
        st.success("Text extracted successfully!")

    # Step 2: Display a preview of the first 1000 characters
    st.subheader("📃 Document Preview")
    st.text_area("Preview of the PDF content", document_text[:1000], height=200)

    # Step 3: Chunk the text
    chunks = chunk_text_by_newlines(document_text, chunk_size=1000, overlap=200)

    # Step 4: User input for the question
    question = st.text_input("Ask a question about the PDF")

    if st.button("Get Answer"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            # Step 5: Retrieve relevant context using RAG
            with st.spinner("Retrieving relevant chunks..."):
                relevant_context = retrieve_relevant_chunks(question, chunks, top_k=5)

            # Step 6: Generate an answer using OpenAI's ChatCompletion API
            with st.spinner("Generating answer..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant. Read the provided document context and answer the user's question accurately and concisely."},
                        {"role": "user", "content": f"Document Context: {relevant_context}\n\nQuestion: {question}"}
                    ],
                    max_tokens=500
                )
                answer = response['choices'][0]['message']['content'].strip()

                # Display the answer
                st.subheader("🤖 Answer")
                st.write(answer)
