'''
검색 함수
문장 임베딩 후 벡터유사도 기반 상위 k개 출력
'''

from utils.embeds import embed

def search(query, texts, metas, index, k):
    q_vec = embed([query])
    D, I = index.search(q_vec, k)

    results = []
    for idx in I[0]:
        results.append({
            "content": texts[idx],
            "metadata": metas[idx]
        })
    return results
