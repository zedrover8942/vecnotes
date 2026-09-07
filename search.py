import argparse
import glob
import os
import pickle

import numpy as np


def load_docs(folder):
    docs = []
    for path in glob.glob(os.path.join(folder, "**", "*.md"),
                          recursive=True):
        with open(path, encoding="utf-8") as f:
            docs.append((path, f.read()))
    return docs


def embed_tfidf(texts):
    # fallback: TF-IDF vectors, no model download needed
    from sklearn.feature_extraction.text import TfidfVectorizer
    return TfidfVectorizer(stop_words="english").fit_transform(texts).toarray()


def embed_st(texts):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model.encode(texts, normalize_embeddings=True)


def embed(texts):
    try:
        return embed_st(texts)
    except Exception:
        return embed_tfidf(texts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--cache", default=".vecache.pkl")
    args = ap.parse_args()

    docs = load_docs(args.folder)
    if not docs:
        raise SystemExit("no .md files under %s" % args.folder)
    if os.path.exists(args.cache):
        with open(args.cache, "rb") as f:
            paths, mat = pickle.load(f)
        if paths != [p for p, _ in docs]:
            mat = None
    else:
        mat = None
    if mat is None:
        mat = embed([t for _, t in docs])
        with open(args.cache, "wb") as f:
            pickle.dump(([p for p, _ in docs], mat), f)

    print("indexed %d docs, type your query (empty to quit)" % len(docs))
    while True:
        q = input(">> ").strip()
        if not q:
            break
        qv = embed([q])[0]
        scores = mat @ qv / (np.linalg.norm(mat, axis=1)
                             * (np.linalg.norm(qv) + 1e-9))
        for i in np.argsort(-scores)[:3]:
            print("%.3f  %s" % (scores[i], docs[i][0]))


if __name__ == "__main__":
    main()
