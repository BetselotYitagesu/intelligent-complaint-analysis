import faiss
import numpy as np
import pickle

from sentence_transformers import SentenceTransformer


class ComplaintRetriever:
    def __init__(self, index_path="../vector_store/index.faiss", 
                 metadata_path="../vector_store/index.pkl"):
        self.index = faiss.read_index(index_path)
        with open(metadata_path, "rb") as f:
            self.metadata = pickle.load(f)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def retrieve(self, query: str, k: int = 5):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), k)
        results = []
        for i in indices[0]:
            if i < len(self.metadata):
                results.append(self.metadata[i] | {"chunk_id": i})  # merge 
        return results
