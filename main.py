from utils.chuncks import load_chunks
from utils.embeds import embed
POS = load_chunks("ragdocs/pos_rules.md", '상점')
NEG = load_chunks("ragdocs/neg_rules.md", '벌점')
chunks = POS + NEG




print(chunks) # 청크13개

import google.generativeai as genai
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API"))

import faiss

texts = [c["content"] for c in chunks]
metas = [c["metadata"] for c in chunks]

vectors = embed(texts)

dim = vectors.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(vectors)

print("FAISS index size:", index.ntotal)

from utils.searchs import search
results = search(
    query="야간 자습 시간에 벌점 받는 행동은?",
    texts=texts,
    metas=metas,
    index=index,
    k=3
)

for r in results:
    print(r["metadata"])
    print(r["content"])
