def chunk_text_by_newlines(text, chunk_size=1000, overlap=200):
    """
    Splits the text into chunks based on a given chunk size and overlap.

    Args:
        text (str): The full document text.
        chunk_size (int): Maximum size of each text chunk.
        overlap (int): Number of overlapping characters between consecutive chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    chunks = []
    current_chunk = []
    current_length = 0

    for line in text.split("\n"):
        if not line.strip():  # Skip empty lines
            continue

        current_chunk.append(line.strip())
        current_length += len(line)

        if current_length >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = current_chunk[-(overlap // 100):]  # Retain overlap
            current_length = sum(len(line) for line in current_chunk)

    # Append any remaining text as the final chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
