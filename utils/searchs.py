from utils.embeds import embed

def search(query, texts, metas, index, k=3):
    q_vec = embed([query])
    D, I = index.search(q_vec, k)

    results = []
    for idx in I[0]:
        results.append({
            "content": texts[idx],
            "metadata": metas[idx]
        })
    return results
