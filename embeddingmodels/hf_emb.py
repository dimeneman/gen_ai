from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

embedding = model.encode("How good is Breaking Bad?")

print(len(embedding))