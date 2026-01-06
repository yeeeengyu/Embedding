import re
BEHAVIOR_DEFINITIONS = {
    "봉사": ["봉사", "자원봉사"],
    "청소": ["청소", "정리"],
    "신고": ["신고", "제보"],
    "프로그램개발": ["프로그램 개발", "앱 개발"],
    "분실물습득": ["분실물", "습득"],
    "문신": ["문신", "타투"],
    "염색": ["염색"],
    "음주": ["음주", "술"],
    "흡연": ["흡연", "담배"],
    "지각": ["지각", "늦음"],
    "욕설": ["욕설", "폭언", "비속어"]
}

def extract_behaviors(text):
    behaviors = []
    for name, keywords in BEHAVIOR_DEFINITIONS.items():
        for kw in keywords:
            if kw in text:
                behaviors.append(name)
                break
    return behaviors

def load_chunks(path, category):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    text = re.sub(r"---.*?---", "", text, flags=re.S)

    chunks = []
    current_section = None

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith("[") and line.endswith("]"):
            current_section = line.strip("[]")
            continue

        if line.startswith("-"):
            content = line.lstrip("- ").strip()
            chunks.append({
                "content": content,
                "metadata": {
                    "category": category,
                    "section": current_section,
                    "behavior": extract_behaviors(content),
                }
            })

    return chunks