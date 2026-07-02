import faiss
import json
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("vector_db/shl_index.faiss")

# Load catalog
with open("data/shl_catalog.json", "r", encoding="utf-8") as file:
    text = file.read()

# JSON issue fix
text = text.replace("Microsoft \n    365 (New)", "Microsoft 365 (New)")

catalog = json.loads(text)

# Test query
query = "Java Developer"

query_embedding = model.encode([query])

distances, indices = index.search(query_embedding, 5)

print("Top 5 Results:\n")

for i in indices[0]:
    print(catalog[i]["name"])