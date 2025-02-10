# 📄 PDF Q&A App with Retrieval-Augmented Generation (RAG)

This project is a Streamlit-based web app that allows users to upload PDF documents, ask questions about the contents, and get accurate answers using **Retrieval-Augmented Generation (RAG)** and **OpenAI's ChatCompletion API**.

## 🚀 Features
- **PDF Upload and Text Extraction:** Uses PyMuPDF (`fitz`) to extract plain text from uploaded PDFs.
- **Text Chunking:** Splits the PDF text into manageable chunks with configurable overlap for better context.
- **Retrieval-Augmented Generation:** Retrieves the most relevant chunks using **Hugging Face's `sentence-transformers`** (`all-MiniLM-L6-v2`) and provides them as context to OpenAI's GPT model.
- **Interactive Q&A:** Users can ask questions about the document and get context-aware, accurate responses.

---

## 📂 Project Structure
```
.
├── main.py              # Streamlit app entry point
├── pdf_reader.py        # Extracts text from the PDF
├── text_chunk.py        # Splits text into chunks for RAG
├── rag.py               # Retrieves relevant chunks using embeddings
└── README.md            # Project documentation
```
---

## 🧰 Requirements
- Python 3.8 or higher
- Streamlit
- PyMuPDF (fitz)
- Sentence Transformers
- OpenAI API
- python-dotenv
  
---

## ⚙️ Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-qa-app.git
   cd pdf-qa-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   **If you don't have a `requirements.txt` yet, create one with:**
   ```bash
   pip freeze > requirements.txt
   ```

---

## 🔑 OpenAI API Key
Create an `.env` file in the project directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

Alternatively, you can hard-code it in the app (not recommended for production).

---

## 🏃️ Running the App
Run the Streamlit app:
```bash
streamlit run main.py
```

The app will launch in your browser at `http://localhost:8501`.

---

## 🔧 How It Works
1. **PDF Upload:** Users upload a PDF file via the Streamlit interface.
2. **Text Extraction:** The app extracts plain text using PyMuPDF.
3. **Text Chunking:** The text is split into overlapping chunks to maintain context across boundaries.
4. **RAG Search:** The user's question is compared to the text chunks using cosine similarity to find the most relevant context.
5. **OpenAI GPT Answer Generation:** The context and user question are passed to OpenAI's ChatCompletion API to generate a response.

---

## 📚 Technologies Used
- **[Streamlit](https://streamlit.io/):** For building the interactive web interface.
- **[PyMuPDF](https://pymupdf.readthedocs.io/en/latest/):** For PDF text extraction.
- **[Sentence Transformers](https://www.sbert.net/):** For computing embeddings and retrieving relevant chunks.
- **[OpenAI API](https://platform.openai.com/docs/):** For generating answers using GPT models.

---

## ✨ Future Enhancements

Add support for large PDFs using chunk-wise processing and external vector databases.

Explore integrating other RAG pipelines, such as FAISS or Pinecone for scalable retrieval.

Improve the chunking logic to handle structured data (tables, headers, etc.).

Combine image processing (maybe too hard).

Refine search/output quality.

Refer to relevant page numbers at the end as a “For more information, refer to:” thing.

---

## 👨‍💻 Author
Built by Mira Kapoor Wadehra (https://github.com/mirakw).

