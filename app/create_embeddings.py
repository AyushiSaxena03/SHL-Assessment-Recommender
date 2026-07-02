import json
from sentence_transformers import SentenceTransformer

# Model load
model = SentenceTransformer("all-MiniLM-L6-v2")

# JSON load
with open("data/shl_catalog.json", "r", encoding="utf-8") as file:
    text = file.read()

# JSON issue fix
text = text.replace("Microsoft \n    365 (New)", "Microsoft 365 (New)")

data = json.loads(text)

print("Model Loaded Successfully!")
print("Total Assessments:", len(data))

documents = []

for assessment in data:
    text = f"""
Name: {assessment['name']}

Description: {assessment['description']}

Job Levels: {', '.join(assessment['job_levels'])}

Categories: {', '.join(assessment['keys'])}

Languages: {', '.join(assessment['languages']) if assessment['languages'] else 'Not Specified'}

Duration: {assessment['duration'] if assessment['duration'] else 'Not Specified'}
"""

    documents.append(text)

print("\nFirst Document:\n")
print(documents[0])
print("\nTotal Documents:", len(documents))

import numpy as np

print("\nGenerating embeddings... Please wait.")

embeddings = model.encode(
    documents,
    show_progress_bar=True,
    convert_to_numpy=True
)

print("Embedding Shape:", embeddings.shape)

# Save embeddings
np.save("vector_db/embeddings.npy", embeddings)

print("Embeddings saved successfully!")

import faiss

# FAISS index create
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, "vector_db/shl_index.faiss")

print("FAISS Index Created Successfully!")
print("Total vectors in index:", index.ntotal)