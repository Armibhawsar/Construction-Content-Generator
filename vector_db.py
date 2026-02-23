from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_vector_db(texts):
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embeddings

def search_vector_db(query, texts, index, top_k=2):
    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, top_k)
    return [texts[i] for i in indices[0]]
