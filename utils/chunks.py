'''
청킹 함수
RAG할 문서들을 정형화하고 프론트매터 안에 있는 메타데이터구조 지움
'''

import re
import yaml

def load_chunks(path, category):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # frontmatter 제거
    text = re.sub(r"---.*?---", "", text, flags=re.S)

    chunks = []
    current_section = None
    buffer = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith("[") and line.endswith("]"):
            if buffer:
                chunks.append({
                    "content": "\n".join(buffer),
                    "metadata": {
                        "category": category,
                        "section": current_section,
                        "document_type": "규정"
                    }
                })
                buffer = []
            current_section = line.strip("[]")
        else:
            buffer.append(line)

    if buffer:
        chunks.append({
            "content": "\n".join(buffer),
            "metadata": {
                "category": category,
                "section": current_section,
                "document_type": "규정"
            }
        })

    return chunks
