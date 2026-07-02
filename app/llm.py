import os
import time
import re

from dotenv import load_dotenv
from google import genai


load_dotenv()


class GeminiClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

    # ---------------------------------------------

    def clean_response(self, text):

        text = text.strip()

        # Remove ```json
        text = re.sub(
            r"^```json",
            "",
            text,
            flags=re.IGNORECASE
        )

        # Remove ```
        text = re.sub(
            r"```$",
            "",
            text
        )

        return text.strip()

    # ---------------------------------------------

    def generate(
        self,
        prompt,
        retries=3
    ):

        for attempt in range(retries):

            try:

                response = self.client.models.generate_content(

                    model="gemini-2.5-flash",

                    contents=prompt

                )

                return self.clean_response(
                    response.text
                )

            except Exception as e:

                print(
                    f"Gemini Error (Attempt {attempt+1}):",
                    e
                )

                time.sleep(2)

        raise Exception(
            "Gemini API failed after multiple retries."
        )