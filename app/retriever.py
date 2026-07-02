import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from app.catalog import load_catalog


class SHLRetriever:

    def __init__(self):

        self.catalog = load_catalog()

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.index = faiss.read_index(
            "vector_db/shl_index.faiss"
        )

    # ---------------------------------------------------------

    def get_test_type(self, categories):

        text = " ".join(categories).lower()

        if "personality" in text:
            return "Personality"

        if "ability" in text:
            return "Ability"

        if "aptitude" in text:
            return "Ability"

        if "competencies" in text:
            return "Competency"

        if "development" in text:
            return "Development"

        if "simulation" in text:
            return "Simulation"

        if "coding" in text:
            return "Knowledge"

        return "Assessment"

    # ---------------------------------------------------------

    def search(
        self,
        query: str,
        top_k: int = 20
    ):

        embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        distances, indices = self.index.search(
            embedding,
            top_k
        )

        results = []

        seen = set()

        for score, idx in zip(
            distances[0],
            indices[0]
        ):

            assessment = self.catalog[idx]

            if assessment["name"] in seen:
                continue

            seen.add(
                assessment["name"]
            )

            results.append(

                {
                    "name":
                    assessment["name"],

                    "url":
                    assessment["link"],

                    "description":
                    assessment["description"],

                    "job_levels":
                    assessment["job_levels"],

                    "categories":
                    assessment["keys"],

                    "languages":
                    assessment["languages"],

                    "duration":
                    assessment["duration"],

                    "remote":
                    assessment["remote"],

                    "adaptive":
                    assessment["adaptive"],

                    "test_type":
                    self.get_test_type(
                        assessment["keys"]
                    ),

                    "score":
                    float(score)

                }

            )

        return results