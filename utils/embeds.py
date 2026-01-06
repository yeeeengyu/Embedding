import google.generativeai as genai
import numpy as np

def embed(texts):
    vectors = []
    for t in texts:
        res = genai.embed_content(
            model="models/text-embedding-004",
            content=t
        )
        vectors.append(res["embedding"])
    return np.array(vectors, dtype="float32")