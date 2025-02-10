from sentence_transformers import SentenceTransformer, util

# Load a sentence-transformer model globally for efficiency
retrieval_model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_relevant_chunks(question, chunks, top_k=3):
    """
    Retrieves the most relevant chunks based on the user's question.

    Args:
        question (str): The user's query.
        chunks (List[str]): The list of text chunks.
        top_k (int): The number of most relevant chunks to retrieve.

    Returns:
        str: Concatenated top-k relevant chunks.
    """
    # Encode the question and text chunks
    question_embedding = retrieval_model.encode(question, convert_to_tensor=True)
    chunk_embeddings = retrieval_model.encode(chunks, convert_to_tensor=True)

    # Compute cosine similarity and retrieve top-k relevant chunks
    similarities = util.pytorch_cos_sim(question_embedding, chunk_embeddings)[0]
    top_k_indices = similarities.topk(k=top_k).indices

    relevant_chunks = [chunks[i] for i in top_k_indices]
    return " ".join(relevant_chunks)
