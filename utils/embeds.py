'''
Gemini 임베딩모델 불러오기
embed 함수로 문장/문서 임베딩
'''

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