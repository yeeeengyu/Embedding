from utils.chuncks import load_chunks
from utils.embeds import embed
POS = load_chunks("ragdocs/pos_rules.md", '상점')
NEG = load_chunks("ragdocs/neg_rules.md", '벌점')
chunks = POS + NEG; chunks = [c for c in chunks if c["metadata"]["section"] is not None]
print(chunks) # 청크13개

import google.generativeai as genai
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv() # Gemini 임베딩모델 가져오기
genai.configure(api_key=os.getenv("GEMINI_API"))

import faiss # VectorDB 설계
texts = [c["content"] for c in chunks]
metas = [c["metadata"] for c in chunks]
vectors = embed(texts)
dim = vectors.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(vectors)

print("FAISS index size:", index.ntotal)

from utils.searchs import search
results = search(
    query = input(),
    texts = texts,
    metas = metas,
    index = index,
    k = int(input())
)

for r in results:
    print(r["metadata"])
    print(r["content"])